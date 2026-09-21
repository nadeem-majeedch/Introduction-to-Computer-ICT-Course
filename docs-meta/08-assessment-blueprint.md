# Assessment Blueprint — Outcomes, Instruments, and Matrices

**Companion to:** `07-teaching-blueprint.md` · **Version:** 1.0 · **Date:** 2026-09-19
**Instructor-review rule:** every weighting in this document is **proposed** and already published on the student site as provisional (`docs/assessment.md`, `docs/syllabus.md`). Institutional weightings, grading scale, and any participation/assignment component require instructor sign-off **before** the schedule is locked (tracked as OQ-13). Nothing here changes graded instruments or keys: those live only in `instructor/`.

---

## 1. Proposed assessment plan

| # | Component | Proposed weight | Format | Timing | Primary evidence | Review status |
|---|---|---|---|---|---|---|
| 1 | Quizzes (best 10 of 14) | **15%** | 5–10 min, 4–6 short questions on the two most recent lectures; graded from `instructor/answer-keys/quiz-answer-keys.md` | Weekly in-lecture, weeks 1–15 (schedule: Q01–Q14) | Recall + short application of lecture objectives | Proposed — OQ-08 cadence, OQ-13 weights |
| 2 | Labs (8 graded practical tasks) | **20%** | Self-contained handouts; criteria published per lab (60/25/15: tasks / artifact / reflection) | One per module; due dates in `docs/labs/index.md` | Working artifacts + reflections | Proposed — OQ-13 weights, OQ-09 platforms |
| 3 | Midterm examination | **20%** | In-class: short conceptual questions + small worked problems (conversion, truth table, file-task description); assembled from `instructor/exams/midterm-exam-bank.md` | Week 9, after L16; covers Modules 1–4 (L01–L16) | Individual demonstration of Stages 1–2 skills | Proposed — OQ-13 weights |
| 4 | Integrated project | **25%** | Proposal (1 p., L16) → design doc + flowchart (2–3 pp., L24) → 5-min working demo (Module-7 week) → live showcase + 6–10 p. report (L32); rubric in `docs/assessments/project/rubric.md` | L08 assigned → L32 showcase | Synthesis artifact (CLO-11) integrating four modules | Proposed — OQ-10 pairing, OQ-13 weights |
| 5 | Final examination | **20%** | Comprehensive; emphasis on Modules 5–8; conceptual + small problems + one scenario-response (security or AI literacy); assembled from `instructor/exams/final-exam-bank.md` | University-scheduled exam period | Cumulative retention + Stage 4 evaluation | Proposed — OQ-13 weights |
| 6 | Formative participation | **0% proposed / decision required** | Exit tickets, activity artifacts (A1–A5), peer-feedback slips, troubleshooting logs, ungraded drafts | Continuous | Feedback loop only; no grade | **OQ-13:** instructor chooses (a) keep ungraded, (b) add 5% participation and rebalance, (c) fold into quiz score via attendance-corrected best-10 |

**Assignment/independent-learning tasks** (career mini-report L04, licence audit L09, troubleshooting log L12, conversion drills L13–L14, credibility audit L23, dataset cleaning L26, AI-verification log L28, footprint audit L30) are deliberately **ungraded feeds**: they prepare quizzes, labs, and exam items. If the instructor wants a graded *Assignments* component, OQ-13 lists rebalancing options — do not grade them silently on top of 100%.

**Sum check:** 15 + 20 + 20 + 25 + 20 = **100%** under option (a) — the only configuration currently consistent with the published student pages. Any other option requires editing `docs/assessment.md` and `docs/syllabus.md` in the same change.

## 2. CLO-to-lecture matrix

Derived **exactly** from the `outcomes:` front-matter of the 32 lecture pages (`scripts/validate_teaching_blueprint.py` re-checks this parity on every run). A lecture appears under a CLO if it teaches or formally practises that outcome.

| CLO | Outcome (verb essence) | Lectures | Count |
|---|---|---|---|
| CLO-1 | Describe evolution; classify computers | L01, L02, L03, L04, L32 | 5 |
| CLO-2 | Explain von Neumann model and hardware roles | L05, L06, L07, L08, L32 | 5 |
| CLO-3 | Software stack; OS and file operations | L09, L10, L11, L12, L32 | 5 |
| CLO-4 | Base conversion; data encoding | L13, L14, L15, L16, L32 | 5 |
| CLO-5 | Truth tables; simple circuits | L17, L18, L32 | 3 |
| CLO-6 | Productivity tools and digital workflows | L19, L20, L26, L32 | 4 |
| CLO-7 | Networking, internet, web, cloud | L21, L22, L23, L24, L32 | 5 |
| CLO-8 | Relational databases; elementary queries | L25, L26, L32 | 3 |
| CLO-9 | Computational thinking; algorithm design | L31, L32 | 2 |
| CLO-10 | Security, privacy, ethics; AI-output evaluation | L04, L23, L26, L27, L28, L29, L30, L32 | 8 |
| CLO-11 | Integrated synthesis project (thread: assigned L08; milestones L16 and L24; showcase) | L32 | 1 |

