# Every flight in the duo planner, in one place, so a live refresh only touches this file.
# Prices in euros, per person, one way.
# status: "gf27"  = checked live on Google Flights on 27 Oct 2026 (1 adult)
#         "est"   = schedule checked 28 Oct 2026 (FlightConnections), price NOT yet checked live: an estimate
# To refresh: change price/status/checked here, then run build_all.py.

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
              "detail": "HK Express 12:45 → 14:10, nonstop 1h25: reaches Dulan the same evening, saving a night in Kaohsiung",
              "alt": "€84 at 18:50 → 20:15, then a night in Kaohsiung"},
    "han":   {"route": "HKG → HAN", "price": 94, "status": "gf27", "dep": "12:55", "carrier": "Sun PhuQuoc", "code": "HANOI",
              "detail": "Sun PhuQuoc Airways 12:55 → 14:00, nonstop 2h05 (€67 cheaper than the first flight after 14:00)",
              "alt": "€161 Vietnam Airlines 14:30 → 15:45 · €67 HK Express at 07:35"},
}

# Fri 6 Nov, her flight back to Hong Kong. Her own flight from HK leaves at 18:00,
# so she should land by about 14:30 (separate tickets: she has to collect bags and check in again).
HER = {
    "tokyo": {"route": "HND → HKG", "price": 220, "status": "est", "time": "09:35 → 13:50",
              "detail": "JAL JL 29, Haneda 09:35 → HK 13:50 (leave Asakusa ~07:20 on the Keikyu line, 40 min)",
              "alt": "ANA NH 859 08:50 → 12:55 · Cathay CX 543 10:10 → 14:25 (tighter) · cheaper: HK Express UO 857 Narita 08:00 → 11:55 (~€130, but a 06:00 Skyliner)"},
    "kix":   {"route": "KIX → HKG", "price": 160, "status": "est", "time": "09:50 → 13:40",
              "detail": "Hong Kong Airlines HX 617, Kansai 09:50 → HK 13:40 (Rapi:t from Namba ~07:30, 40 min)",
              "alt": "Peach MM 63 08:05 → 11:45 (~€110, cheapest) · Cathay CX 567 09:25 → 13:00 / CX 503 09:50 → 13:35"},
    "fuk":   {"route": "FUK → HKG", "price": 150, "status": "est", "time": "08:20 → 11:00",
              "detail": "Greater Bay Airlines HB 383, Fukuoka 08:20 → HK 11:00 (the airport is 5 min from Hakata by subway)",
              "alt": "The only morning nonstop. The next one, HK Express 12:55 → 15:35, leaves her only 2h25 in HK: too tight. Check HB 383 flies on Fridays."},
    "khh":   {"route": "KHH → HKG", "price": 85, "status": "est", "time": "10:10 → 11:50",
              "detail": "HK Express UO 131, Kaohsiung 10:10 → HK 11:50 (MRT to the airport, 20 min)",
              "alt": "EVA BR 845 09:15 → 10:55 · Cathay CX 431 11:25 → 13:15 · China Airlines CI 933 07:50 → 09:30"},
    "han":   {"route": "HAN → HKG", "price": 95, "status": "est", "time": "09:35 → 12:40",
              "detail": "HK Express UO 541, Hanoi 09:35 → HK 12:40 (Grab from the Old Quarter ~45 min, leave 07:00)",
              "alt": "Sun PhuQuoc 9G 530 09:15 → 11:55 · Vietnam Airlines VN 592 10:25 → 13:30 · Cathay CX 740 10:55 → 14:05"},
}

# Your way home: three options, every flight a single ticket (no self-transfers).
#   fri = fly home from the destination on Fri 6 Nov (land Sat 7 Nov)
#   sat = one more night there on your own, fly Sat 7 Nov (land Sun 8 Nov), as in the solo plan
#   hk  = fly to HK with her on Fri, a night with the family, then HK → Paris on Sat 7 Nov
HIS = {
    "tokyo": {
        "fri": {"route": "NRT → BRU", "price": 571, "status": "est", "detail": "Etihad, Fri 17:20 → Sat 06:30 Brussels via Abu Dhabi, if it runs on Fridays (Saturday's was €571 on 27 Oct)"},
        "sat": {"route": "NRT → BRU", "price": 571, "status": "gf27", "detail": "Etihad, Sat 17:20 → Sun 06:30 Brussels via Abu Dhabi"},
    },
    "kix": {
        "fri": {"route": "KIX → CDG", "price": 618, "status": "est", "detail": "Cathay via HK, Fri 19:05 → Sat 07:45 Paris, if Friday's fare matches Saturday's (€618 on 27 Oct)"},
        "sat": {"route": "KIX → CDG", "price": 618, "status": "gf27", "detail": "Cathay via HK, Sat 19:05 → Sun 07:45 Paris (1h50 in HK)"},
    },
    "fuk": {
        "fri": {"route": "FUK → CDG", "price": 612, "status": "est", "detail": "Cathay via HK, Fri 16:35 → Sat 07:45 Paris, if Friday's fare matches Saturday's"},
        "sat": {"route": "FUK → CDG", "price": 612, "status": "gf27", "detail": "Cathay via HK, Sat 16:35 → Sun 07:45 Paris"},
    },
    "khh": {
        "fri": {"route": "KHH → CDG", "price": 370, "status": "est", "detail": "China Airlines + Qatar on one Qatar ticket, Fri 14:45 → Sat 06:35 Paris (2 stops), if Friday's fare matches Saturday's"},
        "sat": {"route": "KHH → CDG", "price": 370, "status": "gf27", "detail": "China Airlines + Qatar on one Qatar ticket, Sat 14:45 → Sun 06:35 Paris (2 stops: Bangkok, Doha)"},
    },
    "han": {
        "fri": {"route": "HAN → CDG", "price": 323, "status": "est", "detail": "Etihad, Fri 20:10 → Sat 06:45 Paris via Abu Dhabi, if Friday's fare matches Saturday's"},
        "sat": {"route": "HAN → CDG", "price": 323, "status": "gf27", "detail": "Etihad, Sat 20:10 → Sun 06:45 Paris via Abu Dhabi"},
    },
}

# HK -> Paris after flying back with her (the "hk" option). The flight to HK is the same as hers.
HK_HOME = {"route": "HKG → CDG", "price": 451, "status": "gf27",
           "detail": "Etihad, Sat 7 Nov 19:45 → Sun 06:30 Paris via Abu Dhabi (€451 on 27 Oct). If her 18:00 flight on Friday goes to Paris, you could also try for a seat on it."}

HIS_LABEL = {"fri": "Fly home Fri", "sat": "Stay a night, fly Sat", "hk": "Back to HK with her"}
