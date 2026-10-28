"""Turn trips.py + fares.py + checks.py into the data the page and the spreadsheet use.
All money in euros. Run build_all.py rather than this file directly."""
import json, os
from fares import OUT, HER, HIS, HK_HOME, HIS_LABEL, FARE_STATUS
from trips import TRIPS
from checks import CHECKS, CHECKED
from places_new import PLACES_NEW

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = json.load(open(os.path.join(HERE, "base_data.json")))

DAYS_TOGETHER = 6          # food days for two (Sat evening .. Fri breakfast)
MISC_PP = 20               # SIM, tips, laundry, per person
MEAL_CREDIT = 0.6          # share of a day's food covered when dinner + breakfast come with the room
WEIGHTS = {"hike": 2, "nature": 2, "food": 2, "culture": 2, "chill": 2, "weather": 2, "value": 1.5, "ease": 1}
CRITERIA = [["hike", "Hiking"], ["nature", "Nature"], ["food", "Food"], ["culture", "Culture & cities"],
            ["chill", "Relaxed pace"], ["weather", "Weather"], ["value", "Value"], ["ease", "Ease for two"]]
POINTS = {"Dry": 1, "Showers": 0.7, "Wet": 0.35, "Heavy rain": 0}
DATES = ["Sat 31 Oct", "Sun 1 Nov", "Mon 2 Nov", "Tue 3 Nov", "Wed 4 Nov", "Thu 5 Nov", "Fri 6 Nov", "Sat 7 Nov"]
FOREIGN = {"JP": "Visa-free 90 days for you (French passport); fill in Visit Japan Web", "TW": "Visa-free 90 days for you; online arrival card", "VN": "Visa-free 45 days for you"}


def home_options(t):
    her = HER[t["her"]]
    his = HIS[t["his"]]
    sat_extra = t["solo_night"] + t["solo_food"]
    return {
        "fri": {"price": his["fri"]["price"], "legs": [his["fri"]],
                "note": "Same day as her: you land in Europe on Sat 7 Nov. One ticket.", "extra": ""},
        "sat": {"price": his["sat"]["price"] + sat_extra, "legs": [his["sat"]],
                "extra": f"+ one night and a day on your own: about €{sat_extra} (room €{t['solo_night']}, food €{t['solo_food']})",
                "note": "As in the solo plan: one more day there, land Sun 8 Nov."},
        "hk": {"price": her["price"] + HK_HOME["price"], "legs": [dict(her, detail="Same flight as her: " + her["detail"]), HK_HOME],
               "note": "Fly back together, see her off at 18:00, an evening and night with the family, home on Sat. Two tickets, but with a full day between them (no tight connection).",
               "extra": ""},
    }


def plan_cost(t, p, home, homes):
    out = 2 * OUT[t["out"]]["price"]
    her = HER[t["her"]]["price"]
    his = homes[home]["price"]
    rooms = sum(n["room"] for n in p["nights"])
    meal_nights = sum(1 for n in p["nights"] if n["meals"])
    food = 2 * t["food_day"] * DAYS_TOGETHER - 2 * MEAL_CREDIT * t["food_day"] * meal_nights
    transport = 2 * p["transport_pp"] + p["shared"]
    activities = 2 * p["activities_pp"]
    misc = 2 * MISC_PP
    flights = out + her + his
    ground = rooms + food + transport + activities + misc
    total = flights + ground
    half = ground / 2
    return {"out": out, "her": her, "his": his, "rooms": rooms, "food": food, "transport": transport,
            "activities": activities, "misc": misc, "flights": flights, "ground": ground, "total": round(total),
            "his_share": round(out / 2 + his + half), "her_share": round(out / 2 + her + half)}


def forecast(t):
    pb = BASE["fc_per_base"]
    bases = []
    for p in t["plans"]:
        for d in p["days"]:
            if d["wx"] and d["wx"] not in bases:
                bases.append(d["wx"])
    per_base = {b: pb[b] for b in bases}
    days = []
    for i, fd in enumerate(BASE["fc_days"]):
        rows = [dict(name=b, **{k: x[k] for k in ("hi", "lo", "p1", "p10", "med", "cls", "cc")}) for b in bases for x in pb[b] if x["md"] == fd["md"]]
        pts = sum(POINTS[r["cls"]] for r in rows) / len(rows)
        cls = "Dry" if pts >= 0.85 else "Showers" if pts >= 0.6 else "Wet" if pts >= 0.25 else "Heavy rain"
        days.append({"md": fd["md"], "label": fd["label"], "ahead": fd["ahead"], "cls": cls, "pts": round(pts, 2),
                     "p1": round(sum(r["p1"] for r in rows) / len(rows)), "cc": round(sum(r["cc"] for r in rows) / len(rows)),
                     "hi": rows[0]["hi"], "lo": rows[0]["lo"], "scored": i < 7, "bases": rows})
    scored = [d for d in days if d["scored"]]
    score = round(sum(d["pts"] for d in scored) / len(scored) * 5 * 2) / 2
    cc = round(sum(d["cc"] for d in scored) / len(scored))
    word = "Mostly dry" if score >= 4.5 else "Some showers" if score >= 3.5 else "Mixed" if score >= 2.5 else "Wet"
    wet = [d["label"] for d in scored if d["cls"] in ("Wet", "Heavy rain")]
    show = [d["label"] for d in scored if d["cls"] == "Showers"]
    note = f"{word} for {', '.join(bases)}. "
    note += (f"Wet: {', '.join(wet)}. " if wet else "No wet day in the run. ")
    if show:
        note += f"Showers: {', '.join(show)}. "
    note += f"Daytime cloud {cc}% on average. From the run fetched {BASE['fc_checked']}; recheck on 29–30 Oct."
    return {"score": score, "word": word, "note": note, "bases": bases, "days": days, "per_base": per_base, "cc": cc}


