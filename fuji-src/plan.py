# Tokyo + Kawaguchiko: the chosen trip (30 Oct 2026). Everything on the page comes from this file.
#
# HOW TO CHANGE THE PLAN
# - Swap a day to another version: change its line in CHOICE (e.g. "mon2": "heavy").
# - Drop or edit a step: edit the "steps" of that version in DAYS.
# - New forecast: edit FORECAST (rain chance %, low, high, sky code) and FC_META.
# - Text markers: [[place_id]] = a map chip (PLACES), {{link_id}} = a timetable/booking chip (LINKS).
# Then: python3 fuji-src/build.py  (writes fuji/index.html, fuji/sw.js, fuji/manifest.webmanifest).

UPDATED = "31 Oct 2026, 13:30 JST"

TRIP = {
    "title": "Tokyo + Kawaguchiko",
    "sub": "Sat 31 Oct → Sat 7 Nov 2026",
    "lede": "Together: one night in Nihonbashi, two by Lake Kawaguchi facing Mount Fuji, one in Asakusa. "
            "She flies back to Hong Kong on Wed 4 Nov; you stay three more nights in Tokyo and fly home on Sat 7.",
}

# Which version of each day is the plan. The other versions stay on the page as one-tap swaps.
CHOICE = {
    "sat31": "nrt",
    "sun1": "main",
    "mon2": "main",
    "tue3": "main",
    "wed4": "main",
    "thu5": "main",
    "fri6": "main",
    "sat7": "main",
}

# ------------------------------------------------------------------ forecast
# 31 Oct 07:00 JST run: JMA's site was unreachable from the updater, so these are tenki.jp (Japan Weather
# Association) 10-day forecasts issued 30 Oct 22:00 (Tokyo, Chiyoda) and 23:00 JST (Fujikawaguchiko town).
# sky: sun | suncloud | cloud | cloudsun | rain
FC_META = {
    "source": "tenki.jp (JMA unreachable), 30 Oct 23:00 JST",
    "fetched": "31 Oct, 07:00 JST",
    "links": ["jma_tokyo", "jma_yamanashi", "fuji_cam"],
}
FORECAST = {
    "tokyo": {
        "10-31": ("suncloud", 40, 13, 25), "11-01": ("suncloud", 30, 13, 20), "11-02": ("rain", 70, 14, 20),
        "11-03": ("suncloud", 30, 12, 22), "11-04": ("rain", 70, 13, 17), "11-05": ("rain", 90, 12, 14),
        "11-06": ("suncloud", 20, 13, 24), "11-07": ("cloud", 30, 12, 16),
    },
    "kawa": {
        "10-31": ("suncloud", 50, 10, 19), "11-01": ("suncloud", 20, 5, 17), "11-02": ("rain", 80, 8, 17),
        "11-03": ("suncloud", 40, 7, 17), "11-04": ("cloud", 40, 8, 15), "11-05": ("rain", 80, 8, 13),
        "11-06": ("suncloud", 30, 9, 20),
    },
}
FC_SUMMARY = [
    "Sun 1 is the best lake day (20%, sunny spells, 5°C at dawn): do the e-bike ride.",
    "Mon 2 turns wetter (80% at the lake, rain from midday): the wet-day plan fits; consider the \"heavy\" version.",
    "Tue 3 is sunny early, cloudier later (40%): hike Chureito/Arakurayama first thing, then the train to Tokyo.",
    "Wed 4 rain in Tokyo by evening (70%), Thu 5 the wettest day (90%, 14°C): keep Thursday as the rainy-Tokyo day.",
    "Fri 6 is the dry, mild one (20%, 24°C): good for Mt Takao. Typhoon In-fa stays near Ogasawara, far south; no mainland impact forecast.",
]

