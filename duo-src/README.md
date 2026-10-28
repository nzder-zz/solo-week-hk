# Week for Two: build files

The duo version of the planner (both of you, 31 Oct → 6 Nov 2026). Published at `duo/` next to the solo page, which is untouched.

## Files
- `trips.py`: the 7 trips × 2 plans (Slow, Fuller): nights and room prices, transport, activities, day-by-day text.
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
