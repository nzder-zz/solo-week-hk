"""Build the duo page (duo/index.html + offline worker + manifest) and the spreadsheet.
Usage:  python3 duo-src/build_all.py            -> page only
        python3 duo-src/build_all.py --xlsx OUT -> page + spreadsheet at OUT
Then commit and push (see duo-src/README.md)."""
import hashlib, json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_data import build

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
OUT_DIR = os.path.join(ROOT, "duo")
T = os.path.join(HERE, "template")

FONTS = sorted(f for f in os.listdir(os.path.join(ROOT, "fonts")) if f.endswith(".woff2"))
ICONS = ["icon-192.png", "icon-512.png", "icon-maskable-512.png", "apple-touch-icon.png", "favicon-32.png"]

SW_REGISTER = r"""(function () {
  var foot = document.querySelector('footer .wrap');
  var s = document.createElement('span');
  s.id = 'offline-status';
  s.style.cssText = 'display:block;margin-top:6px;opacity:.8';
  if (foot) foot.appendChild(s);
  function set(t) { s.textContent = t; }
  if (!('serviceWorker' in navigator)) { set('This browser cannot keep an offline copy.'); return; }
  set('Saving an offline copy…');
  navigator.serviceWorker.register('./sw.js', { scope: './' }).then(function () {
    return navigator.serviceWorker.ready;
  }).then(function () {
    set('Saved for offline use. Open this page again any time, even without a connection.');
  }).catch(function () { set('Offline copy not saved yet: open the page once while online.'); });
  // An older solo-page worker may have cached this page in place of the solo page: put the solo page back.
  if (window.caches && navigator.onLine) {
    caches.keys().then(function (keys) {
      keys.filter(function (k) { return k.indexOf('solo-week-') === 0; }).forEach(function (k) {
        caches.open(k).then(function (c) {
          var solo = new URL('../index.html', location.href).href;
          c.match(solo).then(function (hit) {
            if (!hit) return;
            hit.clone().text().then(function (t) {
              if (t.indexOf('Departures <span>for two</span>') !== -1) {
                fetch(new URL('../', location.href).href, { cache: 'no-store' }).then(function (r) { if (r.ok) c.put(solo, r); });
              }
            });
          });
        });
      });
    }).catch(function () {});
  }
})();"""

SW = """// Offline support for the duo page: every file is cached on first visit, then served from the cache.
// The cache name changes with the content, so a new version replaces the old one on the next online visit.
const CACHE = 'duo-week-%(hash)s';
const ASSETS = %(assets)s;

self.addEventListener('install', event => {
  event.waitUntil(caches.open(CACHE).then(c => c.addAll(ASSETS)).then(() => self.skipWaiting()));
});

self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys()
      .then(keys => Promise.all(keys.filter(k => k.startsWith('duo-week-') && k !== CACHE).map(k => caches.delete(k))))
      .then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', event => {
  const req = event.request;
  if (req.method !== 'GET' || new URL(req.url).origin !== self.location.origin) return;
  const url = new URL(req.url);
  const scope = new URL('./', self.location).pathname;
  const isPage = req.mode === 'navigate' || url.pathname === scope || url.pathname === scope + 'index.html';
  if (req.mode === 'navigate' && !url.pathname.startsWith(scope)) return;
  event.respondWith(caches.open(CACHE).then(cache => {
    const fresh = fetch(req).then(res => {
      if (res && res.ok) cache.put(isPage ? 'index.html' : req, res.clone());
      return res;
    });
    if (isPage) {
      const timeout = new Promise(resolve => setTimeout(resolve, 3000, null));
      return Promise.race([fresh.catch(() => null), timeout]).then(res =>
        (res && res.ok) ? res : cache.match('index.html').then(hit => hit || fresh));
    }
    return cache.match(req, { ignoreSearch: true }).then(hit => {
      if (hit) { event.waitUntil(fresh.catch(() => null)); return hit; }
      return fresh;
    });
  }));
});
"""

MANIFEST = {
    "name": "Week for Two from Hong Kong", "short_name": "Duo Week",
    "description": "Seven ways for two to spend 31 Oct – 6 Nov 2026 after Hong Kong. Works offline.",
    "start_url": "./", "scope": "./", "display": "standalone",
    "background_color": "#F2EFF1", "theme_color": "#241626",
    "icons": [{"src": "../icons/icon-192.png", "sizes": "192x192", "type": "image/png"},
              {"src": "../icons/icon-512.png", "sizes": "512x512", "type": "image/png"},
              {"src": "../icons/icon-maskable-512.png", "sizes": "512x512", "type": "image/png", "purpose": "maskable"}],
}


def page(D):
    css = open(os.path.join(T, "style.css")).read()
    body = open(os.path.join(T, "body.html")).read().replace("{{CHECKED}}", D["checked"]).replace("{{FC_CHECKED}}", D["fc_checked"])
    js = open(os.path.join(T, "app.js")).read()
    data = json.dumps(D, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Week for Two</title>
<meta name="description" content="Seven ways for two to spend the week after Hong Kong (31 Oct – 6 Nov 2026): flights, private rooms, checks after Typhoon Champi, forecast and day-by-day plans. Works offline.">
<meta name="theme-color" media="(prefers-color-scheme: light)" content="#F2EFF1">
<meta name="theme-color" media="(prefers-color-scheme: dark)" content="#161016">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-title" content="Duo Week">
<link rel="manifest" href="manifest.webmanifest">
<link rel="icon" type="image/png" sizes="32x32" href="../icons/favicon-32.png">
<link rel="apple-touch-icon" href="../icons/apple-touch-icon.png">
<style>
{css}
</style>
</head>
<body>
{body}
<script type="application/json" id="data">{data}</script>
<script>
{js}
</script>
<script>
{SW_REGISTER}
</script>
</body>
</html>
"""


def main():
    D = build()
    os.makedirs(OUT_DIR, exist_ok=True)
    html = page(D)
    open(os.path.join(OUT_DIR, "index.html"), "w").write(html)
    json.dump(MANIFEST, open(os.path.join(OUT_DIR, "manifest.webmanifest"), "w"), indent=2)
    assets = ["./", "index.html", "manifest.webmanifest"] + [f"../icons/{i}" for i in ICONS] + [f"../fonts/{f}" for f in FONTS]
    h = hashlib.sha1((html + json.dumps(MANIFEST)).encode()).hexdigest()[:10]
    open(os.path.join(OUT_DIR, "sw.js"), "w").write(SW % {"hash": h, "assets": json.dumps(assets, indent=2)})
    json.dump(D, open(os.path.join(HERE, "duo_data.json"), "w"), ensure_ascii=False, indent=1)
    print("page", len(html), "bytes; cache", h)
    if "--xlsx" in sys.argv:
        from build_xlsx import build_xlsx
        out = sys.argv[sys.argv.index("--xlsx") + 1]
        build_xlsx(D, out)
        print("xlsx", out)


if __name__ == "__main__":
    main()
