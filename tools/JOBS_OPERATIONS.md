# MeritNiti jobs operations

`python tools/refresh_jobs.py` validates `tools/verified_jobs.json`, rebuilds the board and feed, updates the WhatsApp snippets on detail pages, and archives pages absent from the curated set. `--discover` also scans the five configured official websites for candidate links and writes `tools/discovery_report.json`. A GitHub Actions schedule runs daily at 07:50 IST when the repository and workflow are enabled with write permissions.

## Publication rule

Only entries in `verified_jobs.json` publish. Each needs a unique recruitment identifier, official HTTPS notice on an allowlisted host, title, organisation, eligibility, application method, deadline, and a verification date. A link found by the scanner is **only a lead**. A human must read the specific notification and any corrigendum, record exact particulars, create or update its detail page, and add the structured entry before it can publish. This avoids presenting a careers hub, a result notice, or unrelated text from a listing page as an open job.

The initial curated set reflects the two distinct notices in the supplied archive. Its verification dates describe the archive's prior editorial review, not a fresh online verification by this change. Check them again before relying on the dates. Source sites may block automated requests; failures are recorded and do not erase existing published entries.

## Coverage and automation limits

No finite crawler can guarantee **all** jobs in India, and a source listing cannot safely provide every post-specific qualification, fee, vacancy, deadline extension, and application route. The current scanner covers five configured organisations and does not automatically promote its discoveries. Expanding coverage requires a maintained register of official sources across central, state, district, PSU, university, and other recruiters, with source-specific extractors and ongoing editorial checks. Never describe the current board as exhaustive or automatically authenticated in marketing copy.

The scheduled job commits to the checked-out branch; GitHub Pages publication depends on repository settings. No WhatsApp channel post is sent automatically. The generated short message can be copied from each detail page or shared with its WhatsApp link; channel posting requires a supported channel publishing integration and authorization.