# ------------------------------------------------------------------ links (timetables, bookings, info)
LINKS = {
    "bus_tt": ("Bus timetable Shinjuku ⇄ Kawaguchiko", "https://bus.fujikyu.co.jp/en/highway/fujisan/shinjuku-kawaguchiko/#timetable", "tt"),
    "bus_book_sun": ("Book the bus, Sun 1 Nov", "https://www.fujiyamaconnect.jp/bus/product/bus/?departureAreaId=11&arrivalAreaId=31&rideDate=20261101&routeId=20&expandSameNameRoutes=1", "book"),
    "highwaybus": ("highwaybus.com (bus booking)", "https://www.highwaybus.com/", "book"),
    "lake_tt": ("Lake buses: timetable (Red line)", "https://bus.fujikyu.co.jp/en/fujitour/kawaguchiko/#timetable", "tt"),
    "lake_map": ("Lake bus route map (PDF)", "https://bus.fujikyu.co.jp/pdf/omni_map_202604.pdf", "tt"),
    "lake_pass": ("1-day lake bus pass ¥1,500", "https://www.fujiyamaconnect.jp/tenant/31/product/NDP-01/", "book"),
    "fujikko_tt": ("Fujikko-go-go loop bus timetable", "https://bus.fujikyu.co.jp/en/fujitour/fujikko/#timetable", "tt"),
    "fujiexc_tt": ("Fuji Excursion times (Oct 2026)", "https://jr-group.jp/fujikaiyu-timetable/", "tt"),
    "fujiexc_info": ("Fuji Excursion: fares and tickets", "https://ekitan.com/en/article/fujikaiyu", "info"),
    "ekinet": ("Eki-net (book JR seats)", "https://www.eki-net.com/en/", "book"),
    "fujikyu_up": ("Fujikyu line timetable toward Otsuki", "https://timetables.jreast.co.jp/2611/timetable-v/707u1.html", "tt"),
    "nex": ("Narita Express", "https://www.jreast.co.jp/multi/en/nex/", "tt"),
    "skyliner": ("Keisei Skyliner", "https://www.keisei.co.jp/keisei/tetudou/skyliner/us/", "tt"),
    "keikyu": ("Haneda ⇄ Tokyo by Keikyu", "https://www.haneda-tokyo-access.com/en/", "tt"),
    "access_exp": ("Narita ⇄ Tokyo by train (Access Express)", "https://www.narita-airport.jp/en/access/train/", "tt"),
    "maple_col": ("Fujikyu: maple corridor and crowds", "https://bus.fujikyu.co.jp/en/column/imp6s700000005jf.html", "info"),
    "jma_tokyo": ("JMA forecast: Tokyo", "https://www.jma.go.jp/bosai/forecast/#area_type=offices&area_code=130000", "info"),
    "jma_yamanashi": ("JMA forecast: Yamanashi (Fuji lakes)", "https://www.jma.go.jp/bosai/forecast/#area_type=offices&area_code=190000", "info"),
    "fuji_cam": ("Fuji live cameras (is it out?)", "https://www.fujigoko.tv/", "info"),
    "meiji": ("Meiji Jingu", "https://www.meijijingu.or.jp/en/", "info"),
}

