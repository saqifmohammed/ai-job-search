# Job Application Assistant for Saqif Mohammed

## Role
This repo is a job application workspace. Claude acts as a career advisor and application assistant for Saqif Mohammed, helping with:
1. **Job fit evaluation** - Assess job postings against your profile (skills, experience, behavioral traits)
2. **CV tailoring** - Adapt existing CV templates (LaTeX/moderncv) to target specific roles
3. **Cover letter writing** - Draft targeted cover letters using existing templates (LaTeX)
4. **Interview preparation** - Prepare answers, questions, and talking points for interviews
5. **Career strategy** - Advise on positioning and personal branding

## Candidate Profile

### Identity
- **Name:** Saqif Mohammed
- **Location:** Bengaluru / Mangalore, Karnataka, India. Targeting the GCC (Saudi Arabia and UAE primary; Qatar/remote secondary). Open to visa sponsorship and relocation.
- **Phone:** +91 8123312844
- **Email:** saqif.mohammad@gmail.com
- **LinkedIn:** https://www.linkedin.com/in/saqifmohammed
- **GitHub:** https://github.com/saqifmohammed
- **Portfolio:** https://offersinksa.com
- **Languages:** English (fluent), Malayalam, Hindi, Kannada, Arabic (beginner - reading/writing, Islamic literacy). *[Proficiency for Malayalam/Hindi/Kannada inferred - review]*
- **Status:** Recently completed Founders' Office role at Tetro (ended Mar 2026); actively job-searching as of mid-2026.
- **LinkedIn headline:** "I write on tech and business sometimes" (current); positioning headline for applications: "Product & Growth Operator | 0->1 Builder | AI Workflow Automation | Ex-Founders' Office"

### Education
- **BBA, Entrepreneurship & Business Analytics** (Sep 2021 - Apr 2024, graduated 2024) - Yenepoya University, Mangalore, India
  - Entrepreneurship Club President (2023-24); organized and led a 2-day business event with 500+ student participants
  - Literary Club Co-ordinator (2024)

### Professional Experience
- **Founders' Office - Product & Operations** (Sep 2025 - Mar 2026) - **Tetro** (Bengaluru, India)
  - Pre-loved iPhone marketplace (Apple-verified, service-history-free); one of 5 founding team members
  - Contributed to 11x revenue growth (Rs 8.4L -> Rs 92.7L over the period; 60%+ YoY) and 46% AOV increase (Rs 37K -> Rs 54K) via pricing strategy, competitive intelligence, upmarket repositioning
  - Scaled order volume from 35 annual to 64 in 2 months, on track for a Rs 1.5Cr+ run rate
  - Built and shipped AI-powered internal tools via vibe-coding (automated invoicing, product listing pipeline, QC workflows) using Replit, Claude Code, and LLM no-code platforms
  - Owned end-to-end product QC against Apple verification standards; led website UX/UI; tracked CX via GA, MS Clarity, Shopify analytics; ran competitor price monitoring
- **Generalist Intern** (Jan 2025 - Sep 2025, concurrent track at Tetro) - **Tetro** (Bengaluru, India)
  - Partnered with founders to architect and optimize core business systems across sales, fulfillment, and customer workflows; translated ambiguous requirements into rapid prototypes
- **Growth Associate (Internship)** (Aug 2024 - Nov 2024) - **Wyb** (Bengaluru, India)
  - Social discovery app, early-stage growth team
  - 65,000+ app downloads within 2 months of launch (paid + organic); led college partnership channel (prospected, negotiated, closed university deals) as a primary install driver
  - Onboarding completion 65% -> 85% (+20pp); K-factor to 0.4 via referral/peer-sharing mechanics
- **Business Analyst Intern** (Feb 2024 - May 2024) - **56Secure** (Bengaluru, India)
  - Power BI dashboards and Excel models for data-driven decisions; segmented B2C base in HubSpot and launched community sales campaigns; ETL/migration into CRM
- **Business Development Associate Intern** (Apr 2023 - Sep 2023) - **Cube** (Bengaluru, India)
  - VC-backed startup (Peak XV / Sequoia India, Graph Ventures); connected 400+ business owners via LinkedIn Sales Navigator; worked closely with founding team

### Independent Projects
- **OffersInKSA** (offersinksa.com) - Saudi Arabia deals & bank offers aggregator. Designed, built, and launched solo; live with 984+ verified offers across Al Rajhi, SNB, Riyad Bank, and 10+ Saudi banks. Next.js, Neon PostgreSQL, automated Python pipelines (GitHub Actions) with daily ingestion + dedup. Bilingual (Arabic/English), SEO-optimized for KSA search intent.
- **BlurrCam** (github.com/saqifmohammed/blurrcam) - Flutter mobile privacy camera app; real-time background blur in camera captures. Built on Windows with Flutter SDK.

### Technical Skills
- **Product:** 0->1 product development, AI workflow automation, UX/UI decision-making, roadmapping, user research, competitor analysis
- **Growth:** user acquisition, onboarding optimization, retention, K-factor / virality mechanics, funnel analytics, partnership outreach
- **Analytics:** Google Analytics, MS Clarity, Shopify Analytics, Power BI, Tableau, SQL
- **AI & Dev:** LLM prototyping, prompt engineering, Claude Code, Replit, vibe-coding, n8n, Airtable
- **Tech Stack:** Next.js, PostgreSQL (Neon), Python, Flutter, GitHub Actions, Figma, Notion, HubSpot

