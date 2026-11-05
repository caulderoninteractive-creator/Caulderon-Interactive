# MeritNiti jobs operations

## One publication path

The local `GovtJobsEngine` discovers sources, extracts official notices, keeps reviews in its SQLite database, builds `meritniti/jobs/`, and creates WhatsApp copy. The daily GitHub Action now writes only `tools/discovery_report.json`; it never replaces the reviewed website feed or pages with its small curated list. The report is a lead list, not a publication queue. The website changes when Studio builds and you push its generated jobs subtree (or enable the existing optional post-scan Git setting).

Start `START_MERITNITI.bat`; use Sources & health to add an official careers or recruitment URL, then select and scan it. Scans also visit up to five promising first-party careers, opportunities, vacancies and recruitment sections per source. For a missing job, use Jobs & review → Import a specific notice with its official PDF/detail URL. Review the evidence and correct post-wise facts before approving. Build and preview; push only `meritniti/jobs/`. Confirm the public page is live, then copy its WhatsApp message and post it to your channel. The queue records when you mark it sent; WhatsApp Channel posting itself is manual.

OCR uses local Tesseract when available. Install Tesseract plus language packs for scanned notices, then check Sources & health diagnostics. Native PDF text remains available without it. Ambiguous dates, qualifications, fees and amendments need review against the specific official advertisement. A listing page or search result alone cannot establish an open application window. Follow-up events reach an exam page only when the engine can match its tracked recruitment cycle and verify an official source.

The archive contains `GovtJobsEngine/settings.env` and `data/` from the original package. Preserve your newer local settings and database when applying an update. Neither belongs in a public static GitHub Pages repository. Never push `.venv`, database backups, or local logs. Public GitHub Actions has no access to the local Studio database, so it cannot independently publish its newly reviewed entries.

The standalone `python tools/refresh_jobs.py` command still refreshes the separately maintained `verified_jobs.json` board for older workflows. Do not run it on top of a Studio-generated board: it only knows its curated entries. Use `--discover-only` for a safe lead report.
