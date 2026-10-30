// Offline support: every file is cached on first visit, then served from the cache.
// The cache name changes with the content, so a new version replaces the old one on the next online visit.
const CACHE = 'solo-week-1360b9a6ae';
const ASSETS = [
  "./",
  "index.html",
  "manifest.webmanifest",
  "icons/icon-192.png",
  "icons/icon-512.png",
  "icons/icon-maskable-512.png",
  "icons/apple-touch-icon.png",
  "icons/favicon-32.png",
  "fonts/big-shoulders-display-latin-ext-700-normal.woff2",
  "fonts/big-shoulders-display-latin-700-normal.woff2",
  "fonts/big-shoulders-display-latin-ext-800-normal.woff2",
  "fonts/big-shoulders-display-latin-800-normal.woff2",
  "fonts/instrument-sans-latin-ext-400-normal.woff2",
  "fonts/instrument-sans-latin-400-normal.woff2",
  "fonts/instrument-sans-latin-ext-500-normal.woff2",
  "fonts/instrument-sans-latin-500-normal.woff2",
  "fonts/instrument-sans-latin-ext-600-normal.woff2",
  "fonts/instrument-sans-latin-600-normal.woff2",
  "fonts/instrument-sans-latin-ext-700-normal.woff2",
  "fonts/instrument-sans-latin-700-normal.woff2",
  "fonts/ibm-plex-mono-latin-ext-400-normal.woff2",
  "fonts/ibm-plex-mono-latin-400-normal.woff2",
  "fonts/ibm-plex-mono-latin-ext-500-normal.woff2",
  "fonts/ibm-plex-mono-latin-500-normal.woff2"
];

self.addEventListener('install', event => {
  event.waitUntil(caches.open(CACHE).then(c => c.addAll(ASSETS)).then(() => self.skipWaiting()));
});

self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys()
      .then(keys => Promise.all(keys.filter(k => k.startsWith('solo-week-') && k !== CACHE).map(k => caches.delete(k))))
      .then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', event => {
  const req = event.request;
  if (req.method !== 'GET' || new URL(req.url).origin !== self.location.origin) return;
  const url = new URL(req.url);
  // The duo page (duo/) and the trip page (fuji/) have their own workers and caches: leave their requests alone.
  if (url.pathname.includes('/duo/') || url.pathname.includes('/fuji/')) return;
  const isPage = req.mode === 'navigate' || url.pathname.endsWith('/') || url.pathname.endsWith('index.html');
  event.respondWith(caches.open(CACHE).then(cache => {
    const fresh = fetch(req).then(res => {
      if (res && res.ok) cache.put(isPage ? 'index.html' : req, res.clone());
      return res;
    });
    if (isPage) {
      // The page: try the network first so updates show at once; fall back to the saved copy
      // straight away when offline, or after 3 s on a weak connection.
      const timeout = new Promise(resolve => setTimeout(resolve, 3000, null));
      return Promise.race([fresh.catch(() => null), timeout]).then(res =>
        (res && res.ok) ? res : cache.match('index.html').then(hit => hit || fresh));
    }
    // Fonts and icons: the saved copy first, refreshed in the background.
    return cache.match(req, { ignoreSearch: true }).then(hit => {
      if (hit) { event.waitUntil(fresh.catch(() => null)); return hit; }
      return fresh;
    });
  }));
});
