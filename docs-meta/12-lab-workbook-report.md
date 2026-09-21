# Lab Workbook Report — PROMPT 05

**Version:** 1.0 · **Date:** 2026-09-19
Companion to the coverage (`10`) and delivery (`11`) reports. Maps the practical-lab deliverables to locations, states the machine-enforced contract, and — critically — states the **testing scope honestly**.

---

## 1. Deliverables map

| Required deliverable | Location |
|---|---|
| Practical lab workbook (student-facing) | `docs/labs/workbook.md` — mapping, 22-area matrix, consolidated rubric, safety rules, fallbacks |
| Per-lab required elements (14 per lab) | The 8 graded handouts: front-matter (number/lecture/title), Purpose + outcomes, Duration & prerequisites ("Before you start"), equipment, setup ("Before you start" / "Setup"), step-by-step tasks, **expected observations** (new), **questions** (existing reflection sections), **troubleshooting** (new), submission checklist, assessment rubric (handout + workbook), **accessibility alternatives** (new) |
| Skill builders (coverage gaps) | `docs/labs/sb-01…sb-04` — installation/package awareness (L12), database thinking (L25), computational thinking gym (L31), responsible AI trial (L27–28) |
| Instructor lab delivery guide | `instructor/lab-delivery/guide.md` — semester map, in-session flow, grading workflow, private notes pointers |
| Equipment & software checklist | `instructor/lab-delivery/guide.md` §4 (institutional pre-semester + student-side minimums; optional tools marked) |
| Lab validation checklist | `instructor/lab-delivery/guide.md` §5 (per-window pre-flight) + `scripts/validate_lab_workbook.py` (mechanical backstop) |
| Lab-to-lecture mapping | `docs/labs/workbook.md` §mapping (lecture ranges + durations + graded/practice status); consistent with `docs/labs/index.md` |
| Lab assessment rubric | `docs/labs/workbook.md` §rubric (60/25/15 consolidated; per-handout demonstration-weight pointers) |
| Instructor notes (private) | `instructor/answer-keys/lab-answer-notes.md` extended with SB-1–4 expected outcomes, discriminators, watch-points |

## 2. Coverage: all 22 areas, no silent omissions

The workbook's matrix assigns every required area to a named lab/builder/project. Eighteen were already delivered by the graded spine; **four gaps closed by skill builders**: file permissions (5), software installation/package awareness (6), database concepts (19), computational thinking (21). Builders are ungraded practice — the graded 8-lab structure that the schedule, blueprint, and validators enforce is untouched.

## 3. Machine-enforced contract (`validate_lab_workbook.py`, 9th check in CI)

1. Workbook hub lists exactly Labs 1–8 and SB-1–4.
2. Coverage matrix has rows exactly 1..22.
3. Consolidated rubric weights (60/25/15) present; Safety rules + Accessibility fallbacks sections present.
4. Every graded handout: front-matter (`lab`/`title`/`assigned`/`due`, lab number matches filename), Purpose, Before you start, **Expected observations and troubleshooting**, an `**Accessibility alternative:**` paragraph, a questions section, Submission checklist with items, Grading.
5. Every builder: front-matter (`SB-N`/`related`/`duration`/`graded: false`) and the compact contract (outcomes, prerequisites, tasks, observations, questions, troubleshooting, submission).

## 4. Testing scope — what was tested vs not (no-fabrication statement)

- **Machine-validated here:** workbook/handout structural contracts, mapping and matrix consistency, front-matter correctness, section presence, nav↔tree sync (validator), CLO/accessibility/terminology invariants (existing suite), strict MkDocs build of all new public pages.
- **Build-validated here:** all new pages render warning-free; no broken links introduced.
- **NOT tested here — and not claimed:** the logic simulators' current UIs, cloud providers' free-tier flows, spreadsheet menu paths, OS settings screens, and any timing claims. No lab environment exists in this repository, so no practical task was executed. Every handout was written to degrade gracefully (substitution + troubleshooting pattern), and the instructor validation checklist (`guide.md` §5) exists precisely because **only the instructor can run the pre-flight on a real lab image** — that checklist is the test that counts.

## 5. Warnings (for instructor review)

1. **Sample-file dependencies need term-start staging**: Lab 4's miscoded file, Lab 6's gradebook, SB-3's problem cards + seeded bug, SB-4's sample-output pack — all are instructor-distributed by design (so they can be refreshed per term); the delivery guide's map names the week for each.
2. **Cloud-provider drift**: Lab 7's free-tier instructions are provider-neutral by design; the sanctioned-platform list must be (re)published on the LMS each term.
3. **Platform settings screenshots (Lab 8) go stale fast** — the validation checklist requires re-taking them each term.
4. **SB files use a compact contract** (they are ungraded practice); if the instructor later wants them weighted, extend them to the full 14-element graded contract and flip `graded: true` — the validator will then enforce the full contract only if the file lists change (currently builders are checked against the compact contract).
5. Pre-existing open items carry forward (L16 reference [2]; OQ-01/05/06 before publication).

## 6. Sign-off

- `validate_lab_workbook.py`: PASS (8 handouts + 4 builders, 22 matrix rows)
- Full suite: **9/9 checks PASS**; `mkdocs build --strict` clean (site grew by 5 public pages: workbook + 4 builders — nav updated)
- No commit, no push — git untouched
