"""Validate published notices, rebuild the public feed/board, and discover leads.

Run from the repository root: python tools/refresh_jobs.py [--discover].
Discovery is deliberately separate from publication: a link on an official
website does not establish eligibility, dates, or an open application window.
"""
import argparse
import datetime as dt
import html
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import sys
from urllib.parse import urljoin, urlparse
from urllib.parse import quote
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
JOBS = ROOT / "meritniti/jobs"
SOURCE = ROOT / "tools/verified_jobs.json"
HOST = "https://caulderoninteractive.com"
IST = dt.timezone(dt.timedelta(hours=5, minutes=30))
SOURCES = {
    "UPSC": "https://upsc.gov.in/recruitment/recruitment-advertisements",
    "SSC": "https://ssc.gov.in/",
    "IBPS": "https://www.ibps.in/",
    "DRDO": "https://drdo.gov.in/drdo/en/offerings/vacancies",
    "WAPCOS": "https://www.wapcos.co.in/careers",
    "India Post": "https://www.indiapost.gov.in/vacancies",
    "SBI": "https://sbi.co.in/web/careers/current-openings",
    "RBI": "https://opportunities.rbi.org.in/Scripts/Vacancies.aspx",
    "ISRO": "https://www.isro.gov.in/CurrentOpportunities.html",
    "KVS": "https://kvsangathan.nic.in/en/recruitment/",
    "ICMR": "https://www.icmr.gov.in/employment-opportunities",
    "RRB Chandigarh": "https://www.rrbcdg.gov.in/",
    "DSSSB": "https://dsssb.delhi.gov.in/vacancies",
    "Bihar PSC": "https://bpsc.bihar.gov.in/",
    "UPPSC": "https://uppsc.up.nic.in/",
    "TNPSC": "https://www.tnpsc.gov.in/",
}


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.hrefs = []

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            href = dict(attrs).get("href")
            if href:
                self.hrefs.append(href)


def discover():
    """Visit high-value official indexes and a few first-party careers pages."""
    leads, failures = [], []
    for name, source in SOURCES.items():
        origin = urlparse(source).hostname
        frontier, seen = [source], set()
        while frontier and len(seen) < 4:
            page = frontier.pop(0)
            if page in seen:
                continue
            seen.add(page)
            try:
                req = Request(page, headers={"User-Agent": "MeritNitiBot/1.0 (+https://caulderoninteractive.com/meritniti-support.html)"})
                with urlopen(req, timeout=12) as response:
                    if urlparse(response.url).hostname != origin:
                        raise ValueError("source redirected off its official host")
                    data = response.read(1_500_001)
                    if len(data) > 1_500_000:
                        raise ValueError("page exceeds size limit")
                    body = data.decode("utf-8", "replace")
                parser = Links()
                parser.feed(body)
                for href in parser.hrefs:
                    url = urljoin(page, href).split("#")[0]
                    parsed = urlparse(url)
                    if parsed.scheme != "https" or parsed.hostname != origin:
                        continue
                    path = parsed.path.lower()
                    if re.search(r"archive|tender|result|answer.key|login", path):
                        continue
                    if re.search(r"recruit|vacanc|career|opportunit|employment|advert|notice|opening|\.pdf", path):
                        leads.append({"source": name, "url": url})
                        if page == source and not path.endswith(".pdf") and url not in seen and len(frontier) < 3:
                            frontier.append(url)
            except Exception as exc:
                failures.append({"source": name, "page": page, "error": str(exc)[:180]})
    unique = sorted({(x["source"], x["url"]) for x in leads})
    report = {"checked_at": dt.datetime.now(IST).isoformat(),
              "leads": [{"source": name, "url": url} for name, url in unique],
              "failures": failures}
    (ROOT / "tools/discovery_report.json").write_text(json.dumps(report, indent=2) + "\n")
    print(f"Discovered {len(unique)} official-host links; {len(failures)} pages failed. Leads are not published.")


def validate(rows):
    seen, notices = set(), set()
    for row in rows:
        key = row["exam_key"]
        if key in seen or not re.fullmatch(r"[a-z0-9-]+", key):
            raise ValueError(f"duplicate or invalid key: {key}")
        seen.add(key)
        for field in ("title", "organisation", "official_notice", "deadline", "eligibility", "application_method", "verified_on"):
            if not row.get(field):
                raise ValueError(f"{key}: missing {field}")
        url = urlparse(row["official_notice"])
        if url.scheme != "https" or not url.hostname or url.hostname not in row["allowed_hosts"]:
            raise ValueError(f"{key}: notice host is not allowlisted")
        if row["official_notice"] in notices:
            raise ValueError(f"duplicate official notice: {key}")
        notices.add(row["official_notice"])
        deadline = dt.date.fromisoformat(row["deadline"])
        verified = dt.date.fromisoformat(row["verified_on"])
        if verified > dt.datetime.now(IST).date():
            raise ValueError(f"{key}: future verification date")
        if not (JOBS / key / "index.html").is_file():
            raise ValueError(f"{key}: detail page missing")
        if deadline < verified:
            raise ValueError(f"{key}: deadline predates verification")


