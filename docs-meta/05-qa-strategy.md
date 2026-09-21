# QA Strategy

**Version:** 1.0 · **Date:** 2026-09-18
Quality assurance runs at two layers: fast structural validators (Python stdlib) and a real site build (`mkdocs build --strict`). Both run locally and in CI; both must pass before publication.

---

## 1. Validators (scripts/)

| Script | Checks | Failure mode |
|---|---|---|
| `validate_nav_sync.py` | Every file under `docs/**/*.md` (except explicitly whitelisted non-site drafts) appears exactly once in `mkdocs.yml` nav; every nav entry exists on disk | Non-zero exit with file list |
| `validate_lecture_schema.py` | Each of the 32 lectures: front-matter (`lecture`, `module`, `title`, `stage`, `outcomes`), single `h1` matching `LNN — Title`, required sections present (Learning objectives, Key terms, Common misconceptions, Check your understanding, References, Looking ahead), 3–5 objectives, ≥2 misconceptions, 3–5 check questions. **PROMPT 03 additions:** prerequisites/motivation bridge (`NN.0 Before we start`), `Visual explanation` with a Mermaid diagram *and* a `*Figure: …*` text alternative, non-stub `Summary` and `Homework`, 8 instructor module guides present, and an answer-key leak scan (`Answer:`, `Marking scheme:`, …) over student-facing pages | Per-lecture defect report |
| `validate_clo_mappings.py` | Front-matter `outcomes` ids all exist in the CLO catalogue; module pages reference exactly their lectures; lecture numbering gap-free L01–L32; module ranges match architecture | Consistency report |
| `validate_accessibility.py` | Every image has descriptive alt text; no bare-URL or "click here" links; heading levels never skip; tables include header separators | Per-file defect list |
| `validate_terminology.py` | No TODO/TBD/FIXME markers outside `docs-meta/`; forbidden patterns (e.g., "click here"); glossary terms appear bolded at first use spot-checks | Terminology report |
| `check_instructor_exclusion.py` | No file under `docs/` mentions `instructor/` paths; `mkdocs.yml` nav contains no instructor entries; `instructor/` exists outside `docs/` | Hard fail (privacy guard) |
| `validate_teaching_blueprint.py` | Blueprint (07): 32 lecture rows × 16 columns; total 64 contact hours; 8 module blocks; session phases per lecture; row CLOs match lecture front-matter `outcomes`; every quiz in `docs/schedule.md` is referenced in the assessment blueprint (08); no duplicate lecture-objective lines | Consistency report |
| `validate_slide_decks.py` | PROMPT 04 decks: 8 module files; per-lecture section + title slide for L01–L32; run sheet stating 120 min; ≥11 slides with clean S-numbering; required kinds (Today/Objectives, Activity, Quick check, Summary, Exit ticket as final slide); `**Notes:**` with `[~m]` target and TALK cue (TRAN on all non-final slides); answer-key leak scan | Grammar report |
| `validate_lab_workbook.py` | PROMPT 05 labs: workbook hub lists exactly Labs 1–8 + SB-1–4; 22-area coverage matrix rows 1..22; 60/25/15 rubric; safety rules + fallbacks sections; per-handout front-matter (lab/title/assigned/due) and section contract (Purpose, Before you start, Expected observations & troubleshooting, accessibility paragraph, questions, Submission checklist with items, Grading); builder front-matter (SB-N/related/duration/graded:false) and compact contract | Contract report |
| `validate_case_bank.py` | PROMPT 06 bank: 4 public level files × 25 cases; unique IDs across the bank; ID↔level agreement (file, ID prefix, heading label); 12 required student-facing fields per case, non-stub (per-field thresholds); numbered Discussion questions; index→case ID consistency and level-table completeness; 4 private solution banks with exact ID parity and Solution-guide/Common-mistakes blocks; solution-leak scan on public files; CS-\* graded case studies not absorbed into the PB-\* bank | Contract report |
| `validate_assessment_pack.py` | PROMPT 07: framework hub lists all 9 assessment types with proposed-weight marks and the 100% sum; question bank = 46 tagged questions across 10 types with non-stub `<details>` model answers and no duplicate titles; blueprint pages carry marks/timing but zero model-answer/marking-scheme content (public leak scan); rubrics pack has 7 transversal rubrics + links to specialized ones; private draft papers (outside docs/) hold per-item marking schemes, model answers, time-allocation, integrity notes | Contract report |
| `validate_site_integrity.py` | PROMPT 08: 32 lecture pages with unique IDs/titles (duplicate-identifier check); no duplicate H2 anchor slugs per page; unique mkdocs nav entries; generated calendar exists, maps all 32 sessions, its lecture links resolve; core meta pages present (index/syllabus/schedule/accessibility/pathway/help); **built-output leak scan** over all `site/` HTML (instructor paths, answer keys, marking schemes — context-aware for benign policy statements) | Contract report |
| `run_all_checks.py` | Orchestrates all of the above; prints summary; exits non-zero if any fail | CI entry point |

Design rules: stdlib only (no PyYAML dependency — the nav parser is a minimal YAML subset reader scoped to our own file); idempotent; readable messages with file:line.

## 2. Build validation (Layer 2)

- `python -m venv .venv` → `pip install -r requirements.txt` → `mkdocs build --strict`.
- Strict mode treats warnings as errors: broken links, missing pages, malformed nav all fail.
- `mkdocs serve` for local preview; the built `site/` directory is disposable (git-ignored).

## 3. CI/CD design (.github/workflows/)

| Workflow | Trigger | Steps |
|---|---|---|
| `ci.yml` | All pushes and PRs | Set up Python 3.12 → install pinned requirements → `run_all_checks.py` → `mkdocs build --strict` |
| `deploy-pages.yml` | Push to `main` (after CI passes) | Build site → upload `site/` artefact → `actions/deploy-pages` |

- Pages source must be set to **GitHub Actions** in repository settings (instructor one-time step).
- The instructor-leak guard runs in CI *before* deploy, so a leaked key can never reach the public site even if a local check was skipped.

## 4. Manual QA checklist (per release)

PROMPT 03 content QA (in addition to the mechanical checks below):
- Skim each new lecture diagram's *Figure:* line as a reader: does it stand alone if the image fails?
- Confirm instructor guides' exit-ticket answers were not copied into any `docs/` page (the automated leak scan is line-shape based; human skim is the second layer).
- Check one lecture per module end-to-end as a student would: prerequisites → body → summary → homework.

1. Run `python scripts/run_all_checks.py` — all green.
2. Run `mkdocs serve`; walk the nav: home → each module → 3 sampled lectures → labs → assessment.
3. Spot-check one lecture page: objectives↔CLO mapping, misconceptions, no answers in "Check your understanding".
4. Verify no instructor content appears in the built `site/` (search the output for a known key phrase from `instructor/`).
5. Confirm all external links open and are still authoritative (quarterly).

## 5. Known QA limitations (honest scope)

- Validators check structure and conventions, not pedagogical accuracy — citation verification and factual review remain a human instructor task.
- The nav parser reads our own simple `mkdocs.yml` nav format; complex YAML features (anchors, inheritance) are out of scope by design.
- Accessibility validation is automated for the enforceable subset (alt text, headings, links); full WCAG conformance needs periodic manual/assistive-tech review.
- Link rot in external references is checked quarterly by hand, not continuously.
