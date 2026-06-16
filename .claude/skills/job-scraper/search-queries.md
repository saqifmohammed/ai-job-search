# Search Queries for Job Scraper

<!-- PRIMARY: /scrape runs the Scrapling CLIs tools/linkedin_scrape.py (LinkedIn guest API)
     and tools/gulf_scrape.py (Bayt.com). Feed them the ROLE TITLES under "Scraper Keywords"
     below. The bundled TS CLIs (.agents/skills/) are Danish-only and unused here.
     The Google site: queries further down are a FALLBACK for when Scrapling is unavailable. -->

## Scraper Keywords (primary - feed to the CLIs)

Pass these as quoted keywords to `linkedin_scrape.py` / `gulf_scrape.py`.

- **Priority 1 (product):** "product manager", "associate product manager", "product owner"
- **Priority 2 (AI product):** "ai product manager", "ai product", "growth product manager"
- **Priority 3 (growth):** "growth associate", "growth manager", "user acquisition", "growth marketing"
- **Priority 4 (founder's office / strategy):** "founder's office", "chief of staff", "business analyst", "product analyst"
- **Priority 5 (fallback, lowest priority):** "sales and marketing", "marketing associate"

Default `/scrape` runs Priority 1-4 in Saudi Arabia + UAE, last 14 days. "broad" adds Priority 5 and widens to the wider GCC + remote.

Example:
```
python tools/linkedin_scrape.py "product manager" "ai product manager" "growth manager" "founder's office" --location "Saudi Arabia" --max-age-days 14 --max-pages 3
python tools/linkedin_scrape.py "product manager" "growth manager" --location "United Arab Emirates" --max-age-days 14 --max-pages 3
python tools/gulf_scrape.py "product manager" "growth manager" --country saudi-arabia --max-age-days 14 --max-pages 2
python tools/gulf_scrape.py "product manager" "growth manager" --country uae --max-age-days 14 --max-pages 2
```

## Search Sites (KSA / UAE / GCC)

Primary:
- **linkedin.com/jobs** - primary source; filter Saudi Arabia and UAE first, then wider GCC, then remote
- **bayt.com** - largest Gulf/MENA job board
- **wuzzuf** / **naukrigulf.com** - additional Gulf coverage
- **wellfound.com** (AngelList) - early-stage startup roles, often remote/sponsorship-friendly
- **indeed.com** (sa.indeed.com / ae.indeed.com) - broad aggregator

Secondary (company career pages via Google):
- GCC startups and scaleups hiring product/growth (fintech, marketplaces, SaaS, e-commerce)

## Query Categories

Queries are grouped by priority. Combine each with a location term (e.g. "Saudi Arabia", "Riyadh", "Jeddah", "UAE", "Dubai", "Abu Dhabi", "remote") where the site supports it. Add "visa sponsorship" where the site allows it, since sponsorship is a hard filter.

### Priority 1: Product Manager / APM (strongest)

```
site:linkedin.com/jobs "Product Manager" startup Saudi Arabia
site:linkedin.com/jobs "Associate Product Manager" (Saudi Arabia OR UAE)
site:bayt.com "Product Manager" Dubai
site:wellfound.com "Product Manager" Saudi Arabia OR UAE
"Product Manager" startup (Riyadh OR Dubai OR Jeddah) "visa sponsorship"
```

### Priority 2: AI Product Manager

```
site:linkedin.com/jobs "AI Product Manager" (Saudi Arabia OR UAE)
site:linkedin.com/jobs "Product Manager" "LLM" OR "AI" startup GCC
site:wellfound.com "AI Product" (Dubai OR Riyadh)
"Growth Product Manager" AI (UAE OR Saudi Arabia)
```

### Priority 3: Growth

```
site:linkedin.com/jobs "Growth Manager" startup (Saudi Arabia OR UAE)
site:linkedin.com/jobs "Growth Associate" OR "User Acquisition" GCC
site:bayt.com "Growth Marketing" Dubai
"Growth" startup (Riyadh OR Dubai) "app downloads" OR "user acquisition"
```

### Priority 4: Founder's Office / Strategy / Analytics

```
site:linkedin.com/jobs "Founder's Office" (Saudi Arabia OR UAE)
site:linkedin.com/jobs "Chief of Staff" startup GCC
site:linkedin.com/jobs "Product Analyst" OR "Business Analyst" startup (Dubai OR Riyadh)
"Founding team" OR "Founder's Office" startup (UAE OR Saudi Arabia)
```

### Priority 5: Sales & Marketing (fallback, lowest priority)

```
site:linkedin.com/jobs "Marketing Associate" startup (Saudi Arabia OR UAE)
site:bayt.com "Sales and Marketing" Dubai
```

## Location Filter

Tiers (verify each result's location):
- **Ideal:** Saudi Arabia (Riyadh, Jeddah, Dammam/Khobar) and UAE (Dubai, Abu Dhabi), with visa sponsorship
- **Acceptable:** Wider GCC (Qatar, Bahrain, Oman, Kuwait) with sponsorship; fully remote (GCC or global)
- **Borderline:** Remote roles that prefer GCC time zones; roles silent on sponsorship (flag to confirm)
- **Too far / excluded:** GCC roles with no visa sponsorship; India-based on-site roles (fallback only, flag to user)

**Hard filter:** visa sponsorship is required for any GCC on-site role. Flag roles that do not mention sponsorship so the user can confirm before applying.

## Date Filter

Only include jobs posted within the last 14 days, or with an application deadline not yet passed. If a posting date cannot be determined, include it but flag as "date unknown".

## Adapting Queries

If the user specifies a focus area, select queries from the matching category and generate 2-3 custom focus-specific queries. Example: "/scrape ai" -> Priority 2 queries plus custom searches for AI/LLM product roles at GCC startups.