def build():
    dests = []
    for t in TRIPS:
        clim = BASE["climate"][t["climate_of"]]
        homes = home_options(t)
        fc = forecast(t)
        scores = dict(t["scores"])
        scores["weather"] = round((fc["score"] + clim["wx_climate"]) / 2 * 4) / 4
        if t.get("fc_extra"):
            fc["note"] = t["fc_extra"] + " " + fc["note"]
            fc["word"] = "Tokyo only"
            scores["weather"] = clim["wx_climate"]
        scores["value"] = t["value"]
        scores["ease"] = t["ease"]
        fit = round(100 * sum(scores[k] * w for k, w in WEIGHTS.items()) / sum(5 * w for w in WEIGHTS.values()))
        options = []
        for p in t["plans"]:
            travel = sum(l[2] for d in p["days"] for l in d["tr"])
            places = []
            for n in p["nights"]:
                key = n["place"].split(" (")[0].split(",")[0].split(" hotel")[0].split(" guesthouse")[0].split(" B&B")[0].split(" ryokan")[0].split(" shukubo")[0].split(" minshuku")[0].split(" bungalow")[0].split(" onsen inn")[0]
                places.append(key)
            beds = len(set(places))
            moves = sum(1 for a, b in zip(places, places[1:]) if a != b)
            o = {k: p[k] for k in ("style", "name", "chill", "route", "days", "nights", "transport_pp", "shared", "activities_pp")}
            o.update(travel=travel, beds=beds, moves=moves,
                     cost={h: plan_cost(t, p, h, homes) for h in ("fri", "sat", "hk")})
            options.append(o)
        out = dict(OUT[t["out"]])
        her = dict(HER[t["her"]])
        d = {k: t[k] for k in ("id", "country", "region", "cc", "short", "title", "tagline", "food_day", "solo_night", "solo_food", "solo_day",
                               "transport", "crowds", "food", "hikes", "culture", "adventure", "pros", "cons", "calm")}
        d.update(out=out, her=her, homes=homes, entry=FOREIGN[t["cc"]], weather=clim["weather"], scores=scores, fit=fit, fc=fc, options=options)
        dests.append(d)

    by_fit = sorted(dests, key=lambda d: -d["fit"])
    def lowest(d): return min(o["cost"]["fri"]["total"] for o in d["options"])
    picks = [
        {"id": "tw-south", "why": "Easiest and driest", "text": "She speaks the language, Tainan is dry and warm, and Alishan's railway is running again. About half the cost of Japan."},
        {"id": "jp-kansai", "why": "Culture + hiking, no Kyoto", "text": "Nara at dawn, a temple night at Koyasan and, in the Fuller plan, three nights on the Kumano Kodo. Book the inns today."},
        {"id": "jp-kyushu", "why": "Bluest skies, onsen towns", "text": "The Karatsu Kunchi floats on 4 Nov and two quiet onsen towns. Her only good flight back leaves at 08:20."},
        {"id": "jp-fuji", "why": "Tokyo + Fuji, done slowly", "text": "Old Tokyo on foot, three days by the Fuji lakes, and an onsen ryokan for the wet Monday in the Fuller plan."},
    ]
    sources = [
        ["Live fares: Google Flights", "https://www.google.com/travel/flights", "out and Saturday-home fares: 27 Oct 2026, 1 adult"],
        ["Flight schedules: FlightConnections", "https://www.flightconnections.com/", "her return flights and times, 28 Oct 2026"],
        ["Forecast: Open-Meteo ensemble API", "https://open-meteo.com/en/docs/ensemble-api", f"ECMWF 51 runs, fetched {BASE['fc_checked']}"],
    ] + [[f"{c[1]} — {c[4]}", c[5], c[2]] for c in CHECKS]
    seen, src = set(), []
    for s in sources:
        if s[1] in seen and s[0].startswith(("Live", "Flight", "Forecast")) is False:
            pass
        src.append(s)
        seen.add(s[1])
    places = BASE["places"] + PLACES_NEW
    return {
        "dests": dests, "dates": DATES, "criteria": CRITERIA, "weights": WEIGHTS, "picks": picks, "sources": src,
        "checks": [list(c) for c in CHECKS], "checked": CHECKED, "places": places,
        "fc_days": BASE["fc_days"], "fc_bands": BASE["fc_bands"], "fc_last": BASE["fc_last"], "fc_checked": BASE["fc_checked"],
        "home_labels": HIS_LABEL, "fare_status": FARE_STATUS,
        "params": {"days_together": DAYS_TOGETHER, "misc_pp": MISC_PP, "meal_credit": MEAL_CREDIT},
        "fares": {"out": OUT, "her": HER, "his": HIS, "hk_home": HK_HOME},
    }


if __name__ == "__main__":
    D = build()
    for d in D["dests"]:
        print(d["id"], d["fit"], d["fc"]["score"], d["scores"]["weather"], [(o["style"], o["beds"], o["travel"], {h: o["cost"][h]["total"] for h in o["cost"]}) for o in d["options"]])
