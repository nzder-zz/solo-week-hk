# Kanazawa options (29 Oct): Kanazawa & around, or Kanazawa + Tokyo. One chill plan each.
# Both fly HK → Komatsu on Sat 31 Oct (09:30, the only nonstop). No Komatsu → HK flight on Wednesdays,
# so in "Kanazawa & around" she takes the train to Kansai airport (17:20); in "Kanazawa + Tokyo" she flies from Narita 19:00.
from trips import D, N, S, HK_DEP
from trips_tokyo import DAY_WED, SOLO_TOKYO, TOKYO_HOTEL, TOKYO_HOSTEL

KZ_HOTEL = N("Kanazawa hotel double (near Omicho / Higashi Chaya)", 75)

KZ_DAY1 = D("Fly to Komatsu, Higashi Chaya at dusk", "Travel", "both",
            "An early start: Airport Express from Central around 07:00 for the 09:30 HK Express to Komatsu.",
            "Land 14:05; airport bus to Kanazawa station (40 min), check in.",
            "Higashi Chaya's wooden teahouse street at dusk, then oden or a seafood izakaya.", "Kanazawa hotel", "Kanazawa",
            [HK_DEP, ["plane", "HKG → KMQ", 215], ["bus", "Komatsu airport → Kanazawa", 40]],
            "Rain likely on arrival (60%): Kanazawa is famous for it; the teahouses and a long dinner work in the wet.")

KZ_DAY2 = D("Kanazawa by bike: garden, market, samurai lanes", "Active", "both",
            "Machi-nori bike-share (bus + bike day ticket ¥2,000 in the 'Norimasshi Kanazawa' app): Kenrokuen at 8:00 opening (maples turning), the castle park next door.",
            "Ride to Omicho market for a seafood lunch (kaisendon), then the 21st Century Museum (open Sunday) and Nagamachi's samurai lanes. Everything is 5–10 minutes apart by bike, mostly flat.",
            "Kazue-machi's riverside teahouses at dusk; drop the bikes at any port.", "Kanazawa hotel", "Kanazawa",
            [], "Sunday is the dry day (30%), so the ride is today. If it rains, the same loop by the city bus (the ticket covers both).")

