# The other duo trips (Kansai, Kyushu, Taiwan) x 2 plans; the Tokyo + town trips are in trips_tokyo.py.
# Together Sat 31 Oct -> Wed 4 Nov (she flies back to HK that evening); you alone Thu 5 + Fri 6; you fly home Sat 7 Nov.
# Money in euros. Nights: 4 together (room price for the two of you) + 3 alone (your room or bed).
# meals=True means dinner + breakfast come with the room (temple, minshuku, ryokan).
# transport_pp / activities_pp: per person while together; shared: taxis and private cars split between you.
# solo_transport / solo_activities: yours alone, Wed evening -> Sat.
# Each day: t title, e effort, who (both / split / you), am/pm/eve, sleep, wx (forecast base), tr [mode, leg, minutes], b (if it rains)


def D(t, e, who, am, pm, eve, sleep, wx, tr, b=None):
    return {"t": t, "e": e, "who": who, "am": am, "pm": pm, "eve": eve, "sleep": sleep, "wx": wx, "tr": tr, "b": b}


def N(place, room, meals=False, solo=False):
    return {"place": place, "room": room, "meals": meals, "solo": solo}


def S(place, room, meals=False):
    return N(place, room, meals, True)


HK_DEP = ["train", "Central → HK airport (Airport Express)", 25]

