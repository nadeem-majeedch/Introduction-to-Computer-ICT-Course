# Assessment Package QA Report — PROMPT 07

**Date:** 2026-09-19 · **Scope:** the assessment system layer (`docs/assessments/` additions + `instructor/exams/` draft papers) built on top of the PROMPT 02 blueprint, the 14 practice quizzes, the 8 graded labs, and the PROMPT 06 case bank.

---

## 1. Deliverable map

| PROMPT 07 deliverable | Location | Public/Private | Status |
|---|---|---|---|
| Assessment framework (9 assessment types, proposed weightings flagged for approval, integrity rules) | `docs/assessments/index.md` | Public | ✅ |
| Question bank — 46 questions, 10 types, model answers | `docs/assessments/question-bank/` (index + `qb-m01-m04.md`, `qb-m05-m08.md`) | Public (answers are *practice* model answers by design) | ✅ |
| Exam blueprints (midterm + final: structure, marks, timing, difficulty mix, integrity) | `docs/assessments/exams/index.md` | Public — items and answers deliberately absent | ✅ |
| Rubrics (7 transversal + links to project/case/lab rubrics) | `docs/assessments/rubrics.md` | Public (criteria only) | ✅ |
| Midterm draft paper with marking schemes + model answers | `instructor/exams/midterm-draft-paper.md` | **Private** | ✅ |
| Final draft paper (two scenario variants) with marking schemes + model answers | `instructor/exams/final-draft-paper.md` | **Private** | ✅ |
| QA report | this file | Private (`docs-meta/` is not in the published nav) | ✅ |

**Relationship to existing instruments:** the PROMPT 02 item banks (`instructor/exams/*-exam-bank.md`) remain the pools; the draft papers are *assemblies* of those pools per the published blueprints. The 14 practice quizzes, lab handouts, project rubric, and case-bank rubric are untouched; the new framework hub links them rather than duplicating them.

## 2. Weighting policy (no invented official weightings)

All weights remain **proposed and marked for instructor approval** (OQ-13), exactly as published in the PROMPT 02 blueprint: quizzes 15 / labs 20 / midterm 20 / project 25 / final 20 = 100% under the only configuration consistent with the current student pages. The framework hub repeats this with a prominent approval warning; the exam blueprints carry no weighting claims beyond their own mark allocation.

## 3. Question-bank design (understanding over recall)

- **46 questions** (23 + 23) across the ten required types; every question carries a `Module · CLO · Difficulty n/4 · Type` tag line and a non-stub expandable model answer.
- **Difficulty distribution** mirrors the assessment spine: Modules 1–4 set skews 1–2/4 with a 3/4 tail (midterm profile); Modules 5–8 set skews 3/4 with a 4/4 band (final profile). Difficulty scale is aligned with the case-bank levels.
- **Understanding-first construction:** MC items ask *why* (distractors are defensible-sounding errors, not nonsense); T/F items require the reason; scenario/troubleshooting items have defensible-answer ranges with the model stating what a good answer *must contain*; two questions are explicitly **open-verdict** (Q21 dashboard, Q22 broadband) and say so.
- **Verification:** every model answer was written against the lecture content it tags (e.g., Q15 two's complement arithmetic and Q14 conversions were recomputed; the half-adder/NAND chains were hand-checked). The final paper's assembly notes require the same pre-print recomputation of B1/B6 — key validation is treated as the course's own named failure mode (PB-217).

## 4. Public/private separation (enforced, not conventional)

- Blueprint pages state sections, marks, timing, difficulty mix, and integrity rules — the validator's public-leak scan rejects `**Model` blocks, `Marking scheme:` lines, and the model-answer *phrase* on them.
- Draft papers live in `instructor/exams/` (outside `docs/`); the leak guard blocks `instructor/` path references from all public pages.
- Built-site scan: the only matches for answer-adjacent phrases in `site/` are the policy statements themselves ("Model answers and marking schemes are not published…"). No real answers exist in the published output.
- The question bank's `<details>` model answers are the designed exception — they are practice material, not graded keys; this is stated on the bank index's Answer-policy section.

## 5. Validation performed

| Check | Result |
|---|---|
| New 11th validator `validate_assessment_pack.py` (wired into `run_all_checks.py`) | PASS |
| Full suite — **11/11 checks** (nav sync incl. 8 new nav entries, lecture schema, CLO, accessibility, terminology, leak guard, blueprint, decks, labs, case bank, assessment pack) | PASS |
| `mkdocs build --strict` | Clean — one real dead anchor found and fixed during the run (framework hub → case-bank rubric anchor) |
| Question-count/type/duplicate checks | 46/46, all 10 types present (one retag applied), zero duplicate titles |
| Leak scans (validator + built-site grep) | PASS — no answer content in public output |
| CLO coverage of exams | Verified in both papers: midterm covers CLO-1–4 ×≥2; final covers CLO-5–10 with feeders for CLO-1–4 (matches the PROMPT 02 coverage guarantee) |

**Not performed here (and not claimed):** no items were sat by real students; difficulty calibration is design-intent, not empirical; the marking schemes are verified for *structure and answer correctness by the author*, and remain subject to the instructor's human moderation before first use.

## 6. Warnings and instructor-review items

1. **Human moderation before first use** — the validator proves structure; the instructor must review the draft papers' answer quality and marking-scheme generosity (especially the open-verdict scenario rubric) before printing.
2. **Draft papers are single assemblies** — per-sitting refresh should redraw Section A objective items from the banks; the papers note this in their integrity sections.
3. **Model-answer disputes are expected and healthy** — the bank index invites them; instructors should log corrections so the validator's next run sees the fixed text.
4. **Weightings remain OQ-13** — nothing in this package changes that; if the instructor rebalances, `docs/assessment.md` and `docs/syllabus.md` must change in the same edit (framework hub repeats this rule).
5. **Pre-existing open items carry forward:** L16 reference [2]; MkDocs 2.0 banner; OQ-01/05/06 (repo visibility, license, repo name) still gate first publication.
6. **Git untouched:** nothing committed, nothing pushed.