def publish():
    rows = json.loads(SOURCE.read_text())
    validate(rows)
    today = dt.datetime.now(IST).date()
    feed = []
    for row in rows:
        item = {k: row[k] for k in ("exam_key", "title", "organisation", "vacancies", "deadline", "official_notice")}
        item.update(url=f"{HOST}/meritniti/jobs/{row['exam_key']}/", application_status="open" if dt.date.fromisoformat(row["deadline"]) >= today else "closed", verified_on=row["verified_on"], verification_status="editor_reviewed")
        feed.append(item)
    feed.sort(key=lambda x: x["deadline"])
    (JOBS / "feed.json").write_text(json.dumps(feed, ensure_ascii=False, indent=2) + "\n")
    page = (JOBS / "index.html").read_text()
    cards = []
    for row, item in zip(rows, [next(i for i in feed if i['exam_key'] == r['exam_key']) for r in rows]):
        e = lambda v: html.escape(str(v), quote=True)
        status = item["application_status"]
        date = dt.date.fromisoformat(row["deadline"]).strftime("%d %b %Y")
        search = " ".join(str(row.get(k, "")) for k in ("title", "organisation", "eligibility", "sector")).lower()
        cards.append(f'<article class="job" data-status="{status}" data-deadline="{e(row["deadline"])}" data-family="{e(row["sector"])}" data-search="{e(search)}" data-key="{e(row["exam_key"])}"><div class="row"><span class="eyebrow">{e(row["sector"])}</span><span class="pill {status}">{status}</span></div><h3><a href="{e(row["exam_key"])}/">{e(row["title"])}</a></h3><p class="muted">{e(row["organisation"])}</p><dl class="facts"><div><dt>VACANCIES</dt><dd>{e(row["vacancies"] or "See official notice")}</dd></div><div><dt>LAST DATE</dt><dd>{e(date)}</dd></div><div><dt>ELIGIBILITY</dt><dd>{e(row["eligibility"])}</dd></div><div><dt>HOW TO APPLY</dt><dd>{e(row["application_method"])}</dd></div></dl><div class="cardfoot"><a href="{e(row["exam_key"])}/">View details →</a><button class="save" aria-label="Save {e(row["title"])}" aria-pressed="false">☆ Save</button></div></article>')
    page, n = re.subn(r'(<div id="jobs" class="grid">).*?(</div><div id="empty")', lambda m: m[1] + "".join(cards) + m[2], page, count=1, flags=re.S)
    if n != 1:
        raise ValueError("board marker missing")
    page = re.sub(r'(<div class="metrics"><div><strong>).*?(</strong><span>Open applications)', lambda m: m[1] + str(sum(i['application_status']=='open' for i in feed)) + m[2], page, count=1, flags=re.S)
    page = re.sub(r'(<span>Open applications</span></div><div><strong>).*?(</strong><span>Closing within 5 days)', lambda m: m[1] + str(sum(0 <= (dt.date.fromisoformat(i['deadline'])-today).days <= 5 for i in feed)) + m[2], page, count=1, flags=re.S)
    page = re.sub(r'(<span>Closing within 5 days</span></div><div><strong>).*?(</strong><span>Published recruitment pages)', lambda m: m[1] + str(len(feed)) + m[2], page, count=1, flags=re.S)
    (JOBS / "index.html").write_text(page)
    for row in rows:
        path = JOBS / row["exam_key"] / "index.html"
        content = path.read_text()
        message = f"{row['title']} | {row['organisation']}\nLast date: {row['deadline']} · Vacancies: {row['vacancies'] or 'see notice'}\nEligibility: {row['eligibility'][:100]}\nDetails: {HOST}/meritniti/jobs/{row['exam_key']}/\nOfficial notice: {row['official_notice']}"
        content = re.sub(r'(<textarea id="sharetext"[^>]*>).*?(</textarea>)', lambda m: m[1] + html.escape(message) + m[2], content, count=1, flags=re.S)
        content = re.sub(r'https://wa\.me/\?text=[^"\s<]+', lambda m: 'https://wa.me/?text=' + quote(message), content, count=1)
        path.write_text(content)
    active_keys = {row["exam_key"] for row in rows}
    for path in JOBS.glob("*/index.html"):
        if path.parent.name in active_keys:
            continue
        content = path.read_text()
        if '<meta name="robots" content="noindex">' not in content:
            content = content.replace('<head>', '<head><meta name="robots" content="noindex">', 1)
        banner = '<p role="status" style="padding:1rem;background:#fff2d5;color:#32240b;text-align:center">This page is archived and is not a confirmed current opening. <a href="../">Browse the current board</a> and check the official notice.</p>'
        if banner not in content:
            content = content.replace('<body>', '<body>' + banner, 1)
        path.write_text(content)
    urls = [f"{HOST}/meritniti/jobs/"] + [f"{HOST}/meritniti/jobs/{key}/" for key in sorted(active_keys)]
    (JOBS / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + ''.join(f'<url><loc>{html.escape(url)}</loc></url>' for url in urls) + '</urlset>')
    (JOBS / "generated_manifest.json").write_text(json.dumps(sorted(active_keys), indent=2) + "\n")
    print(f"Published {len(feed)} curated notices ({sum(i['application_status']=='open' for i in feed)} open).")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--discover", action="store_true")
    parser.add_argument("--discover-only", action="store_true", help="Report leads without altering Studio-published pages")
    args = parser.parse_args()
    try:
        if not args.discover_only:
            publish()
        if args.discover or args.discover_only:
            discover()
    except (ValueError, KeyError, json.JSONDecodeError) as exc:
        sys.exit(f"Publication blocked: {exc}")
