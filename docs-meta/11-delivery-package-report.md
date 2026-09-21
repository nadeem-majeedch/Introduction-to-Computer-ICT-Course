# Delivery Package Report — PROMPT 04

**Version:** 1.0 · **Date:** 2026-09-19
Companion to the coverage report (`10`) and QA strategy (`05`). Maps the classroom-delivery deliverables to their locations, states the machine-enforced contract, and lists warnings for instructor review.

---

## 1. Deliverables map

| Required deliverable | Location | Notes |
|---|---|---|
| Slide content, all 32 lectures | `instructor/slides/module-0{1..8}-slides.md` | One `## LNN — …` section per lecture; slides are `## S# · Title` headings |
| Speaker notes, all 32 lectures | Same files, `**Notes:**` under every slide | Cues: `[~m]` time · TALK · ASK · MISC (misconception) · DEMO · TRAN (transition) · EXT (extension) · TROUBLE (troubleshooting) |
| Delivery timing guidance | `instructor/slides/00-delivery-guide.md` §1 + per-deck run sheets | Buffer-protected 120-minute allocation; protected segments named |
| Activity instructions | `00-delivery-guide.md` §2 (seven formats) + activity slides in every deck | Think-pair-share, concept checks, guided demos, group discussion, scenarios, hands-on, exit tickets |
| Instructor presentation checklist | `00-delivery-guide.md` §3 | Per-lecture, includes planted-material verification |
| Accessibility & readability checklist | `00-delivery-guide.md` §4 | Slide contrast/word-count/diagram-narration/delivery rules |
| Slide + validation tooling | `scripts/validate_slide_decks.py` (8th check in CI) | Grammar, coverage, required kinds, notes cues, leak scan |

**Slide content per prompt:** every deck carries objectives/Today slide, engaging intro (opening hook slide), key concepts (body slides), visual explanations (referenced from the lecture pages' Mermaid figures; TALK narration verbalizes each), practical examples, short questions (Quick check), classroom activity instructions (named Activity slides), summary, exit question (final Exit ticket slide), and references where required (decks point at the lecture pages' reference blocks rather than duplicating citations).

**Deliberate design:** decks are Markdown, not binary slides — diffable, searchable, leak-guarded, renderable to PDF via any Markdown tool. The grammar maps 1:1 to slides.

## 2. Machine-enforced contract (`validate_slide_decks.py`)

1. 8 module deck files; a section + title slide for every lecture L01–L32 (exactly 32/32).
2. Each lecture: `### Run sheet (120 min)` stating 120 minutes.
3. ≥ 11 slides with clean `S1..Sn` numbering.
4. Required kinds: Today/Objectives, Activity, Quick check, Summary, Exit ticket — and the exit ticket is the **final** slide.
5. Every slide: `**Notes:**` with a `[~minutes]` target and a TALK cue; TRAN required on all slides except the exit ticket.
6. Answer-key leak scan over all deck content (keys live only in module guides).
7. Wired into `run_all_checks.py` — CI runs it; suite is now **8 checks**.

## 3. Validation results

- `validate_slide_decks.py`: PASS (32/32 lectures, 8 module files)
- `run_all_checks.py`: **8/8 PASS** (nav sync, lecture schema, CLO mappings, accessibility, terminology, instructor exclusion, teaching blueprint, slide decks)
- `mkdocs build --strict`: clean, zero warnings (decks are outside `docs/` — site page count unchanged at 85/86)
- **Validator caught real defects during the build** (all fixed): L03/L04 decks missing from module-01; L01 S10 notes lacking a TALK cue; L09/L10 buffer slides sitting after the exit ticket (removed; Q&A folded into exit-ticket time); L32's showcase slide not named as the activity slide; three validator bugs (chunk boundary at the section header, title-prefix regex, TRAN-on-exit-ticket) — corrected.

## 4. Warnings (for instructor review)

1. **Rendering to projection is manual.** No slide-conversion tooling exists in-repo (none existed; none assumed). Decks are print-to-PDF ready via any Markdown renderer; a converter script could be added if the instructor wants automated PPTX/HTML output.
2. **Diagrams live on the lecture pages, not duplicated into decks.** Deck slides referencing a figure assume the lecture page is projected or the figure is pasted at presentation time. Slide text stands alone; visuals are one click away.
3. **Run-sheet times assume 2-hour blocks without built-in breaks.** If the institution mandates a mid-session break, subtract it from the buffer, not from protected segments.
4. **Deck font sizes are renderer-dependent.** The accessibility checklist's ~24 pt rule applies at render time; verify on the lecture-hall projector once per term.
5. **L32's showcase block (55 min) assumes the showcase schedule holds.** If team count changes, re-balance S7 and the buffer only.
6. Existing open items carry forward: L16 reference [2] substitution (PROMPT 01), homework-time calibration (PROMPT 03), OQ-01/05/06 before publication.

## 5. Sign-off

- 8/8 structural checks PASS (exit 0); strict build clean (exit 0)
- No commit, no push — git untouched
