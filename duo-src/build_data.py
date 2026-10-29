"""Turn trips.py + fares.py + checks.py into the data the page and the spreadsheet use.
All money in euros. Run build_all.py rather than this file directly.

Shape: together Sat 31 Oct -> Wed 4 Nov (she flies back to HK on Wed evening),
you alone Thu 5 + Fri 6, you fly home on Sat 7 Nov."""
import json, os
from fares import OUT, HER, HIS, FARE_STATUS
from trips import TRIPS as OTHER_TRIPS
from trips_tokyo import TRIPS_TOKYO
TRIPS = TRIPS_TOKYO + OTHER_TRIPS
from checks import CHECKS, CHECKED
from places_new import PLACES_NEW

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = json.load(open(os.path.join(HERE, "base_data.json")))

DAYS_TOGETHER = 4          # food days for two (Sat evening .. Wed afternoon)
DAYS_SOLO = 3              # your food days alone (Wed evening .. Sat)
MISC_PP = 20               # SIM, tips, laundry, per person
MEAL_CREDIT = 0.6          # share of a day's food covered when dinner + breakfast come with the room
WEIGHTS = {"hike": 2, "nature": 2, "food": 2, "culture": 2, "chill": 2, "weather": 2, "value": 1.5, "ease": 1}
CRITERIA = [["hike", "Hiking"], ["nature", "Nature"], ["food", "Food"], ["culture", "Culture & cities"],
            ["chill", "Relaxed pace"], ["weather", "Weather"], ["value", "Value"], ["ease", "Ease for two"]]
POINTS = {"Dry": 1, "Showers": 0.7, "Wet": 0.35, "Heavy rain": 0}
DATES = ["Sat 31 Oct", "Sun 1 Nov", "Mon 2 Nov", "Tue 3 Nov", "Wed 4 Nov", "Thu 5 Nov", "Fri 6 Nov", "Sat 7 Nov"]
ENTRY = {"JP": "Visa-free 90 days for you (French passport); fill in Visit Japan Web", "TW": "Visa-free 90 days for you; online arrival card"}


TOKYO_PLAN = {
    "stay": "Stay in Ueno or Asakusa: the Skyliner from Narita stops at Ueno, the Tobu train to Nikko leaves from Asakusa, and it's the old, walkable side of Tokyo. Same hotel on Sat and Tue nights; leave the big bags there.",
    "days": [
        {"when": "Sat 31 Oct, evening", "what": "Land at Narita 20:00, Skyliner to Ueno (41 min), late ramen."},
        {"when": "Sun 1 Nov, 8:00", "what": "Senso-ji and Nakamise before the crowds, then the train or bus to the town."},
        {"when": "Tue 3 Nov (Culture Day)", "what": "Back by lunchtime. Meiji Jingu's autumn festival: martial arts, noh and gagaku, chrysanthemums, horseback archery (yabusame). Harajuku's back streets. Evening: Omoide Yokocho's yakitori alleys in Shinjuku."},
        {"when": "Wed 4 Nov", "what": "Yanaka's temples and old shopping street at 9, Ueno park, the Tokyo National Museum (open Wed). Ameyoko for lunch, Kappabashi. She leaves Ueno ~16:30 on the Skyliner for her 19:00 flight."},
    ],
    "menu": [
        "Rain plan: the Tokyo National Museum (closed Mon, open Tue holiday and Wed), or teamLab Planets (book ahead).",
        "Food: Tsukiji outer market breakfast, Ameyoko street food, Omoide Yokocho yakitori, a kaiten-zushi in Ueno.",
        "Evening views: the Sumida river at night with the Skytree, or Shibuya Sky at sunset (book ahead).",
        "Missed by a day: Kanda's used-book fair ends Sun 1 Nov.",
    ],
    "solo": "Your Thu–Fri: in the Slow plans you stay in Tokyo (Mt Takao, Kamakura); in the Fuller plans you go to the mountains (Hakone, or Kawaguchiko if you did Hakone together).",
}


