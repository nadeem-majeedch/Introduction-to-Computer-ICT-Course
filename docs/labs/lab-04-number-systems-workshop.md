---
lab: 4
title: Number Systems Workshop
assigned: L13
due: End of Week 8
---

# Lab 4 — Number Systems Workshop

> **Assigned:** L13 · **Due:** end of Week 8 · **Module 4**

## Purpose

Conversion fluency is earned by hand, not by calculator. This workshop drills the four conversion routes from L13–L14, adds two's complement and overflow drills, and ends by breaking a deliberately miscoded file — encoding forensics from L15.

## Before you start

- 90 minutes; pen and paper for Parts 1–2 (show work!), a hex editor or browser dev-tools for Part 3.
- Calculators are allowed *only* to check answers after you've computed by hand.

## Part 1 — Conversion sprints (25 min, show all work)

Convert, showing every step:

| # | From → To | Value |
|---|---|---|
| 1 | decimal → binary | 77 |
| 2 | binary → decimal | `10110110` |
| 3 | binary → hex | `11101001` |
| 4 | hex → decimal | `0x2F` |
| 5 | decimal → hex | 200 |
| 6 | octal → decimal | `144₈` |
| 7 | decimal → octal | 100 |
| 8 | hex → binary | `0xA7` |

Timed target: 8-bit decimal ↔ binary under 60 seconds each by the due date — record your best time.

## Part 2 — Signed numbers and overflow (25 min)

1. Encode in 8-bit two's complement: −1, −45, −128. Show flip-and-add-one.
2. Decode as *signed*: `1000 0000`, `1111 1111`, `0111 1111`.
3. Overflow drills: compute in 8-bit signed — 100+50, 127+1, −128−1. For each: the wrapped result, and *which carry/lost bit* caused it.
4. One-paragraph answer: why does hardware prefer two's complement over a sign bit? (L14's addition argument.)

## Part 3 — Encoding forensics (25 min)

1. Open the sample file your instructor provides (a text file deliberately saved in the wrong encoding) in a hex editor or browser dev-tools.
2. Identify: intended characters, actual bytes, which wrong encoding step produced the damage.
3. Fix it (re-encode to UTF-8) and document the exact steps you took.
4. Create your own mojibake: type `café`, save as UTF-8, reopen as Latin-1 — record the bytes and the garbled display.

## Part 4 — Reflection questions

1. Which conversion route is fastest for you now, and what single fact makes it fast?
2. Your friend says "hex is what computers use." Correct them using today's Part 1 evidence.
3. Why did Part 3's fix work at the *byte* level rather than the *display* level?

## Expected observations and troubleshooting

**You should see:** Part 1 answers where every place-value step is visible; two's-complement drills where wrapped results name their *lost carry*; a forensics report that distinguishes the file's **bytes** (what hex shows) from the **display** (what the editor drew) — the fix worked at the byte level, which is the reflection's target.

**If something goes wrong:**
- *Hand conversion and calculator disagree* → re-do the hand method; the calculator is right only after your method says so (method marks protect you here).
- *The miscoded sample file won't open* → any plain-text editor with an encoding menu works; you are reading bytes, not rendering pages — if the hex view is unavailable, the browser's "view as UTF-8 / Latin-1" toggle is the accepted alternative.
- *Your own mojibake didn't garble* → some editors auto-detect; force the wrong encoding explicitly from the open-file dialog rather than relying on defaults.

**Accessibility alternative:** Parts 1–2 are pen-and-paper; Part 3's hex reading can be done with a screen-reader-accessible byte dump (print the bytes as text). Colour-coded methods may be replaced by labelled steps. Conversion tables in large-print format are on the labs index.

## Submission checklist

- [ ] Part 1 answers with shown work + best time
- [ ] Part 2 drills with causes identified
- [ ] Forensics report (bytes, diagnosis, fix) + your own mojibake demo
- [ ] Reflections; submitted via LMS

## Grading

Standard rubric ([labs index](index.md#how-labs-are-graded)); *method marks* mean shown work — correct answers with no work score half.
