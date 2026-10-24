// Offline support: every file is cached on first visit, then served from the cache.
// The cache name changes with the content, so a new version replaces the old one on the next online visit.
const CACHE = 'solo-week-e36a327007';
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
  // Cache first (works on a plane), refresh the copy in the background when online.
  event.respondWith(
    caches.open(CACHE).then(cache =>
      cache.match(req, { ignoreSearch: true }).then(hit => {
        const net = fetch(req).then(res => {
          if (res && res.ok) cache.put(req, res.clone());
          return res;
        }).catch(() => null);
        if (hit) { event.waitUntil(net); return hit; }
        return net.then(res => res || (req.mode === 'navigate' ? cache.match('index.html') : Response.error()));
      })
    )
  );
});
