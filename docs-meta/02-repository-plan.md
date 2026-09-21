# Detailed Repository Plan

**Companion to:** `docs-meta/01-course-architecture.md` · **Version:** 1.0 · **Date:** 2026-09-18

---

## 1. Design principles

1. **One public tree (`docs/`), one private tree (`instructor/`).** The build boundary *is* the privacy boundary.
2. **Nav-first authoring.** `mkdocs.yml` declares every page; a validator keeps the tree and nav in lock-step, so orphan or missing files fail early.
3. **Machine-checkable conventions.** Front-matter, lecture headers, CLO mappings, alt text, and terminology are validated by scripts, not by hope.
4. **Zero fabricated content.** Every technical/historical claim traces to a cited source on its lecture page.
5. **Small, boring tooling.** Pure-stdlib Python validators; a single pinned venv for MkDocs.

## 2. Full directory plan (as implemented)

```text
/ (repository root)
├── README.md                          # Repository landing: what this is, how to build/preview
├── .gitignore                         # venv, site/, caches, OS junk
├── LICENSE                            # Placeholder decision → OQ-05 (created only if instructor confirms)
├── requirements.txt                   # mkdocs-material pin for local + CI venv
├── mkdocs.yml                         # Site config + explicit nav (public pages only)
│
├── docs/                              # PUBLIC SITE SOURCE (published by GitHub Pages)
│   ├── index.md                       # Course home
│   ├── syllabus.md                    # Student syllabus
│   ├── schedule.md                    # 32-lecture schedule
│   ├── assessment.md                  # Weights, policies (no keys)
│   ├── help.md                        # FAQ + support
│   ├── glossary.md                    # Course glossary
│   ├── modules/                       # 8 module overview pages
│   │   ├── module-01-foundations.md
│   │   ├── module-02-hardware.md
│   │   ├── module-03-software-operating-systems.md
│   │   ├── module-04-data-representation.md
│   │   ├── module-05-logic-productivity.md
│   │   ├── module-06-networks-internet-cloud.md
│   │   ├── module-07-data-databases-ai.md
│   │   └── module-08-security-society-synthesis.md
│   ├── lectures/                      # 32 lecture pages L01–L32
│   │   └── L{n}-{slug}.md
│   ├── labs/                          # index + workbook hub + 8 graded handouts + 4 skill builders (PROMPT 05)
│   ├── activities/                    # index + 5 in-class activities
│   ├── case-studies/                  # index + 4 case studies
│   ├── assessments/
│   │   ├── project/                   # brief, milestones, rubric (criteria only)
│   │   └── quizzes/                   # practice quizzes (keys in instructor/)
│   └── references/
│       └── index.md                   # Textbooks + vetted online sources
│
├── instructor/                        # INSTRUCTOR-ONLY — outside docs/, never published
│   ├── README.md                      # How to use; why this folder must stay out of docs/
│   ├── answer-keys/
│   │   ├── quiz-answer-keys.md        # Keys for quizzes Q01–Q14
│   │   └── lab-answer-notes.md        # Expected outcomes + grading notes for Labs 1–8
│   ├── exams/
│   │   ├── midterm-exam-bank.md       # Midterm item bank (Modules 1–4)
│   │   └── final-exam-bank.md         # Final item bank (cumulative)
│   ├── module-guides/                 # PROMPT 03: per-module teaching guides (L-tips, demos, answered exit tickets)
│   ├── slides/                        # PROMPT 04: 8 module deck files (32 decks + notes), 00-delivery-guide, README
│   └── lab-delivery/                  # PROMPT 05: lab delivery guide, equipment + validation checklists
│
├── docs-meta/                         # DESIGN DOCS — not part of the published site nav
│   ├── 00-repository-inspection.md    # Phase 1 deliverable
│   ├── 01-course-architecture.md      # Phase 2 deliverable (15 sections)
│   ├── 02-repository-plan.md          # This file
│   ├── 03-development-roadmap.md      # Phase 3/4 sequencing + status
│   ├── 04-documentation-standards.md  # Phase 4 standards
│   ├── 05-qa-strategy.md              # QA strategy + CI design
│   ├── 06-open-questions.md           # OQ-01…OQ-12 for instructor review
│   ├── 07-teaching-blueprint.md       # 32-lecture teaching plans (PROMPT 02)
│   ├── 08-assessment-blueprint.md     # Proposed plan + CLO matrices (PROMPT 02)
│   ├── 09-instructor-review-checklist.md  # Validation rubric + semester checklist
│   ├── 10-content-coverage-report.md  # PROMPT 03: validation warnings + coverage report
│   ├── 11-delivery-package-report.md  # PROMPT 04: slide-deck validation + delivery report
│   └── 12-lab-workbook-report.md      # PROMPT 05: lab workbook validation + testing-scope statement
│   └── 13-case-bank-qa-report.md      # PROMPT 06: case-bank validation + QA statement
│   └── 14-assessment-qa-report.md     # PROMPT 07: assessment package validation + QA statement
│
├── scripts/                           # Validation tooling (Python 3, stdlib only)
│   ├── validate_nav_sync.py           # docs/ tree ↔ mkdocs.yml nav
│   ├── validate_lecture_schema.py     # Lecture header/front-matter contract
│   ├── validate_clo_mappings.py       # objectives ↔ CLO ↔ module consistency
│   ├── validate_accessibility.py      # headings, alt text, link text
│   ├── validate_terminology.py        # terminology/consistency checks
│   ├── check_instructor_exclusion.py  # instructor-leak guard
│   ├── validate_teaching_blueprint.py # Blueprint table schema, hours, CLO parity
│   ├── validate_slide_decks.py        # PROMPT 04: deck grammar + per-lecture coverage
│   ├── validate_lab_workbook.py       # PROMPT 05: workbook + handout contracts
│   ├── validate_case_bank.py          # PROMPT 06: 100-case bank + private solutions parity + leak scan
│   ├── validate_assessment_pack.py    # PROMPT 07: framework/bank/blueprints/rubrics + draft-paper contract
│   ├── validate_site_integrity.py     # PROMPT 08: duplicate anchors/IDs, lecture presence, calendar, built-output leak scan
│   ├── generate_semester_calendar.py  # PROMPT 08: builds docs/schedule-calendar.md from semester.yml
│   └── run_all_checks.py              # Runs everything; CI entry point (12 checks)
    #   validate_lecture_schema.py also enforces the PROMPT 03 teaching-material
    #   contract: NN.0 bridge, Visual explanation + Figure alt text, Summary,
    #   Homework, module-guide presence, answer-leak scan.
│
├── tests/
│   └── expectations.json              # Machine-readable course inventory for validators
│
└── .github/workflows/
    ├── ci.yml                         # Validators + strict build on all pushes/PRs
    └── deploy-pages.yml               # Publish site from main (GitHub Pages)
```

