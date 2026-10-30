"""Forecast refresh of 29 Oct 2026: official weekly forecasts replace the 27 Oct model run for 31 Oct – 4/5 Nov.
Japan: JMA weekly forecasts (reportDatetime 28 Oct 17:00 or 29 Oct 11:00 JST, see SRC_TIME).
Taiwan: CWA one-week county forecast, fetched 29 Oct (no rain percentages on that page).
Days after the official forecasts end keep the 27 Oct ECMWF run and are shown as rough.
Temperatures: the official station where it matches the place; mountain bases keep the model's temperatures.
Run once: python3 duo-src/fc_refresh.py  (writes base_data.json; the 27 Oct data is kept under *_27oct keys)."""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
P = os.path.join(HERE, "base_data.json")
B = json.load(open(P))
if "fc_per_base_27oct" not in B:
    B["fc_per_base_27oct"] = B["fc_per_base"]
    B["fc_days_27oct"] = B["fc_days"]
OLD = B["fc_per_base_27oct"]

DAYS = ["10-31", "11-01", "11-02", "11-03", "11-04", "11-05", "11-06", "11-07"]
LABEL = ["Sat 31 Oct", "Sun 1 Nov", "Mon 2 Nov", "Tue 3 Nov", "Wed 4 Nov", "Thu 5 Nov", "Fri 6 Nov", "Sat 7 Nov"]

# JMA weekly: (weather code, chance of precipitation %), from 31 Oct. Temps (lo, hi) where the station fits the place.
# 30 Oct refresh: weekly forecasts issued 30 Oct 11:00 JST, covering 31 Oct – 6 Nov. 31 Oct PoP from the short-term forecast
# (or the 29 Oct 17:00 issue where the short-term value was not read).
JMA = {
    "tokyo":    {"wx": [(101, 10), (101, 20), (200, 40), (101, 20), (101, 20), (202, 50), (201, 30)], "t": [(14, 24), (14, 21), (14, 21), (14, 22), (12, 19), (11, 15), (13, 21)], "time": "30 Oct 11:00"},
    "yamanashi": {"wx": [(100, 10), (101, 20), (202, 50), (101, 20), (201, 30), (202, 50), (201, 30)], "time": "30 Oct 11:00"},
    "kanagawa": {"wx": [(100, 20), (101, 20), (202, 50), (201, 30), (201, 30), (202, 50), (201, 30)], "time": "30 Oct 11:00"},
    "tochigi":  {"wx": [(100, 10), (101, 20), (200, 40), (101, 20), (101, 20), (202, 50), (201, 30)], "time": "30 Oct 11:00"},
    "osaka":    {"wx": [(101, 10), (101, 10), (202, 60), (101, 20), (201, 30), (202, 50), (101, 20)], "t": [(15, 22), (14, 21), (16, 21), (14, 21), (12, 21), (14, 20), (15, 21)], "time": "30 Oct 11:00"},
    "nara":     {"wx": [(101, 10), (101, 10), (202, 60), (101, 20), (201, 30), (202, 50), (101, 20)], "t": [(12, 22), (11, 21), (13, 20), (11, 20), (9, 20), (12, 19), (12, 21)], "time": "30 Oct 11:00"},
    "wakayama": {"wx": [(101, 0), (101, 10), (202, 60), (101, 20), (201, 30), (202, 50), (101, 20)], "time": "30 Oct 11:00"},
    "fukuoka":  {"wx": [(100, 10), (201, 20), (203, 70), (101, 20), (101, 20), (200, 40), (101, 20)], "t": [(15, 23), (14, 24), (17, 22), (15, 21), (14, 21), (15, 22), (15, 21)], "time": "30 Oct 11:00"},
    "oita":     {"wx": [(100, 10), (101, 10), (202, 60), (101, 20), (101, 20), (200, 40), (101, 20)], "time": "30 Oct 11:00"},
    "ishikawa": {"wx": [(203, 70), (200, 40), (202, 60), (200, 40), (201, 30), (202, 50), (202, 50)], "t": [(13, 21), (11, 19), (14, 18), (11, 17), (9, 17), (12, 18), (13, 19)], "time": "30 Oct 11:00"},
    "gifu":     {"wx": [(101, 30), (111, 30), (202, 60), (201, 30), (201, 30), (202, 50), (201, 30)], "time": "30 Oct 11:00"},
    "kumamoto": {"wx": [(100, 0), (101, 10), (202, 60), (101, 20), (101, 20), (200, 40), (101, 20)], "time": "30 Oct 11:00"},
}
# CWA one-week county forecast (daytime wording), read 30 Oct, 31 Oct – 5 Nov, with (lo, hi).
CWA = {
    "tainan":  [("晴時多雲", 24, 29), ("晴時多雲", 24, 30), ("晴時多雲", 24, 30), ("晴時多雲", 24, 29), ("晴時多雲", 24, 29), ("晴時多雲", 24, 29)],
    "chiayi":  [("晴時多雲", 22, 31)] * 6,
    "nantou":  [("晴時多雲", 21, 30), ("晴時多雲", 22, 31), ("晴時多雲", 22, 30), ("晴時多雲", 22, 30), ("晴時多雲", 22, 31), ("晴時多雲", 22, 30)],
    "taitung": [("陰時多雲短暫雨", 22, 29), ("多雲時陰", 23, 30), ("晴時多雲", 23, 30), ("多雲短暫雨", 24, 30), ("多雲短暫雨", 24, 30), ("多雲短暫雨", 24, 29)],
}
CWA_CLS = {"晴時多雲": ("Dry", 35), "多雲時晴": ("Dry", 50), "多雲時陰": ("Dry", 80), "多雲時陰短暫陣雨": ("Showers", 80),
           "陰時多雲短暫雨": ("Showers", 85), "多雲短暫雨": ("Showers", 70)}

