# Teaching Guide — Module 4: Data and Digital Representation

**Module 4** · Stage 2 · 4 lectures (L13–L16) · 8 contact hours
Companion to lecture pages `L13`–`L16` under `docs/lectures/`. **Not published.** Answers to exit tickets appear here and nowhere student-facing.

> Symbols: **[Slide]** projector visual · **[Board]** board work · **[Demo]** live demonstration · **[Discuss]** think-pair-share or open discussion.

## Before this module

- [ ] Lab 4 (number-systems workshop) runs this module: check the handout's conversion tables against your preferred calculator tool (OS calculator programmer mode recommended).
- [ ] L15 needs four pre-made mojibake samples (UTF-8 read as Latin-1; Latin-1 read as UTF-8; double-encoded; wrong separator) — create them the day before, in the same text editor students have.
- [ ] L16's quality ladder: pre-export the same image/audio at 3–4 quality levels; note file sizes; test the projector's ability to show compression artefacts at hall distance.
- [ ] Programmer mode of the OS calculator works for both L13 and L14; verify it on the lecture-hall machine.

## Misconception warnings (module level)

1. **"Binary is a different kind of math."** It is the *same* positional notation with a two-symbol alphabet; the place-value table students met in primary school is the entire theory. Say this in L13 and again in L14.
2. **"Hexadecimal is a computer language."** It's a *shorthand for binary* — 4 bits per digit, nothing deeper. The nibble bridge kills this misconception permanently.
3. **"Computers are precise, so they don't make numeric mistakes."** Overflow and floating-point rounding are precision *limits*, not sloppiness; L14 gives both honest treatment.
4. **"More compression is always better."** Compression trades fidelity or compute for size; the use case decides, and L16's ladder makes the trade visible.

---

## L13 — Number Systems

**Teaching tips:**
- Open with the *place-value table they already know* (units, tens, hundreds) and simply change the base of each column — decimal becomes one instance of a family. Resist teaching conversion recipes before this lands.
- The relay (A2) awards method points: announce the marking rule before the race so "clean method" is not a surprise. It mirrors exam marking and students take it seriously.
- Hex is motivated by *programmers' sore eyes*: nobody wants to write 32-bit values in binary. Show one real colour code and one real memory address to make hex a tool, not a topic.

**Board / projector plan:**
- [Board] Place-value table with base 10 first, then the same table with base 2 and base 16 columns; keep it up all lecture.
- [Slide] The Mermaid conversion map from the lecture page's "Visual explanation."
- [Board] One worked conversion of *each route* left on the board through the practice segment.

**Suggested demonstration:** OS calculator in programmer mode: type 156 in decimal, watch binary and hex update live; toggle a bit and ask "what happened to the value?" — bit-flipping as computation preview.

**Misconception warnings:**
- "Binary numbers are 'backwards'." They read the same way — biggest place first; only the base changed.
- "Hex is base 16 *digits* so it needs 16 new numerals." It does (0–9, A–F) — the surprise is that A–F are just labels for ten-to-fifteen.
- "You must memorize conversions." No: you must own the *method*; the relay enforces exactly this.

**Discussion prompts:**
1. Why base 2 for hardware? What would base 10 hardware physically require? (Ten reliable voltage states — brittleness; two states are robust.)
2. Where have you already used base 60 and base 12 without fear? (Time; dozens) — base fluency is not new to you.
3. Why does one hex digit correspond to exactly 4 bits, and one octal digit to 3? (Powers: 16 = 2⁴, 8 = 2³.)

**Exit-ticket questions (with answers):**
1. *Convert 156 (decimal) to binary.* — 10011100 (128 + 16 + 8 + 4).
2. *Convert 101101 (binary) to decimal.* — 45 (32 + 8 + 4 + 1).
3. *Convert 0xA3 (hex) to decimal.* — 163 (10×16 + 3).
4. *Why do computers use base 2?* — Two states are the cheapest reliable electronic distinction; noise margin, simple logic.
5. *What does the colour code #FF0000 encode?* — Pure red: FF (255) red, 00 green, 00 blue.