TRIPS = [
# ---------------------------------------------------------------- Kansai without Kyoto
{
 "id": "jp-kansai", "country": "Japan", "region": "Nara, Koyasan & Kumano", "cc": "JP", "short": "Japan · Nara & Kumano",
 "title": "Nara, Koyasan & the Kumano Kodo (no Kyoto)",
 "tagline": "Nara at dawn and a night in a mountain temple together; then the Kumano Kodo pilgrim trail on your own.",
 "out": "kix", "her": "kix", "his": "kix", "climate_of": "jp-kansai",
 "food_day": 28, "solo_food": 25,
 "transport": "Trains (ICOCA card), Nankai to Koyasan, buses in Kumano (confirm times the day before). Luggage can be sent ahead by takkyubin.",
 "crowds": "Nara park fills by 10:00; dawn and evening are empty. Koyasan and Kumano are calm, and your Kumano days are weekdays.",
 "food": ["Osaka: takoyaki, kushikatsu, okonomiyaki", "Nara: kakinoha-zushi (persimmon-leaf sushi), mochi", "Shojin ryori: the monks' vegan dinner at Koyasan", "Onsen-boiled eggs and river fish at Yunomine"],
 "hikes": ["Kasuga primeval-forest trail, Nara (2h)", "Kumano Kodo: Takijiri → Chikatsuyu (14 km)", "Kumano Kodo: Hosshinmon-oji → Hongu Taisha (7 km)"],
 "culture": ["Todai-ji's Great Buddha", "Kasuga Taisha's 3,000 lanterns", "Okunoin cemetery by lantern light", "Kumano Hongu Taisha and the giant torii at Oyunohara"],
 "adventure": [{"name": "Temple stay at Koyasan", "price": "~¥28,000 for two with 2 meals", "note": "Private tatami room, morning prayers, fire ceremony"},
               {"name": "Bathe in Tsuboyu, Yunomine", "price": "¥800 per 30 min (private)", "note": "The only UNESCO-listed hot spring you can bathe in"},
               {"name": "Kumano stamp book", "price": "free", "note": "Stamp boxes at each oji shrine"}],
 "pros": ["No Kyoto, nothing missing: Nara is older and calmer", "The temple night is made for two", "Your solo days on the Kumano Kodo, the best walk on the list", "Dry from 3 Nov on (forecast 27 Oct)"],
 "cons": ["Mon 2 Nov: 50% chance of rain on the Kii mountains (29 Oct forecast)", "Kumano buses are infrequent", "Kumano and Koyasan rooms book out: reserve today", "Your flight home is the priciest (€618)"],
 "calm": "Nara at dawn and the Koyasan temple night together. Then the Kumano Kodo on your own, ending in the Yunomine onsen village.",
 "scores": {"hike": 5, "nature": 4.5, "food": 5, "culture": 5, "chill": 4},
 "value": 2, "ease": 4,
 "plans": [
  {"style": "Chill", "name": "Nara, a temple night, Osaka; the Kumano Kodo on your own", "chill": 70,
   "route": ["Together: 2n Nara, 1n Koyasan temple, 1n Osaka", "Wed: Osaka, she flies from Kansai 17:20", "You: 1n Kii-Tanabe, 1n Chikatsuyu, 1n Yunomine", "Sat: Kansai 19:05"],
   "nights": [N("Nara hotel double", 68), N("Nara", 68), N("Koyasan shukubo, dinner + breakfast", 158, True), N("Osaka (Namba) hotel double", 68),
              S("Kii-Tanabe guesthouse", 35), S("Chikatsuyu minshuku, dinner + breakfast", 85, True), S("Yunomine minshuku, dinner + breakfast", 80, True)],
   "transport_pp": 60, "shared": 0, "activities_pp": 25, "solo_transport": 84, "solo_activities": 10,
   "days": [
    D("Fly to Osaka, bus to Nara", "Travel", "both", "Airport Express around 12:15.", "14:45 HK Express to Kansai, land 19:20.", "Limousine bus to Nara (1h35); late dinner near Kintetsu-Nara.", "Nara hotel", "Osaka",
      [HK_DEP, ["plane", "HKG → KIX", 215], ["bus", "Kansai → Nara", 95]]),
    D("Nara at dawn", "Easy", "both", "Todai-ji at 7:30 opening; the deer, Nigatsu-do's balcony view.", "Isuien garden, then Naramachi's old houses and cafés.", "Kakinoha-zushi and sake in Naramachi.", "Nara hotel", "Osaka",
      []),
    D("Up to Koyasan", "Travel", "both", "Kintetsu + Nankai via Hashimoto (2h), cable car up.", "Kongobu-ji's rock garden and the covered halls of the Danjo Garan.", "Shojin dinner, then Okunoin's lanterns if the rain eases.", "Koyasan shukubo", "Koyasan",
      [["train", "Nara → Hashimoto → Gokurakubashi", 120], ["cable", "Cable car + bus to Koyasan", 20]], "Rain is possible (50%): a temple is the right place for it."),
    D("Morning prayers, down to Osaka", "Travel", "both", "06:00 fire ceremony, temple breakfast, Okunoin in daylight.", "Nankai to Namba (1h50); Shitennoji.", "Dotonbori and Shinsekai: kushikatsu.", "Osaka hotel (Namba)", "Osaka",
      [["cable", "Koyasan → Gokurakubashi", 20], ["train", "Gokurakubashi → Namba", 90]]),
    D("Osaka; she flies at 17:20", "Travel", "split", "Kuromon market and Nakazakicho's lanes together.", "She takes the Nankai to Kansai ~15:00 for HK Express 17:20 (lands HK 21:00). You: Kuroshio express from Tennoji to Kii-Tanabe (2h15).", "You: Tanabe's izakaya street.", "You: Kii-Tanabe guesthouse", "Osaka",
      [["train", "Osaka → Kii-Tanabe", 135]]),
    D("Kumano Kodo: Takijiri → Chikatsuyu", "Big day", "you", "Bus to Takijiri (40 min), steep start up to Takahara.", "On through the cedars to Chikatsuyu (14 km, 6–7h).", "Minshuku dinner.", "Chikatsuyu minshuku", "Kumano Hongu",
      [["bus", "Kii-Tanabe → Takijiri", 40]]),
    D("Into Hongu, Yunomine", "Active", "you", "Bus ahead to Hosshinmon-oji, walk 7 km into Kumano Hongu Taisha.", "Oyunohara's giant torii; bus to Yunomine.", "Tsuboyu bath, inn dinner.", "Yunomine minshuku", "Kumano Hongu",
      [["bus", "Chikatsuyu → Hosshinmon-oji", 30], ["bus", "Hongu → Yunomine", 15]]),
    D("Fly home", "Travel", "you", "Bus Hongu → Kii-Tanabe (2h) at about 09:30.", "Train to Kansai airport (2h30).", "Cathay 19:05 via HK, land Paris Sun 07:45.", "On the plane", "Osaka",
      [["bus", "Hongu → Kii-Tanabe", 120], ["train", "Kii-Tanabe → Kansai", 150]]),
   ]},
 ]},
# ---------------------------------------------------------------- Kyushu
{
 "id": "jp-kyushu", "country": "Japan", "region": "Fukuoka, Yufuin & Kurokawa", "cc": "JP", "short": "Japan · Kyushu",
 "title": "Kyushu: a festival, onsen towns and volcano views",
 "tagline": "Fukuoka's food stalls, an onsen town, and the Karatsu Kunchi floats on her last day; then Kurokawa and the Kuju peaks on your own.",
 "out": "fuk", "her": "fuk", "his": "fuk", "climate_of": "jp-kyushu",
 "food_day": 26, "solo_food": 25,
 "transport": "Highway buses between Fukuoka, Yufuin and Kurokawa (book ahead), JR to Karatsu. Fukuoka airport is 5 min from Hakata.",
 "crowds": "Karatsu fills for the Kunchi (2–4 Nov). Yufuin's main street is busy at midday; mornings by Lake Kinrin are empty.",
 "food": ["Fukuoka: tonkotsu ramen and yatai stalls by the river", "Mentaiko, motsunabe", "Bungo beef and toriten in Oita", "Kaiseki at a Kurokawa inn"],
 "hikes": ["Mt Homan above Dazaifu (3h)", "Kuju: Makinoto pass → Nakadake, Kyushu's highest (5–6h)", "Lake Kinrin and Yufuin's back lanes", "Nokonoshima island paths"],
 "culture": ["Karatsu Kunchi: 14 giant lacquered floats (2–4 Nov)", "Dazaifu Tenmangu shrine", "Kurokawa's onsen-hopping with a wooden pass", "Kyushu National Museum"],
 "adventure": [{"name": "Karatsu Kunchi", "price": "free", "note": "Wed 4 Nov: the floats parade round the old town, then she flies at 20:00"},
               {"name": "Kurokawa onsen pass (nyuto tegata)", "price": "¥1,500", "note": "Three outdoor baths of your choice"},
               {"name": "Kuju highlands hike", "price": "taxi ~¥6,000", "note": "Alert level 1 (normal); Aso is at level 2, so its crater zone is closed"}],
 "pros": ["Bluest skies in the 27 Oct forecast", "The festival falls on her last day", "Her flight back at 20:00 leaves the whole day", "Onsen towns at their calmest"],
 "cons": ["Aso's crater zone closed (alert level 2)", "Highway buses need booking", "Kurokawa inns are pricey, even alone", "Your flight home is €612"],
 "calm": "Yufuin (2 nights together): mist on Lake Kinrin at 7am, a private onsen, the Yufu peak over the rice fields. Then Kurokawa's river gorge on your own.",
 "scores": {"hike": 4, "nature": 4.5, "food": 5, "culture": 4.5, "chill": 4.5},
 "value": 2.5, "ease": 4,
 "plans": [
  {"style": "Chill", "name": "Fukuoka, Yufuin and the Kunchi; Kurokawa and Kuju on your own", "chill": 70,
   "route": ["Together: 2n Fukuoka, 2n Yufuin", "Wed: Karatsu Kunchi, she flies from Fukuoka 20:00", "You: 1n Fukuoka, 2n Kurokawa (Kuju hike)", "Sat: bus to Fukuoka airport, 16:35"],
   "nights": [N("Fukuoka (Hakata) hotel double", 62), N("Fukuoka", 62), N("Yufuin guesthouse, private room", 79), N("Yufuin", 79),
              S("Fukuoka hostel", 25), S("Kurokawa-area minshuku, dinner + breakfast", 90, True), S("Kurokawa-area minshuku", 90, True)],
   "transport_pp": 72, "shared": 0, "activities_pp": 20, "solo_transport": 83, "solo_activities": 10,
   "days": [
    D("Fly to Fukuoka", "Travel", "both", "Airport Express around 10:30.", "12:55 HK Express to Fukuoka, land 17:00; subway to Hakata (5 min).", "Yatai stalls along the river at Nakasu.", "Fukuoka hotel (Hakata)", "Fukuoka",
      [HK_DEP, ["plane", "HKG → FUK", 185], ["metro", "Airport → Hakata", 5]]),
    D("Dazaifu", "Easy", "both", "Train to Dazaifu (30 min): Tenmangu shrine, umegae-mochi.", "Kyushu National Museum and Komyozenji's moss garden.", "Ramen in Hakata.", "Fukuoka hotel", "Fukuoka",
      [["train", "Fukuoka ↔ Dazaifu", 60]]),
    D("Bus to Yufuin", "Travel", "both", "Highway bus Hakata → Yufuin (2h15).", "Private onsen, then the back lanes if it stays dry.", "Dinner in Yufuin.", "Yufuin guesthouse", "Yufuin",
      [["bus", "Hakata → Yufuin", 135]], "Rain is possible (50–60%): a bus and an onsen."),
    D("Lake Kinrin and Yufuin slow", "Easy", "both", "Lake Kinrin in the morning mist, the back lanes along the river.", "Bus to Beppu's hells (50 min) or stay put.", "Toriten and Bungo beef.", "Yufuin guesthouse", "Yufuin",
      [["bus", "Yufuin ↔ Beppu (optional)", 100]]),
    D("Karatsu Kunchi; she flies at 20:00", "Active", "split", "Early bus to Hakata (2h15), JR to Karatsu (1h25).", "The 14 floats parade round the old town. She takes the train straight to Fukuoka airport (~1h30) for 20:00 (lands HK 22:40).", "You: back to Hakata, a last yatai.", "You: Fukuoka hostel", "Fukuoka",
      [["bus", "Yufuin → Hakata", 135], ["train", "Fukuoka → Karatsu → Fukuoka", 170]]),
    D("Bus to Kurokawa", "Travel", "you", "Highway bus Fukuoka → Kurokawa (2h30).", "Onsen-hopping with the wooden pass.", "Minshuku dinner.", "Kurokawa-area minshuku", "Kurokawa",
      [["bus", "Fukuoka → Kurokawa", 150]]),
    D("Kuju: Kyushu's roof", "Big day", "you", "Taxi to Makinoto pass (25 min).", "Up to Nakadake (1,791 m) and back (5–6h).", "Back to the inn's bath.", "Kurokawa-area minshuku", "Kuju",
      [["taxi", "Kurokawa ↔ Makinoto pass", 50]]),
    D("Fly home", "Travel", "you", "Morning bath.", "Bus Kurokawa → Fukuoka airport (about 2h30; confirm the time) by 13:30.", "Cathay 16:35 via HK, land Paris Sun 07:45.", "On the plane", "Kurokawa",
      [["bus", "Kurokawa → Fukuoka airport", 150]]),
   ]},
 ]},
# ---------------------------------------------------------------- Taiwan south
{
 "id": "tw-south", "country": "Taiwan", "region": "Tainan, Sun Moon Lake & Alishan", "cc": "TW", "short": "Taiwan · south",
 "title": "Tainan food, Sun Moon Lake & Alishan",
 "tagline": "Eat your way round Taiwan's oldest city and two days on a mountain lake together; then the Alishan forest on your own. Untouched by Typhoon Champi.",
 "out": "khh", "her": "khh", "his": "khh", "climate_of": "tw-south",
 "food_day": 18, "solo_food": 15,
 "transport": "High-speed rail, buses and an EasyCard. Alishan Forest Railway seats sell out: book as soon as you choose.",
 "crowds": "Weekends at Sun Moon Lake are busy; weekdays calm. Tainan is busy only at the famous breakfast stalls.",
 "food": ["Tainan: beef soup at dawn, milkfish, shrimp rolls, danzai noodles", "Night markets: Garden (Thu–Sun) in Tainan, Ruifeng in Kaohsiung", "Sun Moon Lake black tea and Thao dishes", "Alishan high-mountain oolong"],
 "hikes": ["Ci'en pagoda over Sun Moon Lake (1h)", "Shuishe Mountain, the peak over the lake (5h)", "Alishan giant-tree trail and Zhushan sunrise", "Tashan trail, Alishan (2h, steep)"],
 "culture": ["Tainan's 300-year-old temples and the Chihkan tower", "Anping fort and the tree house", "Thao village at Ita Thao", "Alishan Forest Railway (running again since 25 Oct)"],
 "adventure": [{"name": "Alishan Forest Railway", "price": "~NT$600", "note": "Reopened 25 Oct after Champi; book seats now"},
               {"name": "Sicao mangrove tunnel boat", "price": "NT$200", "note": "30 min under the mangroves"},
               {"name": "Sun Moon Lake by bike", "price": "~NT$400 e-bike", "note": "Lakeside path, one of the world's prettiest rides"}],
 "pros": ["She speaks the language: everything is easy", "Dry, warm forecast (Tainan 30–32°C)", "Half the cost of Japan", "No Champi damage on this route"],
 "cons": ["Alishan train seats may be sold out", "Hot in Tainan at midday", "Her flight back at 21:00 lands 22:40", "Typhoon In-fa: recheck on 30 Oct"],
 "calm": "Sun Moon Lake (2 nights together): the lake at dawn before the boats start, a pagoda walk, tea at Yuchi. Alishan's cedar forest above the clouds on your own.",
 "scores": {"hike": 3.5, "nature": 4.5, "food": 5, "culture": 4.5, "chill": 4},
 "value": 4.5, "ease": 5,
 "plans": [
  {"style": "Chill", "name": "Tainan and Sun Moon Lake; Alishan on your own", "chill": 75,
   "route": ["Together: 2n Tainan, 2n Sun Moon Lake", "Wed: down together, she flies from Kaohsiung 21:00", "You: 2n Alishan, 1n Kaohsiung", "Sat: Kaohsiung 14:45"],
   "nights": [N("Tainan B&B, private double", 49), N("Tainan", 49), N("Sun Moon Lake guesthouse", 77), N("Sun Moon Lake", 77),
              S("Alishan hotel, single room", 55), S("Alishan", 55), S("Kaohsiung hostel", 20)],
   "transport_pp": 54, "shared": 40, "activities_pp": 20, "solo_transport": 56, "solo_activities": 10,
   "days": [
    D("Fly to Kaohsiung, on to Tainan", "Travel", "both", "Day with the family; Airport Express around 16:30.", "18:50 HK Express, land 20:15.", "Taxi to Tainan (50 min, shared), late beef soup.", "Tainan B&B", "Tainan",
      [HK_DEP, ["plane", "HKG → KHH", 85], ["taxi", "Kaohsiung airport → Tainan", 50]]),
    D("Eat your way round Tainan", "Easy", "both", "Beef soup at 7, the Confucius temple, Chihkan tower.", "Bikes to Anping: the fort and the tree house.", "Garden night market (Sun).", "Tainan B&B", "Tainan",
      []),
    D("Up to Sun Moon Lake", "Travel", "both", "HSR to Taichung (40 min), bus to the lake (1h40).", "Ita Thao and the lake path.", "Sunset on the water.", "Sun Moon Lake guesthouse", "Sun Moon Lake",
      [["train", "Tainan → Taichung HSR", 40], ["bus", "Taichung → Sun Moon Lake", 100]]),
    D("Round the lake", "Active", "both", "E-bikes on the lakeside path; Ci'en pagoda.", "Boat across, tea at Yuchi's tea farm.", "Thao dinner.", "Sun Moon Lake guesthouse", "Sun Moon Lake",
      [["boat", "Lake boat", 30]]),
    D("Down together; she flies at 21:00", "Travel", "split", "Last morning on the lake; bus to Taichung HSR together (1h40).", "She takes the HSR to Zuoying and the MRT to Kaohsiung airport for HK Express 21:00 (lands HK 22:40). You: HSR to Chiayi (20 min), bus 7329 up to Alishan (2h30; confirm the time).", "You: dinner in the Alishan village.", "You: Alishan hotel", "Alishan",
      [["bus", "Sun Moon Lake → Taichung HSR", 100], ["train", "Taichung → Chiayi HSR", 20], ["bus", "Chiayi HSR → Alishan", 150]]),
    D("Sunrise and Tashan", "Active", "you", "Zhushan sunrise train at about 05:00, the giant-tree trail.", "Tashan trail for the cliffs (2h).", "Oolong tasting.", "Alishan hotel", "Alishan",
      [["train", "Zhushan line", 30]]),
    D("Forest railway down, to Kaohsiung", "Travel", "you", "Alishan Forest Railway down to Chiayi (2h30).", "HSR to Zuoying (20 min); Pier-2 by the water.", "Ruifeng night market.", "Kaohsiung hostel", "Tainan",
      [["train", "Alishan → Chiayi (forest railway)", 150], ["train", "Chiayi → Zuoying HSR", 25]]),
    D("Fly home", "Travel", "you", "Cijin island by ferry, seafood lunch.", "MRT to the airport by 12:30.", "China Airlines + Qatar 14:45, land Paris Sun 06:35.", "On the plane", "Tainan",
      [["metro", "Kaohsiung → airport", 20]]),
   ]},
 ]},
# ---------------------------------------------------------------- Taiwan east
{
 "id": "tw-east", "country": "Taiwan", "region": "Taitung: Dulan & Luye", "cc": "TW", "short": "Taiwan · quiet east",
 "title": "Taiwan's quiet east: Dulan by the sea, Luye's tea hills",
 "tagline": "Slow days on the Pacific and a tea plateau together; then Tainan's food on your own. The calmest trip on the list.",
 "out": "khh_early", "her": "khh", "his": "khh", "climate_of": "tw-east",
 "food_day": 16, "solo_food": 15,
 "transport": "Trains on the South-link line (Kaohsiung ↔ Taitung) and taxis up the coast. Highway 9 at Duoliang lost a lane to Champi's waves: take the train, which is unaffected.",
 "crowds": "Almost none in November. Dulan's sugar factory gets a crowd on Saturday night for live music.",
 "food": ["Amis cooking in Dulan: wild greens, grilled fish", "Taitung: Lin's dumplings, Chishang rice boxes", "Luye red oolong tea", "Tainan's beef soup and shrimp rolls (your solo days)"],
 "hikes": ["Mt Dulan, the Amis sacred peak (4–5h)", "Jialulan coast and Xiaoyeliu rocks", "Luye Highland lanes", "Brown Avenue by bike (Chishang)"],
 "culture": ["Amis villages and the Dulan sugar factory", "Luye tea farms", "Pier-2 in Kaohsiung", "Tainan's temples"],
 "adventure": [{"name": "Tea tasting on Luye Highland", "price": "~NT$300", "note": "Red oolong at a family tea farm, with the Rift Valley below"},
               {"name": "Jinzun cliffs", "price": "free", "note": "Café over the bay; surfing lessons if the sea is calm"},
               {"name": "Brown Avenue by bike", "price": "NT$150", "note": "Rice fields with nothing in the way"}],
 "pros": ["The calmest trip: sea, then mountains", "She speaks Mandarin: easy everywhere", "Cheap", "No Champi damage reported in Dulan or Luye"],
 "cons": ["Long swells from Typhoon In-fa on 1–3 Nov: no swimming, stay off the waterline rocks", "Few buses: taxis needed", "A 3h train to Kaohsiung on her last day", "Typhoon In-fa: recheck on 30 Oct"],
 "calm": "Dulan (3 nights together): guesthouse by the sea, the sugar factory café, the black-sand beach. Then a night on Luye's tea plateau.",
 "scores": {"hike": 3, "nature": 4.5, "food": 4, "culture": 3.5, "chill": 5},
 "value": 4.5, "ease": 4.5,
 "plans": [
  {"style": "Chill", "name": "Dulan and Luye together; Tainan on your own", "chill": 85,
   "route": ["Together: 3n Dulan, 1n Luye", "Wed: train to Kaohsiung together, she flies 21:00", "You: 3n Tainan (food, Anping, mangroves)", "Sat: Kaohsiung 14:45"],
   "nights": [N("Dulan guesthouse, private double", 55), N("Dulan", 55), N("Dulan", 55), N("Luye B&B (breakfast)", 66),
              S("Tainan hostel", 18), S("Tainan hostel", 18), S("Tainan hostel", 18)],
   "transport_pp": 39, "shared": 60, "activities_pp": 10, "solo_transport": 25, "solo_activities": 10,
   "days": [
    D("Fly to Kaohsiung, train to the coast", "Travel", "both", "Airport Express around 10:30.", "12:45 HK Express, land 14:10; train Kaohsiung → Taitung (2h).", "Taxi up the coast to Dulan (30 min).", "Dulan guesthouse", "Dulan",
      [HK_DEP, ["plane", "HKG → KHH", 85], ["train", "Kaohsiung → Taitung", 120], ["taxi", "Taitung → Dulan", 30]]),
    D("Do nothing by the Pacific", "Easy", "both", "Coffee at the sugar factory.", "Beach, book, nap.", "Grilled fish in the village.", "Dulan guesthouse", "Dulan",
      [], "Long swells from Typhoon In-fa (1–3 Nov): watch the sea from the sand or a café, no swimming."),
    D("Coast walk: Jialulan to Xiaoyeliu", "Easy", "both", "Taxi south to Jialulan (20 min), walk the coast.", "Xiaoyeliu's sculpted rocks.", "Back to Dulan.", "Dulan guesthouse", "Dulan",
      [["taxi", "Dulan ↔ Jialulan", 40]], "Swell day (In-fa, 1–3 Nov): keep to the upper paths, away from the wave-washed rocks."),
    D("Jinzun, then up to Luye", "Travel", "both", "Jinzun cliff café over the bay.", "Train Taitung → Luye (25 min), taxi up the plateau.", "Sunset over the Rift Valley.", "Luye B&B", "Luye",
      [["taxi", "Dulan → Jinzun → Taitung", 60], ["train", "Taitung → Luye", 25]]),
    D("Tea, then Kaohsiung; she flies at 21:00", "Travel", "split", "Red oolong tasting at a tea farm.", "Train Luye → Kaohsiung together (3h); Pier-2 by the water. She takes the MRT to the airport for HK Express 21:00 (lands HK 22:40).", "You: train to Tainan (40 min).", "You: Tainan hostel", "Tainan",
      [["train", "Luye → Kaohsiung", 180], ["train", "Kaohsiung → Tainan", 40]]),
    D("Eat your way round Tainan", "Easy", "you", "Beef soup at 7, the Confucius temple, Chihkan tower.", "Bike to Anping: the fort and the tree house.", "Garden night market (Thu).", "Tainan hostel", "Tainan",
      []),
    D("Mangroves and the sea", "Easy", "you", "Sicao mangrove tunnel boat.", "Sunset on Yuguang island.", "Shennong Street.", "Tainan hostel", "Tainan",
      [["taxi", "Tainan ↔ Sicao", 30]]),
    D("Fly home", "Travel", "you", "Last beef soup.", "Train + MRT to Kaohsiung airport by 12:30 (1h).", "China Airlines + Qatar 14:45, land Paris Sun 06:35.", "On the plane", "Tainan",
      [["train", "Tainan → Kaohsiung airport", 60]]),
   ]},
 ]},
]
