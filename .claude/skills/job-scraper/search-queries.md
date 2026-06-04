# Search Queries for Job Scraper

<!-- PRIMARY: /scrape runs the Scrapling CLIs tools/linkedin_scrape.py (LinkedIn guest API)
     and tools/gulf_scrape.py (Bayt.com). Feed them the ROLE TITLES under "Scraper Keywords"
     below. The bundled TS CLIs (.agents/skills/) are Danish-only and unused here.
     The Google site: queries further down are a FALLBACK for when Scrapling is unavailable. -->

## Scraper Keywords (primary - feed to the CLIs)

Pass these as quoted keywords to `linkedin_scrape.py` / `gulf_scrape.py`.

- **Priority 1 (strongest):** "structural design engineer", "structural engineer"
- **Priority 2 (industrial/oil & gas):** "civil engineer", "civil structural engineer"
- **Priority 3 (QC pivot):** "civil qc engineer", "qa qc civil engineer"
- **Priority 4 (wider net, GCC):** "design engineer"

Default `/scrape` runs Priority 1-3 in KSA, last 14 days. "broad" adds Priority 4 and widens to GCC.

Example:
```
python tools/linkedin_scrape.py "structural design engineer" "structural engineer" "civil engineer" --location "Saudi Arabia" --max-age-days 14 --max-pages 3
python tools/gulf_scrape.py "structural engineer" "civil engineer" --country saudi-arabia --max-age-days 14 --max-pages 2
```

## Search Sites (KSA / GCC)

Primary:
- **linkedin.com/jobs** - primary source; filter Saudi Arabia / Eastern Province, then all KSA, then GCC
- **bayt.com** - largest Gulf/MENA job board
- **gulftalent.com** - strong for engineering roles across the GCC
- **naukrigulf.com** - Gulf arm of Naukri
- **indeed.com** (sa.indeed.com / ae.indeed.com) - broad aggregator

Secondary (company career pages via Google):
- EPC contractors: Hyundai E&C, Samsung E&C, L&T, Saipem, McDermott, Saudi Aramco contractor pages

## Query Categories

Queries are grouped by priority. Combine each with a location term (e.g. "Eastern Province", "Jubail", "Dammam", "Saudi Arabia", "Riyadh", "UAE") where the site supports it.

### Priority 1: Structural Design Engineer (strongest, most desired)

```
site:linkedin.com/jobs "Structural Design Engineer" Saudi Arabia
site:linkedin.com/jobs "Structural Engineer" ETABS STAAD Saudi Arabia
site:bayt.com "Structural Design Engineer" Eastern Province
site:gulftalent.com "Structural Engineer" Saudi Arabia
"Structural Design Engineer" "STAAD Pro" (Dammam OR Jubail OR Riyadh)
```

### Priority 2: Civil / Structural Engineer - industrial & oil & gas

```
site:linkedin.com/jobs "Civil Engineer" "oil and gas" Saudi Arabia
site:linkedin.com/jobs "Structural Engineer" refinery OR industrial Saudi Arabia
site:bayt.com "Civil Structural Engineer" Aramco
site:naukrigulf.com "Structural Engineer" Saudi Arabia
"Civil Engineer" foundations industrial (Saudi Arabia OR UAE OR Qatar)
```

### Priority 3: QA/QC & construction engineering (credentialed pivot)

```
site:linkedin.com/jobs "Civil QC Engineer" Aramco Saudi Arabia
site:bayt.com "QA/QC Civil Engineer" Eastern Province
site:gulftalent.com "Civil Engineer" construction Saudi Arabia
"Aramco approved" "Civil QC Inspector" Saudi Arabia
```

### Priority 4: Broader engineering (wider net, GCC-wide)

```
site:linkedin.com/jobs "Design Engineer" civil OR structural GCC
site:naukrigulf.com "Structural Engineer" (UAE OR Qatar OR Saudi Arabia)
site:indeed.com "Structural Design Engineer" Gulf
```

## Location Filter

Tiers (verify each result's location):
- **Ideal:** Eastern Province KSA - Jubail, Dammam, Khobar, Dhahran
- **Acceptable:** Anywhere in Saudi Arabia - Riyadh, Jeddah, Yanbu, Jubail Industrial City
- **Borderline:** Wider GCC - UAE, Qatar, Bahrain, Oman, Kuwait (relocation acceptable)
- **Too far / excluded:** India and outside the GCC

Flag long-term isolated remote-site / camp postings as friction (deal-breaker tendency), even when location tier passes.

## Date Filter

Only include jobs posted within the last 14 days, or with an application deadline not yet passed. If a posting date cannot be determined, include it but flag as "date unknown".

## Adapting Queries

If the user specifies a focus area, select queries from the matching category and generate 2-3 custom focus-specific queries. Example: "/scrape consultancy" -> Priority 1 queries plus custom searches for structural design consultancies in KSA/GCC.