# ------------------------------------------------------------------ places (each gets a Google Maps link)
# id: (name, maps query, short note)
PLACES = {
    # Tokyo
    "busta": ("Busta Shinjuku", "Busta Shinjuku Shinjuku Expressway Bus Terminal", "Bus terminal on 4F above Shinjuku station's south exit. Arrive 20 min early."),
    "h_apa_hn": ("APA Hotel Higashi Nihombashi Ekimae", "APA Hotel Higashi Nihombashi Ekimae, 3-12-14 Higashinihonbashi, Chuo City, Tokyo", "Tonight's hotel. 1 min from Higashi-nihombashi (Toei Asakusa line, exit B4); 3 min from Bakuro-yokoyama (Toei Shinjuku line). Check-in from 15:00."),
    "higashinihombashi": ("Higashi-nihombashi Station", "Higashi-nihombashi Station", "Toei Asakusa line: direct trains from Narita and Haneda; 3 stops to Asakusa."),
    "bakuroyokoyama": ("Bakuro-yokoyama Station", "Bakuro-yokoyama Station", "Toei Shinjuku line: straight to Shinjuku in about 20 min, no change."),
    "ningyocho": ("Ningyocho", "Ningyocho Amazake Yokocho", "Old-Tokyo streets 10 min's walk away: small izakayas, taiyaki, sukiyaki houses."),
    "omoide": ("Omoide Yokocho", "Omoide Yokocho Shinjuku", "Yakitori alleys under the tracks on Shinjuku's west side."),
    "sensoji": ("Senso-ji", "Senso-ji Asakusa", "Tokyo's oldest temple. Calm before 8:30 and after dark, when it's lit up."),
    "hoppy": ("Hoppy Street", "Hoppy Street Asakusa", "Outdoor izakaya stools and beef stew, two minutes from Senso-ji."),
    "kappabashi": ("Kappabashi", "Kappabashi Dougu Street", "Kitchen-tool street: knives, ceramics, plastic food samples."),
    "yanaka": ("Yanaka Ginza", "Yanaka Ginza", "Old shopping street, temples and cats; the 'Yuyake dandan' steps."),
    "uenopark": ("Ueno Park", "Ueno Park", "Ponds, temples, museums."),
    "tnm": ("Tokyo National Museum", "Tokyo National Museum", "Best collection of Japanese art; closed Mondays."),
    "ameyoko": ("Ameyoko", "Ameyoko Shopping Street", "Market street under the tracks: street food, cheap lunches."),
    "meiji": ("Meiji Jingu", "Meiji Jingu", "Forest shrine next to Harajuku. Autumn festival 1–3 Nov."),
    "catstreet": ("Cat Street, Harajuku", "Cat Street Harajuku", "Quiet back street to Shibuya, small shops."),
    "teamlab": ("teamLab Planets", "teamLab Planets TOKYO", "Walk-through digital art, good on a wet day. Book a time slot."),
    "ginza_depa": ("Ginza Mitsukoshi food hall", "Ginza Mitsukoshi", "Depachika: the basement food hall."),
    "laqua": ("Spa LaQua", "Spa LaQua Tokyo Dome City", "Big onsen spa in central Tokyo, open late."),
    "kiyosumi": ("Kiyosumi Garden", "Kiyosumi Garden", "Stroll garden with stepping stones over the pond."),
    "tsukiji": ("Tsukiji Outer Market", "Tsukiji Outer Market", "Breakfast stalls: tamagoyaki, sushi, grilled scallops. Go by 9."),
    "shimokita": ("Shimokitazawa", "Shimokitazawa Station", "Small bars, vintage shops."),
    # Mt Takao
    "takaosanguchi": ("Takaosanguchi Station", "Takaosanguchi Station", "Keio line from Shinjuku, about 50 min."),
    "takao_shiroyama": ("Shiroyama summit", "Shiroyama Takao", "Teahouse with a Fuji view, 25 min past Takao's summit."),
    "yakuoin": ("Yakuoin temple", "Takaosan Yakuoin", "Mountain temple with tengu statues on trail 1."),
    "gokurakuyu": ("Gokurakuyu onsen", "Keio Takaosan Onsen Gokurakuyu", "Onsen next to the station: the soak after the hike."),
    # Kamakura
    "engakuji": ("Engaku-ji", "Engakuji Kamakura", "Zen temple by Kita-Kamakura station."),
    "daibutsu": ("Great Buddha (Kotoku-in)", "Kotoku-in Kamakura", "End of the Daibutsu hiking course."),
    "yuigahama": ("Yuigahama beach", "Yuigahama Beach", "Kamakura's beach, 15 min from the Buddha."),
    # Kawaguchiko
    "kawa_stn": ("Kawaguchiko Station", "Kawaguchiko Station", "Bus terminal and Fujikyu trains. Coin lockers; bus pass counter."),
    "hoto": ("Hoto Fudo (Higashi Koiji)", "Hoto Fudo Higashi Koiji", "Hoto: thick miso noodles with pumpkin, the Fuji lakes dish."),
    "bike_sora": ("Soranoshita (e-bikes)", "Soranoshita Kawaguchiko rental bike", "E-bike rental; the station shop is closed weekends and holidays. Book."),
    "bike_fujisan": ("fujisanbike (e-bikes)", "fujisanbike Kawaguchiko", "Alternative e-bike rental. Book."),
    "oishi": ("Oishi Park", "Oishi Park Fujikawaguchiko", "North-shore park facing Fuji across the lake; kochia bushes."),
    "tenjoyama": ("Tenjoyama ropeway", "Mt. Fuji Panoramic Ropeway", "3-min ride up to a Fuji viewpoint; walk down in 40 min."),
    "kubota": ("Itchiku Kubota Art Museum", "Itchiku Kubota Art Museum", "Landscape kimonos in a forest garden. Indoors: a good wet-day stop."),
    "asama": ("Kawaguchi Asama Shrine", "Kawaguchi Asama Shrine", "Sengen shrine with 1,200-year-old cedars, 20 min walk from the museum."),
    "yohaisho": ("Haruka Yohaisho (torii in the sky)", "Haruka Yohaisho Kawaguchi Asama Shrine", "Torii framing Fuji, about 30 min uphill from Kawaguchi Asama Shrine."),
    "yurari": ("Fuji Chobo no Yu Yurari", "Fuji Chobo no Yu Yurari", "Day onsen with Fuji-view baths, on the lake bus routes."),
    "kitaguchi": ("Kitaguchi Hongu Fuji Sengen", "Kitaguchi Hongu Fuji Sengen Jinja", "The big Sengen shrine: giant cedar avenue, start of the old Yoshida trail."),
    "oshino": ("Oshino Hakkai", "Oshino Hakkai", "Spring-fed ponds in a village; busy with tour groups after 10."),
    # Fujiyoshida (Sengen hike)
    "shimoyoshida": ("Shimoyoshida Station", "Shimoyoshida Station", "Fujikyu line, 15 min from Kawaguchiko. The Fuji Excursion stops here."),
    "arakura": ("Arakura Fuji Sengen Shrine", "Arakura Fuji Sengen Shrine", "The Sengen shrine at the foot of the 398 steps."),
    "chureito": ("Chureito Pagoda", "Chureito Pagoda", "Five-storey pagoda with Fuji behind: the famous view. Free."),
    "arakurayama": ("Mt Arakurayama summit", "Arakurayama Fujiyoshida summit observation", "Trail behind the pagoda; small platform at 1,180 m with Fuji views."),
    "honcho": ("Honcho-dori", "Honcho Street Fujiyoshida", "Retro shopping street with Fuji at the end of it."),
    "udon": ("Yoshida udon", "Yoshida udon near Shimoyoshida Station", "Fujiyoshida's firm, chewy udon; most shops open lunch only."),
    # Beds (shortlist of 30 Oct, Booking.com)
    "h_royal": ("Royal Hotel Kawaguchiko", "Royal Hotel Kawaguchiko", "Lake + Fuji view Japanese room €227 / €334 half board; onsen."),
    "h_yamagisi": ("Yamagisi Ryokan", "Yamagisi Ryokan Kawaguchiko", "Japanese room €299 / €344 breakfast; lake-view open-air onsen."),
    "h_kawahotel": ("Kawaguchiko Hotel", "Kawaguchiko Hotel", "Lake + mountain view €406 / €470 breakfast; hot spring."),
    "h_maruei": ("Maruei ryokan", "Maruei Kawaguchiko", "Kaiseki dinner + breakfast €828; Fuji-view open-air bath; 9.1."),
    "h_focus": ("Focus Kuramae", "Hotel Focus Kuramae", "Double €50, free cancellation."),
    "h_apa_asakusa": ("APA Asakusa Ekimae", "APA Hotel Asakusa Ekimae", "€51, free cancellation."),
    "h_enhouse": ("EN The HOUSE Asakusa Nitenmon", "EN The HOUSE Asakusa Nitenmon", "€94, 9.5."),
    "h_wasabi": ("Hostel Wasabi Asakusa", "Hostel Wasabi Asakusa", "Dorm, 3 nights €62 with breakfast, free cancellation."),
    "h_samurai": ("Guest House Tokyo Samurai", "Guest House Tokyo Samurai", "Dorm, 3 nights €58."),
}

