---
lab: 6
title: Spreadsheet Data Workshop
assigned: L19
due: End of Week 11
---

# Lab 6 — Spreadsheet Data Workshop

> **Assigned:** L19 · **Due:** end of Week 11 · **Modules 5–7 bridge**

## Purpose

This lab builds the spreadsheet competence every data module assumes: correct references, IF logic, lookups, and one honest chart — applied to a realistic class-gradebook dataset your instructor distributes.

## Before you start

- 90 minutes; Excel, Google Sheets, or LibreOffice Calc (function names differ slightly; the handout gives both `VLOOKUP`/`XLOOKUP` paths).
- The course dataset file (`ict-gradebook-start.xlsx/.csv` — provided on the LMS) with deliberately realistic imperfections.

## Part 1 — Clean and structure (20 min)

1. Audit the data: find the three spellings of one city, the impossible age, and the duplicate row (L26's cleaning pass, small scale).
2. Fix each; add a `cleaned-on` note column documenting what you changed (reproducibility habit).
3. Freeze the header row; format the table as a proper range (no merged cells — justify this to yourself in one cell comment).

## Part 2 — Formulas and references (30 min)

1. Compute `Total` = quiz best-10 sum + lab average for each student — build it so *one* formula copies down the whole column correctly.
2. `Grade` via nested IF: ≥80 "A", ≥70 "B", ≥60 "C", ≥50 "D", else "F".
3. Absolute-reference drill: a grading-thresholds block sits in a fixed range — write `Grade` to *read thresholds from the block* (change "A" to 85 once and watch every grade update; screenshot before/after).
4. Lookup: a `programme` sheet maps student IDs to programmes — use `VLOOKUP` (or `XLOOKUP`) to pull programme names into the main sheet.

## Part 3 — Analysis and one honest chart (25 min)

1. Produce a summary table: count and average per grade; pass rate overall and per programme.
2. Build **one** chart that answers: *"Which programme is struggling most?"* — chart type must match the message (justify in a cell comment next to the chart); label axes; cite the data range.
3. Deliberately make it lie: truncate the axis or pick the wrong type — screenshot the lying version and one-sentence what it misleads about (then keep the honest one in the file).

## Part 4 — Reflection questions

1. Where exactly did an absolute reference save you, and what would have gone wrong without it?
2. Why is documenting cleaning steps a *data-science* habit, not just tidiness (L26)?
3. In one sentence each: what your chart honestly shows, and what its lying twin pretended to show.

## Expected observations and troubleshooting

**You should see:** the threshold block *driving* every grade (change one threshold and the whole column recompute — the before/after screenshot proves it); the lying twin chart lying visibly (truncated axis or wrong type) with a caption that names the deception; the note column documenting all three cleaning fixes.

**If something goes wrong:**
- *`#REF!`/`#N/A` errors after filling down* → classic reference bugs: `#REF!` means a relative shift left the data range; `#N/A` in the lookup means IDs don't match — check for text-vs-number and trailing spaces (L26's whitespace species).
- *Grades didn't change when you edited a threshold* → the formula has hardcoded numbers instead of reading the block — rebuild Part 2 step 3 with absolute references; that's the exercise.
- *Chart looks wrong in Sheets vs Excel* → chart menus differ but the message-criterion doesn't; the cell comment justifying type choice is graded, not the menu path.
- *No spreadsheet application* → university lab machines carry all three accepted tools; the Google Sheets route needs only a browser (see the labs index fallbacks).

**Accessibility alternative:** spreadsheets are screen-reader workable; submit the workbook plus a short text description of your chart (type, axes, message) so chart *reasoning* is assessed without seeing pixels. Large-print threshold tables are on the labs index.

## Submission checklist

- [ ] Cleaned workbook (with note column) as `.xlsx`/`.ods` or Sheets link
- [ ] Before/after threshold screenshot
- [ ] Honest chart + lying-version screenshot with captions
- [ ] Reflections; submitted via LMS

## Grading

Standard rubric ([labs index](index.md#how-labs-are-graded)); the threshold-block design carries the formula-demonstration weight.
