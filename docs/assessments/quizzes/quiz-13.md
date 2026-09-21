---
quiz: Q13
covers: L25-L28
---

# Practice Q13 — L25–L28 (Databases · Data Science · AI)

## Q1

Why does a university enrolment system need a DBMS rather than shared spreadsheets? Two reasons, each naming a spreadsheet weakness.

<details>
<summary>Self-check</summary>

(1) **Concurrent multi-user access with consistency** — spreadsheets corrupt or lock under simultaneous edits; DBMSs manage thousands safely. (2) **Enforced integrity** — a foreign-key constraint makes "enrolment for student 999 who doesn't exist" *impossible*; spreadsheets accept any nonsense typed.
</details>

## Q2

In L25's STUDENTS/ENROLMENTS schema, which column is the foreign key and what does it guarantee?

<details>
<summary>Self-check</summary>

`ENROLMENTS.student_id` → references `STUDENTS.id`. It guarantees referential integrity: every enrolment names a *real* student; deleting a student with enrolments is blocked (or cascaded) by the DBMS, not left to luck.
</details>

## Q3

Write the SQL: list every course taken by student id 2.

<details>
<summary>Self-check</summary>

`SELECT e.course FROM enrolments e WHERE e.student_id = 2;` — single table suffices for *courses by id*; you'd JOIN students only to show the student's *name* alongside. (Reading order: FROM → WHERE → SELECT.)
</details>

## Q4

Trace one bias mechanism end-to-end for a hiring model trained on 20 years of past hiring data.

<details>
<summary>Self-check</summary>

Historical data encodes past preferences (e.g., mostly-male hires) → the model *learns* those correlates as "fit" signals → it scores future candidates by the skewed pattern at scale → decisions repeat and amplify the history. Mechanism: **data → model → outcome**; the fix is representative data + subgroup evaluation, not goodwill.
</details>

## Q5

Before pasting coursework into a chatbot, which two data-use facts must you check, and why?

<details>
<summary>Self-check</summary>

(1) Whether **your inputs are retained/used for training** (privacy of your data and others' embedded in it); (2) whether you can **opt out / delete** (control after the fact). Why: prompts leave your control boundary — L28 §28.3 — and undisclosed or privacy-harming use violates both course rules and the data-protection principles.
</details>
