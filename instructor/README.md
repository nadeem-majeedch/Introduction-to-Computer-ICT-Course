# Instructor-Only Materials

**This directory is NOT part of the published website.** It lives outside `docs/`, has no entry in `mkdocs.yml` nav, and is guarded by `scripts/check_instructor_exclusion.py` + CI. If a `docs/` file ever links here, the build fails.

---

## Contents

| File | Purpose |
|---|---|
| `answer-keys/quiz-answer-keys.md` | Keys for the 14 graded weekly quizzes |
| `answer-keys/lab-answer-notes.md` | Expected outcomes + grading notes for Labs 1–8 |
| `exams/midterm-exam-bank.md` | Midterm item bank (Modules 1–4) |
| `exams/final-exam-bank.md` | Final exam item bank (cumulative) |
| `module-guides/` | Per-module teaching guides: tips, board/projector plans, demos, misconception warnings, discussion prompts, **exit tickets with answers** |

## Rules for this folder

1. **Never move it under `docs/`** — not even "temporarily." Use the issue tracker for reviews instead.
2. **Never link to it** from any `docs/` page (the leak guard scans for this).
3. **Before first publication, resolve OQ-01** (`docs-meta/06-open-questions.md`): if the GitHub repository is **public**, these files are readable in the repo even though they're not on the website — move this folder to a separate private repository instead.
4. Practice quizzes on the public site use *different questions* from graded quizzes by design (see `docs-meta/04-documentation-standards.md` §J) — keep it that way when updating either side.
5. When you change any lecture's "Check your understanding" or a lab's parts, check the corresponding grading notes here still align.

## Suggested semester workflow

1. Before each quiz: adapt the key's items to the sections actually taught this term.
2. During grading: note common wrong answers in the key file — next year's lecture "misconceptions" sections grow from this.
3. After the showcase: archive the project scores against the rubric bands and adjust the band descriptors if calibration drifted.