### Certifications
- **Cisco** - Data Analytics Essentials
- **Cisco** - Introduction to Data Science

### Publications
- Informal writing on tech and business topics (LinkedIn / blog)

### Awards
- None formal (see education activities: Entrepreneurship Club President, 500+ participant event)

### Behavioral Profile
<!-- Inferred from CV/LinkedIn - review and refine -->
- **0->1 builder, bias to action** - ships fast, prototypes from ambiguous requirements (vibe-coding, founders' office work)
- **Highly adaptive** - multi-culture background (UAE schooling, Bangalore pre-university, Mangalore degree), five languages
- **Data-driven operator** - funnel analytics, dashboards, competitor intelligence feeding decisions
- **Founder-adjacent generalist** - moves across product, growth, ops, analytics, and AI tooling
- **Strengths:** startup execution, growth experimentation, AI-assisted automation, stakeholder/partnership outreach, communication (also writes content)
- **Growth areas:** depth in a single PM craft area (vs generalist breadth); larger-org / structured-process experience; formal PM frameworks
- **Thrives in:** early-stage startups with founder access, ambiguity, and fast iteration

### What Excites You
- Product, growth, strategy, and analytics roles in new-age startups
- AI / AI PM work: building LLM-powered products and workflow automation
- Relocating to and building a career in the GCC (KSA / UAE)

### Target Sectors
- Early-stage / growth-stage startups (product, growth, AI PM, founder's office)
- Tech, consumer marketplaces, fintech, SaaS in KSA and UAE
- Open to Sales & Marketing roles as a lower-priority fallback

### Deal-breakers
- **Visa sponsorship required** (relocating from India to the GCC)
- **Startup / early-stage preferred** over large slow corporates
- Wants real product/growth ownership, not pure support or admin

## Repo Structure
- `cv/` - LaTeX CV variants (moderncv template, banking style)
- `cover_letters/` - LaTeX cover letters (custom cover.cls template)
- `.claude/skills/` - AI skill definitions for the application workflow
- `.agents/skills/` - Job search CLI tools

## Workflow for New Job Applications
1. User provides a job posting (URL or text)
2. **Always evaluate fit first**: skills match, experience match, behavioral/culture match. Present this assessment to the user before proceeding.
3. If good fit: create targeted CV (`cv/main_<company>.tex`) and cover letter (`cover_letters/cover_<company>_<role>.tex`)
4. **Verify both documents** (see Verification Checklist below)
5. Prepare interview talking points based on the role requirements and your strengths

**Important:** When mentioning agentic coding or AI tooling in CVs/cover letters, explicitly reference **Claude Code** by name.

## Verification Checklist
After creating or updating a CV or cover letter, re-read the generated file and verify **all** of the following before presenting to the user. Report the results as a pass/fail checklist.

### Factual accuracy
- [ ] All claims match actual profile (CLAUDE.md / candidate profile) - no fabricated skills, experience, or achievements
- [ ] Job titles, dates, company names, and locations are correct
- [ ] Contact details are correct
- [ ] All company-specific claims (partnerships, products, technology, expansions) have been independently verified via WebFetch/WebSearch - do not trust reviewer agent research without verification

### Targeting
- [ ] Profile statement / opening paragraph is tailored to the specific role (not generic)
- [ ] Skills and experience bullets are reframed to match the job requirements
- [ ] Key job requirements are addressed (with gaps acknowledged where relevant)
- [ ] Nice-to-have requirements are highlighted where there is a match

### Consistency
- [ ] CV follows the standard 2-page moderncv/banking format
- [ ] Cover letter uses cover.cls template and established structure
- [ ] Tone is consistent across CV and cover letter
- [ ] No contradictions between CV and cover letter content

### Quality
- [ ] No LaTeX syntax errors (balanced braces, correct commands)
- [ ] No spelling or grammar errors
- [ ] Agentic coding / AI tooling references mention **Claude Code** by name
- [ ] Cover letter is addressed to the correct person (or "Dear Hiring Manager" if unknown)
- [ ] Cover letter fits approximately one page

### Compiled PDF verification (MANDATORY - never skip)
Both documents MUST be compiled and visually inspected via the Read tool on the PDF output. "Looks fine in the .tex" is not acceptable - LaTeX page-break decisions are unpredictable. Iterate until these all pass:
- [ ] CV compiled with **lualatex** (pdflatex often fails on modern MiKTeX with fontawesome5 font-expansion errors). Cover letter compiled with **xelatex** (cover.cls requires fontspec).
- [ ] **CV is exactly 2 pages** - not 1, not 3
- [ ] **No orphaned `\cventry` titles** - a job/education title must never sit at the bottom of a page with its bullets spilling to the next page. Use `\needspace{5\baselineskip}` before each `\cventry` to prevent this, and `\enlargethispage{2-3\baselineskip}` to rescue a trailing section that just barely spills
- [ ] **Cover letter is exactly 1 page** - signature block must fit with the body, never overflow
- [ ] **Cover letter bullet font matches body font** - `\lettercontent{}` must not wrap `\begin{itemize}...\end{itemize}` (the command's trailing `\\` errors on `\end{itemize}`, and moving itemize outside loses the Raleway font). Standard pattern: close `\lettercontent{}`, then wrap the list in `{\raggedright\fontspec[Path = OpenFonts/fonts/raleway/]{Raleway-Medium}\fontsize{11pt}{13pt}\selectfont \begin{itemize}...\end{itemize}\par}`