# ------------------------------------------------------------------ the days
# Each day: id, date, md (forecast key), fc (tokyo | kawa), where, who (together | split | you), bed,
# versions: {key: {label, title, why, steps: [(time, text)], watch}}
DAYS = [
 {"id": "sat31", "date": "Sat 31 Oct", "md": "10-31", "fc": "tokyo", "where": "Tokyo · Nihonbashi", "who": "together",
  "bed": "APA Higashi Nihombashi Ekimae (booked)",
  "versions": {
   "nrt": {"label": "Land at Narita", "title": "Fly to Tokyo, Nihonbashi for the night",
    "steps": [
     ("10:30", "Airport Express from Hong Kong station (24 min) for the 13:00 flight."),
     ("~18:00", "Land at Narita (Tokyo is HK + 1h). Keisei Access Express runs straight through to [[higashinihombashi]], about 1h, no change (Suica fine). If one isn't due, Skyliner to Nippori and taxi. {{access_exp}}"),
     ("19:30", "Check in at [[h_apa_hn]], exit B4, 1 min."),
     ("20:00", "Dinner nearby: walk 10 min to [[ningyocho]] for a small izakaya, or 3 stops on the same line to Asakusa. Halloween crowds are in Shibuya and Shinjuku, not here."),
    ],
    "watch": "Bus for Sunday not booked yet? Do it tonight: {{bus_book_sun}}. Sunday morning you ride from [[bakuroyokoyama]] to Shinjuku, about 20 min."},
   "hnd": {"label": "Land at Haneda", "title": "Fly to Tokyo, Nihonbashi for the night",
    "steps": [
     ("10:30", "Airport Express from Hong Kong station (24 min) for the 13:00 flight."),
     ("~18:00", "Land at Haneda. Keikyu trains run through to the Toei Asakusa line: [[higashinihombashi]] in about 35 min (some need a change at Sengakuji). {{keikyu}}"),
     ("19:00", "Check in at [[h_apa_hn]], exit B4, 1 min."),
     ("19:30", "Dinner nearby: walk 10 min to [[ningyocho]] for a small izakaya, or 3 stops on the same line to Asakusa. Halloween crowds are in Shibuya and Shinjuku, not here."),
    ],
    "watch": "Bus for Sunday not booked yet? Do it tonight: {{bus_book_sun}}. Sunday morning you ride from [[bakuroyokoyama]] to Shinjuku, about 20 min."},
  }},

 {"id": "sun1", "date": "Sun 1 Nov", "md": "11-01", "fc": "kawa", "where": "Kawaguchiko", "who": "together",
  "bed": "Kawaguchiko, night 1 of 2",
  "versions": {
   "main": {"label": "Plan", "title": "Bus to Fuji, e-bikes along the lake",
    "why": "The dry day at the lake (20%): the ride is today.",
    "steps": [
     ("07:05", "Check out. Toei Shinjuku line from [[bakuroyokoyama]] to Shinjuku (about 20 min, no change), then 8 min on foot to [[busta]] (4F, south exit side)."),
     ("08:00", "Morning bus from [[busta]] to [[kawa_stn]], about 1h45 (¥2,200, reserved seats). {{bus_tt}} {{bus_book_sun}}"),
     ("10:00", "Leave the bags at the hotel or in the station lockers."),
     ("11:00", "Early hoto lunch at [[hoto]] before the queue."),
     ("12:00", "E-bikes from [[bike_sora]] or [[bike_fujisan]] (book; about ¥3,000–4,000 each). Over the bridge and along the flat north shore to [[oishi]]: Fuji across the water, about 6 km each way, 2–3h with stops."),
     ("16:00", "Bikes back before dark (sunset ~16:40). Hotel onsen, quiet dinner."),
    ],
    "watch": "The maple corridor light-up only starts on 7 Nov. Sunday afternoon is busy at Oishi Park; it thins out after 15:00."},
   "train": {"label": "Train instead of bus", "title": "Fuji Excursion train, then the bikes",
    "why": "No road traffic, but about twice the price of the bus.",
    "steps": [
     ("07:50", "Check out. Toei Shinjuku line from [[bakuroyokoyama]] to Shinjuku, about 20 min, then the JR platforms."),
     ("08:30", "Fuji Excursion 7 from Shinjuku, reserved seats, arrives [[kawa_stn]] 10:26. {{fujiexc_tt}} {{ekinet}}"),
     ("11:00", "Hoto lunch at [[hoto]]."),
     ("12:00", "E-bikes along the north shore to [[oishi]] and back (see Plan)."),
     ("16:00", "Onsen and dinner."),
    ]},
   "swap": {"label": "Swap: Sengen hike today", "title": "Bus to Fuji, then the Sengen shrine hike",
    "why": "If Sunday looks clearer than Tuesday. The bikes then move to Tuesday morning.",
    "steps": [
     ("07:05", "Toei Shinjuku line from [[bakuroyokoyama]] to Shinjuku, walk to [[busta]]."),
     ("08:00", "Bus from [[busta]] to [[kawa_stn]]. {{bus_tt}}"),
     ("10:30", "Bags at the hotel; Fujikyu train to [[shimoyoshida]] (15 min)."),
     ("11:00", "[[arakura]], up the 398 steps to [[chureito]], then the trail behind the pagoda to [[arakurayama]] and back (about 2h)."),
     ("14:00", "Late lunch: [[udon]]. Train back to the lake; onsen."),
    ]},
  }},

 {"id": "mon2", "date": "Mon 2 Nov", "md": "11-02", "fc": "kawa", "where": "Kawaguchiko", "who": "together",
  "bed": "Kawaguchiko, night 2 of 2",
  "versions": {
   "main": {"label": "Showers plan", "title": "Kimono museum, the cedar shrine, an onsen",
    "why": "The wet day (50% at the lake): mostly indoors, with a short forest walk.",
    "steps": [
     ("08:30", "Check the {{fuji_cam}}. If Fuji is out, [[tenjoyama]] when it opens (around 9), otherwise a slow breakfast."),
     ("10:00", "Red line lake bus to [[kubota]] (indoors, with a garden). {{lake_tt}} {{lake_pass}}"),
     ("12:00", "Walk 20 min to [[asama]], a Sengen shrine with 1,200-year-old cedars. If the rain is light, the little climb (about 30 min) to [[yohaisho]], the torii that frames Fuji."),
     ("14:00", "Late lunch, then the lake bus to [[yurari]] for a long soak, or the hotel's own bath."),
     ("18:00", "Dinner in town."),
    ],
    "watch": "The bus pass page shows the 1-day pass (¥1,500): Red, Green and Blue lines."},
   "heavy": {"label": "Heavy rain", "title": "Museum, the big Sengen shrine, onsen",
    "why": "If the rain is steady: no forest climb, everything short and covered.",
    "steps": [
     ("09:30", "Lake bus to [[kubota]]. {{lake_tt}}"),
     ("12:00", "Loop bus to [[kitaguchi]]: the cedar avenue in the mist is at its best in rain. {{fujikko_tt}}"),
     ("13:30", "Lunch nearby: [[udon]]."),
     ("15:00", "[[yurari]] or the hotel onsen until dinner."),
    ]},
   "dry": {"label": "If it stays dry", "title": "Springs village and the sky torii",
    "why": "If Monday turns out dry after all.",
    "steps": [
     ("09:00", "[[tenjoyama]] for Fuji over the lake."),
     ("09:30", "Bus to [[oshino]], the spring ponds, before the tour groups."),
     ("12:30", "Back to the lake; [[asama]] and the climb to [[yohaisho]]."),
     ("16:00", "Onsen."),
    ]},
  }},

 {"id": "tue3", "date": "Tue 3 Nov", "md": "11-03", "fc": "kawa", "where": "Fujiyoshida → Tokyo · Asakusa", "who": "together",
  "bed": "Asakusa / Kuramae hotel",
  "versions": {
   "main": {"label": "Plan", "title": "Sengen shrine hike, then the train to Tokyo",
    "why": "Clear morning (20%), and Fuji is sharpest early. Culture Day holiday: be at the pagoda by 8.",
    "steps": [
     ("07:00", "Check out, leave the bags at the hotel. Fujikyu train from [[kawa_stn]] to [[shimoyoshida]], 15 min."),
     ("07:45", "Walk 15–20 min to [[arakura]]; climb the 398 steps to [[chureito]] for Fuji behind the pagoda."),
     ("08:30", "The little hike: the trail behind the pagoda up to [[arakurayama]] (1,180 m, steep in places, well signed). About 2h up and back. Good shoes."),
     ("11:00", "Down through [[honcho]], the retro street with Fuji at the end. Lunch: [[udon]]."),
     ("12:45", "Train back to Kawaguchiko, collect the bags."),
     ("14:08", "Fuji Excursion 32 from Kawaguchiko (Shimoyoshida 14:21), Shinjuku 16:06. Reserved seats: book now, it's a holiday. {{fujiexc_tt}} {{ekinet}}"),
     ("16:30", "Metro to Asakusa, check in."),
     ("19:00", "[[sensoji]] lit up and almost empty; dinner on [[hoppy]]."),
    ],
    "watch": "Holiday traffic back to Tokyo is heavy on the expressway in the afternoon: that's why this is the train, not the bus. If the 14:08 is full, the 14:58 (Shinjuku 16:58)."},
   "short": {"label": "Short + Meiji festival", "title": "Pagoda only, then Meiji Jingu's festival",
    "why": "Skip the summit, be in Tokyo for the last day of the autumn festival.",
    "steps": [
     ("07:00", "Train to [[shimoyoshida]] with the bags."),
     ("07:45", "[[arakura]] and the steps to [[chureito]], back down by 9."),
     ("09:30", "Fujikyu train to Otsuki, JR to Shinjuku (about 1h45 in all). {{fujikyu_up}}"),
     ("12:00", "[[meiji]]: Culture Day performances on the last festival day, chrysanthemums along the approach. {{meiji}}"),
     ("15:00", "[[catstreet]] down to Shibuya, then Asakusa to check in."),
    ],
    "watch": "No locker check done at Shimoyoshida: travel light, or send the big bags ahead (see Ideas)."},
   "bus": {"label": "Bus back instead", "title": "Sengen hike, then the bus",
    "why": "Cheaper, but holiday traffic can add an hour or more.",
    "steps": [
     ("07:00", "Train to [[shimoyoshida]]; [[chureito]] and [[arakurayama]] (see Plan)."),
     ("11:30", "Lunch, back to the lake for the bags."),
     ("13:00", "Bus from [[kawa_stn]] to [[busta]]; book early. {{bus_tt}} {{highwaybus}}"),
    ]},
  }},

 {"id": "wed4", "date": "Wed 4 Nov", "md": "11-04", "fc": "tokyo", "where": "Tokyo · Asakusa", "who": "split",
  "bed": "You: Asakusa hostel, night 1 of 3",
  "versions": {
   "main": {"label": "Plan", "title": "Slow last day together; she flies back",
    "steps": [
     ("08:00", "[[sensoji]] and Nakamise before the crowds."),
     ("09:30", "To [[yanaka]]: temples, cats, the old shopping street. Down through [[uenopark]]."),
     ("12:30", "Lunch at [[ameyoko]], then [[kappabashi]]."),
     ("Afternoon", "She heads to the airport (flight time to add). From Asakusa there are direct trains to both Narita and Haneda; Skyliner from Ueno for Narita. {{skyliner}} {{keikyu}}"),
     ("Evening", "You: check in to the hostel; the Sumida river at night."),
    ]},
   "meiji": {"label": "Harajuku day", "title": "Meiji Jingu and Harajuku, then the airport",
    "steps": [
     ("09:00", "[[meiji]] in the morning calm."),
     ("11:00", "[[catstreet]] to Shibuya; lunch."),
     ("Afternoon", "She heads to the airport. {{skyliner}} {{keikyu}}"),
    ]},
  }},

 {"id": "thu5", "date": "Thu 5 Nov", "md": "11-05", "fc": "tokyo", "where": "Tokyo", "who": "you",
  "bed": "Asakusa hostel, night 2 of 3",
  "versions": {
   "main": {"label": "Rainy Tokyo", "title": "Museum, food hall, digital art, a hot bath",
    "why": "Showers likely (50%) and only 15°C.",
    "steps": [
     ("09:30", "[[tnm]] in Ueno (open Thu)."),
     ("12:30", "Lunch at [[ginza_depa]]."),
     ("14:30", "[[teamlab]] (book a slot)."),
     ("18:00", "A long soak at [[laqua]]."),
    ]},
   "kamakura": {"label": "If dry: Kamakura", "title": "Kamakura's temples and the Buddha",
    "steps": [
     ("08:30", "JR to Kita-Kamakura (1h): [[engakuji]]."),
     ("11:00", "Daibutsu hiking course to the [[daibutsu]]."),
     ("14:00", "[[yuigahama]], then back to Tokyo."),
    ]},
  }},

 {"id": "fri6", "date": "Fri 6 Nov", "md": "11-06", "fc": "tokyo", "where": "Tokyo · Mt Takao", "who": "you",
  "bed": "Asakusa hostel, night 3 of 3",
  "versions": {
   "main": {"label": "Plan", "title": "Mt Takao hike",
    "why": "The drier of your solo days (30%).",
    "steps": [
     ("08:00", "Keio line from Shinjuku to [[takaosanguchi]] (about 50 min)."),
     ("09:00", "Trail 6 up past the waterfall (check it's open at the station), along the ridge to [[takao_shiroyama]] for Fuji."),
     ("13:00", "Down trail 1 past [[yakuoin]]."),
     ("15:00", "[[gokurakuyu]] next to the station."),
     ("19:00", "[[shimokita]]'s small bars."),
    ]},
   "kamakura": {"label": "Kamakura", "title": "Kamakura's temples and the beach",
    "steps": [
     ("08:30", "JR to Kita-Kamakura: [[engakuji]]."),
     ("11:00", "Hiking course to the [[daibutsu]]."),
     ("14:00", "[[yuigahama]]."),
    ]},
   "lazy": {"label": "Lazy day", "title": "Gardens and coffee in Kuramae",
    "steps": [
     ("10:00", "[[kiyosumi]]."),
     ("13:00", "Kuramae cafés and small shops, [[kappabashi]] if you missed it."),
    ]},
  }},

 {"id": "sat7", "date": "Sat 7 Nov", "md": "11-07", "fc": "tokyo", "where": "Tokyo → home", "who": "you",
  "bed": "On the plane",
  "versions": {
   "main": {"label": "Plan", "title": "Fly home",
    "steps": [
     ("08:00", "Breakfast at [[tsukiji]]."),
     ("13:30", "Skyliner from Ueno to Narita (41 min). {{skyliner}}"),
     ("17:20", "Your flight home (time from the booking to add here). Land Sun 8 Nov, train to Lille."),
    ]},
  }},
]

