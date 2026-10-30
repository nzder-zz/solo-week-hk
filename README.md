# Solo Week from Hong Kong

Ten ways to spend a solo week after Hong Kong (Sat 31 Oct → Sat 7 Nov 2026): flights, all-in costs, the weather forecast and three day-by-day plans for each trip.

**It works offline.** Open the page once while online. A service worker then keeps a full copy (page, fonts, icons), so it opens later with no connection, on a plane for example. The footer says "Saved for offline use" when the copy is ready.

- **iPhone (Safari):** Share → Add to Home Screen. It opens like an app.
- **Android (Chrome):** menu → Install app, or Add to Home screen.
- **Desktop (Chrome/Edge):** the install icon in the address bar.

When you're online, the page loads the latest version and updates the saved copy.

## Files
- `index.html`: the whole page (data, styles and script inline).
- `sw.js`: the service worker that caches everything for offline use.
- `manifest.webmanifest` and `icons/`: install as an app.
- `fonts/`: Big Shoulders Display, Instrument Sans and IBM Plex Mono (SIL Open Font License, licences included), served locally so nothing loads from elsewhere.

Prices and the forecast were checked on 22–23 Oct 2026. Nothing is booked.

## Week for two
A separate version for the two of you (together 31 Oct → 4 Nov, then solo until 7 Nov) lives in [`duo/`](duo/), built from `duo-src/`. It works offline the same way. This solo page is unchanged.

## Tokyo + Kawaguchiko (chosen trip)
The day-by-day plan for the trip you picked lives in [`fuji/`](fuji/), built from `fuji-src/` (see its README to change a day). It has its own offline copy.
