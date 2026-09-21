---
lab: 3
title: File System Scavenger Hunt
assigned: L11
due: End of Week 6
---

# Lab 3 — File System Scavenger Hunt

> **Assigned:** L11 · **Due:** end of Week 6 · **Module 3**

## Purpose

Paths, extensions, and backups are the skills every later lab silently assumes. This lab drills them as a scavenger hunt on your own machine — CLI-first, GUI-verified.

## Before you start

- 90 minutes; a terminal (Command Prompt/PowerShell on Windows, Terminal elsewhere).
- Lab 1's `ict-course/` tree still in place.

## Part 1 — Path gym (20 min)

On your OS, *write down* (then verify by navigating):

1. The absolute path to your `Downloads` folder.
2. A relative path from your home directory to `ict-course/labs/lab-01`.
3. What `..` resolves to from `ict-course/labs/lab-01`? And from `ict-course`?
4. Rename `lab-01` to `lab-01-archive` — which *paths* break? (Answer before renaming, then check.)

## Part 2 — CLI round (25 min)

Using the terminal only, inside `ict-course/`:

1. Create `labs/lab-01/practice/` and a text file `notes.md` in it.
2. Copy `notes.md` to `project/` in one command; move the original to `resources/`.
3. List all `.md` files recursively; count them (any method).
4. Delete `resources/notes.md` (the copy in `project/` survives).

Windows and macOS/Linux commands differ (`copy` vs `cp`) — state which you used and translate all four commands into the *other* family's syntax on your answer sheet.

## Part 3 — Extension and metadata forensics (20 min)

1. Find three files with misleading extensions on your machine (create one safely: rename a `.txt` to `.jpg`, open it — what happens and why, per L11).
2. Open any photo's properties/metadata: list five fields; circle every privacy-sensitive one (L30 preview).
3. Where does your OS record file *size* vs *size on disk*? Explain the difference in one sentence (hint: blocks).

## Part 4 — Backup plan (15 min)

Write your personal 3-2-1 plan as a table: **what** (which folders), **copy 2 medium**, **copy 3 offsite**, **frequency**, **who verifies it works**. One honest sentence: what is *currently* unprotected that you care about?

## Part 5 — Reflection questions

1. Why does the course enforce a naming convention (dates `YYYY-MM-DD`, hyphens)? Give a failure it prevents.
2. GUI or CLI for bulk renames — argue from today's evidence, not preference.
3. Which Part 3 metadata field could embarrass someone sharing files publicly, and what's the fix?

## Expected observations and troubleshooting

**You should see:** the renamed `lab-01-archive` breaking exactly the absolute paths that spelled the old name (relative paths from the parent survive — that's the point of question 4); a CLI transcript that reads as clean commands and errors, not a screenshot collage; three metadata fields circled as privacy-sensitive (GPS is the classic).

**If something goes wrong:**
- *Terminal refuses a command* → read the error aloud: wrong family's syntax (macOS/Linux vs Windows) is the most common cause — Part 2 asks you to translate anyway.
- *Can't find files with misleading extensions* → create all three yourself (safely, from empty text files); Part 3 explicitly allows it.
- *Size vs size-on-disk shows no difference* → small files hide the block gap; test a 1-byte file — the *size on disk* jumps to a whole block.
- *Permissions block a rename* → work inside your own user folders only; system folders are out of scope (and unsafe to modify — see the labs index safety note).

**Accessibility alternative:** the entire hunt is text-driven — screen readers handle terminals well; submit the transcript as text. GUI-only verification steps may be replaced by equivalent `dir`/`ls -l` output. If you lack file-management access on a shared machine, the lab image grants full rights to your home folder.

## Submission checklist

- [ ] Path answers verified by navigation
- [ ] CLI round transcript (copy your terminal text)
- [ ] Forensics answers with the created test file removed
- [ ] 3-2-1 table complete
- [ ] Reflections; everything submitted via LMS

## Grading

Standard rubric ([labs index](index.md#how-labs-are-graded)); the CLI transcript is the demonstration artifact.