---

## L14 — Numbers in Hardware

**Teaching tips:**
- Two's complement deserves a *derivation*, not a decree: start from the "flip and add one" recipe, show it works with the adder, then show the single-zero elegance. Students who see *why* never re-ask.
- The overflow casino from the lecture page is the best energy in the module; run it twice (8-bit slow, 4-bit fast) and keep a running "house wins" tally on the board.
- Floating point: keep the promise small and honest — sign, exponent, mantissa, "approximation with well-defined surprises." Deep IEEE 754 work belongs to later courses; here, awareness prevents the classic "0.1 + 0.2 ≠ 0.3" shock.

**Board / projector plan:**
- [Board] The 8-bit place-value strip (−128, 64, 32, 16, 8, 4, 2, 1) — the negative leading weight is the whole trick; write it once, circle it.
- [Slide] The Mermaid overflow-decision diagram from the lecture page's "Visual explanation."
- [Board] The "house wins" overflow tally, live during the casino.

**Suggested demonstration:** Programmer-mode calculator again: switch 5 to signed/negative view, flip −5's bits by hand on the board, verify against the calculator; then add 127 + 1 in 8-bit signed and let the class predict before pressing equals.

**Misconception warnings:**
- "The minus sign is stored somewhere." There is no sign bit *added on*; the leading weight is negative — same bits, different interpretation.
- "Overflow is a crash." Silent wrap is the dangerous case; historical date/counter bugs are the story to tell.
- "Floating point is 'broken math'." It's a *specified approximation* (IEEE 754); the surprises are reproducible and documented.

