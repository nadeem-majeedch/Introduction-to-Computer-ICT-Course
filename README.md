# Introduction to Computer (ICT) — Course Repository

University-level, first-semester course: **32 lectures × 2 hours (64 contact hours)**, published as a static educational website on **GitHub Pages**.

- **Repository:** <https://github.com/nadeem-majeedch/Introduction-to-Computer-ICT-Course>
- **Live site (GitHub Pages):** <https://nadeem-majeedch.github.io/Introduction-to-Computer-ICT-Course/>
- **Students:** BS Computer Science / BS Data Science, first semester, mixed computer literacy
- **Site:** MkDocs Material — strict builds, search, accessible formatting
- **Modules:** 8 · **Lectures:** 32 · **Labs:** 8 · **Activities:** 5 · **Case studies:** 4 · **Practice quizzes:** 14

---

## Quickstart (local preview)

Requires Python 3.10+ (3.12 recommended). Windows-friendly — no Unix-only commands.

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt

python scripts/run_all_checks.py   # 12 structural + accessibility + privacy guards
mkdocs serve                       # preview at http://127.0.0.1:8000
```

Production build (exactly what CI runs):

```bash
mkdocs build --strict
```

### Semester calendar (instructor-configurable)

Lecture dates are **not hardcoded**. Edit `semester.yml` (semester start date, lecture weekdays, break weeks, holidays, assessment anchors — milestones are anchored to lecture numbers, so they follow date shifts automatically), then regenerate the published page:

```bash
python scripts/generate_semester_calendar.py    # writes docs/schedule-calendar.md
python scripts/run_all_checks.py                # validators re-check the calendar
mkdocs serve                                    # preview the updated dates
```

Commit the regenerated `docs/schedule-calendar.md` together with your `semester.yml` change.

## Testing

The validation suite (what CI runs) — all checks must pass before a push should be merged or deployed:

```bash
python scripts/run_all_checks.py      # runs all 12 validators, non-zero exit on failure
```

Individually: nav↔tree sync, lecture schema, CLO mappings, accessibility, terminology, instructor-leak guard, teaching blueprint, slide decks, lab workbook, case bank, assessment package, and **site integrity** (duplicate anchors/IDs, 32-lecture presence, calendar mapping, built-output leak scan). A built-output leak scan runs whenever `site/` exists — build first for the fullest check:

```bash
mkdocs build --strict && python scripts/validate_site_integrity.py
```

## Repository layout

| Path | Purpose |
|---|---|
| `docs/` | **Public website source** — all student-facing content |
| `instructor/` | **Instructor-only** (answer keys, exam banks) — *outside* `docs/`, never published; guarded by CI |
| `docs-meta/` | Design documents: architecture, repository plan, roadmap, standards, QA strategy, open questions |
| `scripts/` | Validation tooling (Python stdlib only) |
| `tests/` | `expectations.json` — machine-readable course inventory used by validators |
| `.github/workflows/` | CI (checks + strict build) and GitHub Pages deployment |

## GitHub Pages deployment

Deployment is automatic via GitHub Actions (`.github/workflows/deploy-pages.yml`):

1. The repository must exist at `nadeem-majeedch/Introduction-to-Computer-ICT-Course` (it does — URLs are already configured in `mkdocs.yml` and this README).
2. In GitHub: **Settings → Pages → Build and deployment → Source: GitHub Actions** (one-time setting; the workflow uses the official `actions/deploy-pages` flow and needs this).
3. Push to `main` (or use the workflow's **Run workflow** button): CI runs all content validators, then the site is built strict and published to the Pages URL above.
4. First deploy takes a minute or two; subsequent pushes to `main` redeploy automatically.

The deploy workflow runs the same validation suite as CI before publishing, so a failing check blocks a broken site.

## Publication workflow (instructor, manual)

1. Commit and push to the GitHub repository (see `docs-meta/03-development-roadmap.md`).
2. Ensure **Settings → Pages → Source: GitHub Actions** is selected.
3. Push to `main`: CI validates and the deploy workflow publishes the site.

**The agent that scaffolded this repository did not run any git commands** — initialization, commits, and pushes are the instructor's.

## Troubleshooting

| Symptom | Cause and fix |
|---|---|
| `mkdocs serve`/`build` fails with nav errors | A `docs/` page is missing from nav or vice versa — `validate_nav_sync.py` names both sides; fix the nav block or restore the page |
| Strict build fails on a dead link | The link target moved or was renamed — the build message names the source file and anchor; fix the link (check `index.md#section` slugs — numbered headings produce numbered anchors) |
| `validate_terminology` flags your new text | The validator bans non-inclusive phrasing (e.g., "click here") and enforces glossary consistency — rephrase per the message |
| Calendar shows wrong/old dates | `docs/schedule-calendar.md` is *generated* — edit `semester.yml` and re-run `python scripts/generate_semester_calendar.py`; never hand-edit the generated page |
| Leak guard failure mentioning `instructor/` | A public page references the private directory by path — reword without the path (see `docs/case-bank/index.md` §6 for the accepted phrasing) |
| Unicode console errors on Windows | Run validators with the venv Python (`.venv\Scripts\python`); `course_paths.py` already mitigates cp1252 issues |
| PyYAML import error running the calendar generator | Use the project venv — PyYAML ships with mkdocs-material (`pip install -r requirements.txt`) |
| Pages deploy publishes an old site | Check the Actions tab for a failed `run_all_checks` step (a failed check blocks deploy by design), and confirm Settings → Pages → Source is **GitHub Actions** |

## Content integrity rules

- Every technical/historical claim cites a source on its page (`docs-meta/04-documentation-standards.md`, §F).
- Unverifiable statements are labelled as teaching simplifications.
- Answer keys never appear under `docs/`; CI fails the build if they do.
- Cybersecurity content is educational and authorization-focused only.

## Open items for the instructor

See `docs-meta/06-open-questions.md` — notably **OQ-01 (repo public/private)** and **OQ-05 (license)**, which must be resolved before first publication. No LICENSE file exists yet.
