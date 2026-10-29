# Every flight in the duo planner, in one place, so a live refresh only touches this file.
# Prices in euros, per person, one way.
# status: "gf27"  = checked live on Google Flights on 27 Oct 2026 (1 adult)
#         "est"   = schedule checked 28 Oct 2026 (FlightConnections), price NOT yet checked live: an estimate
# To refresh: change price/status here, then run build_all.py.
#
# Shape (since 28 Oct, 23:25): together Sat 31 Oct -> Wed 4 Nov; she flies back to HK on Wed 4 Nov in the evening;
# you stay on your own Thu 5 + Fri 6 and fly home on Sat 7 Nov (single ticket).

FARE_STATUS = {
    "gf27": "Live fare, Google Flights 27 Oct",
    "est": "Estimate: schedule checked 28 Oct, price not yet live-checked",
}

# Sat 31 Oct, Hong Kong -> destination, both of you on the same flight
OUT = {
    "tokyo": {"route": "HKG → NRT", "price": 116, "status": "gf27", "dep": "14:55", "carrier": "HK Express", "code": "TOKYO NRT",
              "detail": "HK Express 14:55 → 20:00, nonstop 4h05 (cabin bag only; checked bag ~€30)",
              "alt": "Haneda is closer to the city but nothing cheap after 14:00 was found on 27 Oct"},
    "kix":   {"route": "HKG → KIX", "price": 114, "status": "gf27", "dep": "14:45", "carrier": "HK Express", "code": "OSAKA KIX",
              "detail": "HK Express 14:45 → 19:20, nonstop 3h35",
              "alt": "€114 at 15:45 → 20:20 · €156 at 11:50"},
    "fuk":   {"route": "HKG → FUK", "price": 123, "status": "gf27", "dep": "12:55", "carrier": "HK Express", "code": "FUKUOKA",
              "detail": "HK Express 12:55 → 17:00, nonstop 3h05 (nothing cheap after 14:00: Cathay 15:45 was €925)",
              "alt": "€149 at 11:05 · €161 at 07:50"},
    "khh":   {"route": "HKG → KHH", "price": 84, "status": "gf27", "dep": "18:50", "carrier": "HK Express", "code": "KAOHSIUNG",
              "detail": "HK Express 18:50 → 20:15, nonstop 1h25",
              "alt": "€106 at 12:45 → 14:10 (gives you the Saturday evening there)"},
    "khh_early": {"route": "HKG → KHH", "price": 106, "status": "gf27", "dep": "12:45", "carrier": "HK Express", "code": "KAOHSIUNG",
              "detail": "HK Express 12:45 → 14:10, nonstop 1h25: reaches Dulan the same evening",
              "alt": "€84 at 18:50 → 20:15, then a night in Kaohsiung"},
}

OUT["kmq"] = {"route": "HKG → KMQ", "price": 205, "status": "gf27", "dep": "09:30", "carrier": "HK Express", "code": "KOMATSU KMQ",
              "detail": "HK Express 09:30 → 14:05, nonstop 3h35 (the only nonstop; about 3 a week, believed Mon/Thu/Sat), then bus to Kanazawa 40 min. An early start: Airport Express from Central ~07:00",
              "alt": "Or Tokyo (€116, 14:55) and the Hokuriku shinkansen to Kanazawa (2h30)"}

# Wed 4 Nov, her flight back to Hong Kong in the evening.
HER = {
    "tokyo": {"route": "NRT → HKG", "price": 130, "status": "est", "time": "19:00 → 23:25",
              "detail": "HK Express UO 647, Narita 19:00 → HK 23:25 (Skyliner from Ueno ~16:30, 41 min)",
              "alt": "Cathay CX 549 Haneda 16:00 → 20:15 (closer airport, ~€250) · Cathay CX 505 Narita 18:10 → 22:30"},
    "kix":   {"route": "KIX → HKG", "price": 120, "status": "est", "time": "17:20 → 21:00",
              "detail": "HK Express UO 899, Kansai 17:20 → HK 21:00 (Nankai from Namba ~15:00, 40 min)",
              "alt": "Cathay CX 561 17:00 → 20:25 · CX 569 19:05 → 22:40 · HK Express UO 689 20:15 → 23:55"},
    "fuk":   {"route": "FUK → HKG", "price": 130, "status": "est", "time": "20:00 → 22:40",
              "detail": "Greater Bay Airlines HB 2397, Fukuoka 20:00 → HK 22:40. From Yufuin by highway bus to Fukuoka airport (about 1h50, ~¥3,250).",
              "alt": "HK Express UO 639 18:00 → 20:40 · Cathay CX 589 16:35 → 19:40"},
    "kix_kaga": {"route": "KIX → HKG", "price": 120, "status": "est", "time": "17:20 → 21:00",
              "detail": "HK Express UO 899, Kansai 17:20 → HK 21:00. From Yamanaka: bus to Kaga-Onsen, shinkansen to Tsuruga, Thunderbird to Shin-Osaka, Haruka to Kansai (about 3h30, leave by 11:30)",
              "alt": "No Komatsu → HK flight on Wednesdays (HK Express flies it about 3 times a week). Or the shinkansen to Tokyo and Narita 19:00 (UO 647)"},
    "khh":   {"route": "KHH → HKG", "price": 85, "status": "est", "time": "21:00 → 22:40",
              "detail": "HK Express UO 135, Kaohsiung 21:00 → HK 22:40 (MRT to the airport, 20 min)",
              "alt": "Cathay CX 459 19:25 → 21:10 · China Airlines CI 935 18:00 → 19:45"},
}

# Sat 7 Nov, your flight home, single ticket (these are the solo plan's fares, live on 27 Oct).
HIS = {
    "tokyo": {"route": "NRT → BRU", "price": 571, "status": "gf27", "detail": "Etihad, Sat 17:20 → Sun 06:30 Brussels via Abu Dhabi"},
    "kix":   {"route": "KIX → CDG", "price": 618, "status": "gf27", "detail": "Cathay via HK, Sat 19:05 → Sun 07:45 Paris (1h50 in HK)"},
    "fuk":   {"route": "FUK → CDG", "price": 612, "status": "gf27", "detail": "Cathay via HK, Sat 16:35 → Sun 07:45 Paris"},
    "khh":   {"route": "KHH → CDG", "price": 370, "status": "gf27", "detail": "China Airlines + Qatar on one Qatar ticket, Sat 14:45 → Sun 06:35 Paris (2 stops: Bangkok, Doha)"},
}