TRIPS_KANAZAWA = [
# ---------------------------------------------------------------- Kanazawa & around
{
 "id": "jp-kanazawa", "group": "kanazawa", "town": "Kanazawa", "country": "Japan", "region": "Kanazawa, Shirakawa-go & Yamanaka Onsen", "cc": "JP", "short": "Kanazawa & around",
 "title": "Kanazawa & around: gardens by bike and an onsen ryokan",
 "tagline": "Three nights in Kanazawa (a bike-share day between the garden, the market and the samurai lanes), then a Yamanaka onsen ryokan. Shirakawa-go moves to your solo ride.",
 "out": "kmq", "her": "kix_kaga", "his": "tokyo", "climate_of": "jp-kanazawa",
 "food_day": 28, "solo_food": 25,
 "town_card": {"time": "Fly HK → Komatsu (09:30), 40 min bus", "best": "Gardens, teahouse streets and seafood by bike-share, an onsen ryokan", "crowds": "Kenrokuen and Omicho busy from 10:00: ride there early", "rain": "Kanazawa is used to it: museums, teahouses, the market, the ryokan", "room": "Kanazawa hotel ~€75; Yamanaka ryokan with dinner ~€190"},
 "transport": "Airport bus Komatsu ↔ Kanazawa, Machi-nori bike-share and the city bus (one day ticket), the Hokuriku shinkansen to Kaga-Onsen. She leaves on Wednesday by train to Kansai airport (no Komatsu → HK flight that day).",
 "crowds": "Kenrokuen and Omicho fill from 10:00, so ride there first. Yamanaka is quiet. Shirakawa-go (your solo Wednesday) is calmer on a weekday.",
 "food": ["Omicho market: kaisendon (seafood rice bowl), oysters, nodoguro (blackthroat seaperch)", "Kanazawa oden and gold-leaf ice cream", "Hida beef in Takayama (your solo days)", "Kaga kaiseki at the Yamanaka ryokan"],
 "hikes": ["Kanazawa by Machi-nori bike-share (flat, short hops)", "Kakusenkei gorge path, Yamanaka (1.3 km by the river)", "Higashiyama walking course, Kanazawa", "Takayama's Higashiyama temple walk (your solo days)"],
 "culture": ["Kenrokuen, one of Japan's three great gardens", "Higashi Chaya and Kazue-machi teahouse districts", "21st Century Museum and the D.T. Suzuki Museum", "Shirakawa-go's thatched farmhouses (your solo ride)"],
 "adventure": [{"name": "Tea at a Higashi Chaya teahouse", "price": "~¥1,000", "note": "Matcha and a sweet in a 200-year-old geisha house"},
               {"name": "Yamanaka onsen ryokan", "price": "~¥34,000 for two with dinner + breakfast", "note": "Kaga kaiseki, baths, the gorge outside"},
               {"name": "Bus + Machi-nori day ticket", "price": "¥2,000 each", "note": "Unlimited city buses and bike-share for a day (app ticket)"}],
 "pros": ["Japan's best-kept old city, flat and easy by bike", "Excellent food: Omicho's seafood, Kaga cuisine", "Only two beds together and under 1h of transport after the flight", "A ryokan night to finish"],
 "cons": ["An early flight (09:30) on Saturday", "No Wednesday flight from Komatsu: she has a 3h30 train to Kansai airport", "Rainiest of the shortlist (Kanazawa 60% on Sat and Mon)", "Your solo days need a long ride back to Tokyo on Friday"],
 "calm": "Kanazawa at its own pace (3 nights): a bike between the garden, the market and the teahouses; then a ryokan night by Yamanaka's gorge.",
 "scores": {"hike": 2.5, "nature": 4, "food": 5, "culture": 5, "chill": 4.5}, "value": 2.5, "ease": 4,
 "plans": [
  {"style": "Chill", "name": "Kanazawa by bike, a Yamanaka ryokan; Shirakawa-go and Takayama on your own", "chill": 80,
   "route": ["Together: 3n Kanazawa (bike day Sunday), 1n Yamanaka onsen ryokan", "Wed: she takes the train to Kansai airport for 17:20", "You: Shirakawa-go on the way, 2n Takayama, 1n Tokyo", "Sat: Narita 17:20"],
   "nights": [KZ_HOTEL, N("Kanazawa", 75), N("Kanazawa", 75), N("Yamanaka onsen ryokan, dinner + breakfast", 190, True),
              S("Takayama hostel", 30), S("Takayama hostel", 30), TOKYO_HOSTEL],
   "transport_pp": 32, "shared": 0, "activities_pp": 35, "her_extra": 60, "solo_transport": 150, "solo_activities": 15,
   "days": [
    KZ_DAY1,
    KZ_DAY2,
    D("A slow, rainy day in Kanazawa", "Easy", "both", "Myoryuji, the 'ninja temple' full of trap doors (guided visit, book), and the Nomura samurai house's garden.",
      "Tea and gold-leaf sweets in a Higashi Chaya teahouse; the Kanazawa castle's long storehouse (Gojikken Nagaya) inside.", "Oden in an old counter bar.", "Kanazawa hotel", "Kanazawa",
      [["bus", "City bus (same day ticket)", 15]], "Rain likely (60%): everything today is indoors or a few minutes apart."),
    D("D.T. Suzuki Museum, then a ryokan in Yamanaka", "Easy", "both", "The D.T. Suzuki Museum's water garden (open Tue), coffee in Higashi Chaya.",
      "Shinkansen to Kaga-Onsen (20 min), bus to Yamanaka; the Kakusenkei gorge path by the river.", "Kaga kaiseki dinner and the ryokan baths.", "Yamanaka onsen ryokan", "Yamanaka Onsen",
      [["train", "Kanazawa → Kaga-Onsen (shinkansen)", 20], ["bus", "Kaga-Onsen → Yamanaka", 30]]),
    D("Morning bath; she leaves for Kansai airport", "Travel", "split", "Bath before breakfast, the Korogi bridge in the gorge.",
      "11:30 bus to Kaga-Onsen together. She: shinkansen to Tsuruga, Thunderbird to Shin-Osaka, Haruka to Kansai for HK Express 17:20 (lands HK 21:00). You: back to Kanazawa, bus to Shirakawa-go (1h15): the thatched village and the Wada house, then on to Takayama (50 min).",
      "You: Takayama's old town by night.", "You: Takayama hostel", "Shirakawa-go",
      [["bus", "Yamanaka → Kaga-Onsen", 30], ["train", "Kaga-Onsen → Kanazawa", 20], ["bus", "Kanazawa → Shirakawa-go → Takayama", 125]]),
    D("Takayama", "Easy", "you", "Miyagawa morning market, then the Sanmachi old streets and sake breweries.", "Hida Folk Village (thatched houses on a hill) or the Higashiyama temple walk.", "Hida beef.", "Takayama hostel", "Takayama",
      [["bus", "Takayama ↔ Hida Folk Village", 20]]),
    D("Hida-Furukawa, then to Tokyo", "Travel", "you", "Train to Hida-Furukawa (15 min): canals full of carp and white storehouses.", "Hida limited express to Toyama, Hokuriku shinkansen to Tokyo (about 4h).", "Asakusa, Hoppy street.", "Tokyo hostel", "Takayama",
      [["train", "Takayama ↔ Hida-Furukawa", 30], ["train", "Takayama → Toyama → Tokyo", 240]]),
    D("Fly home", "Travel", "you", "Tsukiji outer market breakfast.", "Skyliner to Narita around 14:30.", "Etihad 17:20 to Brussels, land Sun 06:30.", "On the plane", "Tokyo",
      [["train", "Ueno → Narita (Skyliner)", 45]]),
   ]},
 ]},
# ---------------------------------------------------------------- Kanazawa + Tokyo
{
 "id": "jp-kanazawa-tokyo", "group": "kanazawa", "town": "Kanazawa + Tokyo", "country": "Japan", "region": "Kanazawa, then Tokyo", "cc": "JP", "short": "Kanazawa + Tokyo",
 "title": "Kanazawa + Tokyo: the old city, then the big one",
 "tagline": "Fly straight to Kanazawa for two nights of gardens, teahouses and seafood, then the shinkansen to Tokyo for Meiji Jingu's festival and a slow last day.",
 "out": "kmq", "her": "tokyo", "his": "tokyo", "climate_of": "jp-kanazawa",
 "food_day": 28, "solo_food": 25,
 "town_card": {"time": "Fly HK → Komatsu (09:30); shinkansen to Tokyo 2h30 on Monday", "best": "Two cities: Kanazawa's gardens and teahouses, then Tokyo", "crowds": "Kanazawa on Sun is busy from 10:00; Tokyo on the holiday is busy at Meiji Jingu", "rain": "The shinkansen day is the showery Monday", "room": "Kanazawa hotel ~€75; Tokyo hotel ~€85"},
 "transport": "Airport bus Komatsu → Kanazawa, Machi-nori bike-share on Sunday, then the Hokuriku shinkansen Kanazawa → Ueno (2h30, about ¥14,400 each). Suica in Tokyo; she leaves Ueno on the Skyliner.",
 "crowds": "Kenrokuen and Omicho fill from 10:00 on Sunday. Tue 3 Nov is busy in Tokyo, which absorbs it; Meiji Jingu's festival draws a crowd from late morning.",
 "food": ["Omicho market: kaisendon, oysters, nodoguro", "Kanazawa oden", "Tokyo: ramen, Ameyoko, Omoide Yokocho's yakitori", "Ekiben on the shinkansen"],
 "hikes": ["Kanazawa by Machi-nori bike-share (Sunday)", "Yanaka and Ueno park on foot", "Mt Takao from Tokyo (your Thursday)", "Kamakura's Daibutsu hiking course (your Friday)"],
 "culture": ["Kenrokuen and Kanazawa castle park", "Higashi Chaya and Nagamachi", "Senso-ji and Asakusa", "Meiji Jingu's autumn festival (3 Nov)"],
 "adventure": [{"name": "Tea at a Higashi Chaya teahouse", "price": "~¥1,000", "note": "Matcha and a sweet in an old geisha house"},
               {"name": "Hokuriku shinkansen", "price": "~¥14,400 each", "note": "2h30 through the Japan Alps' foothills"},
               {"name": "Meiji Jingu autumn festival", "price": "free", "note": "Tue 3 Nov: yabusame, martial arts, noh"}],
 "pros": ["Two very different cities, only one long train ride", "Kanazawa's food and gardens", "Her last day in Tokyo is slow, with an easy airport", "Your solo days stay in Tokyo"],
 "cons": ["An early flight (09:30) on Saturday", "Flight out is €89 dearer than Tokyo's", "Only two days in Kanazawa", "The shinkansen adds about €80 each"],
 "calm": "Kanazawa's garden at opening time and the teahouse streets at dusk, then the slow Tokyo days of the other plans.",
 "scores": {"hike": 2.5, "nature": 3, "food": 5, "culture": 5, "chill": 4}, "value": 2.5, "ease": 4.5,
 "plans": [
  {"style": "Chill", "name": "Two nights in Kanazawa, two in Tokyo; Tokyo day trips on your own", "chill": 75,
   "route": ["Together: 2n Kanazawa, shinkansen Monday, 2n Tokyo", "Wed: slow day in Tokyo, she flies from Narita 19:00", "You: 3n Tokyo (Mt Takao, Kamakura)", "Sat: Narita 17:20"],
   "nights": [KZ_HOTEL, N("Kanazawa", 75), TOKYO_HOTEL, TOKYO_HOTEL, TOKYO_HOSTEL, TOKYO_HOSTEL, TOKYO_HOSTEL],
   "transport_pp": 108, "shared": 0, "activities_pp": 35, "solo_transport": 45, "solo_activities": 15,
   "days": [
    KZ_DAY1,
    KZ_DAY2,
    D("Shinkansen to Tokyo, Asakusa", "Travel", "both", "Omicho for breakfast, then the Hokuriku shinkansen around 10:30 (2h30, ekiben on board).",
      "Ueno at 13:00, drop the bags; Senso-ji and Nakamise, the Sumida river.", "Hoppy street izakaya in Asakusa.", "Tokyo hotel (Ueno/Asakusa)", "Tokyo",
      [["train", "Kanazawa → Ueno (shinkansen)", 150], ["metro", "Ueno ↔ Asakusa", 20]],
      "Showers possible: a train day is the right use of it; Senso-ji's halls are covered."),
    D("Meiji Jingu's festival", "Easy", "both", "Meiji Jingu's autumn festival (1–3 Nov): martial-arts displays, noh and gagaku, chrysanthemums along the approach, horseback archery (yabusame).",
      "Harajuku's back streets, then Shibuya or Shimokitazawa.", "Omoide Yokocho's yakitori alleys in Shinjuku.", "Tokyo hotel (Ueno/Asakusa)", "Tokyo",
      [["metro", "around Tokyo", 50]], "Showers possible (30–40%): the Tokyo National Museum in Ueno is open on the holiday."),
    DAY_WED,
   ] + SOLO_TOKYO},
 ]},
]
