# Caulderon Interactive website

Static production site for `caulderoninteractive.com`, built for GitHub Pages or
any conventional static host. `site.css` and `script.js` provide the shared studio
presentation; MeritNiti's generated jobs board lives under `meritniti/jobs/`.

## Current title pages

| Title | Status on site | Overview and documents |
| --- | --- | --- |
| Number Run: Pro Edition | Google Play | `numberrun.html`; root `privacy.html`, `terms.html`, `support.html`, `copyright.html` |
| Eltru's Way Home | Google Play | `eltru.html` and `eltru-*` documents |
| Lumen | Google Play release page prepared | `lumen.html` and `lumen-*` documents |
| Block Chakra | Coming soon | `blockchakra.html` and `blockchakra-*` documents |
| MeritNiti: Exam Practice | Google Play | `meritniti.html`, `meritniti-*` documents and `meritniti/jobs/` |
| Ashen Crown: Oath of Greyfen | In development | `ashencrown.html` and `ashencrown-*` documents |
| Untold Realms | Google Play release page prepared | `untoldrealms.html` and `untoldrealms-*` documents |

The old `tiltmaze*.html` paths remain as no-index redirect pages so existing store,
support and policy links continue to reach the renamed Eltru pages.

## Important assets

- `eltru-icon-512.png` and `eltru-screenshot-*.png` — current Google Play artwork.
- `lumen-icon.svg` and `lumen-icon-512.png` — Lumen web/store presentation icon.
- `assets/google-play.png` — shared official-format store badge.
- `site.css` — shared responsive design and per-title colour system.
- `sitemap.xml`, `robots.txt`, `CNAME`, `.well-known/security.txt` — deployment metadata.

## MeritNiti government-jobs integration

The sibling `GovtJobsengine` project generates the entire `meritniti/jobs/` subtree,
including `index.html`, detail routes, `feed.json`, `sitemap.xml`, and the owned
`assets/jobs.css` / `assets/jobs.js`. The main `meritniti.html` page reads
`meritniti/jobs/feed.json` through `meritniti/home.js`.

Do not hand-edit generated job pages. Improve the renderer or verification logic in
`GovtJobsengine`, run its tests, and rebuild instead. Job summaries are independent
convenience material; recruiting authorities' current official notices always control.

## Deployment

1. Copy the website folder to the repository root without changing relative paths.
2. Keep `CNAME` as `caulderoninteractive.com` when deploying through GitHub Pages.
3. Confirm `support@`, `business@`, and `admin@caulderoninteractive.com` are routed.
4. Run the local link checker and preview desktop and mobile layouts.
5. Commit and push; GitHub Pages/Cloudflare will serve the new static files after deployment.

No private keys, Android signing material, API credentials, build caches, or local
virtual environments belong in the published website repository.
