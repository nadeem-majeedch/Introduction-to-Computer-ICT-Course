# Lab Delivery Guide — Instructor

**Private instructor tree.** Companion to the public [Practical Lab Workbook](../../docs/labs/workbook.md) and the grading notes in `instructor/answer-keys/lab-answer-notes.md`. This guide covers *delivery*: what to prepare, what happens in session, and how grading flows.

---

## 1. Semester delivery map

| Week | Event | Your preparation |
|---|---|---|
| 1 | Lab 1 assigned (L01) | Confirm lab-machine image; upload any large-print/accessible formats |
| 2 | Lab 1 due | Grade with answer-notes Lab 1; note "N-device" quality for L02 discussion |
| 4 | Lab 2 due (assigned L06) | Verify timing-page (or stopwatch plan) works in the lab image; record a per-section baseline (answer-notes watch-point) |
| 6 | Lab 3 kickoff (L11) + due Week 6 end | Lab machines need full home-folder rights; prepare CLI transcripts examples per OS family |
| 7–8 | Lab 4 window (assigned L13) | **Create the miscoded sample file the day before** (handout Part 3); keep your byte-level key in the answer notes |
| 10 | Lab 5 in session (L18) | Test the chosen simulator on the lab image **and** offline fallback; seed one buggy circuit for the troubleshooting demo |
| 11 | Lab 6 start (L19) + due Week 11 end | Distribute the deliberately imperfect gradebook (three city spellings, impossible age, duplicate row — per handout); verify it loads in all three accepted tools |
| 12–13 | Lab 7 window (assigned L21) | Confirm the sanctioned cloud platform (or approved free tiers) is on the LMS; check lab-image network allows `nslookup`/`tracert` or prepare the in-browser visualizer |
| 15 | Lab 8 window opens | Refresh platform privacy-settings screenshots (they change often); confirm the report-phishing path on students' platform |
| 16 | Lab 8 due | Grade the security plans; watch for real passwords (answer-notes watch-point: immediate integrity conversation) |

**Skill builders (SB-1–SB-4):** ungraded, feedback-only. Assign SB-1 in Week 7 (L12), SB-2 in Week 14 (L25), SB-3 in Week 16 (L31), SB-4 in Week 15 (L27–L28 window). Each needs **no preparation except SB-3's problem cards** (and the seeded buggy pseudocode version).

## 2. In-session flow (for labs run in class: 5, 6, and kickoff 3)

1. **Read-aloud the safety note** for that lab (workbook §Safety) — one minute, every time; normalization matters.
2. **Demo the first step only.** Students who see step one done execute steps two-to-five; students who see everything done execute nothing.
3. **Circulate with the handout's expected observations** in hand — your circulating question is "what do you see?", not "are you stuck?".
4. **Troubleshooting section is teachable material, not an appendix**: when two+ pairs hit the same wall, stop the room and run that troubleshooting item live.
5. **Never hand out the answer notes' expected outcomes** — the public handouts' "you should see" paragraphs are the student-facing version; the private notes add discriminators and watch-points.

## 3. Grading workflow

1. Grade against the public criteria (workbook rubric: 60/25/15) with `lab-answer-notes.md` open for expectations and watch-points.
2. Method marks: where a handout says "show work," correct answers without method score half (already public — apply it uniformly).
3. Record one sentence per recurring misconception in the answer-notes' calibration section — those sentences become next revision's handout troubleshooting items.
4. Skill builders: completion mark + one "excellent-descriptor" sentence of feedback; no weights, no rubric bureaucracy.

## 4. Equipment and software checklist

**Before semester (institutional):**
- [ ] Lab machines: three OS-capable images or one with documented alternatives; students have home-folder rights
- [ ] Spreadsheet tools present: Excel *or* LibreOffice; Google Sheets reachable (browser)
- [ ] Browser current; dev-tools unblocked; certificate viewer reachable (Lab 7)
- [ ] Logic simulator approved and bookmarked on lab image + offline fallback documented (Lab 5)
- [ ] Cloud platform sanctioned (or free-tier list published); sandbox/Cloud-Shell alternative identified (Lab 7)
- [ ] Terminal access unrestricted in home folders (Labs 3, 4)
- [ ] Timing page or stopwatches available (Lab 2)
- [ ] Sample files staged: Lab 4 miscoded file, Lab 6 gradebook, SB-3 problem cards + seeded bug, SB-4 sample-output pack
- [ ] LMS: submission slots for 8 labs + 4 builders; accessible-format folder created

**Optional tools (mark clearly if you provide):** hex editor with GUI (Lab 4 — plain editors/browser toggles suffice); Logisim-evolution desktop (Lab 5 — browser simulator suffices); `mtr` (Lab 7 — `tracert`/`traceroute` suffice). None are required; the workbook's no-expensive-software rule holds.

**Student-side minimums (publish on the course site):** any OS, a browser, a terminal, the LMS. Everything else is platform-neutral or substitutable — see the workbook fallbacks.

## 5. Lab validation checklist (run before each lab's window opens)

For each lab, confirm:

- [ ] Every handout link resolves (nav validator covers site-wide, but check the LMS copies too)
- [ ] The lab's required tools work **on the lab image as students will meet it** — not just your staff machine
- [ ] Sample files open correctly and their defects are present as designed
- [ ] The accessibility alternative is actually executable (open it and follow it once)
- [ ] Due date on the handout matches the LMS slot and the schedule
- [ ] Troubleshooting items match this term's environment (screenshots menu paths drift across OS versions — refresh the stale ones)
- [ ] For Lab 8: platform privacy-setting screenshots re-taken *this term*; report-phishing path verified

**Mechanical backstop:** `python scripts/run_all_checks.py` includes `validate_lab_workbook.py` — it verifies the workbook's structural contract (12 labs/builder rows, 22-area matrix, per-handout required sections). Run the full suite before publishing any lab change.

## 6. What was tested vs what was not

Honest scope, per the course's no-fabrication rule:

- **Machine-validated:** workbook structure, handout section contracts, mapping/matrix consistency (validator, this repo).
- **Build-validated:** all pages render in the strict MkDocs build.
- **Not tested here (by design — no lab environment exists in this repository):** the simulators' current UIs, the cloud providers' free-tier flows, spreadsheet menu paths, and OS settings screens. Every handout was written to degrade gracefully across versions (troubleshooting + substitution pattern), but **instructors must run §5's checklist on their own image before each window** — that is the test that counts, and only you can run it.
