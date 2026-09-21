---
lecture: L15
module: 4
title: Character Encoding
stage: 2
outcomes: [CLO-4]
---

# L15 — Character Encoding

> **Module 4** · Stage 2 · 2 hours

## Learning objectives

By the end of this lecture, you will be able to:

1. **Trace** a keystroke to a displayed character through an encoding. (CLO-4)
2. **Explain** the relationship between ASCII, Unicode, and UTF-8. (CLO-4)
3. **Diagnose** common encoding failures (mojibake) from their symptoms. (CLO-4)

## Key terms

character set · code point · ASCII · Unicode · UTF-8 · mojibake

## 15.0 Before we start — prerequisites and motivation

**You need from earlier lectures:** L13's binary fluency — a code point *is* a number, and UTF-8's variable-length bytes are place-value arithmetic; L11's file concepts explain *where* encoding metadata lives. L01's data-vs-information distinction returns with force: wrong encoding destroys information silently.

**Why this matters:** every dataset, web page, and CSV you will ever open carries an encoding. DS students meet it as the CSV that “just has weird characters”; CS students meet it in every string library. After this lecture, mojibake is not a mystery but a *symptom with a differential diagnosis* — and “it's just characters” becomes the most dangerous sentence in data handling.

## 15.1 From key to glyph

Press `A`: the keyboard sends a scan code; the OS layer converts it to a **code point** — a number naming the character; the running program stores that number as bits via an **encoding**; the font renders the glyph the number selects. The whole lecture lives in that chain: characters are *numbers agreed upon* by standards.

## 15.2 ASCII: the 128-character foundation

**ASCII** (American Standard Code for Information Interchange, 1963) assigned 0–127 to English letters, digits, punctuation, and control codes (`A`=65, `a`=97, `0`=48) [1]. Seven bits fit one byte with room to spare — and that spare top bit is exactly how hundreds of incompatible national 8-bit variants ("code pages") later emerged, each redefining 128–255. Chaos: the same byte `0xE9` was `é` in one page and something else in another.

## 15.3 Unicode and UTF-8

**Unicode** assigns every character in every living (and many dead) scripts a permanent **code point** — `U+0041` for `A`, `U+0627` for `ا`, `U+0915` for `क`, plus emoji. Unicode is the *map*; **UTF-8** is the dominant *encoding* of that map into bytes [2]:

- 0–127 → one byte, **identical to ASCII** (backward compatibility by design).
- Other characters → 2–4 bytes, with leading bits signalling length.

Consequences: English text stays one byte per character (no storage penalty); the same file decodes identically worldwide; the web standardized on UTF-8 (over 98% of web pages today). Always declare encoding: `<meta charset="utf-8">` in HTML, UTF-8 option in editors — a two-second habit that prevents a class of bugs.

## 15.4 Mojibake — encoding failure forensics

**Mojibake** is garbled text from decoding bytes with the wrong encoding: `é` (UTF-8 bytes `0xC3 0xA9`) read as Latin-1 shows `Ã©`. Diagnosis is pattern-matching: `Ã©`-style pairs → UTF-8 read as Latin-1; `???` or boxes → characters missing from the target set entirely; `éé` doubled weirdness → double-encoding. The fix is *re-decoding with the right encoding at the right stage* — and the prevention is declaring UTF-8 everywhere.

## Lecture activity

In-class, no handout: encoding detective — the instructor shows four garbled samples; teams name the failure class, the probable wrong encoding used, and the fix, using only the patterns above.

## Visual explanation

```mermaid
flowchart LR
    K["Key press: é"] --> CP["Code point: U+00E9<br>(a number — Unicode)""]
    CP --> ENC["Encoded bytes: C3 A9<br>(a choice — UTF-8)""]
    ENC --> ST["Stored / transmitted / copied"]
    ST --> DEC["Decoded with the SAME scheme"]
    DEC --> GL["Font renders the glyph é"]
    DEC -.->|"wrong scheme here = mojibake"| X["Garbled output"]
```
*Figure: the keystroke-to-glyph pipeline. Unicode assigns the number; UTF-8 chooses the bytes; decoding must mirror encoding exactly — every mojibake is one broken mirror.*

## Common misconceptions

1. **"Unicode is an encoding."** Unicode assigns numbers to characters; UTF-8 (UTF-16, UTF-32 exist too) encodes those numbers as bytes. Confusing the two is the root of most mojibake.
2. **"One character always equals one byte."** Only for ASCII-in-UTF-8; `क` takes 3 bytes, emoji take 4 — byte counts ≠ character counts (why string "lengths" surprise programmers).
3. **"Garbled text means corrupted data."** Usually the bytes are intact; the *interpretation* was wrong — which is why re-decoding fixes what "repair tools" only pretend to.

## Check your understanding

1. Write the ASCII codes for `A`, `a`, `0` and explain the deliberate offset between them.
2. Why does UTF-8 dominate over UTF-16 for the web? Give two reasons.
3. A file shows `Ã©` where `é` should be. What happened and what fixes it?
4. How many bytes does `क` take in UTF-8, and why more than `A`?
5. Where in your editor/HTML workflow do you *declare* UTF-8?

## Lab link

[Lab 4 — Number Systems Workshop](../labs/lab-04-number-systems-workshop.md) — §4 breaks a deliberately miscoded file; due end of Week 8. **Midterm follows L16 — Modules 1–4.**

## References & further reading

1. ANSI. (1986). *ANSI X3.4: Coded Character Sets — 7-Bit American National Standard Code for Information Interchange (7-Bit ASCII)*. American National Standards Institute.
2. Unicode Consortium. (n.d.). *UTF-8, a transformation format of Unicode and ISO 10646* (FAQ). https://unicode.org/faq/utf_utf8.html — retrieved 2026.

## Summary

- A **code point** (Unicode) is the number for a character; an **encoding** (UTF-8) is the byte-level choice; the two questions are independent.
- **ASCII** survives inside UTF-8: code points 0–127 encode as identical single bytes — the compatibility that made UTF-8 the web's default.
- **Mojibake** is misinterpretation, not damage: name the symptom pattern, infer the wrong scheme, re-decode correctly.

## Homework

1. **Pipeline on paper:** trace your own full name through the pipeline — which characters are single-byte UTF-8, and which (if any) need two or more bytes? (10 min)
2. **Detective at home:** find or create one mojibake example (paste a non-ASCII character through any tool that mangles it), diagnose the failure class, and write the two-sentence fix report. (15 min)
3. **Dataset thinking:** a CSV of 5,000 student names opens with every 'ö' shown as 'Ã¶'. Write the first three steps of your response as the data custodian. *(Advanced extension: explain why "delete the bad rows" is the wrong response.)*

## Looking ahead

Text done; now the senses. L16 digitizes images, sound, and video — and meets compression, the reason streaming exists.