def plan_cost(t, p):
    out_pp = OUT[t["out"]]["price"]
    out = 2 * out_pp
    her = HER[t["her"]]["price"]
    his = HIS[t["his"]]["price"]
    both = [n for n in p["nights"] if not n["solo"]]
    solo = [n for n in p["nights"] if n["solo"]]
    rooms = sum(n["room"] for n in both)
    food = 2 * t["food_day"] * DAYS_TOGETHER - 2 * MEAL_CREDIT * t["food_day"] * sum(1 for n in both if n["meals"])
    transport = 2 * p["transport_pp"] + p["shared"]
    activities = 2 * p["activities_pp"]
    misc = 2 * MISC_PP
    solo_rooms = sum(n["room"] for n in solo)
    solo_food = t["solo_food"] * DAYS_SOLO - MEAL_CREDIT * t["solo_food"] * sum(1 for n in solo if n["meals"])
    solo_total = solo_rooms + solo_food + p["solo_transport"] + p["solo_activities"]
    flights = out + her + his
    together = rooms + food + transport + activities + misc
    total = flights + together + solo_total
    return {"out": out, "her": her, "his": his, "rooms": rooms, "food": food, "transport": transport, "activities": activities, "misc": misc,
            "solo_rooms": solo_rooms, "solo_food": solo_food, "solo_transport": p["solo_transport"], "solo_activities": p["solo_activities"],
            "solo": solo_total, "flights": flights, "together": together, "ground": together + solo_total, "total": round(total),
            "his_share": round(out_pp + his + together / 2 + solo_total), "her_share": round(out_pp + her + together / 2)}


def forecast(t):
    pb = BASE["fc_per_base"]
    last = BASE["fc_last"]
    bases = []
    for p in t["plans"]:
        for d in p["days"]:
            if d["wx"] and d["wx"] not in bases:
                bases.append(d["wx"])
    per_base = {b: pb[b] for b in bases}
    days = []
    for i, fd in enumerate(BASE["fc_days"]):
        rows = [dict(name=b, **{k: x.get(k) for k in ("hi", "lo", "p1", "p10", "med", "cls", "cc", "src")}) for b in bases for x in pb[b] if x["md"] == fd["md"]]
        known = [r for r in rows if r["cls"]]
        if known:
            pts = sum(POINTS[r["cls"]] for r in known) / len(known)
            cls = "Dry" if pts >= 0.85 else "Showers" if pts >= 0.6 else "Wet" if pts >= 0.25 else "Heavy rain"
            p1s = [r["p1"] for r in known if r["p1"] is not None]
            day = {"cls": cls, "pts": round(pts, 2), "p1": round(sum(p1s) / len(p1s)) if p1s else None,
                   "cc": round(sum(r["cc"] for r in known) / len(known))}
        else:
            day = {"cls": None, "pts": None, "p1": None, "cc": None}
        day.update(md=fd["md"], label=fd["label"], ahead=fd["ahead"], hi=rows[0]["hi"], lo=rows[0]["lo"], scored=fd["md"] <= last, bases=rows)
        days.append(day)
    scored = [d for d in days if d["cls"]]
    score = round(sum(d["pts"] for d in scored) / len(scored) * 5 * 2) / 2
    cc = round(sum(d["cc"] for d in scored) / len(scored))
    word = "Mostly dry" if score >= 4.5 else "Some showers" if score >= 3.5 else "Mixed" if score >= 2.5 else "Wet"
    firm = [d for d in days if d["scored"] and d["cls"]]
    wet = [d["label"] for d in firm if d["cls"] in ("Wet", "Heavy rain")]
    show = [d["label"] for d in firm if d["cls"] == "Showers"]
    note = f"{word} for {', '.join(bases)}. 31 Oct – 4 Nov (official forecasts): "
    note += (f"wet on {', '.join(wet)}; " if wet else "no wet day; ")
    note += (f"showers possible on {', '.join(show)}. " if show else "no showers forecast. ")
    late = [d for d in days if not d["scored"] and d["cls"] in ("Wet", "Heavy rain")]
    if late:
        note += f"5–7 Nov (27 Oct model run, rough): wet on {', '.join(d['label'] for d in late)}. "
    note += f"Daytime cloud {cc}% on average. Checked {BASE['fc_checked']}; recheck on 30 Oct."
    return {"score": score, "word": word, "note": note, "bases": bases, "days": days, "per_base": per_base, "cc": cc}


def place_key(s):
    for cut in (" (", ",", " hotel", " guesthouse", " B&B", " ryokan", " shukubo", " minshuku", " onsen inn", " hostel", "-area"):
        s = s.split(cut)[0]
    return s


