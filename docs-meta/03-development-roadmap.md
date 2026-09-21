# Course Development Roadmap

**Version:** 1.0 · **Date:** 2026-09-18
This roadmap sequences the initial build and the instructor's ongoing workflow. Status markers reflect the initial scaffolding run and the PROMPT 02 teaching-blueprint extension.

---

## 1. Initial build sequence (this run)

| Stage | Scope | Validation gate | Status |
|---|---|---|---|
| 0 | Inspect repository; write inspection report | Report matches observed state | ✅ Done |
| 1 | Master architecture; repository plan; roadmap | Architecture covers all 15 required sections | ✅ Done |
| 2 | Standards, QA strategy, open-questions log | Standards cover every required domain | ✅ Done |
| 3 | Repo scaffolding: README, .gitignore, requirements, mkdocs.yml, workflows | YAML parses; nav complete | ✅ Done |
| 4 | Core pages: index, syllabus, schedule, assessment, help, glossary, references | Validators pass | ✅ Done |
| 5 | 8 module overview pages | Validators pass | ✅ Done |
| 6 | Lectures L01–L16 (Modules 1–4) | Lecture-schema validator | ✅ Done |
| 7 | Lectures L17–L32 (Modules 5–8) | Lecture-schema validator | ✅ Done |
| 8 | 8 labs + indexes | Lab schema; activity counts | ✅ Done |
| 9 | 5 activities + 4 case studies + indexes | Cross-reference checks | ✅ Done |
| 10 | Instructor materials (keys, exam banks) | Outside docs/; leak guard passes | ✅ Done |
| 11 | Validators + tests/expectations.json | run_all_checks.py green | ✅ Done |
| 12 | Full validation incl. mkdocs build --strict in venv | Zero warnings; zero orphans | ✅ Done (86 HTML pages built; strict build warning-free) |
| 13 | 32-lecture teaching blueprint (session phases, pacing, dependency map) | validate_teaching_blueprint.py green | ✅ Done (PROMPT 02: `docs-meta/07`) |
| 14 | Assessment blueprint + CLO matrices + instructor review checklist | Quiz-coverage parity; rubric checklist | ✅ Done (PROMPT 02: `docs-meta/08`, `docs-meta/09`) |
| 15 | Full teaching material: student sections on all 32 lectures (prerequisites, diagrams, summaries, homework) + 8 instructor module guides + validator extensions | Schema + leak scan + strict build green | ✅ Done (PROMPT 03; report in `docs-meta/10-content-coverage-report.md`) |
| 16 | Classroom delivery package: 32 slide decks with integrated speaker notes, run sheets, delivery guide, deck validator | validate_slide_decks.py green; 8/8 checks | ✅ Done (PROMPT 04; report in `docs-meta/11-delivery-package-report.md`) |
| 17 | Practical lab workbook: hub + per-handout contract completion (observations/troubleshooting/accessibility) + 4 skill builders + instructor delivery guide | validate_lab_workbook.py green; 9/9 checks | ✅ Done (PROMPT 05; report in `docs-meta/12-lab-workbook-report.md`) |
| 18 | Problem-solving case bank: 100 cases in 4 progressive levels (public) + 4 instructor solution banks (private) + bank index with method/rubric/mappings + bank validator | validate_case_bank.py green; 10/10 checks; strict build clean | ✅ Done (PROMPT 06; report in `docs-meta/13-case-bank-qa-report.md`) |
| 19 | Assessment package: public framework hub + 46-question bank + exam blueprints + 7 transversal rubrics (public); assembled draft papers with model answers + marking schemes (private) + validator | validate_assessment_pack.py green; 11/11 checks; strict build clean | ✅ Done (PROMPT 07; report in `docs-meta/14-assessment-qa-report.md`) |
| 20 | Publication pass: instructor-configurable semester calendar (semester.yml + generator + published page), accessibility statement, learning pathway, breadcrumbs, site-integrity validator (incl. built-output leak scan), README completion | validate_site_integrity.py green; 12/12 checks; strict build clean | ✅ Done (PROMPT 08; report in `docs-meta/15-publication-qa-report.md`) |
| 21 | Final integration audit: full test execution, independent content/consistency sweeps, findings register, workflow calendar-regeneration fix (F-01) | 12/12 checks; build clean; verdict recorded | ✅ Done (PROMPT 09; **PASS WITH WARNINGS** — report in `docs-meta/16-final-audit-report.md`) |

## 2. Instructor first-session checklist (git is untouched by the agent)

```bash
git init
git add -A
git commit -m "Initial course scaffold: Introduction to Computer (ICT)"
git remote add origin https://github.com/nadeem-majeedch/Introduction-to-Computer-ICT-Course.git
git branch -M main
git push -u origin main
```

Then, once, in GitHub web UI: **Settings → Pages → Source: GitHub Actions**. The site publishes to:
`https://nadeem-majeedch.github.io/Introduction-to-Computer-ICT-Course/`

Then, once, in GitHub web UI: **Settings → Pages → Source: GitHub Actions**.

## 3. Ongoing maintenance workflow

1. **Branch per change:** edit lecture/lab/quiz content on a branch; run `python scripts/run_all_checks.py` and `mkdocs serve` locally.
2. **Merge to main:** CI runs the same checks; the deploy workflow publishes on success.
3. **Semester refresh:** review schedule dates, due dates, and OQ decisions; update `docs/schedule.md`; re-run validators.
4. **Content corrections:** fix on the source page, then verify the citing lectures' reference blocks still hold.
5. **Versioning:** bump the version in `docs-meta/*.md` when architecture-level changes occur; keep lecture table, nav, and expectations.json in sync (validators enforce this).

## 4. Suggested content-extension backlog (post-launch, instructor's discretion)

- Video recordings per lecture with transcripts (accessibility §11 of architecture).
- Auto-graded practice quizzes with randomized question banks.
- Student-facing glossary expansions driven by semester questions.
- Localisation of key pages if the institution requires a second language.
- Optional "advanced tracks" sidebars for CS vs DS emphasis cohorts.
