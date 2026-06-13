#!/usr/bin/env python3
"""
expatriates.com classifieds job scraper using Scrapling.

expatriates.com is a high-traffic KSA/Gulf classifieds board. Jobs are posted as
classified ads under /classifieds/<region>/jobs/ with individual ads at /cls/<id>.html.
Listing pages expose ad titles + links; the ad detail page carries the city and
posted date. This scraper pulls the listing pages, keyword-filters the titles, then
fetches detail pages only for matches to attach location/date.

Usage:
    python tools/expatriates_scrape.py "civil engineer" "structural engineer" \
        --region saudi-arabia --max-age-days 30 --max-pages 4

Output: JSON array of job objects on stdout:
    [{"title","company","location","date","url","source","posted_days_ago","query"}]

Requires: pip install "scrapling[fetchers]"
"""
import argparse
import json
import re
import sys
from datetime import date, datetime

from scrapling.fetchers import Fetcher

BASE = "https://www.expatriates.com"


def parse_age_days(text: str):
    """expatriates detail pages show a posting date like 'Tuesday, June 10, 2026'."""
    if not text:
        return None
    m = re.search(r"([A-Z][a-z]+ \d{1,2}, \d{4})", text)
    if not m:
        return None
    for fmt in ("%B %d, %Y", "%b %d, %Y"):
        try:
            d = datetime.strptime(m.group(1), fmt).date()
            return (date.today() - d).days
        except ValueError:
            continue
    return None


def fetch(url):
    try:
        r = Fetcher.get(url, stealthy_headers=True)
        if r.status != 200:
            print(f"INFO: {url} -> {r.status}", file=sys.stderr)
            return None
        return r
    except Exception as e:  # noqa
        print(f"INFO: fetch error {url}: {e}", file=sys.stderr)
        return None


def listing_urls(region, max_pages):
    """First page is /classifieds/<region>/jobs/, then indexN00.html pagination."""
    urls = [f"{BASE}/classifieds/{region}/jobs/"]
    for p in range(1, max_pages):
        urls.append(f"{BASE}/classifieds/{region}/jobs/index{p}00.html")
    return urls


def scrape_listing(url):
    r = fetch(url)
    if not r:
        return []
    out = []
    for a in r.css("a"):
        href = a.attrib.get("href", "")
        if href.startswith("/cls/") and href.endswith(".html"):
            title = (a.text or "").strip()
            if title:
                out.append({"title": title, "url": BASE + href})
    return out


def matches(title, keywords):
    t = title.lower()
    for kw in keywords:
        # match all whitespace-separated tokens of the keyword
        if all(tok in t for tok in kw.lower().split()):
            return kw
    return None


def enrich(job):
    """expatriates guest detail pages expose 'Region:' but NOT an exact posting date,
    so location comes from the Region field and recency is proxied by ad id."""
    r = fetch(job["url"])
    job["location"] = None
    job["body"] = None
    if not r:
        return job
    html = r.html_content if hasattr(r, "html_content") else str(r.body)
    flat = re.sub(r"<[^>]+>", " ", html)
    flat = re.sub(r"\s+", " ", flat)
    m = re.search(r"Region:\s*([A-Za-z\-\(\) ]+?)\s*(?:\(|Posting ID|Category|$)", flat)
    if m:
        job["location"] = m.group(1).strip() or None
    return job


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("keywords", nargs="+")
    ap.add_argument("--region", default="saudi-arabia",
                    help="region slug: saudi-arabia, riyadh, jubail, dammam, eastern-province, jeddah, ...")
    ap.add_argument("--max-age-days", type=int, default=30)
    ap.add_argument("--max-pages", type=int, default=4)
    args = ap.parse_args()

    seen_url = set()
    candidates = []
    for url in listing_urls(args.region, args.max_pages):
        for item in scrape_listing(url):
            if item["url"] in seen_url:
                continue
            seen_url.add(item["url"])
            kw = matches(item["title"], args.keywords)
            if kw:
                item["query"] = kw
                candidates.append(item)

    # ad id is sequential -> use as recency proxy (newer = higher), newest first
    def ad_id(j):
        m = re.search(r"/cls/(\d+)\.html", j["url"])
        return int(m.group(1)) if m else 0
    candidates.sort(key=ad_id, reverse=True)

    results = []
    for job in candidates:
        job["company"] = None
        job["source"] = "expatriates"
        job["date"] = None            # expatriates does not expose exact post date to guests
        job["posted_days_ago"] = None
        enrich(job)
        results.append(job)

    print(json.dumps(results, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
