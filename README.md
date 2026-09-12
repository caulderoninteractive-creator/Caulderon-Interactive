# Caulderon Interactive — website (v3)

The studio homepage plus a dedicated overview + legal suite for every title:
Number Run: Pro Edition, Tilt Maze, Block Chakra, MeritNiti: Exam Practice,
and Ashen Crown: Oath of Greyfen. One shared stylesheet (`site.css`) and
script (`script.js`) drive the whole site.

## What changed in this revision

- **Fixed a real bug, not just styling.** The previous version used a
  scroll-triggered "fade content in as you scroll" effect. It relied on
  JavaScript adding a class as each section entered the viewport — and
  until that fired, the content sat at `opacity:0` while still taking up
  its full layout space. On first load (or in any screenshot/quick glance
  before scrolling), that showed up as large blank gaps with nothing in
  them, exactly the "broken, too much empty space" look you saw. That
  mechanism has been removed entirely. Every page now renders fully
  visible immediately, with no JavaScript dependency for content to
  simply *appear*.
- Tightened vertical spacing (`.section` padding 96px → 76px, hero padding
  reduced) so pages feel denser rather than airy-to-the-point-of-empty.
- **NetPrepQuiz renamed to MeritNiti: Exam Practice** — all files, links,
  colors, and copy updated (`meritniti*.html`).
- **New title added: Ashen Crown: Oath of Greyfen**, a dark fantasy
  adventure, currently in development. Full overview + Privacy/Terms/
  Support/Copyright pages, legal structure based on the same pattern as
  Tilt Maze and Block Chakra (pre-launch, draft-labeled).
- Every "More from Caulderon Interactive" cross-promo grid, the homepage
  games grid, the About page's titles grid, and both multi-column footers
  now list all five titles.

## Before you upload this anywhere — three things to do first

1. **Replace the placeholder domain.** Every canonical link and Open Graph
   tag points to `https://caulderoninteractive.com/` as a placeholder.
   Once you own a real domain, find-and-replace
   `caulderoninteractive.com` across every `.html` file. Internal links
   between pages are all relative, so nothing else needs to change.

2. **Copy your real image assets across.** This bundle does not include
   binary image files. Copy these from your current repo into the same
   filenames/locations here:
   - `icon.png`, `favicon.png`, `favicon-32.png`, `apple-touch-icon.png` (site root)
   - `assets/google-play.png`, `assets/app-store.png` (store badges)

3. **Add a `CNAME` file** (custom domain on GitHub Pages only) once you
   know your domain, containing just the domain name, then point DNS at
   GitHub Pages per their custom-domain instructions.

## Structure

```
index.html                    Studio homepage (about/craft/all 5 titles)
about.html                    Full "About the studio" page
site.css                      Shared stylesheet for the entire site
script.js                     Shared JS: footer year, mobile nav toggle
404.html                      Custom not-found page
robots.txt, sitemap.xml       Crawler config
app-ads.txt                   AdMob publisher record — copied over unchanged

numberrun.html                Number Run: Pro Edition overview (live app)
privacy.html / terms.html /
support.html / copyright.html Number Run's legal + support pages

tiltmaze.html                 Tilt Maze overview (coming soon)
tiltmaze-privacy.html / -terms.html / -support.html / -copyright.html

blockchakra.html              Block Chakra overview (coming soon)
blockchakra-privacy.html / -terms.html / -support.html / -copyright.html

meritniti.html                 MeritNiti: Exam Practice overview (in development)
meritniti-privacy.html / -terms.html / -support.html / -copyright.html

ashencrown.html                Ashen Crown: Oath of Greyfen overview (in development)
ashencrown-privacy.html / -terms.html / -support.html / -copyright.html

devlog/                       Number Run's existing build-notes blog,
                               restyled to match, content unchanged
```

## Why Number Run's legal page URLs didn't change

Number Run: Pro Edition is already live on Google Play, and its Privacy
Policy URL is very likely already registered in Google Play Console (and
possibly referenced from in-app screens). To avoid breaking that link,
`privacy.html`, `terms.html`, `support.html`, and `copyright.html` kept
their existing root-level paths — only the visual design changed. You'll
still need to update the Privacy Policy URL field in Google Play Console
once you move to the new domain, regardless of file paths.

## About MeritNiti and Ashen Crown

Both are early — I only had a name and (for MeritNiti) a rough sense of
"exam practice" to go on, so:

- **MeritNiti: Exam Practice** is framed as a general competitive-exam
  practice app: timed sets, instant scoring, topic organization. No
  specific exam is named anywhere.
- **Ashen Crown: Oath of Greyfen** is framed as a dark fantasy
  adventure/RPG (exploration, tactical battles, a story built around an
  oath), since that's what the title evokes — but genre, mechanics, and
  currency name ("Sigils") are my best guess, clearly marked as drafts.

Both titles' Privacy Policy, Terms of Use, and Copyright pages are
explicitly labeled as drafts describing *planned* behavior (no accounts,
local-only storage, the same AdMob/Play Billing pattern as the shipped
titles), following the same structure as the existing apps' legal
documents. Once you can share real specifics — subject focus or genre
details, whether either will have accounts or a backend, monetization —
I can tighten the copy and finalize the legal pages accordingly.

## Design notes

- One token system in `site.css` drives color, spacing, and type across
  every page: Number Run (cyan), Tilt Maze (purple), Block Chakra (pink),
  MeritNiti (green/blue), Ashen Crown (ember/ash).
- Mobile navigation has a working hamburger menu.
- Structured data (JSON-LD) is included for the organization and for
  Number Run.
- Every legal document uses the same sidebar-table-of-contents layout.

## Contacts

- Business: caulderoninteractive@gmail.com
- Player support: support.caulderoninteractive@gmail.com
