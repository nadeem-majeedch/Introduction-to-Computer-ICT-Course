# Lab Grading Notes and Expected Outcomes (Labs 1–8)

**Instructor-only.** Public lab handouts carry criteria; this file carries expected outcomes, discriminators between excellent/developing work, and integrity watch-points.

---

## Lab 1 — Digital Basics and System Orientation

**Expected:** system info screenshots match the claimed machine; folder tree exactly as specified; eight-device table with at least one defended "N" and at least one embedded system.
**Discriminator (excellent):** processing evidence is *observable behaviour*, not restated specifications.
**Watch for:** screenshot recycling between classmates (compare serials/uptime); the "N" device is usually a kettle — accept only argued cases.

## Lab 2 — Hardware Inventory and Benchmarking

**Expected:** inventory from real OS tools (cross-checkable); hierarchy experiment with environment notes (background load, thermal state); recommendations cite *workload* properties.
**Discriminator:** the fair-test design — variables named and held constant; anomalies reported, not deleted.
**Watch for:** invented timings (check plausibility vs hardware class); recommendations that cite price as a technical justification.

## Lab 3 — File System Scavenger Hunt

**Expected:** paths verified by navigation; CLI transcript complete (copy-paste text, not retype); mojibake-free; 3-2-1 table with a *named offsite*.
**Discriminator:** the "which paths break on rename" question answered *before* renaming — thinking-first is visible.
**Watch for:** transcripts that don't match the student's OS (lab-machine transcripts handed in as personal work); backup plans naming "the cloud" generically with no provider/mode.

## Lab 4 — Number Systems Workshop

**Expected:** all Part 1 work shown; two's-complement drills with causes; forensics report with actual byte values.
**Discriminator:** overflow items name the *specific lost carry/borrow*; forensics distinguishes bytes from display.
**Watch for:** calculator-first answers dressed as hand work (method marks handle this); identical timing logs across submissions (record a per-section baseline).

## Lab 5 — Logic Circuit Simulator

**Expected:** four-row XOR verification; half adder four-row verification; paper sketch precedes build.
**Discriminator:** full-adder bonus verified across all eight rows, not just two.
**Watch for:** shared simulator links from one account (check edit history if suspicious); screenshots without visible input states.

## Lab 6 — Spreadsheet Data Workshop

**Expected:** cleaning documented in the note column; threshold block *drives* the IF logic; one honest chart + the deliberate lying twin with caption.
**Discriminator:** the threshold-block design — grades recompute when thresholds change (ask for the before/after screenshot).
**Watch for:** hardcoded grades instead of formulas (click a cell during grading); lying-chart captions that describe rather than explain the deception.

## Lab 7 — Networking and Cloud Lab

**Expected:** private/public IP explanation correct (NAT/router role); DNS evidence with responding server; teardown screenshots final.
**Discriminator:** the traceroute "missing hops are normal" sentence — students who assume failure misread output.
**Watch for:** public IPs of dorm-mates' machines (privacy); teardown omission (grade the teardown explicitly); certificate fields copied from the wrong site.

## Lab 8 — Security Habits Lab

**Expected:** credential table with NO passwords recorded (check!); MFA settings-page screenshots only; test-restore evidence; AI-tool settings answered specifically.
**Discriminator:** the personal security plan has *triggers* ("when X, I do Y") rather than intentions.
**Watch for:** any submission containing a real password → immediate integrity conversation per syllabus; MFA screenshots containing live codes/QRs (instruct immediate rotation if seen).

---

## Skill Builders (SB-1–SB-4) — completion-marked practice

Feedback-only items (not weighted). One "excellent-descriptor" sentence of feedback per submission; misconceptions migrate to the calibration notes below like graded labs do.

## SB-1 — Software Installation and Package Awareness

**Expected:** three-channel inventory with vet-source named per channel; installer-reading sentences that treat option screens as *claims*; a personalized post-install routine (not the generic list).
**Discriminator:** the update-control answer names the cost of control (manual updates = responsibility).
**Watch for:** students completing the installer anyway — the task says open, not complete; sandbox it if machines allow.

## SB-2 — Database Thinking with Flat Tables

**Expected:** PK justified by uniqueness-and-not-empty; the orphan row found; hand-join result correct (filter → project → match); three violations each naming its refusing concept.
**Discriminator:** the SQL-shaped pseudocode uses JOIN semantics, not just WHERE — a real match condition.
**Watch for:** `name` proposed as PK without failure cases; formula-heavy approaches that re-create the spreadsheet-as-database problem.

## SB-3 — Computational Thinking Gym

**Expected:** decompositions separate inputs/outputs/rules; card B flowchart has closure (no dangling paths); card C pseudocode handles 23 (the 5×4+1×3 edge); bug isolation names the *step*, not a guess.
**Discriminator:** the one-input-testing reflection says "one passing input proves only that input" in the student's own words.
**Watch for:** seeded-bug users copying the diagnosis from neighbours — the isolation *note* is individual even when the pseudocode is shared.

## SB-4 — Responsible AI Use Trial

**Expected:** audit lines cite the tool's own docs/settings; per-sentence verification marks (verified/corrected/unverifiable) with named sources; disclosure block matches the rubric's four parts.
**Discriminator:** "nothing wrong found" submissions that still list per-claim sources — earned negative results only.
**Watch for:** personal data pasted into external tools (the setup rule forbids it — treat as an integrity conversation); disclosure blocks copied from the builder's own example verbatim.

---

## Calibration notes

- Grade with the public criteria open; this file is for expectations, not secret criteria.
- Semester-end: migrate recurring misconceptions into lecture "Common misconceptions" sections; retire lab items that this file had to over-explain.
