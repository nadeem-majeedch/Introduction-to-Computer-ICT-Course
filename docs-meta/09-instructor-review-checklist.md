# Instructor Review Checklist

**Companion to:** `07-teaching-blueprint.md` + `08-assessment-blueprint.md` · **Version:** 1.0 · **Date:** 2026-09-19
Use this checklist to review the blueprint set before the semester starts and to run the course week by week. Machine-validated items are marked ✅ with the exact evidence; human-review items are marked 👁. Re-run the two commands below any time you edit anything.

---

## 1. Ten-point validation rubric

| # | Required check | Evidence source | Status |
|---|---|---|---|
| 1 | **Exactly 32 lectures** | Teaching-plan tables in `07-teaching-blueprint.md` §2–3 hold exactly 32 lecture rows, L01–L32, no gaps or duplicates; re-checked automatically by `scripts/validate_teaching_blueprint.py` inside `run_all_checks.py` | ✅ 32/32, machine-checked |
| 2 | **Exactly 64 contact hours** | Same tables sum to 32 × 2 h = 64 h; validator asserts the total and each row's 2 h duration; every session follows the §1 template within load discipline (max two concept blocks) | ✅ 64/64, machine-checked |
| 3 | **No major topic gaps** | `07` §4 completeness table: 16 mandated strands each mapped to lecture ranges (including practical computer literacy and the integrated project thread); `02-repository-plan.md` §3 topic traceability table | ✅ 16/16 strands covered |
| 4 | **No duplicate lecture objectives** | Blueprint objective cells are unique across all 32 rows (validator flags duplicates); lecture-page objectives are lecture-specific, with shared strands written as progressions (security L12→L23→L29→L30; productivity L19 vs L20; logic L17 vs L18) | ✅ 0 duplicates, machine-checked |
| 5 | **Appropriate first-semester difficulty** | Stage gating (Stages 1–2 through week 8, Stages 3–4 after midterm — `07` §6); load discipline (`07` §1); no-reorder dependency list; CI gate: `mkdocs build --strict` on every push/PR (`.github/workflows/ci.yml`) | ✅ structure machine-checked · 👁 pacing feel during delivery |
| 6 | **Prerequisite relationships documented** | Dependency map `07` §6 with hard dependencies marked "do not reorder" (L05→L06–L08; L13→L14–L18; L17→L18; L21→L22–L24; L25→L26; L27→L28; L29→L30; L31→L32) and soft dependencies noted | ✅ |
| 7 | **Assessment coverage of all CLOs** | `08-assessment-blueprint.md` §3 CLO-to-assessment matrix: every CLO has primary (●) evidence in ≥2 graded components; Bloom-alignment check in same section; item banks tagged to the matrix | ✅ 11/11 CLOs, machine-checked |
| 8 | **Proposed weightings marked, not silently assumed** | `08` §1: every component row carries "Proposed — OQ-13"; participation component is 0%/decision-required; sum = 100% only under option (a); OQ-13 recorded in `06-open-questions.md` | ✅ all six components flagged |
| 9 | **Student/instructor separation intact** | Blueprint set lives in `docs-meta/` (outside `docs/` and the published nav); leak guard `check_instructor_exclusion.py` scans `docs/`; answer keys and exam banks remain under `instructor/` only | ✅ validator green |
| 10 | **Student-site parity** | Objectives, vocabulary, and CLO cells in `07` are condensed from the published lecture pages; `docs/schedule.md` and the 8 module pages restate the same plan; validator enforces CLO parity between blueprint rows and lecture front-matter | ✅ parity machine-checked |

**Machine-check gate:** `python scripts/run_all_checks.py` (7 validators) and, in the pinned venv, `mkdocs build --strict`. Both green before any commit.

## 2. Before first lecture

1. Resolve the publication blockers **OQ-01** (repo visibility), **OQ-05** (license), **OQ-06** (repo name/URL) in `06-open-questions.md`.
2. Decide **OQ-13** (participation component). If option (b) or (c): rebalance `docs/assessment.md` + `docs/syllabus.md`, update the `08` §3 matrix, re-run both validation commands.
3. Review the 32 plan rows and module MLO headers in `07`; pre-decide any trims using the §5 trim order (never trim formative segments, lab kickoffs, or milestone checkpoints).
4. Confirm **OQ-04** (textbook edition); adjust the `Prepare` column sources in `docs/schedule.md` if it changes.
5. Print/handle A1–A5 materials; test projector, logic simulator, browser DevTools, and DB Browser for SQLite; list software students must install (Lab 1 covers it).
6. Run `python scripts/run_all_checks.py` and the venv strict build; file any failure before week 1.

## 3. During the semester

- **Weekly:** deliver per the blueprint row (segments and time boxes in `07` §1); collect exit tickets; assign the row's homework.
- **Quizzes:** announce in lecture, grade from `instructor/answer-keys/quiz-answer-keys.md` — keys never move into `docs/`. Adjust cadence (OQ-08) in weeks 1–3 and record the resolution.
- **Labs:** assigned/due per `docs/labs/index.md`; lab platforms per OQ-09.
- **Project milestones:** proposal L16 → design L24 → working check (Module-7 week) → showcase L32; grading per `docs/assessments/project/milestones.md`.
- **End of term:** archive this checklist with resolutions recorded in `06-open-questions.md`.

**Value:** one operational instrument ties every remaining human-review item to its evidence; the machine-checkable items above are already green, so instructor judgment concentrates on the 👁 items that genuinely require a person.
