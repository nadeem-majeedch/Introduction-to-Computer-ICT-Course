# Slide Decks — Instructor Package

**Not published.** This folder is instructor-only (outside `docs/`, no nav entry, leak-guarded). One deck file per module; every lecture L01–L32 has a deck with integrated speaker notes.

## Files

| File | Lectures |
|---|---|
| `module-01-slides.md` | L01–L04 |
| `module-02-slides.md` | L05–L08 |
| `module-03-slides.md` | L09–L12 |
| `module-04-slides.md` | L13–L16 |
| `module-05-slides.md` | L17–L20 |
| `module-06-slides.md` | L21–L24 |
| `module-07-slides.md` | L25–L28 |
| `module-08-slides.md` | L29–L32 |

## Deck grammar (validated by `scripts/validate_slide_decks.py`)

```text
# LNN · Title                      ← deck title slide (LNN + module/hours line)
### Run sheet (120 min)            ← block allocation table
## S# · Title                      ← one slide per heading
**Notes:** [~m] TALK: … ASK: … …   ← speaker notes line under each slide
## S# · Activity — …               ← activity slides named explicitly
## S# · Exit ticket                ← final numbered slide, exactly one per deck
```

**Notes notation:** `[~minutes]` delivery target · `TALK:` what to say · `ASK:` question(s) to put to students · `MISC:` misconception to expect · `DEMO:` demonstration instruction · `TRAN:` transition to the next concept · `EXT:` optional extension · `TROUBLE:` what to do when it breaks.

## Slide-count floors (per validated design)

- 11–15 slides per standard lecture; L32 carries 11 plus the 55-minute showcase block.
- Every deck: objectives slide, activity slide(s) with instructions, quick-check slide, summary slide, exit-ticket slide (last).

## Relationship to other materials

- **Lecture pages** (`docs/lectures/`): the student-facing content the decks *present* — decks never replace them and never contain answer keys.
- **Module guides** (`instructor/module-guides/`): the deeper instructor narrative (tips, demos, answered exit tickets). Decks reference the same activities and demos; the guide holds the prose.
- **Delivery guide** (`00-delivery-guide.md`): timing policy, activity instructions index, presentation + accessibility checklists.

## Rendering

Decks are Markdown by design (diffable, searchable, no binary assets). To project: print to PDF via any Markdown renderer, or paste slides into your institution's tool. The grammar maps 1:1 to slides — one `##` heading, one slide, notes below the line.