# base -> (source, region, use official temps?)
BASES = {
    "Tokyo": ("J", "tokyo", True), "Kawaguchiko": ("J", "yamanashi", False), "Hakone": ("J", "kanagawa", False), "Nikko": ("J", "tochigi", False),
    "Osaka": ("J", "osaka", True), "Nara": ("J", "nara", True), "Koyasan": ("J", "wakayama", False), "Kumano Hongu": ("J", "wakayama", False),
    "Fukuoka": ("J", "fukuoka", True), "Yufuin": ("J", "oita", False), "Kuju": ("J", "oita", False), "Kurokawa": ("J", "kumamoto", False),
    "Kanazawa": ("J", "ishikawa", True), "Yamanaka Onsen": ("J", "ishikawa", False), "Shirakawa-go": ("J", "gifu", False), "Takayama": ("J", "gifu", False),
    "Tainan": ("C", "tainan", True), "Alishan": ("C", "chiayi", False), "Sun Moon Lake": ("C", "nantou", False),
    "Dulan": ("C", "taitung", True), "Luye": ("C", "taitung", False),
}


def jma_cls(code, pop):
    c = code // 100
    if c == 1:
        return "Dry", {100: 20, 101: 35}.get(code, 50)
    if c == 2:
        cc = {200: 80, 201: 60}.get(code, 85)
        if code in (200, 201):
            return ("Showers" if pop >= 40 else "Dry"), cc
        return ("Wet" if pop >= 60 else "Showers" if pop >= 30 else "Dry"), cc
    return ("Heavy rain" if code in (300, 302) and pop >= 80 else "Wet"), 90


out = {}
for base, (src, reg, own_t) in BASES.items():
    old = {x["md"]: x for x in OLD.get(base, [])}
    rows = []
    for i, md in enumerate(DAYS):
        o = old.get(md)
        e = {"md": md, "label": LABEL[i], "p10": None, "med": None}
        if src == "J" and i < len(JMA[reg]["wx"]):
            code, pop = JMA[reg]["wx"][i]
            cls, cc = jma_cls(code, pop)
            t = JMA[reg].get("t")
            hi, lo = (t[i][1], t[i][0]) if (own_t and t and i < len(t)) else ((o["hi"], o["lo"]) if o else (None, None))
            e.update(cls=cls, cc=cc, p1=pop, hi=hi, lo=lo, src="J")
        elif src == "C" and i < len(CWA[reg]):
            w, lo, hi = CWA[reg][i]
            cls, cc = CWA_CLS[w]
            if not own_t:
                hi, lo = (o["hi"], o["lo"]) if o else (None, None)
            e.update(cls=cls, cc=cc, p1=None, hi=hi, lo=lo, src="C", w=w)
        elif o:
            e.update(cls=o["cls"], cc=o["cc"], p1=o["p1"], hi=o["hi"], lo=o["lo"], p10=o["p10"], med=o["med"], src="E")
        else:
            e.update(cls=None, cc=None, p1=None, hi=None, lo=None, src=None)
        rows.append(e)
    out[base] = rows

B["fc_per_base"] = out
B["fc_days"] = [{"md": md, "label": LABEL[i], "ahead": 1 + i} for i, md in enumerate(DAYS)]
B["fc_bands"] = [{"g": 0, "n": 7, "label": "Official forecasts of 30 Oct (JMA, CWA; Taiwan to 5 Nov)"}, {"g": 1, "n": 1, "label": "27 Oct model (rough)"}]
B["fc_last"] = "11-06"
B["fc_checked"] = "30 Oct 2026, 15:00 Hong Kong time"
B["fc_src_time"] = {k: v["time"] for k, v in JMA.items()}
json.dump(B, open(P, "w"), ensure_ascii=False, indent=0)
for b, rows in out.items():
    print(f"{b:14}", " ".join(f"{(r['cls'] or '—')[:5]:5}{'' if r['p1'] is None else r['p1']:>3}{r['src'] or '-'}" for r in rows))
