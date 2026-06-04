#!/usr/bin/env python3
"""
LinkedIn job scraper using Scrapling (https://github.com/D4Vinci/Scrapling).

Uses LinkedIn's public *guest* jobs endpoint (no login required):
    /jobs-guest/jobs/api/seeMoreJobPostings/search
which returns 10 job cards per `start` offset as HTML. Each card carries an
absolute ISO posting date (<time datetime=...>), so age filtering is exact.

Usage:
    python tools/linkedin_scrape.py "structural engineer" "civil engineer" \
        --location "Saudi Arabia" --max-age-days 14 --max-pages 3

Optional LinkedIn filters:
    --geo-id 113582820        (e.g. Jubail; overrides --location matching)
    --tpr r1209600            (server-side "last 14 days"; r604800 = 7 days)
    --remote                  (sets f_WT=2)

Output: JSON array on stdout in the shared job shape:
    [{"title","company","location","date","url","source","query"}]

Requires: pip install "scrapling[fetchers]"
"""
import argparse
import json
import sys
import time
import urllib.parse as u
from datetime import date, datetime

from scrapling.fetchers import Fetcher

GUEST_URL = "https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search"


def _first(card, selector):
    try:
        v = card.css(selector).get()
        return v.strip() if v else None
    except Exception:
        return None


def canonical_url(href: str) -> str:
    if not href:
        return href
    return href.split("?", 1)[0]


def parse_card(card):
    title = _first(card, "h3::text") or _first(card, ".base-search-card__title::text")
    href = (_first(card, "a.base-card__full-link::attr(href)")
            or _first(card, "a::attr(href)"))
    if not title or not href:
        return None
    company = (_first(card, "h4 a::text")
               or _first(card, ".base-search-card__subtitle::text"))
    location = _first(card, ".job-search-card__location::text")
    posted = _first(card, "time::attr(datetime)")  # ISO yyyy-mm-dd
    return {
        "title": title,
        "company": company,
        "location": location,
        "date": posted,
        "url": canonical_url(href),
        "source": "linkedin",
    }


def age_days(iso_date: str):
    if not iso_date:
        return None
    try:
        d = datetime.strptime(iso_date[:10], "%Y-%m-%d").date()
        return (date.today() - d).days
    except ValueError:
        return None


def scrape_linkedin(keyword, location, geo_id, tpr, remote, max_pages):
    out = []
    for page in range(max_pages):
        params = {"keywords": keyword, "start": page * 10}
        if geo_id:
            params["geoId"] = geo_id
        else:
            params["location"] = location
        if tpr:
            params["f_TPR"] = tpr
        if remote:
            params["f_WT"] = "2"
        url = f"{GUEST_URL}?{u.urlencode(params)}"
        try:
            resp = Fetcher.get(url, stealthy_headers=True)
        except Exception as e:
            sys.stderr.write(f"[linkedin] fetch failed (page {page}): {e}\n")
            break
        status = getattr(resp, "status", 200)
        if status == 429:
            sys.stderr.write("[linkedin] 429 rate-limited; stopping. Retry later.\n")
            break
        if status != 200:
            sys.stderr.write(f"[linkedin] status {status} (page {page}); stopping.\n")
            break
        cards = resp.css("li")
        if not cards:
            break
        for c in cards:
            rec = parse_card(c)
            if rec:
                rec["query"] = keyword
                out.append(rec)
        time.sleep(1.0)  # politeness between pages
    return out


def main():
    ap = argparse.ArgumentParser(description="Scrape LinkedIn guest jobs API via Scrapling.")
    ap.add_argument("keywords", nargs="+", help="Search keywords, e.g. 'structural engineer'")
    ap.add_argument("--location", default="Saudi Arabia", help="Location string for LinkedIn")
    ap.add_argument("--geo-id", default=None, help="LinkedIn geoId (overrides --location)")
    ap.add_argument("--tpr", default="r1209600",
                    help="Server-side recency filter: r1209600=14d, r604800=7d, '' to disable")
    ap.add_argument("--remote", action="store_true", help="Remote only (f_WT=2)")
    ap.add_argument("--max-age-days", type=int, default=14,
                    help="Drop postings older than this (keeps unknown-date postings)")
    ap.add_argument("--max-pages", type=int, default=3, help="Pages per keyword (10 results/page)")
    args = ap.parse_args()

    results, seen = [], set()
    for kw in args.keywords:
        for rec in scrape_linkedin(kw, args.location, args.geo_id,
                                   args.tpr or None, args.remote, args.max_pages):
            if rec["url"] in seen:
                continue
            a = age_days(rec["date"])
            if a is not None and a > args.max_age_days:
                continue
            seen.add(rec["url"])
            rec["posted_days_ago"] = a
            results.append(rec)

    sys.stdout.buffer.write(json.dumps(results, ensure_ascii=False, indent=2).encode("utf-8"))
    sys.stdout.buffer.write(b"\n")
    sys.stderr.write(f"[linkedin_scrape] {len(results)} unique postings <= {args.max_age_days}d\n")


if __name__ == "__main__":
    main()
