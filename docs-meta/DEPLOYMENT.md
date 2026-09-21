# Deployment and Technical Documentation

**Audience:** instructors and repository maintainers. Students do not need anything on this page — the student-facing course lives in the root [README](../README.md) and on the [published website](https://nadeem-majeedch.github.io/Introduction-to-Computer-ICT-Course/).

---

## 1. Repository at a glance

- **Repository:** <https://github.com/nadeem-majeedch/Introduction-to-Computer-ICT-Course>
- **Published site (GitHub Pages):** <https://nadeem-majeedch.github.io/Introduction-to-Computer-ICT-Course/>
- **Site generator:** MkDocs (Material for MkDocs), pinned in `requirements.txt` (mkdocs 1.6.1 / mkdocs-material 9.7.7)
- **Validation:** 12 Python validators (stdlib-only except PyYAML), wired into `scripts/run_all_checks.py`
- **CI/CD:** `.github/workflows/ci.yml` (checks + strict build) and `.github/workflows/deploy-pages.yml` (checks + build + publish)

### Repository layout

| Path | Purpose |
|---|---|
| `docs/` | **Public website source** — all student-facing content |
| `instructor/` | **Instructor-only** (answer keys, exam banks, case solutions, teaching guides) — *outside* `docs/`, never published; guarded by CI |
| `docs-meta/` | Design documents: architecture, plans, standards, QA reports, open questions, this page |
| `scripts/` | Validation tooling + the calendar generator |
| `tests/` | `expectations.json` — machine-readable course inventory used by validators |
| `semester.yml` | Instructor-configurable semester calendar source |
| `.github/workflows/` | CI and GitHub Pages deployment |

## 2. Local setup

Requires Python 3.10+ (3.12 recommended — it is what CI uses). Windows-friendly; no Unix-only commands.

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt
```

### Build and preview

```bash
mkdocs serve                        # preview at http://127.0.0.1:8000
mkdocs build --strict               # production build — exactly what CI runs
```

`mkdocs build --strict` fails on any warning: broken internal links, unknown nav entries, bad anchors. Treat it as the gate.

## 3. Validation

Run everything (non-zero exit on any failure — this is the single gate):

```bash
python scripts/run_all_checks.py
```

The 12 checks: nav↔tree sync, lecture schema, CLO mappings, accessibility, terminology, instructor-leak guard, teaching blueprint, slide decks, lab workbook, case bank, assessment package, and site integrity (duplicate anchors/IDs, 32-lecture presence, calendar mapping, built-output leak scan). The built-output leak scan runs whenever `site/` exists — build first for the fullest check:

```bash
mkdocs build --strict && python scripts/validate_site_integrity.py
```

## 4. Semester calendar (instructor-configurable)

Lecture dates are **not hardcoded**. Edit `semester.yml` (semester start date, lecture weekdays, break weeks, holidays, assessment anchors — milestones are anchored to lecture numbers, so they follow date shifts automatically), then regenerate the published page:

```bash
python scripts/generate_semester_calendar.py    # writes docs/schedule-calendar.md
python scripts/run_all_checks.py                # validators re-check the calendar
mkdocs serve                                    # preview the updated dates
```

Commit the regenerated `docs/schedule-calendar.md` **together with** your `semester.yml` change. Never hand-edit the generated page. Both CI and the deploy workflow regenerate the calendar before validating, so a stale committed calendar cannot silently ship — but keep them in sync anyway.

## 5. GitHub Pages deployment

Deployment is automatic via GitHub Actions (`.github/workflows/deploy-pages.yml`):

1. URLs are already configured in `mkdocs.yml` (`site_url`, `repo_url`, `repo_name`) and the README — no placeholder edits needed.
2. In GitHub: **Settings → Pages → Build and deployment → Source: GitHub Actions** (one-time setting; the workflow uses the official `actions/upload-pages-artifact@v3` → `actions/deploy-pages@v4` flow and requires it).
3. Push to `main` (or use the workflow's **Run workflow** button): CI runs all content validators and regenerates the calendar, then the site is built strict, `.nojekyll` is added, and the artifact is published.
4. First deploy takes a minute or two; subsequent pushes to `main` redeploy automatically.

The deploy workflow runs the same validation suite as CI before publishing, so a failing check blocks a broken site. `concurrency` is configured so a rapid push sequence cancels superseded deploys rather than racing them.

## 6. Publication workflow (instructor, manual)

1. Commit and push to the GitHub repository.
2. Ensure **Settings → Pages → Source: GitHub Actions** is selected (one time).
3. Push to `main`: CI validates, then the deploy workflow publishes the site.
4. Check the **Actions** tab for a green run; then hard-refresh the Pages URL.

## 7. Troubleshooting

| Symptom | Cause and fix |
|---|---|
| Validators pass locally but fail in CI | Version-behaviour difference. **Real case (fixed 2026-09-21):** `validate_case_bank.py` used `Path` in an annotation without importing it — Python 3.14 tolerates missing annotation names via PEP 649 lazy annotations, CI's Python 3.12 evaluates them eagerly → `NameError`. Reproduce with `python3.12 -m venv .venv312 && .venv312/bin/python -m pip install -r requirements.txt` and run the suite under 3.12 before pushing |
| `mkdocs serve`/`build` fails with nav errors | A `docs/` page is missing from nav or vice versa — `validate_nav_sync.py` names both sides; fix the nav block or restore the page |
| Strict build fails on a dead link | The link target moved or was renamed — the build message names the source file and anchor; fix the link (check `index.md#section` slugs — numbered headings produce numbered anchors) |
| `validate_terminology` flags your new text | The validator bans non-inclusive phrasing (e.g., "click here") and enforces glossary consistency — rephrase per the message |
| Calendar shows wrong/old dates | `docs/schedule-calendar.md` is *generated* — edit `semester.yml` and re-run `python scripts/generate_semester_calendar.py` |
| Leak guard failure mentioning `instructor/` | A public page references the private directory by path — reword without the path (see `docs/case-bank/index.md` §6 for the accepted phrasing) |
| Unicode console errors on Windows | Run validators with the venv Python (`.venv\Scripts\python`); `course_paths.py` already mitigates cp1252 issues |
| PyYAML import error running the calendar generator | Use the project venv — PyYAML ships with mkdocs-material (`pip install -r requirements.txt`) |
| Pages deploy publishes an old site | Check the Actions tab for a failed `run_all_checks` step (a failed check blocks deploy by design), and confirm Settings → Pages → Source is **GitHub Actions** |
| 404 on the Pages URL right after setup | The first successful `deploy-pages.yml` run hasn't completed yet, or Settings → Pages → Source is still "Deploy from a branch" — switch it to **GitHub Actions** |

## 8. Content integrity rules

- Every technical/historical claim cites a source on its page (`docs-meta/04-documentation-standards.md`, §F).
- Unverifiable statements are labelled as teaching simplifications.
- Answer keys never appear under `docs/`; CI fails the build if they do.
- Cybersecurity content is educational and authorization-focused only.
- All organizations and scenarios in labs and cases are fictional and marked as such.

## 9. Open items for the instructor

See `docs-meta/06-open-questions.md`. The two that gate publication mechanics:

- **OQ-05 (license):** no LICENSE file exists yet — all rights reserved by default. The README currently says exactly that; add a license and update the README section only after deciding.
- **OQ-01 (instructor materials):** this repository is public, so `instructor/` files are viewable by anyone browsing the repo (they are *not* on the website, and CI enforces that). If that is unacceptable, move `instructor/` to a separate private repository.

Also outstanding: OQ-02 (credit hours), OQ-03 (institutional policy placeholders), OQ-04 (textbook edition), OQ-13 (final weightings confirmation).
