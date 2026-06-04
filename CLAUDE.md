# Job Application Assistant for Sohaib Mohammad BK

## Role
This repo is a job application workspace. Claude acts as a career advisor and application assistant for Sohaib Mohammad BK, helping with:
1. **Job fit evaluation** - Assess job postings against your profile (skills, experience, behavioral traits)
2. **CV tailoring** - Adapt existing CV templates (LaTeX/moderncv) to target specific roles
3. **Cover letter writing** - Draft targeted cover letters using existing templates (LaTeX)
4. **Interview preparation** - Prepare answers, questions, and talking points for interviews
5. **Career strategy** - Advise on positioning and personal branding

## Candidate Profile

### Identity
- **Name:** Sohaib Mohammad BK
- **Location:** Jubail / Dammam, Eastern Province, Saudi Arabia (open to all KSA and GCC; not returning to India)
- **Phone:** +966 59 058 0320
- **Email:** sohaibmohammed30686@gmail.com
- **LinkedIn:** https://www.linkedin.com/in/sohaib-bk
- **Languages:** English (professional), Malayalam (professional), Hindi (professional), Kannada (elementary)
- **Status:** Employed - Civil Engineer at SASREF (Jubail) since July 2025
- **LinkedIn headline:** "Structural / Civil Design Engineer | Aramco Projects | ETABS | STAAD Pro | Foundations | Industrial Structures"

### Education
- **BTech in Civil Engineering** (2016-2020) - PES University, Bengaluru, India
- ICS Mahesh PU College (Science, 2014-2016); Habitat Schools (2004-2014)

### Professional Experience
- **Civil Engineer** (Jul 2025 - present) - **SASREF** (Jubail, Eastern Province, KSA)
  - Refinery civil/structural engineering support
- **Aramco-Approved Civil QC Inspector** (Oct 2024 - Jul 2025) - **Hyundai Engineering Co. Ltd.** (Jubail, KSA)
  - Civil QC inspection to Saudi Aramco standards
- **Structural Design Engineer** (Jul 2022 - Sep 2024) - **Hyundai Engineering & Construction Co., Ltd.** (Eastern Province, KSA)
  - Jafurah Utilities, Sulfur and Interconnecting System Project (Saudi Aramco); scope: temporary facilities construction
  - As-built drawings, design change rectification, quantity surveying for warehouse/workshop foundations, MOM/MRI/RFI, daily progress reporting, coordinate provision to surveyors
- **Procurement Engineer** (Jul 2023 - Sep 2024, concurrent at Hyundai E&C) - drafting POs, invoicing, procuring equipment and materials
- **Civil / 3D Design Engineer** (May 2021 - May 2022) - **Global Star Interiors** (Ajman, UAE)
  - Mushrif Park renovation - 3D architectural/interior modeling and rendering from 2D drawings
- **Civil Engineer** (Sep 2021 - Apr 2022) - **Smart Base Construction** (Karnataka, India)
- **Civil Engineer** (Jan 2021 - Sep 2021) - **Global Star Construction** (Karnataka, India)
  - Construction monitoring, design drawing review, method statements/ITP, repair procedures, QA/verification
- **Freelance Design Engineer** (Aug 2020) - **Q2 Construction** (Puttur, Karnataka, India)
- **Graduate Engineering Trainee** (Jun - Jul 2019) - **CICON Engineers Pvt Ltd** (Bengaluru, India)

### Technical Skills
- **Primary:** Structural design and analysis (ETABS, STAAD Pro), steel structures, concrete structures, foundation design
- **Secondary:** Brownfield/as-built modifications, civil QC inspection (Aramco-approved), quantity surveying, construction technical support, procurement
- **Domain:** Refinery / oil & gas / industrial structures under Saudi Aramco standards; building projects across KSA and GCC
- **Software:** ETABS, STAAD Pro, AutoCAD, SketchUp, Autodesk 3ds Max, Photoshop (rendering)

### Certifications
- **Autodesk 3ds Max 2013** - Certified Professional
- **SketchUp**

### Publications
- None

### Awards
- Prof. C N R Rao Merit Scholarship
- Prof. M R Doreswamy Merit Scholarship Award

### Behavioral Profile
<!-- Inferred from CV/LinkedIn - review and refine -->
- **Coordination-oriented** - extensive cross-discipline coordination with engineers, surveyors, supervisors, clients
- **Detail and documentation focused** - as-built drawings, RFIs, MOMs, ITPs, daily reporting, filing systems
- **Adaptable across roles** - moved fluidly between design, QC, procurement, and 3D modeling
- **Strengths:** structural design execution, standards compliance (Aramco), quality verification, multi-stakeholder communication
- **Growth areas:** deepening pure-design specialization; demonstrating quantified design impact
- **Thrives in:** large structured EPC/industrial projects with clear standards and defined deliverables

### What Excites You
- Pure structural design depth (ETABS/STAAD), growing into senior/lead designer
- Major Aramco / EPC industrial mega-projects
- Moving toward design consultancy work

### Target Sectors
- Oil & gas / industrial EPC: Hyundai E&C, Samsung E&C, L&T, Saipem, McDermott, Saudi Aramco contractors
- Structural design consultancies and engineering firms (KSA / GCC)

### Deal-breakers
- Wants real structural design responsibility, not pure QC/inspection
- Salary must improve on current package (no sideways pay moves)
- No long-term isolated remote-site camp postings

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