Reading notes: CLO-10 is intentionally the most-spread outcome (ethics/security/verification recur across modules — each occurrence has distinct objectives, see `07-teaching-blueprint.md` §4). CLO-9 concentrates late by design (computational thinking after concrete artefacts exist). CLO-11 is the project thread culminating in L32, not a single-lecture outcome — its row records the milestone checkpoints.

## 3. CLO-to-assessment matrix

**Legend:** ● primary graded evidence · ○ secondary/synthetic evidence (sampled, not the component's focus) · A = activity/formatative, ungraded.

| Component (weight) | CLO-1 | CLO-2 | CLO-3 | CLO-4 | CLO-5 | CLO-6 | CLO-7 | CLO-8 | CLO-9 | CLO-10 | CLO-11 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Quizzes Q01–Q02 (→15%) | ● (Q01) · ○ (Q02) | | | | | | | | | ○ (Q02, via L04) | |
| Quizzes Q03–Q04 | | ● (both) | | | | | | | | | |
| Quizzes Q05–Q07 | | | ● (all three) | | | | | | | | |
| Quizzes Q08–Q09 | | | | ● (both) | | | | | | | |
| Quiz Q10 | | | | | ● | | | | | | |
| Quizzes Q11–Q12 | | | | | | ● (Q11) | ● (Q11, Q12) | | | ○ (Q12, via L23) | |
| Quizzes Q13–Q14 | | | | | | ○ (Q13) | | ● (Q13) | ○ (Q14, via L31) | ● (Q13, Q14) | |
| Labs 1–4 (→20%) | ● (Lab 1) | ● (Lab 2) | ● (Lab 3) | ● (Lab 4) | | | | | | | |
| Labs 5–8 | | | | | ● (Lab 5) | ● (Lab 6) | ● (Lab 7) | ○ (Lab 6 bridge) | | ● (Lab 8) | |
| Midterm (20%) | ● | ● | ● | ● | | | | | | ○ (via L04 ethics item) | |
| Integrated project (25%) | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ (M2 flowchart) | ○ (track-dependent) | ● |
| Final exam (20%) | ○ | ○ | ○ | ○ | ● | ● | ● | ● | ● | ● (scenario item) | ○ (synthesis question) |
| Formative (A1–A5, exit tickets, peer slips) | A | A | A | A (A2) | A (A3) | A | A (A4) | A | A (L31 peer review) | A (A5, audits) | A (peer-feedback slips) |

**Coverage guarantee (validated):** every CLO has **primary (●)** evidence in at least two graded components — CLO-1…CLO-4 via quizzes + lab + midterm; CLO-5…CLO-10 via quizzes + lab + final; CLO-11 via the project plus the final's synthesis item. No CLO relies on a single instrument.

**Bloom alignment check:** Understand-level CLOs (1, 2, 7) are sampled by recall-style quiz items and conceptual exam items; Apply/Analyze CLOs (3–6, 8–10) by lab artifacts and worked problems; Evaluate/Create CLOs (10's evaluation strand, 11) by the scenario-response exam item and the project showcase. Exam banks in `instructor/exams/` are tagged to this matrix so assembly preserves it.

## 4. Module learning outcomes → assessment

Module MLOs (published on each `docs/modules/module-0N-*.md` page and restated in `07-teaching-blueprint.md` §2–3) roll up to CLOs; assessment sampling per module:

| Module (lectures) | MLO CLOs | Graded sampling in the module window |
|---|---|---|
| M1 (L01–L04) | CLO-1, CLO-10 | Q01, Q02 · Lab 1 · A1 · midterm items |
| M2 (L05–L08) | CLO-2 | Q03, Q04 · Lab 2 · CS-01 (formative) · project assigned |
| M3 (L09–L12) | CLO-3 | Q05–Q07 · Lab 3 · troubleshooting log (feed) |
| M4 (L13–L16) | CLO-4 | Q08, Q09 · Lab 4 · A2 · midterm · milestone 1 |
| M5 (L17–L20) | CLO-5, CLO-6 | Q10, Q11 · Labs 5–6 · A3 |
| M6 (L21–L24) | CLO-7, CLO-10 | Q11, Q12 · Lab 7 · A4, CS-02 · milestone 2 |
| M7 (L25–L28) | CLO-8, CLO-6, CLO-10 | Q13 · CS-03 · Lab 8 assigned · milestone 3 demo |
| M8 (L29–L32) | CLO-9, CLO-10, CLO-11 | Q14 · A5, CS-04 · Lab 8 due · showcase + final report · final exam emphasis |

## 5. Blueprint validation hooks

`scripts/validate_teaching_blueprint.py` (added to `run_all_checks.py`) enforces:

1. Blueprint §2–3 teaching-plan tables contain exactly 32 lecture rows, numbered L01–L32 without gaps or duplicates.
2. Total scheduled time = 64 hours (32 × 2 h) and every row's duration parses as 2 h.
3. Every row's CLO-mapping cell equals that lecture's `outcomes:` front-matter in `docs/lectures/` (parity, order-insensitive).
4. Blueprint module blocks match `module_lecture_ranges` in `tests/expectations.json`.
5. Objective cells are unique across the 32 rows (no duplicated objective strings) — the "no duplicate lecture objectives" check.
6. Quiz coverage rows here match `docs/schedule.md`'s quiz plan strings.

Anything pedagogical beyond that (time-box quality, difficulty feel) is human review — see `09-instructor-review-checklist.md`.