## 3. Coverage traceability (brief requirement → lectures)

Every topic mandated in the course brief maps to at least one lecture; no major ICT topic is silently omitted.

| Required topic | Lecture(s) |
|---|---|
| Computer fundamentals and evolution | L01, L02 |
| Types and applications of computers | L03 |
| Hardware components and architecture | L05 |
| CPU, memory, storage, peripherals | L06, L07, L08 |
| System software and application software | L09 |
| Operating system fundamentals | L10 |
| File systems and file management | L11 |
| Software installation, updates, troubleshooting | L12 |
| Number systems and data representation | L13, L14 |
| Character encoding and multimedia | L15, L16 |
| Boolean logic and digital logic fundamentals | L17, L18 |
| Productivity tools and digital workflows | L19, L20 |
| Computer networking concepts | L21 |
| Internet and World Wide Web | L22, L23 |
| Cloud computing and virtualization | L24 |
| Databases and information systems | L25 |
| Data science computing foundations | L26 |
| AI and responsible AI literacy | L27, L28 |
| Cybersecurity, privacy, digital citizenship | L29, L30 |
| Computational thinking and problem solving | L31 |
| Emerging technologies and social implications | L32 (plus L04) |
| Practical integrated projects | L08 assign → L16/L24 milestones → L32 showcase |

## 4. Naming conventions summary

| Artefact | Pattern | Example |
|---|---|---|
| Lecture page | `L{NN}-{kebab-slug}.md` | `L13-number-systems.md` |
| Module page | `module-{NN}-{kebab-slug}.md` | `module-04-data-representation.md` |
| Lab | `lab-{NN}-{kebab-slug}.md` | `lab-03-file-system-scavenger-hunt.md` |
| Activity | `activity-{N}-{kebab-slug}.md` | `activity-2-number-system-relay.md` |
| Case study | `case-study-{NN}-{kebab-slug}.md` | `case-study-04-ransomware-response.md` |
| Quiz | `quiz-{NN}.md` | `quiz-01.md` |
| Validator script | `validate_*.py` / `check_*.py` | `validate_nav_sync.py` |

Full rules: `docs-meta/04-documentation-standards.md`.

## 5. Boundaries and guards

| Boundary | Enforcement |
|---|---|
| `instructor/` never published | Not under `docs/`; not in nav; `check_instructor_exclusion.py` scans docs for links/mentions; CI fails on violation |
| `docs-meta/` not in student nav | Design docs live outside `docs/`; not referenced from public pages |
| No answer keys on public site | Keys for **graded** quizzes/exams only under `instructor/answer-keys/`; public practice quizzes may include collapsible self-check answers **for distinct questions** written separately from graded items |
| Safe cybersecurity content | L29/L30 and Lab 8 use simulated, authorized, educational scenarios only; misuse explicitly out of scope |
