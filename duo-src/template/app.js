(function () {
  const D = JSON.parse(document.getElementById('data').textContent);
  const S = { style: 'Slow', sort: 'fit', country: 'All', home: 'fri' };
  try { const s = JSON.parse(localStorage.getItem('duoweek') || '{}'); Object.assign(S, s); } catch (e) {}
  if (!['Slow', 'Fuller'].includes(S.style)) S.style = 'Slow';
  if (!['fri', 'sat', 'hk'].includes(S.home)) S.home = 'fri';
  const save = () => { try { localStorage.setItem('duoweek', JSON.stringify(S)); } catch (e) {} };
  const eur = n => '€' + Math.round(n).toLocaleString('en-GB');
  const esc = s => String(s).replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
  const HOME = D.home_labels;
  const fs = st => `<span class="fs fs-${st === 'est' ? 'est' : 'live'}" title="${esc(D.fare_status[st] || '')}">${st === 'est' ? 'estimate' : 'live 27 Oct'}</span>`;

  // ---- place notes
  const PLACES = D.places || [];
  const plCache = {};
  function plRe(trip) {
    if (plCache[trip]) return plCache[trip];
    const map = {};
    PLACES.forEach((p, i) => { if (!p.t || p.t.includes(trip)) p.a.forEach(a => { if (!(a in map)) map[a] = i; }); });
    const alts = Object.keys(map).sort((a, b) => b.length - a.length).map(a => esc(a).replace(/[.*+?^${}()|[\]\\]/g, '\\$&'));
    const re = alts.length ? new RegExp('(^|[^A-Za-z0-9-])(' + alts.join('|') + ')(?![A-Za-z0-9-])', 'g') : null;
    return (plCache[trip] = { re, map });
  }
  const pl = (s, trip) => {
    const t = esc(s), r = plRe(trip);
    return r.re ? t.replace(r.re, (m, pre, name) => `${pre}<span class="pl" role="button" tabindex="0" data-p="${r.map[name]}">${name}</span>`) : t;
  };
  const fmtH = m => m < 60 ? `${m} min` : `${Math.floor(m / 60)}h${m % 60 ? String(m % 60).padStart(2, '0') : ''}`;
  const skyKey = c => c <= 40 ? 'blue' : c <= 64 ? 'mixed' : 'grey';
  const SKY = { blue: 'Blue sky', mixed: 'Sun and cloud', grey: 'Grey sky' };
  const MODE = { plane: 'Flight', train: 'Train', metro: 'Metro', bus: 'Bus', van: 'Van', taxi: 'Taxi', boat: 'Boat', cable: 'Cable car' };

  const opt = (d, style) => d.options.find(o => o.style === style);
  const cost = (d, o, home) => o.cost[home || S.home];
  const range = d => { const t = d.options.map(o => cost(d, o).total); return [Math.min(...t), Math.max(...t)]; };

  // ---- board
  const board = [...D.dests].sort((a, b) => a.out.dep.localeCompare(b.out.dep));
  function renderBoard() {
    document.getElementById('board').innerHTML = board.map(d => `
      <tr tabindex="0" data-go="${d.id}"><td>${d.out.dep}</td><td>${esc(d.out.carrier)}</td>
      <td class="dest">${esc(d.out.code)}</td><td class="tripcol">${esc(d.title)}</td><td class="fcw">${esc(d.fc.word)}</td><td class="fcw"><i class="sk sk-${skyKey(d.fc.cc)}"></i>${esc(SKY[skyKey(d.fc.cc)])}</td><td class="right">${d.fit}</td><td class="right">${eur(range(d)[0])}</td></tr>`).join('');
  }
  document.getElementById('board').addEventListener('click', e => { const tr = e.target.closest('tr'); if (tr) go(tr.dataset.go); });
  document.getElementById('board').addEventListener('keydown', e => { const tr = e.target.closest('tr'); if (tr && e.key === 'Enter') go(tr.dataset.go); });
  function go(id) { const el = document.getElementById(id); if (el) el.scrollIntoView({ behavior: matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth', block: 'start' }); }

  // ---- picks
  function renderPicks() {
    document.getElementById('picks').innerHTML = D.picks.map(p => {
      const d = D.dests.find(x => x.id === p.id), r = range(d);
      return `<a class="pick" href="#${d.id}"><span class="why">${esc(p.why)}</span><strong>${esc(d.title)}</strong>
        <span class="meta">fit ${d.fit} · ${eur(r[0])}–${eur(r[1]).slice(1)} for two</span><p>${esc(p.text)}</p></a>`;
    }).join('');
  }

  // ---- checks
  const CHK = { ok: 'Open / fine', warn: 'Open, with a caveat', out: 'Closed or damaged: left out', todo: 'Still to verify' };
  const cnt = k => D.checks.filter(c => c[2] === k).length;
  const ORDER = { out: 0, todo: 1, warn: 2, ok: 3 };
  const chkCard = c => `<div class="chk-card"><span class="st st-${c[2]}">${CHK[c[2]]}</span><b>${esc(c[1])}</b><span class="where">${esc(c[0])}</span><p>${esc(c[3])}</p><a href="${esc(c[5])}" target="_blank" rel="noopener">${esc(c[4])} ↗</a></div>`;
  const sorted = [...D.checks].sort((a, b) => ORDER[a[2]] - ORDER[b[2]]);
  document.getElementById('checks').innerHTML =
    `<p class="chk-sum"><span class="st st-out">${cnt('out')} closed or damaged</span> <span class="st st-todo">${cnt('todo')} still to verify</span> <span class="st st-warn">${cnt('warn')} with a caveat</span> <span class="st st-ok">${cnt('ok')} fine</span></p>` +
    `<div class="chk-grid">${sorted.filter(c => c[2] === 'out' || c[2] === 'todo').map(chkCard).join('')}</div>` +
    `<details class="chk-more"><summary>Show the ${cnt('warn') + cnt('ok')} other checks</summary><div class="chk-grid">${sorted.filter(c => c[2] === 'warn' || c[2] === 'ok').map(chkCard).join('')}</div></details>`;

  // ---- controls
  function seg(id, key, items) {
    const el = document.getElementById(id);
    el.innerHTML = items.map(([v, l]) => `<button type="button" data-v="${v}" aria-pressed="${S[key] === v}">${l}</button>`).join('');
    el.addEventListener('click', e => {
      const b = e.target.closest('button'); if (!b) return;
      S[key] = b.dataset.v; save();
      if (key === 'style') Object.keys(planSel).forEach(k => delete planSel[k]);
      el.querySelectorAll('button').forEach(x => x.setAttribute('aria-pressed', x.dataset.v === S[key]));
      render();
    });
  }
  seg('style', 'style', [['Slow', 'Slow'], ['Fuller', 'Fuller']]);
  seg('home', 'home', [['fri', HOME.fri], ['sat', HOME.sat], ['hk', HOME.hk]]);
  seg('sort', 'sort', [['fit', 'Best fit'], ['cost', 'Cheapest'], ['weather', 'Best weather'], ['travel', 'Least travel']]);
  seg('country', 'country', ['All', ...new Set(D.dests.map(d => d.country))].map(c => [c, c]));

  function list() {
    let L = D.dests.filter(d => S.country === 'All' || d.country === S.country);
    const c = d => cost(d, opt(d, S.style)).total;
    if (S.sort === 'fit') L.sort((a, b) => b.fit - a.fit || c(a) - c(b));
    if (S.sort === 'cost') L.sort((a, b) => c(a) - c(b));
    if (S.sort === 'weather') L.sort((a, b) => b.scores.weather - a.scores.weather || b.fc.score - a.fc.score || a.fc.cc - b.fc.cc);
    if (S.sort === 'travel') L.sort((a, b) => opt(a, S.style).travel - opt(b, S.style).travel || c(a) - c(b));
    return L;
  }

  // ---- chart
  const tip = document.getElementById('tip');
  function tipHtml(d, p) {
    return `<b>${esc(d.short)} · ${S.style} · ${esc(HOME[S.home])}</b>
      <div class="tl"><span>Flights out (×2)</span><span>${eur(p.out)}</span></div>
      <div class="tl"><span>Her flight to HK</span><span>${eur(p.her)}</span></div>
      <div class="tl"><span>Your way home</span><span>${eur(p.his)}</span></div>
      <div class="tl"><span>Rooms (6 nights)</span><span>${eur(p.rooms)}</span></div>
      <div class="tl"><span>Food (two)</span><span>${eur(p.food)}</span></div>
      <div class="tl"><span>Getting around</span><span>${eur(p.transport)}</span></div>
      <div class="tl"><span>Activities + misc</span><span>${eur(p.activities + p.misc)}</span></div>
      <div class="tl" style="border-top:1px solid currentColor;margin-top:3px;padding-top:3px"><span>Total for two</span><span>${eur(p.total)}</span></div>
      <div class="tl"><span>Your share · hers</span><span>${eur(p.his_share)} · ${eur(p.her_share)}</span></div>`;
  }
  function chart(L) {
    const all = L.map(d => cost(d, opt(d, S.style)).total);
    const max = Math.max(1000, Math.ceil(Math.max(...all, 0) / 500) * 500 + 250);
    const pct = v => (100 * v / max);
    const step = max > 2000 ? 1000 : 500;
    const ticks = []; for (let v = 0; v <= max; v += step) ticks.push(v);
    document.getElementById('chart-sub').textContent = `For the two of you: ${S.style} plan · ${HOME[S.home]}. Hover or tap a bar for the split.`;
    const rows = document.getElementById('rows');
    rows.innerHTML = L.map(d => {
      const o = opt(d, S.style), p = cost(d, o);
      return `<div class="row" tabindex="0" data-id="${d.id}"><div class="lbl">${esc(d.short)}<small>fit ${d.fit} · ${fmtH(o.travel)} travel</small></div>
        <div class="track"><div class="gridlines">${ticks.slice(1).map(v => `<i style="left:${pct(v)}%"></i>`).join('')}</div>
        <div class="bar" style="width:calc(${pct(p.total)}% - 2px)"><b class="f" style="width:${100 * p.flights / p.total}%"></b><b class="g" style="width:${100 * p.ground / p.total}%"></b></div>
        <span class="val">${eur(p.total)}</span></div></div>`;
    }).join('');
    document.getElementById('ticks').innerHTML = ticks.map(v => `<span style="left:${pct(v)}%">€${v.toLocaleString('en-GB')}</span>`).join('');
    const card = document.getElementById('chart');
    rows.querySelectorAll('.row').forEach(r => {
      const show = () => {
        const d = D.dests.find(x => x.id === r.dataset.id), p = cost(d, opt(d, S.style));
        tip.innerHTML = tipHtml(d, p); tip.hidden = false;
        const cr = card.getBoundingClientRect(), rr = r.getBoundingClientRect();
        let top = rr.bottom - cr.top + 4;
        if (top + tip.offsetHeight > card.offsetHeight) top = rr.top - cr.top - tip.offsetHeight - 4;
        const left = Math.max(8, Math.min(card.offsetWidth - tip.offsetWidth - 8, rr.left - cr.left + rr.width * 0.45));
        tip.style.top = top + 'px'; tip.style.left = left + 'px';
      };
      r.addEventListener('mouseenter', show); r.addEventListener('focus', show); r.addEventListener('click', show);
      r.addEventListener('mouseleave', () => tip.hidden = true); r.addEventListener('blur', () => tip.hidden = true);
    });
    document.getElementById('cost-table').innerHTML = `<thead><tr><th>Trip</th><th class="r">Out ×2</th><th class="r">Her back</th><th class="r">You home</th><th class="r">Rooms</th><th class="r">Food</th><th class="r">Transport</th><th class="r">Act. + misc</th><th class="r">Total</th><th class="r">You · her</th></tr></thead><tbody>` +
      L.map(d => { const p = cost(d, opt(d, S.style)); return `<tr><td>${esc(d.short)}</td><td class="r">${eur(p.out)}</td><td class="r">${eur(p.her)}</td><td class="r">${eur(p.his)}</td><td class="r">${eur(p.rooms)}</td><td class="r">${eur(p.food)}</td><td class="r">${eur(p.transport)}</td><td class="r">${eur(p.activities + p.misc)}</td><td class="r"><b>${eur(p.total)}</b></td><td class="r">${eur(p.his_share)} · ${eur(p.her_share)}</td></tr>`; }).join('') + '</tbody>';
  }

  // ---- forecast
  const slug = c => ({ 'Dry': 'dry', 'Showers': 'show', 'Wet': 'wet', 'Heavy rain': 'heavy' }[c]);
  const fcCls = sc => sc >= 4.5 ? 'Dry' : sc >= 3.5 ? 'Showers' : sc >= 2.5 ? 'Wet' : 'Heavy rain';
  const short = c => c === 'Heavy rain' ? 'Heavy' : c;
  const tips = {};
  let tipN = 0;
  const temps = (hi, lo) => hi === null || hi === undefined || hi === '' ? '—' : `${hi}°/${lo}°`;
  function fcCell(c, label, hi, lo, p1, rough, tipT, cc) {
    const k = 't' + (tipN++); tips[k] = tipT + `<div class="tl"><span>Sky by day</span><span>${SKY[skyKey(cc)]} · ${cc}% cloud</span></div>`;
    return `<td class="fc c-${slug(c)}${rough ? ' rough' : ''}" tabindex="0" data-k="${k}" aria-label="${esc(label)}: ${esc(c)}, ${p1}% chance of rain, ${SKY[skyKey(cc)]}"><em><i class="sk sk-${skyKey(cc)}"></i>${short(c)}</em><b>${p1}%</b><span>${temps(hi, lo)}</span></td>`;
  }
  function fcHead() {
    return `<thead><tr><th></th>${D.fc_bands.map(b => `<th class="band" colspan="${b.n}">${esc(b.label)}</th>`).join('')}</tr>
      <tr><th></th>${D.fc_days.map(x => `<th>${esc(x.label.replace(/ (Oct|Nov)$/, ''))}</th>`).join('')}</tr></thead>`;
  }
  function fcGrid(L) {
    const rows = L.map(d => `<tr><th class="rowh" scope="row"><a href="#${d.id}">${esc(d.short)}</a><small>${d.fc.score}/5 · ${esc(d.fc.word)} · ${esc(SKY[skyKey(d.fc.cc)])} · temps ${esc(d.fc.bases[0])}</small></th>${
      d.fc.days.map(x => fcCell(x.cls, `${d.short} ${x.label}`, x.hi, x.lo, x.p1, !x.scored,
        `<b>${esc(d.short)} · ${esc(x.label)}</b><div style="margin-bottom:4px">${x.ahead} days out (from ${esc(D.fc_checked)})${x.scored ? '' : ' · only if you stay'}</div>` +
        x.bases.map(b => `<div class="tl"><span>${esc(b.name)}</span><span>${temps(b.hi, b.lo)} · ${b.p1}% · ${b.med} mm · ${b.cc}% cloud</span></div>`).join(''), x.cc)).join('')}</tr>`).join('');
    document.getElementById('fc-table').innerHTML = fcHead() + `<tbody>${rows}</tbody>`;
  }
  function fcPanel(d) {
    const rows = d.fc.bases.map(b => `<tr><th class="rowh" scope="row">${esc(b)}</th>${d.fc.per_base[b].map(x => fcCell(x.cls, `${b} ${x.label}`, x.hi, x.lo, x.p1, x.md > D.fc_last,
      `<b>${esc(b)} · ${esc(x.label)}</b><div class="tl"><span>High / low</span><span>${temps(x.hi, x.lo)}</span></div><div class="tl"><span>Chance of rain</span><span>${x.p1}%</span></div><div class="tl"><span>Chance of 10 mm+</span><span>${x.p10}%</span></div><div class="tl"><span>Typical amount</span><span>${x.med} mm</span></div>`, x.cc)).join('')}</tr>`).join('');
    return `<p class="fc-note">${esc(d.fc.note)}</p><div class="fc-wrap"><table class="fc">${fcHead()}<tbody>${rows}</tbody></table></div>`;
  }
  const gtip = document.getElementById('gtip');
  function showTip(td) {
    gtip.innerHTML = tips[td.dataset.k] || ''; gtip.hidden = false;
    const r = td.getBoundingClientRect(), w = gtip.offsetWidth, h = gtip.offsetHeight;
    let top = r.bottom + 6; if (top + h > window.innerHeight - 8) top = r.top - h - 6;
    gtip.style.top = Math.max(8, top) + 'px';
    gtip.style.left = Math.max(8, Math.min(window.innerWidth - w - 8, r.left + r.width / 2 - w / 2)) + 'px';
  }
  const hideTip = () => { gtip.hidden = true; };
  document.addEventListener('mouseover', e => { const td = e.target.closest('td.fc'); td ? showTip(td) : hideTip(); });
  document.addEventListener('focusin', e => { const td = e.target.closest('td.fc'); td ? showTip(td) : hideTip(); });
  document.addEventListener('click', e => { const td = e.target.closest('td.fc'); td ? showTip(td) : hideTip(); });
  window.addEventListener('scroll', hideTip, { passive: true });

  // ---- dossiers
  const tabState = {};
  const planSel = {};
  const EFF = { 'Travel': 'travel', 'Easy': 'easy', 'Active': 'active', 'Big day': 'big' };
  function wxChip(d, wx, i) {
    if (!wx || !d.fc.per_base[wx] || !D.fc_days[i]) return '';
    const md = D.fc_days[i].md, x = d.fc.per_base[wx].find(y => y.md === md);
    if (!x) return '';
    return `<span class="wxchip c-${slug(x.cls)}" title="Forecast for ${esc(wx)}, from ${esc(D.fc_checked)}: ${SKY[skyKey(x.cc)]}, ${x.cc}% cloud"><i class="sk sk-${skyKey(x.cc)}"></i>${esc(wx)} · ${short(x.cls)} ${x.p1}%${x.hi !== null && x.hi !== undefined ? ` · ${x.hi}°/${x.lo}°` : ''}</span>`;
  }
  function trCol(x) {
    const t = x.tr.reduce((a, l) => a + l[2], 0);
    const lvl = t === 0 ? 'none' : t < 90 ? 'low' : t < 180 ? 'mid' : 'high';
    return `<div class="day-tr tr-${lvl}"><span class="ttl">Transport</span><span class="tt">${t ? fmtH(t) : '0'}</span>
      <span class="ttbar" aria-hidden="true"><b style="width:${Math.min(100, 100 * t / 360)}%"></b></span>
      ${x.tr.length ? `<ul>${x.tr.map(l => `<li><i>${MODE[l[0]]}</i> ${esc(l[1])} · <b>${fmtH(l[2])}</b></li>`).join('')}</ul>` : '<ul><li>On foot all day</li></ul>'}</div>`;
  }
  function dayByDay(d, o) {
    const n = {}; o.days.forEach(x => { n[x.e] = (n[x.e] || 0) + 1; });
    const sum = ['Travel', 'Easy', 'Active', 'Big day'].filter(k => n[k]).map(k => k === 'Big day' ? `${n[k]} big day${n[k] > 1 ? 's' : ''}` : `${n[k]} ${k.toLowerCase()}`).join(' · ');
    const solo = S.home === 'sat' ? `<li class="day solo"><div class="day-when"><b>+1</b><span class="dt">${esc(D.dates[7])}</span><span class="eff eff-easy">You</span></div><div class="day-body"><div class="day-top"><h5>Your solo day</h5></div><p>${pl(d.solo_day, d.id)}</p></div><div class="day-tr tr-none"><span class="ttl">Transport</span><span class="tt">—</span></div></li>` : '';
    return `<div class="dbd-head"><h4>Day by day · ${esc(o.name)}</h4><span class="dbd-sum">${sum}</span></div>
      <p class="wk"><span><b>${fmtH(o.travel)}</b> of transport</span><span><b>${o.beds}</b> different beds, ${o.moves} move${o.moves === 1 ? '' : 's'}</span></p>
      ${PLACES.length ? '<p class="pl-hint">Tap or hold an <i>underlined place</i> to see what it is, why go, and where.</p>' : ''}
      <ol class="days">${o.days.map((x, i) => `<li class="day">
        <div class="day-when"><b>Day ${i + 1}</b><span class="dt">${esc(D.dates[i])}</span><span class="eff eff-${EFF[x.e]}">${esc(x.e)}</span></div>
        <div class="day-body"><div class="day-top"><h5>${pl(x.t, d.id)}</h5>${wxChip(d, x.wx, i)}</div>
          <dl class="parts"><dt>Morning</dt><dd>${pl(x.am, d.id)}</dd><dt>Afternoon</dt><dd>${pl(x.pm, d.id)}</dd>${x.eve ? `<dt>Evening</dt><dd>${pl(x.eve, d.id)}</dd>` : ''}</dl>
          <p class="day-sleep"><span class="lb">Sleep</span><span>${pl(x.sleep, d.id)}</span></p>${x.b ? `<p class="day-b"><span class="lb">If it rains</span><span>${pl(x.b, d.id)}</span></p>` : ''}</div>${trCol(x)}</li>`).join('')}${solo}</ol>`;
  }
  function plansPanel(d) {
    const chosen = planSel[d.id] || S.style;
    const opts = d.options.map(o => {
      const p = cost(d, o), on = o.style === chosen;
      return `<div class="opt ${on ? 'sel' : ''}" role="button" tabindex="0" aria-pressed="${on}" data-trip="${d.id}" data-style="${o.style}"><div class="opt-top"><span class="chip">${o.style}</span><span class="opt-cost">${eur(p.total)}</span></div>
        <h5>${esc(o.name)}</h5>
        <div class="mix" aria-hidden="true"><span class="c" style="width:${o.chill}%"></span><span class="a" style="width:${100 - o.chill}%"></span></div>
        <span class="mixl">${o.chill}% slow · ${100 - o.chill}% active</span>
        <ol>${o.route.map(s => `<li>${pl(s, d.id)}</li>`).join('')}</ol>
        <p class="opt-tt"><span><b>${fmtH(o.travel)}</b> of transport</span><span><b>${o.beds}</b> different beds</span></p>
        <p class="bd">For two: flights ${eur(p.flights)} · rooms ${eur(p.rooms)} · food ${eur(p.food)} · transport ${eur(p.transport)} · activities + misc ${eur(p.activities + p.misc)}. You ${eur(p.his_share)}, her ${eur(p.her_share)}.</p>
        <span class="opt-go">${on ? 'Day by day below ↓' : 'See it day by day'}</span></div>`;
    }).join('');
    return `<p class="pick-hint">Tap a plan to read it day by day.</p><div class="opts">${opts}</div><div class="dbd" id="dbd-${d.id}">${dayByDay(d, d.options.find(o => o.style === chosen))}</div>`;
  }
  function roomsPanel(d) {
    return `<div class="rooms">${d.options.map(o => `<div><h4>${esc(o.style)} · ${esc(o.name)}</h4><table class="plain"><thead><tr><th>Night</th><th>Where</th><th class="r">Room for two</th></tr></thead><tbody>${
      o.nights.map((n, i) => `<tr><td>${esc(D.dates[i])}</td><td>${pl(n.place, d.id)}${n.meals ? ' <span class="chip">dinner + breakfast</span>' : ''}</td><td class="r">${eur(n.room)}</td></tr>`).join('')
    }<tr><td></td><td><b>6 nights</b></td><td class="r"><b>${eur(o.nights.reduce((a, n) => a + n.room, 0))}</b></td></tr></tbody></table></div>`).join('')}
      <p class="fc-note">Typical prices for the cheapest decent private double (estimates, not quotes). Your night alone if you stay on Friday: about ${eur(d.solo_night)}.</p></div>`;
  }
  function homePanel(d) {
    return `<div class="homes">${['fri', 'sat', 'hk'].map(k => { const h = d.homes[k], on = k === S.home;
      return `<div class="home ${on ? 'sel' : ''}"><div class="opt-top"><span class="chip">${esc(HOME[k])}</span><span class="opt-cost">${eur(h.price)}</span></div>
        <ul>${h.legs.map(l => `<li><b>${esc(l.route)}</b> ${eur(l.price)} ${fs(l.status)}<small>${esc(l.detail)}</small></li>`).join('')}${h.extra ? `<li>${esc(h.extra)}</li>` : ''}</ul>
        <p class="bd">${esc(h.note)}</p></div>`; }).join('')}</div>`;
  }
  function tabList() { return [['plans', '2 plans, day by day'], ['home', 'Your way home'], ['rooms', 'Rooms'], ['fc', 'Forecast'], ['todo', 'Things to do'], ['prac', 'Scores & practical']]; }
  function dossier(d) {
    const sel = opt(d, S.style), sp = cost(d, sel), r = range(d);
    const tab = tabState[d.id] || 'plans';
    const todo = `<div class="todo"><div><h4>Highlights</h4><div class="adv">${d.adventure.map(a => `<div><b>${esc(a.name)}</b><span class="p">${esc(a.price)}</span><small>${esc(a.note)}</small></div>`).join('')}</div></div>
      <div style="display:grid;gap:16px;align-content:start"><div><h4>Hikes & walks</h4><ul>${d.hikes.map(h => `<li>${pl(h, d.id)}</li>`).join('')}</ul></div>
      <div><h4>Food</h4><ul>${d.food.map(h => `<li>${pl(h, d.id)}</li>`).join('')}</ul></div>
      <div><h4>Culture &amp; city</h4><ul>${d.culture.map(h => `<li>${pl(h, d.id)}</li>`).join('')}</ul></div></div></div>`;
    const prac = `<div class="prac"><div><h4>Fit score breakdown (out of 5)</h4><div style="display:grid;gap:6px">${D.criteria.map(([k, l]) => `<div class="sb"><span>${esc(l)}</span><span class="t"><b style="width:${d.scores[k] * 20}%"></b></span><span class="v">${d.scores[k]}</span></div>`).join('')}</div></div>
      <div><p><span class="k">Forecast. </span>${esc(d.fc.note)}</p><p><span class="k">Climate. </span>${esc(d.weather.note)}</p><p><span class="k">Getting around. </span>${esc(d.transport)}</p><p><span class="k">Crowds. </span>${esc(d.crowds)}</p><p><span class="k">Entry. </span>${esc(d.entry)}</p>
      <p><span class="k">Flight alternatives. </span>Out: ${esc(d.out.alt)}. Her return: ${esc(d.her.alt)}.</p></div></div>`;
    const panels = { plans: plansPanel(d), home: homePanel(d), rooms: roomsPanel(d), fc: fcPanel(d), todo, prac };
    return `<article class="trip" id="${d.id}">
      <div class="trip-head"><span class="cc">${d.cc}</span>
        <div><p class="eyebrow">${esc(d.country)} · ${esc(d.region)}</p><h3>${esc(d.title)}</h3><p class="tag">${esc(d.tagline)}</p></div>
        <div class="nums"><div><span class="n fitpill">${d.fit}</span><span class="l">fit / 100</span></div>
          <div><span class="n">${eur(sp.total)}</span><span class="l">${S.style}, for two</span><span class="rg">you ${eur(sp.his_share)} · her ${eur(sp.her_share)}</span></div></div></div>
      <dl class="facts">
        <div><dt>Out · Sat 31 Oct · both</dt><dd><span class="price">${eur(d.out.price)}</span> each · ${esc(d.out.route)} ${fs(d.out.status)}<small>${esc(d.out.detail)}</small></dd></div>
        <div><dt>Her · Fri 6 Nov → HK</dt><dd><span class="price">${eur(d.her.price)}</span> ${esc(d.her.route)} ${fs(d.her.status)}<small>${esc(d.her.detail)}</small></dd></div>
        <div><dt>You · ${esc(HOME[S.home])}</dt><dd><span class="price">${eur(d.homes[S.home].price)}</span> ${esc(d.homes[S.home].legs.map(l => l.route).join(' + '))} ${d.homes[S.home].legs.some(l => l.status === 'est') ? fs('est') : fs('gf27')}<small>${esc(d.homes[S.home].note)}</small></dd></div>
        <div><dt>Forecast 31 Oct–6 Nov</dt><dd><span class="fcw-pill c-${slug(fcCls(d.fc.score))}">${esc(d.fc.word)}</span> <span class="mono">${d.fc.score}/5</span><small><i class="sk sk-${skyKey(d.fc.cc)}"></i>${esc(SKY[skyKey(d.fc.cc)])}, ${d.fc.cc}% cloud by day</small><small>Normal for early Nov: ${d.weather.lo}–${d.weather.hi}°C, ${esc(d.weather.rain)}</small></dd></div>
      </dl>
      <div class="pc"><div class="pros"><h4>Pros</h4><ul>${d.pros.map(x => `<li>${esc(x)}</li>`).join('')}</ul></div>
        <div class="cons"><h4>Cons</h4><ul>${d.cons.map(x => `<li>${esc(x)}</li>`).join('')}</ul></div></div>
      <div class="calm"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M2 17l5-7 4 5 3-4 8 6"/><path d="M2 21c2-1.2 4-1.2 6 0s4 1.2 6 0 4-1.2 6 0"/><circle cx="17" cy="6" r="2.2"/></svg><div><h4>Calm days by the sea or in the mountains</h4><p>${pl(d.calm, d.id)}</p></div></div>
      <div class="tabs" role="tablist" data-id="${d.id}">
        ${tabList().map(([k, l]) => `<button type="button" role="tab" id="tab-${d.id}-${k}" aria-controls="pn-${d.id}-${k}" aria-selected="${tab === k}" data-k="${k}">${l}</button>`).join('')}
      </div>
      ${tabList().map(([k]) => `<div class="panel" role="tabpanel" id="pn-${d.id}-${k}" aria-labelledby="tab-${d.id}-${k}" ${tab === k ? '' : 'hidden'}>${panels[k]}</div>`).join('')}
    </article>`;
  }
  const trips = document.getElementById('trips');
  function pickPlan(card) {
    const id = card.dataset.trip; planSel[id] = card.dataset.style;
    const d = D.dests.find(x => x.id === id);
    document.getElementById(`pn-${id}-plans`).innerHTML = plansPanel(d);
    const box = document.getElementById(`dbd-${id}`);
    if (box && box.getBoundingClientRect().top > window.innerHeight * 0.6) box.scrollIntoView({ behavior: matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth', block: 'start' });
    const again = document.querySelector(`#pn-${id}-plans .opt[data-style="${card.dataset.style}"]`); if (again) again.focus({ preventScroll: true });
  }
  trips.addEventListener('keydown', e => {
    const card = e.target.closest('.opt[data-style]');
    if (card && (e.key === 'Enter' || e.key === ' ')) { e.preventDefault(); pickPlan(card); }
  });
  trips.addEventListener('click', e => {
    const card = e.target.closest('.opt[data-style]'); if (card) { pickPlan(card); return; }
    const b = e.target.closest('.tabs button'); if (!b) return;
    const id = b.parentElement.dataset.id, k = b.dataset.k; tabState[id] = k;
    b.parentElement.querySelectorAll('button').forEach(x => x.setAttribute('aria-selected', x.dataset.k === k));
    tabList().forEach(([p]) => { const el = document.getElementById(`pn-${id}-${p}`); if (el) el.hidden = p !== k; });
  });

  function render() {
    const L = list();
    for (const k in tips) delete tips[k];
    renderBoard(); renderPicks();
    fcGrid(L);
    chart(L);
    trips.innerHTML = L.map(dossier).join('');
  }
  render();

  // ---- place card
  if (PLACES.length) {
    const card = document.createElement('div');
    card.id = 'placecard'; card.hidden = true; card.setAttribute('role', 'dialog');
    document.body.appendChild(card);
    let cardFor = null, holdT = null, held = false;
    const openPlace = el => {
      const p = PLACES[+el.dataset.p]; if (!p) return;
      if (cardFor) cardFor.classList.remove('on');
      cardFor = el; el.classList.add('on');
      card.setAttribute('aria-label', p.n);
      card.innerHTML = `<div class="pc-h"><b>${esc(p.n)}</b><button type="button" class="pc-x" aria-label="Close">×</button></div>
        <dl class="pc-d"><dt>What</dt><dd>${esc(p.w)}</dd><dt>Why go</dt><dd>${esc(p.y)}</dd><dt>Where</dt><dd>${esc(p.l)}</dd></dl>
        <a class="pc-map" href="https://www.google.com/maps/search/?api=1&query=${encodeURIComponent(p.q)}" target="_blank" rel="noopener">Open in Google Maps ↗</a>`;
      card.hidden = false;
    };
    const closePlace = () => { card.hidden = true; if (cardFor) { cardFor.classList.remove('on'); cardFor = null; } };
    const plOf = e => e.target && e.target.closest ? e.target.closest('.pl') : null;
    document.addEventListener('click', e => {
      const el = plOf(e);
      if (el) {
        e.preventDefault(); e.stopPropagation();
        if (held) { held = false; return; }
        if (cardFor === el && !card.hidden) closePlace(); else openPlace(el);
        return;
      }
      if (e.target.closest && e.target.closest('.pc-x')) { e.preventDefault(); closePlace(); return; }
      if (!card.hidden && !(e.target.closest && e.target.closest('#placecard'))) closePlace();
    }, true);
    document.addEventListener('keydown', e => {
      if (e.key === 'Escape' && !card.hidden) { closePlace(); return; }
      const el = plOf(e);
      if (el && (e.key === 'Enter' || e.key === ' ')) { e.preventDefault(); e.stopPropagation(); openPlace(el); }
    }, true);
    document.addEventListener('pointerdown', e => {
      const el = plOf(e); held = false; clearTimeout(holdT);
      if (el) holdT = setTimeout(() => { held = true; openPlace(el); if (navigator.vibrate) navigator.vibrate(8); }, 420);
    }, true);
    ['pointerup', 'pointercancel', 'scroll'].forEach(t => document.addEventListener(t, () => clearTimeout(holdT), true));
    document.addEventListener('contextmenu', e => { if (plOf(e)) e.preventDefault(); }, true);
  }

  document.getElementById('sources').innerHTML = D.sources.map(([n, u, note]) => `<li><a href="${esc(u)}" target="_blank" rel="noopener">${esc(n)}</a>${note ? ` <span style="color:var(--muted)">(${esc(note)})</span>` : ''}</li>`).join('');
})();
