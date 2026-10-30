"""Builds the Tokyo + Kawaguchiko page from plan.py.
Writes fuji/index.html, fuji/sw.js and fuji/manifest.webmanifest.  Run: python3 fuji-src/build.py
Checks every [[place]] and {{link}} marker and every CHOICE before writing anything."""
import hashlib, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
OUT = os.path.join(ROOT, "fuji")
sys.path.insert(0, HERE)
import plan as P  # noqa: E402

errors = []


def scan(text, where):
    for pid in re.findall(r"\[\[([a-z0-9_]+)\]\]", text):
        if pid not in P.PLACES:
            errors.append(f"{where}: unknown place [[{pid}]]")
    for lid in re.findall(r"\{\{([a-z0-9_]+)\}\}", text):
        if lid not in P.LINKS:
            errors.append(f"{where}: unknown link {{{{{lid}}}}}")


days = []
for d in P.DAYS:
    choice = P.CHOICE.get(d["id"], next(iter(d["versions"])))
    if choice not in d["versions"]:
        errors.append(f"CHOICE[{d['id']}] = {choice!r}, but the day only has {list(d['versions'])}")
    f = P.FORECAST.get(d["fc"], {}).get(d["md"])
    wx = None
    if f:
        wx = {"sky": f[0], "pop": f[1], "lo": f[2], "hi": f[3], "rough": len(f) > 4}
    versions = []
    for key, v in d["versions"].items():
        for t, txt in v["steps"]:
            scan(txt, f"{d['id']}/{key}")
        scan(v.get("watch", ""), f"{d['id']}/{key} watch")
        versions.append({"key": key, "label": v["label"], "title": v["title"], "why": v.get("why", ""),
                         "steps": [list(s) for s in v["steps"]], "watch": v.get("watch", "")})
    days.append({"id": d["id"], "date": d["date"], "where": d["where"], "who": d["who"], "bed": d["bed"],
                 "fc": d["fc"], "wx": wx, "choice": choice, "versions": versions})

for i, (t, txt) in enumerate(P.IDEAS):
    scan(txt, f"idea {i}")
for i, txt in enumerate(P.CHECKLIST):
    scan(txt, f"checklist {i}")
for b in P.BEDS:
    for o in b["options"]:
        if o not in P.PLACES:
            errors.append(f"bed option {o} not in PLACES")
for l in P.FC_META["links"]:
    if l not in P.LINKS:
        errors.append(f"forecast link {l} not in LINKS")

if errors:
    print("Not built:\n  " + "\n  ".join(errors))
    sys.exit(1)

data = {
    "trip": P.TRIP, "updated": P.UPDATED, "fc_meta": P.FC_META, "fc_summary": P.FC_SUMMARY,
    "days": days,
    "places": {k: {"name": v[0], "q": v[1], "note": v[2]} for k, v in P.PLACES.items()},
    "links": {k: {"label": v[0], "url": v[1], "kind": v[2]} for k, v in P.LINKS.items()},
    "beds": P.BEDS, "ideas": [list(x) for x in P.IDEAS], "checklist": P.CHECKLIST,
}
blob = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")

# Fonts: the same local fonts as the other two pages.
fontcss = "\n".join(l for l in open(os.path.join(ROOT, "duo-src", "template", "style.css"), encoding="utf-8")
                    if l.startswith("@font-face"))
tpl = open(os.path.join(HERE, "template.html"), encoding="utf-8").read()
html = (tpl.replace("/*%%FONTS%%*/", fontcss).replace("%%DATA%%", blob)
        .replace("%%TITLE%%", P.TRIP["title"]).replace("%%UPDATED%%", P.UPDATED))
os.makedirs(OUT, exist_ok=True)
open(os.path.join(OUT, "index.html"), "w", encoding="utf-8").write(html)

fonts = sorted(f for f in os.listdir(os.path.join(ROOT, "fonts")) if f.endswith(".woff2"))
assets = ["./", "index.html", "manifest.webmanifest"] + [f"../icons/{i}" for i in
          ["icon-192.png", "icon-512.png", "icon-maskable-512.png", "apple-touch-icon.png", "favicon-32.png"]] + [f"../fonts/{f}" for f in fonts]
digest = hashlib.sha1(html.encode()).hexdigest()[:10]
sw = open(os.path.join(HERE, "sw.template.js"), encoding="utf-8").read()
sw = sw.replace("%%CACHE%%", f"fuji-trip-{digest}").replace("%%ASSETS%%", json.dumps(assets, indent=2))
open(os.path.join(OUT, "sw.js"), "w", encoding="utf-8").write(sw)

manifest = {
    "name": "Tokyo + Kawaguchiko", "short_name": "Fuji trip",
    "description": "Day-by-day plan for Tokyo + Kawaguchiko, 31 Oct – 7 Nov 2026. Works offline.",
    "start_url": "./", "scope": "./", "display": "standalone",
    "background_color": "#F1F3F6", "theme_color": "#1B2A41",
    "icons": [{"src": "../icons/icon-192.png", "sizes": "192x192", "type": "image/png"},
              {"src": "../icons/icon-512.png", "sizes": "512x512", "type": "image/png"},
              {"src": "../icons/icon-maskable-512.png", "sizes": "512x512", "type": "image/png", "purpose": "maskable"}],
}
json.dump(manifest, open(os.path.join(OUT, "manifest.webmanifest"), "w"), indent=2)
print(f"Built fuji/ ({len(html)//1024} KB, {len(days)} days, {len(P.PLACES)} places, {len(P.LINKS)} links, cache fuji-trip-{digest})")
for d in days:
    print(f"  {d['date']:10} {d['choice']:6} {next(v['title'] for v in d['versions'] if v['key'] == d['choice'])}")
