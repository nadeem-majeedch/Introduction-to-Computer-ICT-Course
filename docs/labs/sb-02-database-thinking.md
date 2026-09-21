---
lab: SB-2
title: Database Thinking with Flat Tables
related: L25
duration: 30–40 min
graded: false
---

# SB-2 — Database Thinking with Flat Tables

> **Related lecture:** L25 · **Duration:** 30–40 min · **Practice (completion-marked)**

## Learning outcomes

1. **Design** a two-table schema with primary and foreign keys for a familiar scenario. (L25)
2. **Execute** a query-by-hand on flat tables (filter, project, join) and predict its result rows. (L25)
3. **Explain** which integrity constraints a spreadsheet *cannot* enforce. (L25)

## Prerequisites and equipment

Lab 6's spreadsheet habits; any spreadsheet application (Excel/Sheets/LibreOffice) **as a table editor only** — no database software, no installs. Accessibility alternative: everything submits as text tables; screen-reader friendly.

## Setup

Create a blank spreadsheet with two sheets: `STUDENTS` (columns: `student_id`, `name`, `programme`) and `ENROLMENTS` (columns: `enrolment_id`, `student_id`, `course_code`, `semester`). Enter six realistic student rows and eight enrolment rows — include **one enrolment pointing at a student_id that does not exist** (you'll catch it in the tasks).

## Step-by-step tasks

1. **Key identification (5 min).** Mark each table's primary key; justify uniqueness in one sentence. Which column in `ENROLMENTS` is the foreign key, and to what?
2. **The broken reference (10 min).** Write a two-step manual procedure (as a spreadsheet filter or by eye) that finds the enrolment row whose `student_id` has no matching student. This is what a **foreign-key constraint** does automatically — state what the DBMS would have refused, and when.
3. **Query by hand (10 min).** Using your tables, write the result rows (on paper or in a spare sheet) for: *names and programmes of students enrolled in `ICT101` this semester.* Label your steps as filter → project → (implicit) join. Then translate your steps into one English sentence a DBMS would accept as SQL-shaped pseudocode (`SELECT … FROM … WHERE … JOIN …`).
4. **Spreadsheet limits (5 min).** List three bad rows a spreadsheet would accept that your design's constraints would refuse; name the refusing concept for each (from L25: PK uniqueness, FK validity, type/NOT NULL constraints).

## Expected observations

The orphan row is findable by hand at this size and *unfindable* by hand at thousands of rows — that's the scale argument for constraints. The hand-join produces exactly the rows where the FK matches the PK.

## Questions

1. Why is `name` a poor primary key for `STUDENTS`? Give two failure cases.
2. Your hand-join missed one row on first attempt. What class of mistake was it — filter, projection, or match condition?

## Troubleshooting

- *Formulas misbehave* → this builder needs no formulas beyond filtering; if you used them and they fought back, that *is* the lesson about spreadsheets-as-databases.
- *Can't decide the PK* → ask: which column would you bet never repeats and never goes empty? That instinct is the definition.

## Submission and assessment

Completion-marked practice: submit the schema sketch, the orphan-find procedure, your hand-query result, and the three-violations list. Feedback against the "excellent" descriptors; not weighted into the final grade. All steps work in any spreadsheet or on paper — no tool barrier exists for this builder.
