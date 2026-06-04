#!/usr/bin/env python3
"""
Gulf job scraper using Scrapling (https://github.com/D4Vinci/Scrapling).

Replaces the Denmark-only TS CLIs / generic WebSearch for KSA/GCC job boards.
Currently supports Bayt.com (largest Gulf board, scrapes cleanly over plain HTTP
with stealth headers - no browser needed). Other boards can be added as parsers.

Usage:
    python tools/gulf_scrape.py "structural engineer" "civil engineer" \
        --country saudi-arabia --max-age-days 14 --max-pages 2

Output: JSON array of job objects on stdout:
    [{"title","company","location","date","url","source","posted_days_ago"}]

Requires: pip install "scrapling[fetchers]"
"""
import argparse
import json
import re
import sys
from datetime import date, timedelta

from scrapling.fetchers import Fetcher

BAYT_BASE = "https://www.bayt.com"


def slugify(keyword: str) -> str:
    s = keyword.strip().lower()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return s.strip("-")


def parse_relative_age(text: str):
    """Return approximate age in days from Bayt's '16 days ago' / '2 hours ago' / 'yesterday'."""
    if not text:
        return None
    t = text.lower()
    if "just now" in t or "hour" in t or "minute" in t or "today" in t:
        return 0
    if "yesterday" in t:
        return 1
    m = re.search(r"(\d+)\s*day", t)
    if m:
        return int(m.group(1))
    m = re.search(r"(\d+)\s*week", t)
    if m:
        return int(m.group(1)) * 7
    m = re.search(r"(\d+)\s*month", t)
    if m:
        return int(m.group(1)) * 30
    return None


def _first(card, selector):
    try:
        v = card.css(selector).get()
        return v.strip() if v else None
    except Exception:
        return None


def parse_bayt_card(card):
    title = _first(card, "h2 a::text")
    href = _first(card, "h2 a::attr(href)")
    if not title or not href:
        return None
    url = href if href.startswith("http") else BAYT_BASE + href
    company = _first(card, "a[href*='/en/company/']::text") or _first(card, "a[href*='/company/']::text")
    # Location: city + country live in muted span/div elements (date is the t-bold one).
    seen, ordered = set(), []
    for s in card.css("span, div"):
        cls = s.attrib.get("class", "")
        if "t-mute" not in cls or "bold" in cls:
            continue
        txt = (s.css("::text").get() or "").strip()
        if not txt or txt in ("·", ".") or "ago" in txt.lower():
            continue
        if txt not in seen:
            seen.add(txt)
            ordered.append(txt)
    location = ", ".join(ordered[:2]) if ordered else None
    # Date: the bold-mute span ("X days ago")
    date_text = None
    for t in card.css("span::text").getall():
        if t and "ago" in t.lower():
            date_text = t.strip()
            break
    if not date_text:
        for t in card.css("span::text").getall():
            if t and ("yesterday" in t.lower() or "today" in t.lower()):
                date_text = t.strip()
                break
    age = parse_relative_age(date_text)
    posted = None
    if age is not None:
        posted = (date.today() - timedelta(days=age)).isoformat()
    return {
        "title": title,
        "company": company,
        "location": location,
        "date": posted,
        "posted_days_ago": age,
        "date_text": date_text,
        "url": url,
        "source": "bayt",
    }


def scrape_bayt(keyword: str, country: str, max_pages: int):
    slug = slugify(keyword)
    out = []
    for page in range(1, max_pages + 1):
        url = f"{BAYT_BASE}/en/{country}/jobs/{slug}-jobs/"
        if page > 1:
            url += f"?page={page}"
        try:
            resp = Fetcher.get(url, stealthy_headers=True)
        except Exception as e:
            sys.stderr.write(f"[bayt] fetch failed {url}: {e}\n")
            break
        if getattr(resp, "status", 200) != 200:
            sys.stderr.write(f"[bayt] status {resp.status} for {url}\n")
            break
        cards = resp.css("li[data-js-job]")
        if not cards:
            break
        for c in cards:
            rec = parse_bayt_card(c)
            if rec:
                rec["query"] = keyword
                out.append(rec)
    return out


def main():
    ap = argparse.ArgumentParser(description="Scrape Gulf job boards (Bayt) via Scrapling.")
    ap.add_argument("keywords", nargs="+", help="Search keywords, e.g. 'structural engineer'")
    ap.add_argument("--country", default="saudi-arabia",
                    help="Bayt country slug: saudi-arabia, uae, qatar, bahrain, oman, kuwait")
    ap.add_argument("--max-age-days", type=int, default=14,
                    help="Drop postings older than this (keeps unknown-date postings)")
    ap.add_argument("--max-pages", type=int, default=2, help="Pages per keyword (30 results/page)")
    args = ap.parse_args()

    results, seen_urls = [], set()
    for kw in args.keywords:
        for rec in scrape_bayt(kw, args.country, args.max_pages):
            if rec["url"] in seen_urls:
                continue
            age = rec.get("posted_days_ago")
            if age is not None and age > args.max_age_days:
                continue
            seen_urls.add(rec["url"])
            results.append(rec)

    sys.stdout.buffer.write(json.dumps(results, ensure_ascii=False, indent=2).encode("utf-8"))
    sys.stdout.buffer.write(b"\n")
    sys.stderr.write(f"[gulf_scrape] {len(results)} unique postings <= {args.max_age_days}d\n")


if __name__ == "__main__":
    main()
