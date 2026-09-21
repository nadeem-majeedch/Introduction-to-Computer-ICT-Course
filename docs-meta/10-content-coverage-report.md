# Content Coverage & Validation Report — PROMPT 03

**Version:** 1.0 · **Date:** 2026-09-19
Companion to the teaching blueprint (`07`) and assessment blueprint (`08`). This report maps the PROMPT 03 deliverables to where they live, states what is machine-enforced, and lists warnings for instructor review.

---

## 1. Deliverables map (required element → location)

For **each of the 32 lectures** (`docs/lectures/L01…L32`):

| Required element | Where it lives | Enforcement |
|---|---|---|
| Lecture title and number | `# LNN — Title` + front-matter `lecture`/`title` | `validate_lecture_schema.py` |
| Module | Front-matter `module` + blockquote line | Schema validator; CLO validator |
| Duration (2 hours) | Blockquote `· 2 hours` under the h1 | Schema validator (h1 block format) |
| Learning objectives | `## Learning objectives` (3–5, CLO-mapped) | Schema validator (count + CLO regex) |
| Prerequisite knowledge | `## NN.0 Before we start — prerequisites and motivation` (¶1) | Schema validator (exact heading) |
| Introduction and motivation | Same NN.0 section (¶2, "Why this matters") | Schema validator |
| Detailed conceptual explanations | Numbered `## NN.k` body sections (112 across 32 lectures) | Pre-existing; nav/CLO validators |
| Key terminology | `## Key terms` + bolded first use + glossary | Schema + terminology validators |
| Real-world examples | Within body sections; in-class activities | Human QA (QA strategy §4) |
| Diagrams / visual explanations | `## Visual explanation` (Mermaid) | Schema validator (diagram + alt text present) |
| Accessible alt text | `*Figure: …*` text alternative under every diagram | Schema validator (fails if missing) |
| Step-by-step demonstrations | Instructor guides: "Suggested demonstration" | Guide-existence check (schema validator) |
| Common misconceptions | `## Common misconceptions` (≥2) + module guide warnings | Schema validator |
| Guided classroom activity | `## Lecture activity` (linked to labs/activities or in-class spec) | Pre-existing validator checks |
| Problem-solving questions | `## Check your understanding` + activity problem-solving steps | Schema validator (3–5 questions) |
| Formative assessment questions | Check questions + exit tickets (answers in guides only) | Leak scan (below) |
| Summary | `## Summary` (non-stub) | Schema validator (length floor) |
| Further reading | `## References & further reading` (numbered, author–date) | Pre-existing validator checks |
| Homework / extension | `## Homework` (3 items; third marked advanced extension) | Schema validator (length floor) |

Per **module** (`instructor/module-guides/module-0N-teaching-guide.md`, N=1–8 — private tree):

| Teacher-friendly material | Section in each guide |
|---|---|
| Instructor teaching guide | Whole file (module-level prep + per-lecture) |
| Suggested board/projector explanations | "Board / projector plan" ([Board]/[Slide] items) |
| Teaching tips | "Teaching tips" per lecture |
| Misconception warnings | Module-level list + per-lecture additions |
| Discussion prompts | 3 per lecture with expected-answer hints |
| Suggested demonstrations | "Suggested demonstration" per lecture |
| Exit-ticket questions | "Exit-ticket questions (with answers)" — answers **only** here |

## 2. Machine-enforced guarantees (this prompt's additions to `validate_lecture_schema.py`)

1. All 32 lectures carry `NN.0 Before we start`, `Visual explanation`, `Summary`, `Homework`.
2. Every `Visual explanation` contains a Mermaid fence **and** a `*Figure: …*` text alternative (image-failure fallback, WCAG-aligned).
3. `Summary` and `Homework` are non-stubs (length floor).
4. All 8 module guides exist in the private tree (guide-existence check).
5. **Answer-leak scan**: lines matching `Answer:`, `Answers:`, `Answer key:`, `Model answer:`, `With answers:`, `Marking scheme:` fail validation on any `docs/` page.
6. Existing guards re-verified after the changes: nav sync (85/85), CLO mappings, accessibility, terminology, instructor-exclusion, blueprint parity.

## 3. Practical-activity coverage (prompt's list → lectures)

| Category | Primary lectures / labs |
|---|---|
| Operating-system exploration | L10 (dual-interface race), Lab 3 |
| File and folder management | L11 + Lab 3 (scavenger hunt) |
| Hardware identification | L03, L05, L08 + Lab 2 (inventory) |
| Binary and data-encoding exercises | L13 (A2 relay), L14 (overflow casino), L15 (encoding detective), Lab 4 |
| Browser and network concepts | L21–L23 (campus map, A4 role-play, DevTools), Lab 7 |
| Privacy and security scenarios | L29 (A5 audit), L30 (footprint self-audit), Lab 8 |
| Spreadsheet and data organization | L19 + Lab 6 (grade-book), L26 (cleaning exercise) |
| Introductory command-line exploration | L10, L21 (ping), Lab 7 CLI segments |
| Data-science computing examples | L19 (charts), L26 (lifecycle + CS-03), L25 (SQL reading), L27 (training-loop demo) |

All activities remain safe/feasible for beginners: read-only system inspection, simulated (fabricated) phishing samples, first-person defensive security only.

## 4. Warnings (for instructor review)

1. **Diagram placement is in-page, not separate assets.** All 32 diagrams are Mermaid (rendered by the site; text alternatives provided). If the instructor later wants image exports for slide decks, they must be generated at presentation time — none are committed as binary assets (deliberate: keeps the repo text-only and diffable).
2. **Exit-ticket answers are prose-graded, not machine-graded.** The leak scan is line-shape based; a paraphrased answer embedded mid-sentence would not trip it. The QA strategy's manual skim (§4) is the second layer — keep both.
3. **Homework time estimates are pedagogical targets.** The (10–30 min) figures assume the stated preparation; calibrate after the first cohort's actual load and record in the blueprint (07) next revision.
4. **Two content items previously flagged remain open from PROMPT 01**: the L16 reference [2] placeholder (instructor must substitute an available authoritative article) and MkDocs 2.0 upstream deprecation banner (informational).
5. **Demo feasibility** (open HDD spin-up, VM/container timing demo) depends on local equipment; each guide lists a fallback, but confirm before class.
6. **No new public pages** were added, so the site page count (85 markdown / 86 HTML) is unchanged; guides and this report live outside the published nav by design.

## 5. Sign-off

- `python scripts/run_all_checks.py` — 7/7 PASS (exit 0)
- `mkdocs build --strict` (pinned venv) — zero warnings (exit 0)
- Built-site leak scan (built HTML): only benign meta-statements ("answer keys are not published"); no real answers in `site/`
- No commit, no push — git untouched
