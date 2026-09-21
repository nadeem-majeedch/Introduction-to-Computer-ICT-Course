# Publication QA Report — PROMPT 08

**Date:** 2026-09-19 · **Scope:** website publication readiness — calendar, accessibility statement, learning pathway, breadcrumbs, site-integrity validation, README completeness, workflows.

---

## 1. Requirement coverage

| PROMPT 08 requirement | Where it lives | Status |
|---|---|---|
| Homepage · course overview · learning outcomes | `docs/index.md` (+ full CLO list on `syllabus.md`) | Pre-existing, verified |
| 32-lecture schedule | `docs/schedule.md` + **new generated calendar** `docs/schedule-calendar.md` | ✅ Extended |
| Module navigation · lecture notes · labs · case studies · assessments · references | Existing nav sections (Modules / Lectures / Labs / Case Studies / Problem Bank / Assessment Tools / References) | Pre-existing, verified |
| **Semester calendar, instructor-configurable** | `semester.yml` (start date, lecture weekdays, break weeks, holidays, lecture-anchored assessment milestones, per-session overrides) + `scripts/generate_semester_calendar.py` → published page + internal generation log | ✅ Built |
| **Accessibility information** | `docs/accessibility.md` (WCAG 2.1 AA target, built-in features, content accessibility, escalation routes, known limitations) | ✅ Built |
| Instructor information where appropriate | LMS/contact routing on `help.md`; instructor *materials* deliberately private | Pre-existing |
| **Search** | Material search plugin (`search.suggest` + `search.highlight`) | Pre-existing |
| **Breadcrumbs** | `navigation.path` feature — renders `md-path` trail on nested pages (verified in built HTML) | ✅ Enabled |
| **Learning pathway / progress** | `docs/pathway.md` — four-stage route map with unlocks, graded checkpoints per stage, recovery map | ✅ Built |
| Design (responsive, contrast, keyboard, print) | Material theme (responsive + WCAG-checked palettes + keyboard-complete), print-friendly pages, alt-text/Figure discipline enforced by validators | Pre-existing + statement |
| **Student/instructor separation + automated checks** | Leak guard (12 private files→28), answer-leak scans in 4 validators, **new built-output leak scan** over all published HTML | ✅ Extended |
| **Broken links / missing pages / duplicate identifiers** | Strict build (links/anchors) + nav-sync (orphans/missing) + **new `validate_site_integrity.py`** (duplicate lecture IDs/titles, duplicate H2 anchors per page, duplicate nav entries, 32-lecture presence, calendar mapping) | ✅ Extended |
| **GitHub Actions** | CI + deploy-pages workflows verified valid (YAML parse + step review); deploy gates on the full check suite; `.nojekyll` step; URLs configured (PROMPT 07's pass) | Pre-existing + hardening |
| **README** | Local setup, dependencies, build, preview, **testing** (12 validators + built-output scan), **Pages deployment**, manual commit/push, **troubleshooting table** (8 symptom→fix rows), calendar regeneration | ✅ Completed |

## 2. The semester calendar design

- **No hardcoded calendar.** `semester.yml` carries: `semester_start`, `lecture_days` (weekday pattern — any pattern, not just Mon/Wed), `break_weeks`, `holidays`, `lecture_count`, lecture-anchored `assessments` (milestone dates follow start-date shifts automatically), `session_overrides` for hall rebookings, and a `generated_on` control for COMPLETED/PLANNED status.
- **Generated, not hand-edited:** the published page carries its generation date and derivation note; the internal log (`docs-meta/semester-calendar-log.md`) carries the full session map for the instructor.
- **Verified:** generator produced 32 sessions over the placeholder Mon/Wed pattern with correct week numbering and 7 assessment milestones; `validate_site_integrity.py` enforces presence, session count, and link resolution on every future run.
- The shipped dates are a **placeholder start (2026-10-05)** — the instructor edits `semester.yml` and regenerates; the page itself says exactly that.

## 3. Validation performed

| Check | Result |
|---|---|
| New 12th validator `validate_site_integrity.py` wired into `run_all_checks.py` | PASS |
| Full suite — **12/12 checks** | PASS |
| `mkdocs build --strict` | Clean (104 pages); no new warnings/anchors |
| Breadcrumbs rendered | Verified (`md-path` nav present in built lecture pages) |
| Built-output leak scan | 102 HTML pages scanned; context-aware scanner passes (only benign policy statements match) |
| Workflow YAML parse | Both workflows valid; mkdocs.yml's `!!python/name` tags require the mkdocs loader (strict build is the parser verdict) |
| Terminology validator self-catch | It flagged a "click here" example *in the new accessibility page* — reworded; the validators demonstrably police new content too |

**Not performed here (and not claimed):** no real GitHub Pages deployment was observed — the deploy workflow is verified by inspection and local equivalence (same validators + same strict build the workflow runs), not by a live run. The instructor's push will be the first true deploy; the README documents the one-time Pages setting.

## 4. Warnings and instructor actions

1. **Calendar placeholder:** regenerate after setting the real semester start in `semester.yml` (command documented on the generated page and in the README).
2. **GitHub UI actions (unchanged from PROMPT 07):** Settings → Pages → Source: **GitHub Actions**; repo visibility (OQ-01) must be public for free Pages.
3. **OQ-05 (license)** remains open — the site footer states content is pending license decision.
4. **COMPLETED/PLANNED is a generation snapshot**, not live tracking; regenerate mid-semester if that distinction matters on the page.
5. **Git untouched** — nothing committed, nothing pushed.
