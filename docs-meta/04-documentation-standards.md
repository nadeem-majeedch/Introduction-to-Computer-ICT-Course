# Documentation Standards

**Version:** 1.0 · **Date:** 2026-09-18
Applies to every page under `docs/`. The machine-checkable subset is enforced by `scripts/` validators; the rest is review-level policy.

---

## A. Markdown rules

1. **Headings:** exactly one `h1` (the page title); `h2` for major sections; never skip a level.
2. **Paragraphs:** first sentence of every section must be understandable without the rest (plain-language rule).
3. **Lists:** use `-`; indent nested items with 4 spaces; numbered lists only for genuinely ordered steps.
4. **Emphasis:** bold for defined terms on first use; italics sparingly; never use emphasis as the only carrier of meaning.
5. **Tables:** header row mandatory; used for comparative data; not for prose.
6. **Code:** fenced blocks with language tags; commands the student must type get `bash` (or `powershell` when Windows-specific).
7. **Math:** KaTeX blocks (`$$ … $$`); always accompany with a plain-language sentence.
8. **Line discipline:** sentences per paragraph ≤ 5 where possible; pages ≤ ~120 lines of body prose before a heading or visual break.

## B. File naming

- Kebab-case, ASCII letters/digits/hyphens only; no spaces.
- Lecture: `L{NN}-{slug}.md` (zero-padded, semester-wide numbering, e.g., `L07-memory-hierarchy.md`).
- Module: `module-{NN}-{slug}.md`; Lab: `lab-{NN}-{slug}.md`; Activity: `activity-{N}-{slug}.md`; Case study: `case-study-{NN}-{slug}.md`.
- One page = one file; assets under `docs/assets/` with page-scoped subfolders (`assets/L13/…`).

## C. Lecture page structure (fixed template, enforced)

```text
# LNN — Title
> Module N · Stage k · 2 hours
## Learning objectives      (3–5; each maps to a CLO: CLO-x)
## Key terms                (bold-defined in body; listed in glossary.md)
## NN.0 Before we start     (prerequisites + motivation; PROMPT 03)
## NN.1 Section …           (progressive explanation; practical example early)
## Visual explanation       (Mermaid diagram + *Figure: …* text alternative; PROMPT 03)
## Lecture activity         (link to content/activities/… where applicable)
## Common misconceptions    (≥2 per lecture)
## Check your understanding (3–5 questions; NO answers on the public page)
## Lab link                 (when scheduled)
## References & further reading (numbered; citation format below)
## Summary                  (course-level recap; PROMPT 03)
## Homework                 (3 items; third marked advanced extension; PROMPT 03)
## Looking ahead            (one-paragraph bridge to next lecture)
```

Exit-ticket answers, board plans, demonstrations, and discussion-prompt keys live in the private instructor module guides (`instructor/module-guides/`), never on these pages (enforced by the schema validator's answer-leak scan).

Front-matter (YAML, validated): `lecture`, `module`, `title`, `stage`, `outcomes` (CLO ids).

## D. Learning objectives and CLO mapping

- Each objective uses a Bloom-aligned verb (describe, explain, apply, analyze, evaluate, create); avoid "understand" alone as a stated objective verb.
- Every lecture objective maps to exactly one CLO from `docs/syllabus.md`; the mapping is duplicated in front-matter `outcomes:` and validated for consistency.
- Module overviews restate their lectures' objectives in aggregate.

## E. Terminology

- Define every technical term at **first use** in bold; add it to `docs/glossary.md` the same day.
- One canonical spelling per concept (e.g., "Wi-Fi", "email", "internet" for the network, "Internet" in proper-noun historical use per style decision OQ-07).
- Do not use trademarked product names as generic nouns (e.g., say "search engine", not a brand, in definitions).
- Avoid idioms that do not translate across cultures; the cohort is international.

## F. Citation format (author-date, course-adapted)

In-text: `(Tanenbaum & Austin, 2013)` — Reference block, numbered:
`[1] Tanenbaum, A. S., & Austin, T. (2013). *Structured Computer Organization* (6th ed.). Pearson.`

Rules: cite **verified** sources only; textbook chapters are acceptable; URLs must be to stable pages (official documentation, standards bodies, universities, museums); no personal blogs for factual claims; no citation may be invented — if a claim cannot be sourced, it is rewritten as a teaching simplification **labelled as such** ("simplification:").

## G. Diagrams

- Default: Mermaid blocks (rendered natively by MkDocs Material) — versionable and text-accessible.
- Every diagram gets: a caption (`Figure N — …`), alt-equivalent description in the surrounding text, and no meaning carried by colour alone.
- Complex raster images (screenshots) must have detailed alt text; screenshots avoid showing real personal data.

## H. Code examples

- Every code block states its purpose in one sentence before the block.
- Shell examples default to cross-platform commands; platform-specific variants shown side by side when they differ.
- No executable code that could harm a system; system-modifying commands are described, not scripted.
- All code is checked into the page (no "left as exercise" hidden dependencies).

## I. Alt text and accessibility (enforced subset)

- Every `![…](…)` has non-empty, descriptive alt text (validator).
- Link text is meaningful — no bare URLs, no "click here" (validator).
- One `h1` per page; no skipped heading levels (validator).
- Tables have header rows; images of text are avoided entirely.

## J. Student/instructor separation

- **Public (`docs/`):** lecture questions without answers; practice quizzes with collapsible self-check answers for questions *distinct* from graded weekly quizzes; rubric criteria without sample graded responses; exam coverage without item banks.
- **Instructor-only (`instructor/`):** graded-quiz answer keys, exam banks, grading notes, integrity-case guidance.
- The validator `check_instructor_exclusion.py` fails the build if any file under `docs/` links to, embeds, or names an `instructor/` path, and fails if nav ever includes `instructor/`.
- Never move instructor content into `docs/` "temporarily" — use the issue tracker instead.

## K. Automated testing hooks

- Validators are idempotent, stdlib-only, and exit non-zero with a readable message on failure.
- `tests/expectations.json` is the single source of truth for inventory counts (32 lectures, 8 modules, 8 labs, 5 activities, 4 case studies, 14 quizzes); validators compare reality against it.
- CI runs `run_all_checks.py` then `mkdocs build --strict`; both must be green before deploy.

## L. Build validation policy

- A page is "done" only when: validators pass, `mkdocs build --strict` is warning-free, and the page renders correctly in `mkdocs serve`.
- No page is published with TODO markers (validator flags `TODO`/`TBD`/`FIXME` outside `docs-meta/`).
