# Job Scraper

**name:** job-scraper
**description:** Scrapes KSA/GCC job boards (LinkedIn + Bayt) for new positions matching your profile. Deduplicates across runs. Triggers on: job scrape, find jobs, search jobs, new jobs, job search, scrape jobs, /scrape
**allowed-tools:** Read, Write, Edit, Glob, Grep, Bash, WebFetch, WebSearch, Agent, AskUserQuestion

---

## How It Works

This skill runs two Scrapling-based CLI scrapers (`tools/linkedin_scrape.py` and `tools/gulf_scrape.py`) against LinkedIn's guest jobs API and Bayt.com, deduplicates against previously seen jobs and the application tracker, and presents new matches with a quick fit assessment. WebSearch/WebFetch are only a fallback when the CLIs are unavailable.

## Prerequisites

The scrapers need Scrapling (Python 3.10+):
```bash
pip install "scrapling[fetchers]"
```
If a scraper errors with `ModuleNotFoundError: scrapling`, tell the user to run the line above, then continue.

## Invocation

The user triggers this skill by saying things like:
- "Find new jobs"
- "Scrape for jobs"
- "Any new positions?"
- "/scrape"

Optional arguments:
- A focus area, e.g. "/scrape consultancy" or "/scrape QC"
- "broad" to run all query categories, e.g. "/scrape broad"
- A country/region, e.g. "/scrape uae"

---

## Execution Steps

### Step 0: Load State

1. Read `job_scraper/seen_jobs.json` (create if missing - start with `{"seen": {}}`)
2. Read `job_search_tracker.csv` to extract already-applied companies+roles
3. Read `.claude/skills/job-scraper/search-queries.md` for the role keywords and location tiers

### Step 1: Pick keywords & location

From `search-queries.md`, take the **role titles** in the Priority categories (not the raw `site:` Google strings - those are for the WebSearch fallback). By default use **Priority 1-3**; if the user said "broad", use all priorities; if the user named a focus area, prefer the matching category.

Map location:
- Default `--location "Saudi Arabia"` (LinkedIn) and `--country saudi-arabia` (Bayt)
- If user says "uae"/"qatar"/etc., set LinkedIn `--location "United Arab Emirates"` and Bayt `--country uae` (slugs: saudi-arabia, uae, qatar, bahrain, oman, kuwait)
- For an Eastern-Province-only sweep, pass LinkedIn `--geo-id 113582820` (Jubail) or filter results to the "ideal" tier afterward

### Step 2: Run the scrapers

Run both CLIs with the chosen keywords (quote each keyword). Run them in parallel where possible. Example for the default structural/civil sweep in KSA:

```bash
python tools/linkedin_scrape.py "structural design engineer" "structural engineer" "civil engineer" --location "Saudi Arabia" --max-age-days 14 --max-pages 3
python tools/gulf_scrape.py "structural engineer" "civil engineer" --country saudi-arabia --max-age-days 14 --max-pages 2
```

Each prints a JSON array of objects: `{title, company, location, date, url, source, posted_days_ago, query}`. Parse stdout as JSON. Ignore the stderr `INFO: Fetched (200)` log lines - they are normal. If a run returns `[]` or errors, note it and continue with the other source.

Merge the arrays from both scrapers. De-duplicate within the merged set by normalized URL (strip query string) and by `company+title`.

### Step 3: Quick Fit Assessment

For each posting, do a rapid fit check (NOT the full `04-job-evaluation.md` - just a quick signal) using the candidate profile:

- **High match**: structural design / ETABS / STAAD / foundations / Aramco-standard industrial role, mid-level (≈3-8 yrs)
- **Medium match**: general civil engineer, QA/QC, construction, procurement, or design-adjacent role
- **Low match**: requires 12-15+ yrs / lead / PE-SCE licensure, or a discipline outside civil/structural

Flag friction from the profile deal-breakers: long-term isolated remote camp postings; pure-QC-only roles; titles implying a sideways/junior move.

### Step 4: Deduplicate & Store

1. Drop any posting whose normalized URL (or `company+title` key) already exists in `seen_jobs.json` or whose company+role already appears in `job_search_tracker.csv`.
2. Add ALL scraped postings (new and skipped) to `seen_jobs.json` so future runs skip them:
```json
{
  "seen": {
    "<normalized_url>": {
      "title": "...",
      "company": "...",
      "location": "...",
      "url": "...",
      "source": "linkedin|bayt",
      "first_seen": "YYYY-MM-DD",
      "fit": "high|medium|low",
      "status": "new|skipped|evaluated"
    }
  }
}
```
3. Only present postings NOT already seen / tracked before this run.

### Step 5: Present Results

Present new jobs in a table sorted by fit (high first):

```
## New Job Matches - YYYY-MM-DD

Found X new positions (Y high, Z medium, W low match). Sources: LinkedIn, Bayt.

| # | Fit | Title | Company | Location | Posted | Source | URL |
|---|-----|-------|---------|----------|--------|--------|-----|
| 1 | High | ... | ... | ... | Xd ago | LinkedIn | [Link](...) |

### High-Match Highlights
For each high-match job, add 2-3 bullet points:
- Why it matches the profile
- Key requirements to check (fetch the posting URL with WebFetch if detail is needed)
- Any red flags / friction
```

After presenting, ask:
> "Want me to evaluate any of these in detail? Just give me the number(s)."

If the user picks a number, invoke the **job-application-assistant** / `/apply` workflow (fit evaluation first, then CV + cover letter if approved). WebFetch the posting URL there to pull full requirements.

### Step 6: Update Tracker (Optional)

If the user decides to apply to any job, add a row to `job_search_tracker.csv`.

---

## Fallback: WebSearch / WebFetch

If Scrapling is not installed and the user does not want to install it, fall back to the `site:` Google queries in `search-queries.md` via WebSearch, then WebFetch individual postings. Note that WebSearch is US-region and most Gulf boards block WebFetch (403) or geo-redirect LinkedIn to US results, so this path is unreliable - prefer the CLIs.

---

## Important Rules

1. **Never fabricate job postings.** Only present postings returned by the scrapers (or real WebFetch results).
2. **Respect deduplication.** Always check seen_jobs.json AND job_search_tracker.csv before presenting.
3. **Focus on configured geographic area.** Use the location tiers in `search-queries.md`; flag GCC-relocation roles, exclude India/non-GCC.
4. **Only open positions.** The scrapers filter by `--max-age-days`; still skip anything that reads as closed/expired.
5. **Don't over-fetch.** The CLIs already return structured cards; only WebFetch a posting URL when you need full requirements for a fit deep-dive.
6. **Parallelize.** Run the two CLIs (and multiple keywords) together; they each handle their own retry/backoff and politeness delays.