def build():
    dests = []
    for t in TRIPS:
        clim = BASE["climate"][t["climate_of"]]
        fc = forecast(t)
        scores = dict(t["scores"])
        scores["weather"] = round((fc["score"] + clim["wx_climate"]) / 2 * 4) / 4
        scores["value"] = t["value"]
        scores["ease"] = t["ease"]
        fit = round(100 * sum(scores[k] * w for k, w in WEIGHTS.items()) / sum(5 * w for w in WEIGHTS.values()))
        options = []
        for p in t["plans"]:
            travel = sum(l[2] for d in p["days"] for l in d["tr"])
            together_travel = sum(l[2] for d in p["days"] if d["who"] != "you" for l in d["tr"])
            places = [place_key(n["place"]) for n in p["nights"]]
            o = {k: p[k] for k in ("style", "name", "chill", "route", "days", "nights", "transport_pp", "shared", "activities_pp", "solo_transport", "solo_activities")}
            o.update(travel=travel, together_travel=together_travel, beds=len(set(places[:4])), solo_beds=len(set(places[4:])),
                     moves=sum(1 for a, b in zip(places, places[1:]) if a != b), cost=plan_cost(t, p))
            options.append(o)
        d = {k: t[k] for k in ("id", "country", "region", "cc", "short", "title", "tagline", "food_day", "solo_food",
                               "transport", "crowds", "food", "hikes", "culture", "adventure", "pros", "cons", "calm")}
        d.update(group=t.get("group", "other"), town=t.get("town"), town_card=t.get("town_card"), out=dict(OUT[t["out"]]), her=dict(HER[t["her"]]), his=dict(HIS[t["his"]]), entry=ENTRY[t["cc"]], weather=clim["weather"],
                 scores=scores, fit=fit, fc=fc, options=options)
        dests.append(d)

    picks = [
        {"id": "jp-fuji", "why": "The Fuji view", "text": "Two nights by Lake Kawaguchi facing Mount Fuji. Sunday is forecast dry: the Fuji day. Busiest on the holiday."},
        {"id": "jp-hakone", "why": "Easiest and most relaxing", "text": "85 minutes from Shinjuku, two nights in an onsen inn, and something good to do whatever the weather."},
        {"id": "jp-nikko", "why": "Culture and autumn colour", "text": "Japan's most ornate shrines, and Iroha-zaka and Lake Chuzenji at peak colour. Leaves from Asakusa, next to the hotel."},
        {"id": "jp-kansai", "why": "If you'd rather skip Tokyo", "text": "Nara and a temple night together, then the Kumano Kodo on your own. Taiwan stays on the page as the cheaper option."},
    ]
    sources = [
        ["Live fares: Google Flights", "https://www.google.com/travel/flights", "out and Saturday-home fares: 27 Oct 2026, 1 adult"],
        ["Flight schedules: FlightConnections", "https://www.flightconnections.com/", "her Wednesday flights, 28 Oct 2026"],
        ["Forecast: JMA weekly forecasts (Japan)", "https://www.jma.go.jp/bosai/forecast/", "issued 28 Oct 17:00 / 29 Oct 11:00 JST, read 29 Oct"],
        ["Forecast: CWA one-week county forecast (Taiwan)", "https://www.cwa.gov.tw/V8/C/W/County/index.html", "read 29 Oct"],
        ["Forecast for 5–7 Nov: Open-Meteo ensemble API", "https://open-meteo.com/en/docs/ensemble-api", "ECMWF 51 runs, fetched 27 Oct 2026"],
    ] + [[f"{c[1]} — {c[4]}", c[5], c[2]] for c in CHECKS]
    return {
        "tokyo": TOKYO_PLAN,
        "dests": dests, "dates": DATES, "criteria": CRITERIA, "weights": WEIGHTS, "picks": picks, "sources": sources,
        "checks": [list(c) for c in CHECKS], "checked": CHECKED, "places": BASE["places"] + PLACES_NEW,
        "fc_days": BASE["fc_days"], "fc_bands": BASE["fc_bands"], "fc_last": BASE["fc_last"], "fc_checked": BASE["fc_checked"],
        "fare_status": FARE_STATUS,
        "params": {"days_together": DAYS_TOGETHER, "days_solo": DAYS_SOLO, "misc_pp": MISC_PP, "meal_credit": MEAL_CREDIT},
        "fares": {"out": OUT, "her": HER, "his": HIS},
    }


if __name__ == "__main__":
    D = build()
    for d in D["dests"]:
        print(d["id"], d["fit"], d["fc"]["score"], d["scores"]["weather"],
              [(o["style"], o["beds"], o["solo_beds"], o["travel"], o["cost"]["total"], o["cost"]["his_share"], o["cost"]["her_share"]) for o in d["options"]])