# ------------------------------------------------------------------ beds
BEDS = [
 {"nights": "Sat 31 Oct · 1 night", "where": "Higashi-nihombashi (Nihonbashi)", "status": "Booked",
  "options": ["h_apa_hn"], "note": "Direct trains from both airports; 20 min to Shinjuku for Sunday's bus."},
 {"nights": "Sun 1 – Tue 3 Nov · 2 nights", "where": "Kawaguchiko", "status": "Shortlist",
  "options": ["h_royal", "h_yamagisi", "h_kawahotel", "h_maruei"], "note": "Konanso, Mizno, Asafuji and Fuji Lake Hotel sold out on Booking."},
 {"nights": "Tue 3 Nov · 1 night", "where": "Asakusa / Kuramae", "status": "Shortlist",
  "options": ["h_focus", "h_apa_asakusa", "h_enhouse"], "note": "Direct trains from Asakusa to both airports. Tonight's APA (Higashi-nihombashi) is on the same line, 3 stops away, if you'd rather go back to it."},
 {"nights": "Wed 4 – Sat 7 Nov · 3 nights (you)", "where": "Asakusa", "status": "Shortlist",
  "options": ["h_wasabi", "h_samurai"], "note": "Private single: APA Asakusa ~€277 for 3 nights."},
]

