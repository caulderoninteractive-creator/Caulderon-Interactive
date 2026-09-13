# Caulderon Interactive

The studio homepage plus a dedicated overview + legal suite for every title:
Number Run: Pro Edition, Tilt Maze, Block Chakra, MeritNiti: Exam Practice,
Ashen Crown: Oath of Greyfen, and Untold Realms. One shared stylesheet (`site.css`) and
script (`script.js`) drive the whole site.

## What changed in this revision

- **Domain finalized.** Every canonical link, Open Graph tag, and email
  address now points at the real `caulderoninteractive.com` — nothing left
  to find-and-replace.
- **Contact addresses split three ways** — `support@`, `business@`, and
  `admin@` — routed by purpose across every page. See "Contact addresses"
  below for exactly what goes where.
- Added `.well-known/security.txt` pointing security researchers at
  `admin@caulderoninteractive.com`.

### Carried over from the previous revision

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
- Real icons swapped in for Tilt Maze, Block Chakra, and MeritNiti.
- MeritNiti's content rewritten from the real product description you
  provided (diagnostic feedback, misconception tags, Smart Revision, etc.).

## Before you upload this anywhere — two things to do first

1. **Copy your remaining image assets across.** Real icons for Tilt Maze,
   Block Chakra, and MeritNiti are now included in this bundle
   (`tiltmaze-icon.png`, `blockchakra-icon.png`, `meritniti-icon.png`) — you
   don't need to supply those. Still missing (I don't have the source art):
   - `icon.png`, `favicon.png`, `favicon-32.png`, `apple-touch-icon.png` (site root — Number Run/studio icon)
   - `assets/google-play.png`, `assets/app-store.png` (store badges)
   - Ashen Crown doesn't have real artwork yet, so it still uses a placeholder inline icon.

2. **Add a `CNAME` file** (custom domain on GitHub Pages only) containing
   just `caulderoninteractive.com`, then point DNS at GitHub Pages per
   their custom-domain instructions. If you're hosting elsewhere, this
   step doesn't apply.

Every canonical link, Open Graph tag, and email address across the site
now points at `caulderoninteractive.com` — no more placeholder domain.

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

## MeritNiti: Exam Practice — now built from the real product description

MeritNiti's overview page, and its Privacy/Terms/Copyright pages, have been
rewritten using the real product description you provided: answer-specific
(distractor-level) feedback, misconception tags, Smart Revision, growing
question-bank content packs, offline practice, bookmarking, and an
exam-booklet style interface. The "Independent preparation app" disclaimer
(no official affiliation with UPSC/SSC/NTA/RRB/IBPS/State PSCs/etc.) appears
on the overview page and as its own "No Official Affiliation" section in
the Terms of Use — reproduced closely since it's your own first-party
legal disclaimer, not third-party content.

Real icons are now used for Tilt Maze, Block Chakra, and MeritNiti
throughout the site (see "Real icons now included," below). Status was
upgraded from "In development" to "Coming soon" given how finished this
description reads — change it back on `meritniti.html` and its cross-promo
cards elsewhere if that's premature. The MeritNiti WhatsApp channel is
linked from its hero, its Support page, and the homepage/About footer.

## About Ashen Crown

Ashen Crown is early, so it's framed as a
dark fantasy adventure/RPG (exploration, tactical battles, a story built
around an oath), since that's what the name evokes, but genre, mechanics,
and the currency name ("Sigils") are my best guess, clearly marked as
drafts throughout its Privacy Policy, Terms of Use, and Copyright pages.

## About Untold Realms

As the name suggests, it's a text based RPG.

## Real icons now included

`tiltmaze-icon.png`, `blockchakra-icon.png`, and `meritniti-icon.png` are
your real uploaded artwork, now used as the actual `<img>` icon everywhere
those titles appear — their own hero banner, the homepage grid, and every
cross-promo card on other titles' pages. The inline SVG placeholders I'd
drawn for those three are gone. Ashen Crown still uses a placeholder inline
SVG (a simple crown mark) since no real art exists for it yet — swap it out
the same way once you have one.

## Design notes

- One token system in `site.css` drives color, spacing, and type across
  every page: Number Run (cyan), Tilt Maze (purple), Block Chakra (pink),
  MeritNiti (green/blue), Ashen Crown (ember/ash).
- Mobile navigation has a working hamburger menu.
- Structured data (JSON-LD) is included for the organization and for
  Number Run.
- Every legal document uses the same sidebar-table-of-contents layout.

## Contact addresses

The site now uses three separate `@caulderoninteractive.com` addresses,
routed by purpose:

- **support@caulderoninteractive.com** — player-facing: app support, bug
  reports, and the contact link on every Privacy Policy, Terms of Use, and
  Support page.
- **business@caulderoninteractive.com** — partnerships, licensing, and
  commercial/press enquiries: the "Business enquiries" links on the
  homepage/About/footer, and every Copyright & Licenses page's licensing
  contact (since that's fundamentally a licensing question).
- **admin@caulderoninteractive.com** — account administration, platform
  ownership, security, and registrar/hosting matters. This one isn't
  surfaced anywhere in the page content (it's not something a player or
  press contact would need), but it is wired up as the contact in
  `.well-known/security.txt`, so security researchers who go looking for
  a disclosure contact will find it there.

Make sure all three addresses actually exist and are monitored before
this goes live — a `mailto:` link to a dead inbox is worse than no link.

