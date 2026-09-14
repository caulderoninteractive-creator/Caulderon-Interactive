MERITNITI GOVERNMENT JOBS — WEBSITE INTEGRATION

Files changed:
- meritniti.html: adds Government Jobs & Exam Updates section + nav link
- site.css: adds native dark-theme update cards matching MeritNiti
- script.js: reads /meritniti/jobs/feed.json and renders verified updates safely
- robots.txt: adds the generated jobs sitemap
- meritniti-support.html: adds jobs-update support information
- meritniti-terms.html: adds recruitment/exam-update terms and official-source precedence
- meritniti-privacy.html: adds static website/update-page data-handling disclosure

UPLOAD / REPLACE THESE FILES IN THE SAME WEBSITE ROOT USED BY CLOUDFLARE.

Then use MeritNiti GovJobs v3.2 scanner with:
GOVJOB_PUBLIC_BASE_URL=https://caulderoninteractive.com/meritniti/jobs
GOVJOB_SITE_ROOT_DIR=<the folder containing meritniti.html and site.css>

Run run_scan_once.bat once. It will create:
  meritniti/jobs/index.html
  meritniti/jobs/feed.json
  meritniti/jobs/sitemap.xml
  meritniti/jobs/<exam-slug>/index.html

Deploy the whole site root to Cloudflare.

Test:
https://caulderoninteractive.com/meritniti.html#govt-jobs
https://caulderoninteractive.com/meritniti/jobs/
https://caulderoninteractive.com/meritniti/jobs/feed.json

The main MeritNiti page fails closed: if feed.json is missing or invalid, it shows an unavailable message instead of inventing or displaying stale unverified data.

Future meritniti.com migration:
The JavaScript automatically changes the feed/index path from /meritniti/jobs/ to /jobs/ whenever the hostname is meritniti.com (or a subdomain of it).
