# Tokyo + one smaller town (29 Oct): the same Tokyo days for all three, then Kawaguchiko, Hakone or Nikko.
# Shape: Sat night Tokyo -> Sun to the town (dry day) -> Mon in the town (40% showers) -> Tue back to Tokyo before the
# holiday traffic -> Wed a slow last day in Tokyo, she leaves Ueno ~16:30 for Narita 19:00. Thu–Fri you alone, Sat home.
# One chill plan per town (29 Oct: the Fuller plans were removed at your request): gentle days, your solo days based in Tokyo.
from trips import D, N, S, HK_DEP

TOKYO_HOTEL = N("Tokyo (Ueno/Asakusa) hotel double", 85)
TOKYO_HOSTEL = S("Tokyo hostel or capsule (Asakusa)", 35)

DAY1 = D("Fly to Tokyo", "Travel", "both", "Morning with the family; Airport Express from Central around 12:30.", "14:55 HK Express to Narita, land 20:00.",
         "Skyliner to Ueno (41 min), late ramen near the hotel. Leave the big bags here for Tuesday: most hotels keep them.", "Tokyo hotel (Ueno/Asakusa)", "Tokyo",
         [HK_DEP, ["plane", "HKG → NRT", 245], ["train", "Narita → Ueno (Skyliner)", 45]])


def day_tue(town, leg, eve="Omoide Yokocho's yakitori alleys under the Shinjuku tracks."):
    return D("Back to Tokyo; Meiji Jingu's festival", "Easy", "both",
             f"Leave {town} by 09:30, before the holiday traffic home.",
             "Meiji Jingu's autumn festival (1–3 Nov): on Culture Day there are martial-arts displays, noh and gagaku on the stage, chrysanthemums along the approach, and horseback archery (yabusame). Then Harajuku's back streets.",
             eve, "Tokyo hotel (Ueno/Asakusa)", "Tokyo", leg + [["metro", "around Tokyo", 30]],
             "Showers are unlikely (30%). If it rains, the Tokyo National Museum in Ueno is open on the holiday.")


DAY_WED = D("A slow last day in Tokyo; she flies at 19:00", "Easy", "split",
            "Yanaka at 9: temples, cats and the old shopping street; down through Ueno park, the Tokyo National Museum if you like (open Wed).",
            "Ameyoko for lunch, then Kappabashi kitchen street. She takes the Skyliner from Ueno ~16:30 for HK Express 19:00 (lands HK 23:25).",
            "You: check in to a hostel in Asakusa; the Sumida river at night.", "You: Tokyo hostel", "Tokyo",
            [["metro", "Ueno ↔ Asakusa", 20]])

SOLO_TOKYO = [
    D("Mt Takao", "Active", "you", "Keio line from Shinjuku to Takaosanguchi (50 min), trail 6 up past the waterfall.", "Along the ridge to Shiroyama for a view of Fuji, down trail 1 via Yakuoin.", "Shimokitazawa's bars.", "Tokyo hostel", "Tokyo",
      [["train", "Tokyo ↔ Takaosanguchi", 110]]),
    D("Kamakura", "Easy", "you", "JR to Kita-Kamakura (1h): Engaku-ji and Kencho-ji.", "Daibutsu hiking course to the Great Buddha, then the beach at Yuigahama.", "Back to Tokyo.", "Tokyo hostel", "Tokyo",
      [["train", "Tokyo ↔ Kamakura", 130]]),
    D("Fly home", "Travel", "you", "Tsukiji outer market breakfast.", "Skyliner to Narita around 14:30.", "Etihad 17:20 to Brussels, land Sun 06:30; train to Lille about 1h30.", "On the plane", "Tokyo",
      [["train", "Ueno → Narita (Skyliner)", 45]]),
]

