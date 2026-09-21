# Repository Inspection Report — Phase 1

**Course:** Introduction to Computer (ICT)
**Inspection date:** 2026-09-18
**Inspector:** Course-scaffolding agent (Phase 1 of the course build)

---

## 1. Inspection method

The following checks were executed **before any file was created**:

| Check | Result |
|---|---|
| Recursive directory listing | Root contains **one directory**: `.freebuff/` |
| Contents of `.freebuff/` | `project-id` (tooling metadata only) |
| Git repository status | `git status` → `fatal: not a git repository (or any of the parent directories)` |
| Git history / branches | Unavailable — no `.git` directory exists |
| README files | None found |
| Documentation files | None found |
| Configuration files (`mkdocs.yml`, `package.json`, `requirements.txt`, `pyproject.toml`, etc.) | None found |
| Build tools | None found |
| Python scripts / scripts directory | None found |
| GitHub Actions workflows (`.github/workflows/`) | None found |
| Website framework | None found |
| Dependencies (`node_modules/`, `venv/`, lock files) | None found |
| Testing infrastructure | None found |
| Existing course files | None found |

## 2. Conclusion of inspection

**The repository is a greenfield workspace.** There are no existing assets to preserve,
no conventions to follow, and no conflicts to resolve. Per rule 4 ("do not assume that
the repository is empty"), this conclusion is based on direct inspection, not assumption.

The environment does have usable local tooling:

| Tool | Version | Relevance |
|---|---|---|
| Python | 3.14.7 | Runs validation scripts; runs MkDocs |
| PyYAML | **not installed** (global) | Validation scripts must use stdlib only, or a project venv |
| Node.js | 24.19.0 | Not required (MkDocs toolchain chosen) |
| Git | 2.51.0 (Windows) | Instructor will `git init` / commit / push manually |

## 3. Existing assets inventory

| Asset | Status | Action |
|---|---|---|
| `.freebuff/project-id` | Tooling metadata for the Freebuff client | **Untouched** (not part of the course) |
| Everything else | Does not exist | To be created in Phases 2–4 |

## 4. Reusable components

None exist. Everything must be created from scratch. The chosen stack
(MkDocs Material + Markdown sources + Python stdlib validators) was selected partly
because it minimises external dependencies for a fresh, instructor-maintained repository.

## 5. Potential conflicts

| Risk | Assessment | Mitigation |
|---|---|---|
| Existing content overwritten | None — no content exists | N/A |
| Port/process collisions | None running | N/A |
| Git state | No repo initialised; **no commits were made by the agent** (rule 1) | Instructor runs `git init` manually; see `docs-meta/02-development-roadmap.md` |
| Global Python lacks PyYAML | Would break YAML parsing in validators if assumed | Validators use **stdlib only**; the real site build runs in a project-local venv (`python -m venv .venv`) |
| Windows host | The instructor works on Windows | All shell snippets in documentation avoid Unix-only syntax |

## 6. Missing infrastructure (to be created)

1. **Documentation site** — `mkdocs.yml` + `docs/` (MkDocs Material, strict mode)
2. **Course content** — 8 module overviews + 32 lectures + labs + activities + case studies
3. **Instructor-only materials** — `instructor/` directory *outside* `docs/` so it is never published
4. **Validation** — `scripts/` validators (pure stdlib) + `tests/expectations.json`
5. **CI/CD** — GitHub Actions: site build, content QA, and instructor-leak guard
6. **Repository hygiene** — `README.md`, `.gitignore`, `requirements.txt`, `LICENSE` decision
7. **Metadata** — architecture, roadmap, standards, QA strategy, open questions

## 7. Recommended implementation strategy

1. **Foundation first:** metadata documents (inspection → architecture → roadmap → standards → QA) so the build follows a written specification.
2. **Config before content:** `mkdocs.yml` and `requirements.txt`, with the complete 32-lecture navigation declared up front; every page is then written to a fixed skeleton (no broken nav, no orphan files).
3. **Content incrementally, validated after each stage:** core pages → module overviews → lectures 1–16 → lectures 17–32 → labs → activities/case studies → references → instructor materials.
4. **Enforce the student/instructor boundary structurally:** instructor materials live *outside* `docs/` and are *never* listed in `mkdocs.yml` nav; a CI guard (`scripts/check_instructor_exclusion.py`) fails the build if the docs tree ever references or includes them.
5. **Validate with two layers:** (a) fast stdlib structural validators runnable anywhere; (b) a real `mkdocs build --strict` in a local venv so warnings fail the build exactly as CI will.
6. **Never commit or push** — the instructor performs all git operations manually (rules 1–3).

## 8. Decisions taken during inspection (with user approval)

| Decision | Choice | Rationale |
|---|---|---|
| Static site generator | **MkDocs Material** | Search, tabs, admonitions, math via MathJax/KaTeX, strict-build warnings, simple Python toolchain, YAML nav explicit enough for CI checks |
| Instructor-material placement | **Same repo, excluded `instructor/` folder** | Simplest workflow for a solo instructor; enforced by build exclusion + CI leak guard. Documented caveat: if this GitHub repo is public, instructor files are visible in the repository even though they are not on the website — see open question OQ-01 |
| Validation tooling | Pure-Python-stdlib validators + real MkDocs strict build in venv | No global pip installs; reproducible locally and in CI |

## 9. Phase 1 sign-off

- Inspection complete; report reflects direct observation of the actual workspace.
- No files existed to preserve; nothing was modified or deleted except files created by this course build.
- Approved to proceed to Phase 2 (Master Course Architecture).
