# Verification log: what was checked, the result, and where. Shown on the page and in the spreadsheet.
# status: ok = checked and fine · warn = open but with a caveat · out = closed/damaged, kept out of the plans · todo = not yet verified
CHECKED = "28 Oct 2026"

CHECKS = [
    # Typhoon Champi (23–24 Oct)
    ("Taiwan", "Yangmingshan (Taipei)", "out", "Heavy Champi damage: roads cut and power out near Zhongshan Hall; visitor centres closed 25 Oct. Taipei/Hualien trip removed.",
     "Yahoo News TW / Taiwan News", "https://www.taiwannews.com.tw/zh/news/6464901"),
    ("Taiwan", "Hualien: Wanli river landslide-dam lake", "out", "Overflowing during Champi, 140 people moved; Taroko closed as a precaution from 21 Oct. Kept out of the plans.",
     "The Watchers / CNA", "https://watchers.news/2026/10/25/typhoon-champi-leaves-one-dead-and-hundreds-injured-as-recovery-continues-in-taiwan/"),
    ("Taiwan", "North-link & Yilan railway lines", "ok", "Fallen trees cleared; back to normal service from 15:00 on 24 Oct (not on any plan's route).",
     "United Daily News", "https://udn.com/news/story/125052/9835165"),
    ("Taiwan", "Alishan Forest Railway & recreation area", "ok", "Main line and Zhushan line running again from 25 Oct; branch lines from 24 Oct.",
     "Alishan Forest Railway (official)", "https://afrch.forest.gov.tw/AllNews"),
    ("Taiwan", "Highway 9 at Duoliang (South-link road)", "warn", "Waves washed out ~40 m of roadbed on 23 Oct; one lane. The plans use the South-link train instead, which is unaffected.",
     "ETtoday", "https://www.ettoday.net/news/20261023/3259595.htm"),
    ("Taiwan", "Highway 11 km 61 (Fengbin, Hualien)", "ok", "Lane undermined by waves 24 Oct, two-way traffic restored the same day. North of Dulan, not on the route.",
     "CNA", "https://cna.com.tw/news/asoc/202610240088.aspx"),
    ("Taiwan", "Taitung coast (Dulan, Luye)", "warn", "No damage reported in Dulan or Luye; big waves hit Fugang and Changbin harbours and foehn winds hurt crops. Check beach flags.",
     "Focus Taiwan", "https://focustaiwan.tw/society/202610230010"),
    ("Taiwan", "Bus 6739 Alishan ↔ Sun Moon Lake", "todo", "Listed in 2026 sources; timetable not confirmed. Check with the operator before the Fuller south plan.",
     "NOWnews", "https://www.nownews.com/news/6794109"),
    # Typhoon In-fa
    ("All", "Typhoon In-fa", "warn", "Expected to stall near the Ogasawara islands from 1 Nov; unlikely to reach Honshu and very unlikely to affect Taiwan. Recheck on 30 Oct.",
     "tenki.jp (28 Oct) / China Times (28 Oct)", "https://tenki.jp/forecaster/gureweather/2026/10/28/41126.html"),
    # Japan
    ("Japan", "Aso volcano", "warn", "Alert level 2: the zone within ~1 km of the Nakadake crater is closed. Plans avoid the crater; Kusasenri viewpoints are outside it.",
     "Japan Meteorological Agency (9 Oct)", "https://www.data.jma.go.jp/vois/data/report/volinfo/VK20261009160000_503.html"),
    ("Japan", "Kuju volcano", "ok", "Alert level 1 (normal); stay away from the Iozan fumaroles.",
     "Japan Meteorological Agency", "https://www.data.jma.go.jp/vois/data/report/activity_info/502.html"),
    ("Japan", "Hakone Ropeway", "ok", "No suspension announced for autumn 2026; runs 9:00–17:00, stops for strong wind or heavy rain.",
     "Hakone Navi / Vegcale (26 Sep)", "https://vegcale.com/2026/09/27/hakone-koyo-2026/"),
    ("Japan", "Nikko: Akechidaira ropeway", "out", "Closed for renovation until 31 Aug 2027: not used in the plans.",
     "Vegcale", "https://vegcale.com/2026/09/14/nikko-momiji-2026/"),
    ("Japan", "Nikko: Senjogahara shuttle bus", "warn", "Runs with a self-driving trial from 4 to 30 Nov; the walk itself is unchanged.",
     "Vegcale", "https://vegcale.com/2026/09/14/nikko-momiji-2026/"),
    ("Japan", "Nankai line + Koyasan cable car", "ok", "No suspension notice found for Oct–Nov 2026 (searched 28 Oct). Confirm the day before.",
     "Search of Nankai / news sites", "https://www.nankai.co.jp/"),
    ("Japan", "Kumano Kodo trail conditions", "todo", "The official trail-conditions page could not be loaded today. Check it before booking the Fuller Kansai plan.",
     "Tanabe City Kumano Tourism Bureau", "https://www.tb-kumano.jp/en/kumano-kodo/conditions/"),
    ("Japan", "Karatsu Kunchi", "ok", "Held every year on 2–4 Nov; 4 Nov is the last parade day.",
     "Japan Travel / JNTO", "https://ja.japantravel.com/saga/karatsu-kunchi-festival/32010"),
    ("Japan", "Mon 2 Nov / Tue 3 Nov", "warn", "Heavy rain forecast on 2 Nov across Japan (27 Oct run); 3 Nov is a national holiday (Culture Day).",
     "Open-Meteo ECMWF ensemble (27 Oct)", "https://open-meteo.com/en/docs/ensemble-api"),
    # Vietnam
    ("Vietnam", "Ninh Binh & Pu Luong", "warn", "Northern Vietnam flooded in mid-Sept 2026; no late-Oct flood reports found. Ask the Pu Luong homestay about the road.",
     "Local 10 (17 Sep)", "https://www.local10.com/espanol/2026/09/17/fuertes-lluvias-e-inundaciones-en-el-norte-de-vietnam-anegan-casas-y-afectan-economia/"),
    # Flights and prices
    ("All", "Flights out on 31 Oct", "warn", "Prices are live fares from 27 Oct for 1 person; the last 1–2 seats in a fare bucket can cost more for two. Recheck before booking.",
     "Google Flights (27 Oct)", "https://www.google.com/travel/flights"),
    ("All", "Her flight back on Fri 6 Nov", "todo", "Schedules checked 28 Oct; prices are estimates (no browser was reachable to check them live).",
     "FlightConnections (28 Oct)", "https://www.flightconnections.com/"),
    ("All", "Your flight home", "warn", "Saturday fares are live from 27 Oct; Friday fares assumed equal (estimate).",
     "Google Flights (27 Oct)", "https://www.google.com/travel/flights"),
    ("All", "Private-room prices", "todo", "Typical rates for a private double in each place, not live quotes. Check on Booking/Agoda once you pick.",
     "Estimates", "https://www.booking.com/"),
]