TRIPS_TOKYO = [
# ---------------------------------------------------------------- Tokyo + Kawaguchiko
{
 "id": "jp-fuji", "group": "tokyo", "town": "Kawaguchiko", "country": "Japan", "region": "Tokyo + Lake Kawaguchi (Mount Fuji)", "cc": "JP", "short": "Tokyo + Kawaguchiko",
 "title": "Tokyo + Kawaguchiko: Mount Fuji across the lake",
 "tagline": "Two nights by Lake Kawaguchi facing Mount Fuji: an e-bike ride along the shore, a kimono museum, an onsen; old Tokyo either side.",
 "bike": "E-bikes along the lake to Oishi park (Sun)",
 "out": "tokyo", "her": "tokyo", "his": "tokyo", "climate_of": "jp-fuji",
 "food_day": 28, "solo_food": 25,
 "town_card": {"time": "Bus from Shinjuku 1h55", "best": "Mount Fuji views, an easy e-bike ride along the lake, an onsen", "crowds": "Busy Sun and Tue (holiday) at Chureito and Oishi park; mornings are calm", "rain": "The Kubota Itchiku kimono museum (open daily in Nov) and an onsen", "room": "Lake guesthouse, private room ~€75"},
 "transport": "Highway bus Shinjuku ↔ Kawaguchiko (book on highwaybus.com), the lake loop buses (2-day pass ¥2,000), Suica in Tokyo.",
 "crowds": "Sun 1 Nov and Tue 3 Nov (Culture Day) are busy at the lakes: Chureito is calm only at sunrise. The maple-corridor light-up only starts on 7 Nov.",
 "food": ["Hoto: thick miso noodles with pumpkin, the Fuji lakes dish", "Tokyo: ramen, izakaya under the Ueno tracks, Omoide Yokocho's yakitori", "Ameyoko street food", "Tsukiji outer market (your Saturday)"],
 "hikes": ["E-bike along the north shore to Oishi park (flat, 12 km return)", "Tenjoyama: up on foot (40 min) or by ropeway, for Fuji over the lake", "Chureito pagoda's 398 steps at sunrise (optional)", "Mt Takao from Tokyo (your Thursday)"],
 "culture": ["Senso-ji and old Asakusa at 8am", "Oishi park and the kochia bushes", "Kubota Itchiku kimono museum", "Meiji Jingu's autumn festival (3 Nov)"],
 "adventure": [{"name": "E-bikes along the lake", "price": "~¥3,000–4,000 a day each", "note": "Flat north shore to Oishi park; rentals near Kawaguchiko station (book, and check they open on Sundays)"},
               {"name": "Kubota Itchiku Art Museum", "price": "¥1,300", "note": "Landscape kimonos in a forest garden; open daily in Nov"},
               {"name": "Meiji Jingu autumn festival", "price": "free", "note": "Tue 3 Nov: yabusame, martial arts, noh"}],
 "pros": ["The Fuji view, the strongest single image of the three towns", "A flat e-bike ride along the lake on the dry Sunday", "Slow pace: two nights in one place", "Her language skills make the bus and menus easy"],
 "cons": ["Busiest of the three on the holiday", "Two bus rides of 2h (there and back); Fuji hides in cloud after midday", "Maple light-up starts only on 7 Nov", "Japan prices"],
 "calm": "Two nights at Lake Kawaguchi: an easy bike ride along the shore to Oishi park, the kimono museum, an onsen at night.",
 "scores": {"hike": 3.5, "nature": 5, "food": 4.5, "culture": 4, "chill": 4.5}, "value": 2.5, "ease": 4.5,
 "plans": [
  {"style": "Chill", "name": "Tokyo, two nights facing Fuji, Tokyo; Tokyo day trips on your own", "chill": 80,
   "route": ["Together: 1n Tokyo, 2n Kawaguchiko, 1n Tokyo", "Wed: slow day in Tokyo, she flies from Narita 19:00", "You: 3n Tokyo (Mt Takao, Kamakura)", "Sat: Narita 17:20"],
   "nights": [TOKYO_HOTEL, N("Kawaguchiko guesthouse, private room", 75), N("Kawaguchiko", 75), TOKYO_HOTEL, TOKYO_HOSTEL, TOKYO_HOSTEL, TOKYO_HOSTEL],
   "transport_pp": 70, "shared": 0, "activities_pp": 40, "solo_transport": 45, "solo_activities": 15,
   "days": [
    DAY1,
    D("Bus to Fuji, e-bikes round the lake", "Active", "both", "Senso-ji and Nakamise before the crowds; metro to Shinjuku, 10:00 bus to Kawaguchiko (1h55). Leave the bags at the guesthouse.",
      "Hoto lunch, then e-bikes from near the station (about ¥3,000–4,000 a day; book): over the bridge and along the flat north shore to Oishi park, where the kochia bushes turn red in early November and Fuji sits across the water (about 6 km each way, 2–3h with stops).",
      "Lakeside onsen, dinner in town.", "Kawaguchiko guesthouse", "Kawaguchiko",
      [["metro", "Asakusa → Shinjuku", 30], ["bus", "Shinjuku → Kawaguchiko", 115]],
      "Sunday is the dry day (20%), so the ride is today. If it does rain, swap it with Monday."),
    D("Kimono museum and an onsen", "Easy", "both", "A slow breakfast; the Tenjoyama ropeway next to the station if Fuji is out (5 min).", "Lake bus to the Kubota Itchiku kimono museum and its garden (open daily in Nov).", "Onsen, quiet dinner.", "Kawaguchiko guesthouse", "Kawaguchiko",
      [["cable", "Tenjoyama ropeway", 5], ["bus", "Lake bus to the museum and back", 40]], "Showers possible (40%): the museum is indoors; add the onsen."),
    day_tue("the lake", [["bus", "Kawaguchiko → Shinjuku", 120]]),
    DAY_WED,
   ] + SOLO_TOKYO},
 ]},
# ---------------------------------------------------------------- Tokyo + Hakone
{
 "id": "jp-hakone", "group": "tokyo", "town": "Hakone", "country": "Japan", "region": "Tokyo + Hakone", "cc": "JP", "short": "Tokyo + Hakone",
 "title": "Tokyo + Hakone: onsen, a crater valley and Lake Ashi",
 "tagline": "Two nights at a hot-spring inn in the hills: an open-air museum, the ropeway over steaming vents, gardens a short walk away.",
 "bike": None,
 "out": "tokyo", "her": "tokyo", "his": "tokyo", "climate_of": "jp-fuji",
 "food_day": 28, "solo_food": 25,
 "town_card": {"time": "Romancecar from Shinjuku 85 min", "best": "Onsen inns, a varied loop (train, cable car, ropeway, boat), art", "crowds": "Busy loop on Sun and the holiday; go early, ride it on Monday", "rain": "The Open-Air Museum, the Pola Museum, the inn's baths", "room": "Small onsen inn, private room with breakfast ~€120"},
 "transport": "Romancecar Shinjuku ↔ Hakone-Yumoto (book seats for Tue, the holiday), then the Hakone Freepass covers the Tozan train, cable car, ropeway, boat and buses.",
 "crowds": "Sun 1 Nov and Tue 3 Nov are busy on the loop; the ropeway queues at Sounzan from 10:00. Lake Ashi's colours peak in early November.",
 "food": ["Kaiseki or a set dinner at the inn", "Black eggs boiled in Owakudani's vents", "Soba in Hakone-Yumoto", "Tokyo: ramen, Ameyoko, Omoide Yokocho"],
 "hikes": ["Old Tokaido stone road: Hatajuku → Moto-Hakone (2h, under cedars)", "Sengokuhara's silver-grass fields (short, flat)", "Lake Ashi shore path to Hakone shrine", "Mt Takao from Tokyo (your Thursday)"],
 "culture": ["Hakone Open-Air Museum (sculpture park, Picasso pavilion)", "Hakone shrine's torii in the lake", "Senso-ji and old Asakusa", "Meiji Jingu's autumn festival (3 Nov)"],
 "adventure": [{"name": "Onsen inn", "price": "~¥21,000 a night for two with breakfast", "note": "Private room, the inn's baths morning and night"},
               {"name": "Hakone Freepass (2 days, from Shinjuku)", "price": "¥6,100 each", "note": "Every train, cable car, ropeway, boat and bus in Hakone"},
               {"name": "Hakone Open-Air Museum", "price": "¥2,000", "note": "Free footbath in the grounds"}],
 "pros": ["The easiest of the three: 85 min from Shinjuku", "The most onsen for the money", "Plenty to do whatever the weather", "Lake Ashi's colours peak in early November"],
 "cons": ["Fuji is only a glimpse (it shows from the ropeway and the lake on clear days)", "The loop is crowded at weekends and on holidays", "Owakudani closes in strong wind or high volcanic gas", "Inns are dearer than the lake guesthouses"],
 "calm": "Two nights in a small onsen inn: baths before breakfast, the sculpture park, Gora's gardens. Nothing to rush for, and too hilly for an easy bike ride.",
 "scores": {"hike": 3.5, "nature": 4.5, "food": 4.5, "culture": 4.5, "chill": 5}, "value": 2.5, "ease": 5,
 "plans": [
  {"style": "Chill", "name": "Tokyo, two onsen nights in Hakone, Tokyo; Tokyo day trips on your own", "chill": 85,
   "route": ["Together: 1n Tokyo, 2n Hakone onsen inn, 1n Tokyo", "Wed: slow day in Tokyo, she flies from Narita 19:00", "You: 3n Tokyo (Mt Takao, Kamakura)", "Sat: Narita 17:20"],
   "nights": [TOKYO_HOTEL, N("Hakone onsen inn, private room, breakfast", 120), N("Hakone onsen inn", 120), TOKYO_HOTEL, TOKYO_HOSTEL, TOKYO_HOSTEL, TOKYO_HOSTEL],
   "transport_pp": 85, "shared": 0, "activities_pp": 30, "solo_transport": 45, "solo_activities": 15,
   "days": [
    DAY1,
    D("Senso-ji at 8, Romancecar to Hakone", "Travel", "both", "Senso-ji before the crowds; metro to Shinjuku, Romancecar to Hakone-Yumoto (85 min).", "Tozan train up the switchbacks to Gora; the Hakone Open-Air Museum and its footbath.", "Inn dinner and the baths.", "Hakone onsen inn", "Hakone",
      [["metro", "Asakusa → Shinjuku", 30], ["train", "Shinjuku → Hakone-Yumoto (Romancecar)", 85], ["train", "Tozan train to Gora", 40]]),
    D("Owakudani and Gora, close to the inn", "Easy", "both", "Cable car and ropeway up to Owakudani's steaming vents (black eggs at the top), then straight back down.",
      "Gora park and the Hakone Museum of Art's moss garden, both a short walk from the cable car; a long soak at the inn.",
      "Inn dinner and the baths.", "Hakone onsen inn", "Hakone",
      [["cable", "Gora → Owakudani and back", 50]], "Showers possible (40%): if the ropeway stops, the Pola Museum (bus 15 min) or the inn's baths. Lake Ashi by boat is the optional extra if the sky is clear (+75 min)."),
    day_tue("Hakone", [["train", "Hakone-Yumoto → Shinjuku (Romancecar)", 85]]),
    DAY_WED,
   ] + SOLO_TOKYO},
 ]},
# ---------------------------------------------------------------- Tokyo + Nikko
{
 "id": "jp-nikko", "group": "tokyo", "town": "Nikko", "country": "Japan", "region": "Tokyo + Nikko", "cc": "JP", "short": "Tokyo + Nikko",
 "title": "Tokyo + Nikko: gold-leaf shrines and a mountain lake",
 "bike": None,
 "tagline": "Two nights in Nikko, all on foot: the most ornate shrines in Japan in a cedar forest, a riverside path of stone Jizo, autumn colour.",
 "out": "tokyo", "her": "tokyo", "his": "tokyo", "climate_of": "jp-fuji",
 "food_day": 28, "solo_food": 25,
 "town_card": {"time": "Tobu Limited Express from Asakusa 1h50", "best": "Shrines and temples, autumn colour at its peak, waterfalls", "crowds": "Shrines busy from 10:00; Iroha-zaka road jams on Sun and the holiday", "rain": "Shrine halls are covered; Rinnoji's treasure house; a town onsen", "room": "Guesthouse near the shrines, private room ~€62"},
 "transport": "Tobu Limited Express from Asakusa, two minutes from the Tokyo hotel. Nikko's buses with the Tobu Nikko pass. Suica works on both.",
 "crowds": "The shrines are calmest at 8–9am and after 15:00. Iroha-zaka (the optional lake trip) was at peak colour on 26 Oct and jams on weekends and holidays.",
 "food": ["Yuba (tofu skin) in every form: Nikko's dish", "Trout from Lake Chuzenji", "Tokyo: ramen, Ameyoko, Omoide Yokocho", "Ekiben on the Tobu train"],
 "hikes": ["Senjogahara boardwalk (3h, flat): swap it in for the lake shore on Monday if you like", "Lake Chuzenji shore to the old embassy villas", "Kanmangafuchi's riverside path", "Mt Takao from Tokyo (your Thursday)"],
 "culture": ["Nikko Toshogu: carved gates, the three monkeys, the sleeping cat", "Taiyuin and Futarasan", "Kanmangafuchi's row of stone Jizo", "Meiji Jingu's autumn festival (3 Nov)"],
 "adventure": [{"name": "Toshogu at 9:00", "price": "¥1,600", "note": "Before the tour buses"},
               {"name": "Kegon falls elevator", "price": "¥570", "note": "To a platform at the base of the 97 m fall"},
               {"name": "Iroha-zaka in colour", "price": "bus pass", "note": "Peak colour on 26 Oct (Weathernews); leaves start falling around 11 Nov"}],
 "pros": ["Best culture of the three", "Autumn colour at its peak right now", "The train leaves from Asakusa, next to the hotel", "Cheapest rooms of the three"],
 "cons": ["Shrines crowded on Sunday afternoon", "The Akechidaira ropeway is closed until Aug 2027", "Colder: 5–15°C at the lake", "Fewer evening options than Hakone"],
 "calm": "Nikko after 16:00, when the day-trippers leave: the cedar avenue, the Jizo by the river at dusk, a quiet guesthouse.",
 "scores": {"hike": 3.5, "nature": 4.5, "food": 4, "culture": 5, "chill": 4.5}, "value": 3, "ease": 4.5,
 "plans": [
  {"style": "Chill", "name": "Tokyo, two nights in Nikko, Tokyo; Tokyo day trips on your own", "chill": 80,
   "route": ["Together: 1n Tokyo, 2n Nikko, 1n Tokyo", "Wed: slow day in Tokyo, she flies from Narita 19:00", "You: 3n Tokyo (Mt Takao, Kamakura)", "Sat: Narita 17:20"],
   "nights": [TOKYO_HOTEL, N("Nikko guesthouse, private room", 62), N("Nikko", 62), TOKYO_HOTEL, TOKYO_HOSTEL, TOKYO_HOSTEL, TOKYO_HOSTEL],
   "transport_pp": 70, "shared": 0, "activities_pp": 25, "solo_transport": 45, "solo_activities": 15,
   "days": [
    DAY1,
    D("Senso-ji at 8, Tobu to Nikko", "Travel", "both", "Senso-ji before the crowds; Tobu Limited Express from Asakusa at about 9:00 (1h50); bus to the guesthouse near the shrines (5 min).", "Kanmangafuchi's Jizo by the river and the Shinkyo bridge, on foot; the shrines after 15:00 when the crowds thin.", "Yuba dinner in town.", "Nikko guesthouse", "Nikko",
      [["train", "Asakusa → Tobu-Nikko", 110], ["bus", "station → shrines", 5]]),
    D("Toshogu and the temples, on foot", "Easy", "both", "Toshogu at 9:00 opening, then Taiyuin and Futarasan, all within a 10-minute walk.", "Rinnoji's treasure house and garden, a café on the old cedar avenue.", "Town onsen.", "Nikko guesthouse", "Nikko",
      [], "Showers possible (40%): the shrine halls are covered. If the sky is clear, the bus up Iroha-zaka to Lake Chuzenji and Kegon falls is the optional extra (+100 min, peak colour)."),
    day_tue("Nikko", [["train", "Tobu-Nikko → Asakusa", 110]], eve="Asakusa's Hoppy street izakaya."),
    DAY_WED,
   ] + SOLO_TOKYO},
 ]},
]
