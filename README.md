# Caulderon Interactive 
A full rebuild of the site as a studio-level presence: the homepage is now
about **Caulderon Interactive** the studio, and every title — Number Run:
Pro Edition, Tilt Maze, Block Chakra, and MeritNiti: Exam Practice — has its own overview
page plus dedicated Privacy, Terms, Support, and Copyright &amp; Licenses
pages. One shared stylesheet (`site.css`) and script (`script.js`) drive the
whole site.

## Before you upload this anywhere — three things to do first

1. **Replace the placeholder domain.** Every canonical link and Open Graph
   tag in this bundle points to `https://caulderoninteractive.com/` as a
   placeholder so you can see how the site will look once you own a real
   domain. Once you've actually registered one, find-and-replace
   `caulderoninteractive.com` across every `.html` file with your real
   domain. (Everything else — every internal link between pages — uses
   relative paths, so the rest of the site doesn't need any changes.)

2. **Copy your real image assets across.** This bundle does **not** include
   binary image files, since I don't have access to your existing artwork.
   Copy these from your current repo into the same filenames/locations here:
   - `icon.png`, `favicon.png`, `favicon-32.png`, `apple-touch-icon.png` (site root)
   - `assets/google-play.png`, `assets/app-store.png` (store badges)
   Every page already references these exact filenames, so once they're in
   place everything will render correctly.

3. **Decide on a CNAME file (custom domain only).** If you're hosting on
   GitHub Pages with a custom domain, add a file literally named `CNAME`
   (no extension) at the repo root containing just your domain, e.g.
   `caulderoninteractive.com`, then point your domain's DNS at GitHub Pages
   per GitHub's custom-domain instructions. This file isn't included here
   since it depends on the exact domain you end up buying.

## Structure

```
index.html                    Studio homepage (About/craft/all 4 titles)
about.html                    Full "About the studio" page
site.css                      Shared stylesheet for the entire site
script.js                     Shared JS: footer year, mobile nav, scroll-reveal
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

MeritNiti: Exam Practice.html              MeritNiti: Exam Practice overview (in development)
MeritNiti: Exam Practice-privacy.html / -terms.html / -support.html / -copyright.html

devlog/                       Number Run's existing build-notes blog,
                               restyled to match, content unchanged
```

## Why Number Run's legal page URLs didn't change

Number Run: Pro Edition is already live on Google Play, and its Privacy
Policy URL is very likely already registered in Google Play Console (and
possibly referenced from in-app screens). To avoid breaking that link, I
kept `privacy.html`, `terms.html`, `support.html`, and `copyright.html` at
the same root-level paths they already had — only the visual design changed,
not the URLs. Everything else (the new homepage, `about.html`, and the new
`numberrun.html` overview page) is new, so there was nothing to preserve
there.

If you do change domains, you'll still need to update the Privacy Policy
URL field in Google Play Console to point at the new domain — that's
unavoidable when moving off GitHub Pages regardless of file paths.

## About MeritNiti: Exam Practice

I didn't have details on this title beyond its name, so I've drafted it as
a general exam/certification-prep quiz app, in the same visual and
structural family as your other titles, clearly marked as "in development"
with draft legal pages (each one says so, the same way Block Chakra's
pre-launch pages already flagged an unfinished "Last updated" date). Once
you can share specifics — subject focus, whether it'll have accounts or a
backend, monetization plans — I can tighten the copy and finalize the
Privacy Policy and Terms accordingly.

## Design notes

- One token system in `site.css` drives color, spacing, and type across
  every page — extending the palette you already had (Number Run cyan,
  Tilt Maze purple, Block Chakra pink) with a new green/blue pairing for
  MeritNiti: Exam Practice.
- Mobile navigation now has a working hamburger menu (previously the nav
  links simply disappeared under ~760px with no alternative).
- Subtle scroll-reveal animations respect `prefers-reduced-motion` and
  degrade gracefully with JavaScript disabled.
- Structured data (JSON-LD) was added for the organization and for Number
  Run, for slightly better search-result presentation.
- Tilt Maze's pages (previously a one-off inline-styled design) and Number
  Run's legal pages (previously a separate older stylesheet) are now on the
  same shared design system as Block Chakra, with a consistent
  sidebar-table-of-contents layout for every legal document.

## Contacts

- Business: caulderoninteractive@gmail.com
- Player support: support.caulderoninteractive@gmail.com