**Discussion prompts:**
1. Why does one adder circuit handle signed and unsigned addition identically? (Two's complement makes addition rules coincide.)
2. Your phone's step counter: which failure mode hurts it at 2 a.m. after a marathon day? (Counter overflow — playful but real.)
3. Where did you personally meet a rounding surprise this month? (Bank cents, spreadsheet percentages — collect stories.)

**Exit-ticket questions (with answers):**
1. *Encode −5 in 8-bit two's complement.* — +5 = 00000101 → flip 11111010 → +1 → 11111011.
2. *Range of 8-bit signed integers.* — −128 to +127.
3. *What is 127 + 1 in 8-bit signed, and what is the behaviour called?* — Wraps to −128; overflow (silent wrap).
4. *Why does hardware prefer two's complement?* — One adder serves signed and unsigned; subtraction becomes addition; unique zero.

---

## L15 — Character Encoding

**Teaching tips:**
- The keystroke→glyph pipeline is the lecture's spine; draw it once and keep it visible while the mojibake forensics run — every diagnosis is a *broken link in that chain*.
- ASCII's 128 characters and 'A' = 65 are worth memorizing as anchors; say plainly that Unicode assigns *numbers*, UTF-8 chooses *bytes*, and the two questions are independent.
- The encoding detective activity needs the four samples on the projector *and* the patterns table from the lecture page; teams diagnose from symptoms like physicians, not by trial-and-error in editors.

**Board / projector plan:**
- [Board] Pipeline: key press → code point (Unicode) → encoded bytes (UTF-8) → storage/web → decode → font glyph; each lab's breakage point gets a red X as samples appear.
- [Slide] The Mermaid pipeline from the lecture page's "Visual explanation."
- [Board] Two-column symptom table for mojibake classes as the detective round proceeds.

**Suggested demonstration:** Live editor: type an é, switch file encoding between UTF-8 and Latin-1, reopen with the other — mojibake appears on demand; then fix it by re-decoding correctly (no data was ever "corrupted" — interpretation was wrong).

**Misconception warnings:**
- "The file is corrupted." Usually it is *misinterpreted*, not damaged; re-decoding restores sense. This distinction prevents panic.
- "Unicode = UTF-8." Code points are the numbers; UTF-8 is one (dominant) byte-level choice among several.
- "Emoji are images." They're Unicode code points like any letter — which is why they survive copy-paste into plain text.

**Discussion prompts:**
1. Why did UTF-8 win the web where older encodings fragmented? (ASCII-compatible, self-synchronizing, universal coverage — accept any two.)
2. A dataset of student names loses every é, ñ, and ع. Which pipeline stage failed, and what does this cost downstream? (Encoding stage; real people's data integrity — the DS ethics hook.)
3. Why does one missing font turn correct text into boxes? (Decode succeeded; *rendering* lacks the glyph — a different stage entirely.)

**Exit-ticket questions (with answers):**
1. *List the pipeline stages from keystroke to displayed glyph.* — Key press → code point → encoded bytes → stored/transmitted → decoded → font glyph.
2. *ASCII values of 'A' and 'a'.* — 65 and 97 (case differs by one bit — flag the elegance).
3. *Why is UTF-8 "ASCII-compatible"?* — Code points 0–127 encode as exactly the same single bytes as ASCII.
4. *You see Ã© where é was typed. What happened?* — UTF-8 bytes interpreted as Latin-1 (accept: wrong-decoding class of mojibake).

---

## L16 — Multimedia and Compression

**Teaching tips:**
- The digitization pipeline (sample → quantize → encode) covers *all three media*; draw it once for audio, then reuse for images (spatial sampling = pixels) and video (temporal sampling = frames). One pipeline, three costumes — say so explicitly.
- The quality ladder needs a secret ballot: individual acceptability votes *before* discussion prevents anchoring on the first confident voice. Tabulate votes against file sizes on one slide.
- Raster vs vector is a *tool-choice* lecture moment: one logo, shown zoomed to 800% in both formats, ends the debate faster than any definition.

**Board / projector plan:**
- [Board] The pipeline with three labelled rows (audio/image/video) showing what varies per medium (rate/pixel-grid/frame-rate).
- [Slide] The Mermaid pipeline from the lecture page's "Visual explanation."
- [Board] The ladder's vote table: medium × quality level × class votes, beside file sizes.

**Suggested demonstration:** Same logo as SVG and PNG zoomed progressively to 800%: raster blocks, vector crisp; then the audio ladder's smallest files played aloud — perceptual loss becomes audible, not just describable.

**Misconception warnings:**
- "PNG is 'higher quality' than JPEG." PNG is *lossless*; for photographs JPEG's lossy trade is usually the right tool — format choice is per-use-case, not a loyalty question.
- "Deleting pixels/samples deletes 'the real thing'." Digitization is already an approximation; lossy compression discards what perception misses — the ladder shows exactly where that becomes visible.
- "Compression creates information." It only removes or rewrites; generators (Module 7's AI) synthesize, codecs compress — keep the boundary clean.

**Discussion prompts:**
1. Why does 44.1 kHz sampling appear everywhere audio is sold? (CD legacy; Nyquist-class reasoning at awareness level — anything above ~20 kHz human hearing.)
2. Your project's dashboard screenshot: raster or vector export, and why? (Both defensible; resolution-independence argues vector, embedding argues raster.)
3. Where does compression interact with Module 6? (Everything the web ships is compressed — bandwidth is the why.)

**Exit-ticket questions (with answers):**
1. *Define pixel, sampling rate, and frame in one line each.* — Pixel: smallest addressable image element; sampling rate: measurements per second of a wave; frame: one still image in a video sequence.
2. *Raster vs vector for a university logo that must scale from badge to banner.* — Vector: shapes redraw at any scale, no blockiness.
3. *Lossless vs lossy for archiving a scanned transcript.* — Lossless (every detail must survive; legal document).
4. *Why JPEG for photos but diagrams as PNG?* — Photos tolerate imperceptible loss for big savings; diagrams' sharp edges/text suffer visible artefacts, and lossless keeps lines crisp.