# ------------------------------------------------------------------ ideas to drop in anywhere
IDEAS = [
 ("Send the big bags ahead", "From tonight's hotel front desk, send the suitcases to the Asakusa hotel (takkyubin, next day, roughly ¥2,000–3,000 a bag). You travel to Fuji with day packs only. Ask on Saturday night."),
 ("The three Sengen shrines", "[[arakura]] (Chureito pagoda + Arakurayama trail, Tue), [[asama]] (cedars + the climb to [[yohaisho]], Mon), [[kitaguchi]] (the cedar avenue, heavy-rain version of Mon)."),
 ("Tenjoyama on foot", "Skip the ropeway: the path up to [[tenjoyama]] takes about 40 min from the lake shore."),
 ("Oshino Hakkai", "[[oshino]]: clear spring ponds, Fuji behind thatched roofs. Go before 10."),
 ("Fuji-view bath", "[[yurari]]: day onsen with Fuji in the outdoor bath, good after any wet day."),
 ("Maple corridor", "Colour is coming in early November, but the light-up and festival start on 7 Nov. {{maple_col}}"),
]

CHECKLIST = [
 "Book the Sunday bus (or Fuji Excursion seats): {{bus_book_sun}}",
 "Book Tuesday's Fuji Excursion 32 (14:08 Kawaguchiko → Shinjuku): {{ekinet}}",
 "Book e-bikes for Sunday 12:00 ([[bike_sora]] or [[bike_fujisan]]); the station shop is closed on weekends.",
 "Lock the Kawaguchiko and Asakusa beds (Saturday is booked).",
 "Add her flight time (Wed) and your flight home (Sat).",
 "Suica on the phone for metro, trains and buses.",
 "Warm layer: mornings 6–9°C at the lake.",
]
