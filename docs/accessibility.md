# Accessibility

This website is built to be usable by everyone, including students who rely on assistive technologies. This page states the standards the site targets, the features built in, and what to do if something blocks you.

---

## Our commitment

The course and this website aim to conform to the **Web Content Accessibility Guidelines (WCAG) 2.1, level AA**. That target is a design input, not an afterthought: the site's build tools check a growing subset of it automatically, and the rest is reviewed against the checklist below.

## What the site does for accessibility

| Area | What is built in |
|---|---|
| **Contrast** | The colour schemes (light and dark) use Material for MkDocs palettes checked to meet WCAG AA contrast; the site respects your OS light/dark preference, with a manual toggle |
| **Keyboard operation** | All navigation, search, menus, and content tabs are keyboard-operable (Tab / Shift+Tab, Enter, arrows); a "skip to content" link is the first focusable element on every page |
| **Screen readers** | Landmarks and labelled regions on every page; diagrams carry text alternatives (see below); tables have header rows; expandable sections use proper `<details>` semantics |
| **Diagrams** | Every meaningful diagram on the lecture pages is a Mermaid graphic **paired with a text-alternative figure caption** describing the same content in prose — no meaning is image-only |
| **Typography** | Responsive layout for phone, tablet, and desktop; body text sizes and line lengths kept readable; code blocks wrap or scroll with keyboard focus |
| **Links** | Link text describes its destination (e.g., "L13 — Number Systems"), so every link is meaningful out of context |
| **Search** | Full-text search with highlighted matches and keyboard access — an alternative way to reach any content |
| **Print** | Lecture pages print cleanly (browser print → PDF): navigation and decorative chrome drop out, content flows; the offline plugin also makes the whole site readable without JavaScript |
| **Language** | `lang="en"` set site-wide; terminology consistent with the [Glossary](glossary.md) so terms never shift meaning mid-course |

## Content accessibility (course materials, not just the site)

Accessibility is also a *content* commitment, enforced by the course's validators:

- Every lecture page must carry a diagram **plus** its text alternative — the build fails otherwise.
- Slide-deck guidance requires verbalized diagrams, AA contrast at hall distance, and non-visual activity paths (instructor materials).
- Lab handouts each include an **accessibility alternative** — a no-install or assistive-tech-friendly route to the same learning outcome.
- Case studies and question banks avoid colour-only or image-only meaning.

## If something blocks you

1. **Tell the instructor** — content will be provided in an alternative form (text version of a diagram, larger print, extended lab time) without delay.
2. **Contact the institutional accessibility office** for accommodations that outlast a single task (see [Help → Getting help](help.md#3-getting-help)).
3. **Report site issues** (contrast, keyboard traps, missing alt text) via the course's usual channel — the site is maintained in this repository and fixes are build-verified.

## Known limitations

- The site search requires JavaScript; the [Glossary](glossary.md) and module pages serve as no-JS navigation alternatives, and the offline build works fully without it.
- Mermaid diagrams render client-side; their paired text alternatives are the non-visual path (and the print path).
- Third-party embedded content is deliberately minimal: the only external script is the MathJax CDN for formulas.

*This statement follows the structure of a WCAG 2.1 AA accessibility statement: standards target, implemented features, known limitations, and feedback routes. The site's validators (`scripts/validate_accessibility.py` and the site-integrity checks) enforce the machine-checkable subset on every build.*
