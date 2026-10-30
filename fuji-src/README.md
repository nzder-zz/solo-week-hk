# Tokyo + Kawaguchiko: build files

The chosen trip (31 Oct → 7 Nov 2026), published at `fuji/`. Works offline like the other two pages.

## Files
- `plan.py`: **everything on the page.** Days (each with a main version and swaps), forecast, places (Google Maps links), timetable/booking links, beds, ideas, to-do list.
- `template.html`: page style and script; the data is embedded as JSON and rendered in the browser.
- `sw.template.js`: offline worker (cache `fuji-trip-…`).
- `build.py`: checks every marker, then writes `fuji/index.html`, `fuji/sw.js`, `fuji/manifest.webmanifest`.

## Changing the plan
- Swap a day: change its entry in `CHOICE` (e.g. `"mon2": "heavy"`).
- Edit a step, drop an activity: edit that version's `steps`.
- New forecast: edit `FORECAST` and `FC_SUMMARY`.
- In text, `[[place_id]]` makes a map chip and `{{link_id}}` a timetable/booking chip.

```
python3 fuji-src/build.py
git add fuji fuji-src && git commit -m "…" && git push
```
Commit with 314790236+nzder-zz@users.noreply.github.com.

On the page, tapping another version of a day swaps it on that phone only (stored in the browser); `CHOICE` is the shared plan.
