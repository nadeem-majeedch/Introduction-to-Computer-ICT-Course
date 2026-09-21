# Case-Study Bank QA Report — PROMPT 06

**Date:** 2026-09-19 · **Scope:** the 100-case problem-solving bank (`docs/case-bank/`) and its private solution companion (`instructor/case-bank-solutions/`)

---

## 1. Deliverable map

| PROMPT 06 deliverable | Location | Status |
|---|---|---|
| Student-facing case bank (100 cases, 4 levels) | `docs/case-bank/level-1.md` … `level-4.md` — 25 cases each, PB-101…PB-425 | ✅ Built |
| Case-study index (method, progression, domain matrix, rubric, mappings) | `docs/case-bank/index.md` | ✅ Built |
| Difficulty progression map | `index.md` §5 (progression diagram + level-placement rules the validator's level checks enforce) | ✅ Built |
| Lecture-to-case mapping | `index.md` §8 anchor table + every case's **Related lectures** field (validated: IDs referenced by the index exist in the bank) | ✅ Built |
| Learning-outcome mapping | `index.md` §7 (12 problem-solving skills → practise-from / master-by case ranges) | ✅ Built |
| Assessment rubric (all levels) | `index.md` §9 (six criteria, weights, level-adjustment rule) | ✅ Built |
| Instructor-only solution bank | `instructor/case-bank-solutions/level-1…4.md` — one solution entry per case: **Solution guide / Alternatives / Trade-offs / Common mistakes** (fields 15–18 of the 22-field teaching template) | ✅ Built, outside `docs/` |
| Case-study QA report | this file | ✅ This file |

**Relationship to the graded case studies (CS-01–04):** preserved untouched. The CS-* lecture-linked graded cases keep their own IDs, files, and assessment role; the PB-* bank is a separate practice/teaching resource and the validator rejects any PB- ID appearing in `docs/case-studies/`.

## 2. Template compliance (the 22-field contract)

- **Public fields (1–14, 19–22):** unique ID, level, title, domain, related lectures, scenario, problem statement, stakeholders, learning objectives, constraints, available information, student task, suggested thinking time, expected solution characteristics, discussion questions, extension challenge, references — all present in every case, enforced mechanically (12 required fields checked per case with per-field stub thresholds; Discussion questions must be a numbered list).
- **Private fields (15–18):** instructor solution guide, alternative solutions, trade-offs, common mistakes — present in every entry of the private solution files (Solution-guide/Common-mistakes blocks checked per case; parity enforced: exactly 25 entries per level, IDs matching the public file).
- **Public/private split:** the public *Expected solution characteristics* field deliberately describes the *shape* of good reasoning without stating a verdict; verdicts, alternatives, and trade-off analyses exist only in `instructor/`. The structural leak scan (solution-bearing bold markers, "answer key:") runs on all public bank files.

## 3. Scale, progression, and domain coverage

- **Exactly 100 cases** — 4 levels × 25 (validator enforces the count and rejects duplicates bank-wide).
- **Progression spine:** L1 understand → L2 decompose & compare → L3 criteria-first justification → L4 interacting-constraint design with named sacrifices. Level placement rules live in `index.md` §5; the validator enforces ID↔level agreement three ways (file placement, ID prefix, heading label).
- **Domain coverage:** all 23 prompt-required domains (incl. healthcare *conceptual*, university administration, small business, education technology, public service, accessibility, sustainability, ethics) — matrix in `index.md` §4. Fictional/generalized scenarios are marked as such; sensitive domains (PB-216 clinic, PB-402 clinic network, PB-411 hospital, PB-421 NGO) carry explicit fictional-content notes.

## 4. Validation performed (this repository)

| Check | Result |
|---|---|
| New 10th validator `validate_case_bank.py` (wired into `run_all_checks.py`; expectations updated: `case_bank_levels: 4`, `case_bank_cases: 100`) | PASS |
| Full suite — **10/10 checks** (nav sync incl. 5 new nav entries, lecture schema, CLO, accessibility, terminology, leak guard, blueprint, decks, labs, case bank) | PASS |
| `mkdocs build --strict` | Clean; one real anchor defect found and fixed during the run (`level-1.md` → rubric anchor slug) |
| Leak guard (`check_instructor_exclusion.py`) | PASS — 28 private files, zero `instructor/` references in `docs/` (one real leak found in the index's §6 wording and fixed) |
| Nav sync | PASS — Problem Bank section added to `mkdocs.yml` (index + 4 levels) |
| Validator self-catch during build | Field parser initially mis-modeled the compact `**Constraints:**`/thinking-time formats → corrected; two real field gaps found and filled (PB-223 *Available information*, PB-418 *Learning objectives*) |

**Not performed here (and not claimed):** classroom trialling of cases, instructor vetting of solution-guide verdicts, timing calibration of the thinking-time values, and any external reference verification beyond the course's established citation policy (course pages + published reference list; fast-moving factual areas supply their facts internally and flag themselves).

## 5. Warnings and instructor-review items

1. **Solution-guide vetting is a human step.** The validator proves structure and parity, not pedagogical correctness. Instructors should skim all 100 guides once before first classroom use — the open-verdict cases (PB-215, PB-306, PB-310, PB-314, PB-417, PB-419, PB-421) especially, where the guide itself says the verdict is instructor-framing.
2. **Thinking times are estimates** (8–35 min by level); calibrate against the first cohort.
3. **Case↔nav coupling:** the bank index's lecture anchors are a curated subset; the full per-lecture linkage lives in the cases' *Related lectures* fields. If lecture numbering ever changes, both the index table and the case fields need a sweep (the validator catches index→bank drift, not lecture-number drift).
4. **The 22-field template is enforced in two files by design** — public files carry fields 1–14/19–22, private files carry 15–18. If the template is ever extended, extend the validator's `REQUIRED_FIELDS` and the solution-parity checks together.
5. **Pre-existing open items carry forward:** L16 reference [2] substitution; MkDocs 2.0 upstream banner; and the PROMPT 01 publication blockers OQ-01/05/06 (repo visibility, license, repo name) — still gating first publication.
6. **Git untouched:** nothing committed, nothing pushed.

## 6. Quick reuse guide for instructors

- Classroom method (8-step pattern + timing table): `index.md` §3.
- Assigning by level: level placement rules, §5; rubric, §9.
- Finding a case for a lecture: anchor table, §8, or search the level files for the lecture number in *Related lectures*.
- Solution access: `instructor/case-bank-solutions/` (repo access required; never paste into the site or the LMS).
