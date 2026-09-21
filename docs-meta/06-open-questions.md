# Open Questions Requiring Instructor Review

**Version:** 1.0 · **Date:** 2026-09-18
These decisions were deliberately **not** guessed during scaffolding. Each item lists context, options, and current safe default. Nothing blocks local validation; OQ-01, OQ-05, and OQ-06 must be resolved **before first publication**.

---

| ID | Decision | Context / options | Current safe default |
|---|---|---|---|
| OQ-01 | Will the GitHub repository be **public or private**? | Instructor materials (keys, exams) live in `instructor/` inside this repo. Website exclusion is enforced by CI, but if the repo is public, the raw files are viewable. If private → current design is fine. If public → move `instructor/` to a separate private repo and delete it here. | Assume private until confirmed; flagged in `instructor/README.md` |
| OQ-02 | Credit-hour mapping | 64 contact hours: 3+1 (3 theory + 1 lab)? 4+0? Institution-specific | None recorded; syllabus shows contact hours only |
| OQ-03 | Grading scale, attendance policy, integrity procedure wording | Institution-specific | Syllabus carries placeholders marked `[Institution policy]` |
| OQ-04 | Primary textbook edition/availability | Brookshear & Brylow 13e proposed; check local availability/price | Listed as "proposed" on references page |
| OQ-05 | **License for public content** | No LICENSE file created. Options: CC BY (attribution), CC BY-NC (non-commercial), CC BY-NC-SA, all-rights-reserved | **No license = all rights reserved**; file intentionally absent pending decision |
| OQ-06 | Repository name, org, and final Pages URL | **Resolved 2026-09-19:** `nadeem-majeedch/Introduction-to-Computer-ICT-Course` · Pages: `https://nadeem-majeedch.github.io/Introduction-to-Computer-ICT-Course/` — set in `mkdocs.yml` (site_url, repo_url, repo_name) and README | Instructor still selects **Settings → Pages → Source: GitHub Actions** once, in the GitHub UI |
| OQ-07 | Style: capital-I "Internet" vs lowercase "internet" | Textbooks differ | lowercase "internet" as common noun; "the Internet" kept only in quoted historical titles |
| OQ-08 | Quiz cadence | 14 quizzes assumed (weekly, best 10 of 14 scored) | Assumption stated in syllabus; adjust to calendar |
| OQ-09 | Lab software choices | Spreadsheets: any of Excel/Google Sheets/LibreOffice assumed acceptable; OS screenshots: which platform(s) to include | Handouts are platform-neutral; screenshots deferred |
| OQ-10 | Project pairing model | Individual vs pairs for the integrated project | Rubric supports either; instructor sets at L08 |
| OQ-11 | Localisation needs | Second language for any pages? | English only for now |
| OQ-12 | Department rubric/course-file integration | Some universities require standard CLO/PLO mapping forms | CLO table provided; mapping form to be attached by instructor |
| OQ-13 | Assessment weightings and quiz cadence (from PROMPT 02) | `docs-meta/08` marks every weighting **[Instructor review]**; weekly-quiz cadence assumed | Decide weightings and cadence before Week 1; update syllabus to match |

## How to resolve an item

1. Decide and record the outcome in this table (add a "Resolution" note with date).
2. Update the affected files listed in the context column.
3. Run `python scripts/run_all_checks.py` to confirm nothing structural broke.
