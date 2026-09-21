---
quiz: Q06
covers: L11-L12
---

# Practice Q06 — L11–L12 (File Systems · Troubleshooting)

## Q1

Your home is `C:\Users\ayesha`. Write: (a) the absolute path to `cv.pdf` inside `Documents\applications`; (b) the relative path from `Documents` to `Music\song.mp3`.

<details>
<summary>Self-check</summary>

(a) `C:\Users\ayesha\Documents\applications\cv.pdf` — full tree from the drive root. (b) `..\Music\song.mp3` — `..` climbs from the current directory (`Documents`) up to `ayesha`, then down into `Music`.
</details>

## Q2

Why does `2026-09-18-notes.md` sort correctly while `18-9-2026-notes.md` sorts wrong? What property of the date format does this?

<details>
<summary>Self-check</summary>

Lexicographic (alphabetical) order must equal chronological order. `YYYY-MM-DD` pads each unit to fixed width, most-significant first — so string sort = date sort. Variable-width day-first formats break the equivalence. (The property: fixed-width, big-endian fields.)
</details>

## Q3

List the five troubleshooting steps in order, applied to "app X won't open."

<details>
<summary>Self-check</summary>

1. Define precisely (exact error/symptom, since when, what changed). 2. Reproduce reliably. 3. Isolate (another user account? reinstall? reboot? logs?). 4. Hypothesis → cheapest test first (settings reset before full reinstall). 5. Escalate with evidence / document the fix.
</details>

## Q4

Why are *security* updates more urgent than feature updates? Give the mechanism.

<details>
<summary>Self-check</summary>

Security updates close **known** vulnerabilities that are already published and actively exploited — the attack uses a public recipe against the known hole. Every unpatched day is exposure to a scripted attack; feature updates add capability but don't close standing holes.
</details>

## Q5

Rewrite this help request professionally: "internet not working pls help asap"

<details>
<summary>Self-check</summary>

Model: goal ("Wi-Fi pages won't load on my laptop"), exact symptom ("Chrome: ERR_CONNECTION_REFUSED; other devices on same Wi-Fi fine"), tried ("rebooted router and laptop; forgot-and-rejoined Wi-Fi"), environment ("Windows 11, university dorm network"). The rewrite demonstrates the minimal-reproducible-example mindset.
</details>
