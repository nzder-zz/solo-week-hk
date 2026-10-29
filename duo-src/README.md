# Week for Two: build files

The duo version of the planner: together Sat 31 Oct → Wed 4 Nov 2026 (she flies back to HK that evening), then you alone until your flight home on Sat 7 Nov. Japan and Taiwan only. Published at `duo/` next to the solo page, which is untouched.

## Files
- `trips_tokyo.py`: Tokyo + one smaller town (Kawaguchiko, Hakone, Nikko) with one chill plan each (the Fuller plans were removed on 29 Oct), and the shared Tokyo days.
- `trips_kanazawa.py`: Kanazawa & around (bike-share day, Yamanaka ryokan; Shirakawa-go on your solo ride) and Kanazawa + Tokyo, one chill plan each.
- `trips.py`: the other trips (Kansai, Kyushu, Taiwan), one chill plan each: 4 nights together + 3 alone, room prices, transport, activities, day-by-day text.
- `fc_refresh.py`: the 29 Oct forecast refresh (JMA + CWA official weekly forecasts).
- `fares.py`: every flight and its status (`gf27` = live Google Flights fare of 27 Oct, `est` = estimate). **Refresh fares here.**
- `checks.py`: the verification log (Typhoon Champi damage, closures, volcano levels, prices still to check).
- `places_new.py`: place notes added for the duo trips; the rest come from `base_data.json`.
- `base_data.json`: forecast run (27 Oct), climate and place notes reused from the solo page.
- `build_data.py`: costs, shares, fit scores and forecast summaries.
- `build_xlsx.py`: Duo-Week-Planner.xlsx (inputs in blue, totals as formulas).
- `build_all.py`: writes `duo/index.html`, `duo/sw.js` and `duo/manifest.webmanifest`.
- `template/`: page style, markup and script.

## Update
```
python3 duo-src/build_all.py --xlsx Duo-Week-Planner.xlsx
git add duo duo-src && git commit -m "…" && git push
```
Commit with the no-reply email 314790236+nzder-zz@users.noreply.github.com.

## Offline
`duo/sw.js` caches the page, the shared fonts and icons under its own cache name (`duo-week-…`). The root worker skips `/duo/` requests, and the duo page repairs the solo page's cache if an older root worker stored the wrong page.
