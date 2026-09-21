# Module 4 Slide Decks — L13–L16

**Format:** One `## S# · Title` per slide; `**Notes:**` carry [~minutes], TALK, ASK, MISC, DEMO, TRAN, EXT, TROUBLE cues. Run sheets allocate the full 120 minutes.

---

## L13 — Number Systems (Slides + Speaker Notes)

**Resources:** OS calculator in programmer mode (tested on lecture-hall machine); A2 relay cards/method-marking sheet; colour-code examples.

### Run sheet (120 min)

| Block | Slides | Time |
|---|---|---|
| Place value you already own + objectives | S1–S2 | 10 |
| Binary | S3–S4 | 16 |
| Hex and octal | S5–S6 | 14 |
| The four conversion routes | S7–S8 | 16 |
| Activity: Number relay (A2) | S9 | 28 |
| Concept check | S10 | 12 |
| Summary + exit ticket | S11–S12 | 12 |
| Buffer | — | 12 |

### Slides

# L13 · Number Systems
**Module 4 · Stage 1 · 2 hours**

## S1 · You already know base 10
**Notes:** [~7] TALK: the primary-school place-value table on the board — units, tens, hundreds; today we only *change the base of each column*. ASK: "What does the '2' mean in 245?" MISC: "binary is a different kind of math" — module-level warning; kill it in the first ten minutes. TRAN: "Change one number."

## S2 · Today
- One notation, many bases · binary, hex, octal · four conversion routes
**Notes:** [~3] TALK: promise the relay with method points — mirrors exam marking (guide tip). TRAN: base 2.

## S3 · Binary: why two states
- Two reliable states beat ten fragile ones
**Notes:** [~8] TALK: hardware motivation — noise margins, simple logic (guide's discussion answers); connect back to L02's transistors. ASK: "What would base-10 hardware physically need?" MISC: none. TRAN: "Reading binary."

## S4 · Reading binary
- Place values 1, 2, 4, 8… — decompose by place
**Notes:** [~8] TALK: one worked conversion, method visible; the *method* is the deliverable, not the answer. ASK: "Convert 101101 with me — talking aloud." MISC: "binary reads backwards" — biggest place first, same as decimal; the feel differs, the rule doesn't. TRAN: "Shorthand time."

## S5 · Hexadecimal: programmers' eyes
- 16 digits (0–9, A–F) · one hex digit = 4 bits
**Notes:** [~7] TALK: nibble bridge; A–F are labels for ten-to-fifteen, nothing deeper (guide). ASK: "Why do programmers prefer hex over binary?" MISC: "hex is a computer language" — it's *shorthand for binary*; computers never see it. TRAN: "Where you've met it."

## S6 · Hex in the wild
- Colour codes · memory addresses · error codes
**Notes:** [~7] TALK: decode #FF0000 live; one real address. DEMO: programmer-mode calculator — type 156, watch binary/hex update, toggle a bit (module guide demo). ASK: "What happened to the value when I flipped that bit?" MISC: none. TRAN: "The four routes."

## S7 · The conversion map
- Binary is the hub; regroup by 4 (hex), by 3 (octal)
**Notes:** [~8] TALK: project the lecture page's figure; the hub idea means four routes, one skeleton. ASK: "Why 4 bits per hex digit and 3 per octal digit?" (Powers: 16=2⁴, 8=2³.) MISC: none. TRAN: "Two routes worked."

## S8 · Worked: decimal→binary, binary→hex
- Divide by 2, read remainders · regroup by nibbles
**Notes:** [~8] TALK: leave both worked conversions on the board through the relay (guide's plan). ASK: "Which route would you use for 0xA3→decimal?" MISC: recipe-memorizers — the *place-value* explanation is the durable one. TRAN: "Race time."

## S9 · Activity — Number relay (A2, 28 min)
Teams race conversions · method points awarded
**Notes:** [~28] TALK: per the A1…—per the A2 handout; announce marking rule *before* the race (guide tip). ASK (circulating): "Talk me through your method, not your answer." MISC: sloppy-but-right answers — that's what method points are for; award visibly. TROUBLE: pace uneven — run the last leg as a whole-class solve. EXT: a leg in octal. TRAN: "Method, not luck."

## S10 · Quick check
1. 156 (dec) → binary.
2. 101101 (bin) → decimal.
3. 0xA3 → decimal.
**Notes:** [~12] TALK: write-pair-resolve with method shown — the relay's rule applies to the check too. MISC: Q1 — a silent "10011100" with no work gets half credit; the method is graded. TRAN: "Summary."

## S11 · Summary
- One notation, many bases · binary is the hub · hex is the shorthand
**Notes:** [~6] TALK: exam skeleton; fluency here removes a whole class of confusion for the degree. TRAN: exit ticket.

## S12 · Exit ticket
**Decode #1A2B3C into its three channel values (decimal) — show method.**
**Notes:** [~6] TALK: expected: 26, 43, 60. Sort slips; method-less answers flag the conversion clinic need before Lab 4.

---

## L14 — Numbers in Hardware (Slides + Speaker Notes)

**Resources:** programmer-mode calculator; the overflow casino board tally; the 8-bit place-value strip.

### Run sheet (120 min)

| Block | Slides | Time |
|---|---|---|
| Fluency check + objectives | S1–S2 | 8 |
| Unsigned integers | S3 | 12 |
| Two's complement, derived | S4–S6 | 24 |
| Overflow casino | S7 | 22 |
| Floating point, honestly | S8–S9 | 16 |
| Concept check | S10 | 12 |
| Summary + exit ticket | S11–S12 | 12 |
| Buffer | — | 14 |

### Slides

# L14 · Numbers in Hardware
**Module 4 · Stage 1 · 2 hours**

## S1 · L13's fluency, one question
**Notes:** [~5] TALK: one quick binary read from an exit slip; today: what happens when numbers meet real, finite hardware. ASK: none. TRAN: "Counting in 8 bits."

## S2 · Today
- Unsigned vs signed · two's complement · overflow · floating point
**Notes:** [~3] TALK: promise the casino. TRAN: unsigned first.

## S3 · Unsigned integers
- All bits magnitude: 0…255 in 8 bits
**Notes:** [~12] TALK: the 8-bit strip with positive weights; addition works, subtraction doesn't — the problem statement. ASK: "How would *you* represent −5 with no minus sign available?" MISC: none. TRAN: "Hardware's answer."

## S4 · Two's complement: the idea
- Give the leading place a *negative* weight
**Notes:** [~10] TALK: the derivation, not the decree (guide tip) — write −128, 64, 32… strip once, circle the negative weight. ASK: "What's 10000000 now?" (−128.) MISC: "a sign bit is stored somewhere" — no sign *added*; the leading weight IS negative. TRAN: "The recipe."

## S5 · The flip-and-add-one recipe
- Human shortcut to the same encoding
**Notes:** [~8] TALK: −5 worked two ways: recipe *and* the negative-weight strip — they agree; that agreement is the proof-feeling. ASK: "Encode −42 with me." MISC: recipe-without-understanding — acceptable short-term; the strip is the repair. TRAN: "Why hardware loves it."

## S6 · Why hardware prefers it
- One adder serves signed and unsigned; unique zero
**Notes:** [~6] TALK: the L14 promise link — L18's adder will keep this promise in silicon. ASK: "What does 11111111 + 1 give in 8 bits?" (00000000 — wrap; bridge to overflow.) MISC: none. TRAN: "The casino opens."

## S7 · Activity — Overflow casino (22 min)
8-bit signed addition chains · first wrap calls it · class verifies
**Notes:** [~22] TALK: per the lecture page's activity; run 8-bit slow then 4-bit fast (guide tip); keep the house-wins tally on the board. ASK (during): "Predict before you add — wrap or not?" MISC: computing without predicting — prediction is the point; the tally makes it visible. TROUBLE: wraps too rare — drop to 4 bits sooner. EXT: find the *largest* pair that doesn't wrap. TRAN: "When numbers aren't whole."

## S8 · Real numbers, honestly
- Fixed-point, then floating point: sign, exponent, mantissa
**Notes:** [~9] TALK: awareness level per the lecture page's 14.4; the 0.1+0.2 surprise named now. ASK: "Why can't 0.1 be exact in binary?" MISC: "computers are precise so they don't err" — precision has *limits*; the surprises are documented (IEEE 754), not sloppiness. TRAN: "The standard."

## S9 · IEEE 754 in one line
- A specified approximation — reproducible, documented surprises
**Notes:** [~7] TALK: one line, as promised; deep IEEE work deferred to later courses — say so. ASK: none. MISC: none. TRAN: "Check the width."

## S10 · Quick check
1. Encode −5 in 8-bit two's complement.
2. Range of 8-bit signed?
3. 127 + 1 = ? and what's the behaviour called?
**Notes:** [~12] TALK: write-pair-resolve. MISC: Q1 — recipe slips work; the strip explanation earns the extension nod. Q3 — "128" answers are the wrap; make the class who wrote it explain *where* their arithmetic left the representable range. TRAN: "Summary."

## S11 · Summary
- Two's complement: negative weight, one adder, unique zero · overflow wraps · floats approximate
**Notes:** [~6] TALK: exam skeleton; the 2038 problem is the homework story — mention it. TRAN: exit ticket.

## S12 · Exit ticket
**Why does the *same* adder circuit correctly add signed and unsigned numbers?**
**Notes:** [~6] TALK: expected: two's complement makes the arithmetic coincide — same bit patterns, correct interpretation. This answer reappears on the L18 exam-relevant path; keep slips.

---

## L15 — Character Encoding (Slides + Speaker Notes)

**Resources:** four pre-made mojibake samples (made day before, guide prep); live editor for the encoding switch demo; pipeline diagram.

### Run sheet (120 min)

| Block | Slides | Time |
|---|---|---|
| From L13: numbers as letters + objectives | S1–S2 | 8 |
| The pipeline | S3 | 12 |
| ASCII | S4 | 10 |
| Unicode and UTF-8 | S5–S6 | 16 |
| Encoding detective activity | S7 | 24 |
| Mojibake forensics debrief | S8 | 10 |
| Concept check | S9 | 12 |
| Summary + exit ticket | S10–S11 | 12 |
| Buffer | — | 16 |

### Slides

# L15 · Character Encoding
**Module 4 · Stage 1 · 2 hours**

## S1 · Numbers wearing letters
**Notes:** [~5] TALK: L13 made fluency in number systems; a character *is* a number — today, the agreement about which numbers mean which letters. ASK: none. TRAN: "The pipeline."

## S2 · Today
- Keystroke → glyph: one pipeline, many breakage points
**Notes:** [~3] TALK: promise the detective game. TRAN: pipeline drawn.

## S3 · The pipeline
- Key → code point → encoded bytes → stored/sent → decoded → glyph
**Notes:** [~12] TALK: draw once, keep visible all hour (guide tip); every diagnosis later is a broken link *in this chain*. ASK: "Which link do you think breaks most in the wild?" (Decode — coming.) MISC: "the file is corrupt" reflex — usually *interpretation*, not damage; name it now, prove it at S7. TRAN: "The foundation."

## S4 · ASCII: the 128-character foundation
- 7 bits · 'A' = 65, 'a' = 97 — one bit apart
**Notes:** [~10] TALK: the anchors worth memorizing; the one-bit case difference is the elegance to point at. ASK: "Why would English-centric computing accept 128 characters — and who does that leave out?" MISC: none. TRAN: "The universal answer."

## S5 · Unicode: numbers for everyone
- Code points: one number per character — the world's writing systems
**Notes:** [~8] TALK: Unicode assigns *numbers*; encoding is a separate question — the independence is the lecture's key distinction (guide warning). ASK: "Is é a code point or bytes?" MISC: "Unicode = UTF-8" — the conflation to kill; say both halves separately. TRAN: "The byte-level choice."

## S6 · UTF-8: the web's choice
- Variable-length bytes; ASCII-compatible (0–127 identical)
**Notes:** [~8] TALK: why UTF-8 won — ASCII-compatible, self-synchronizing, universal (accept any two, guide). DEMO: live editor, é switched between UTF-8 and Latin-1, reopened wrong — mojibake on demand, then *fixed* by re-decoding. ASK: "Was the file ever damaged?" MISC: none. TRAN: "Detective time."

## S7 · Activity — Encoding detective (24 min)
Four garbled samples · name the failure class, the wrong encoding, the fix
**Notes:** [~24] TALK: per the lecture page's activity; the four samples from the guide's prep list; diagnose from *symptoms*, not editor trial-and-error. ASK (circulating): "Which pipeline link carries the red X?" MISC: teams re-encoding randomly — ban it; symptoms first. TROUBLE: a sample stumps everyone — reveal its pipeline stage; the reasoning, not the answer, is graded. TRAN: "Forensics debrief."

## S8 · Debrief: the symptom table
- Pattern → wrong scheme → fix
**Notes:** [~10] TALK: two-column debrief per the guide's plan; the four classes stated as *patterns to recognize*. ASK: "Which class would you catch before submitting a dataset?" MISC: none. TRAN: "Check the chain."

## S9 · Quick check
1. List the pipeline stages in order.
2. 'A' and 'a' — values, and the relationship?
3. Ã© where é was typed — what happened?
**Notes:** [~12] TALK: write-pair-resolve. MISC: Q3 — "corrupted file" answers are the S3 misconception resurfacing; route them back through the decode link. TRAN: "Summary."

## S10 · Summary
- Code points ≠ encoding · ASCII inside UTF-8 · mojibake is misinterpretation
**Notes:** [~6] TALK: exam skeleton; "it's just characters" is the dangerous sentence — the homework names it. TRAN: exit ticket.

## S11 · Exit ticket
**A CSV of 5,000 names shows Ã¶ for every ö. Which pipeline link failed — and is the data damaged?**
**Notes:** [~6] TALK: expected: decode link; *not* damaged — re-decode restores. The custodian-response version is the homework's advanced item; keep slips for L26's cleaning segment.

---

## L16 — Multimedia and Compression (Slides + Speaker Notes)

**Resources:** pre-exported quality ladders (image/audio/video, guide prep); SVG vs PNG logo zoom demo; midterm is next — closing slide notes it.

### Run sheet (120 min)

| Block | Slides | Time |
|---|---|---|
| Midterm framing + objectives | S1–S2 | 10 |
| One pipeline, three media | S3–S4 | 18 |
| Raster vs vector | S5 | 10 |
| Lossless vs lossy | S6 | 10 |
| Quality-ladder activity | S7 | 24 |
| Format decisions | S8 | 10 |
| Concept check | S9 | 12 |
| Summary + exit ticket | S10–S11 | 12 |
| Buffer | — | 14 |

### Slides

# L16 · Multimedia and Compression
**Module 4 · Stage 1 · 2 hours**

## S1 · Module 4 closes; midterm next
**Notes:** [~7] TALK: midterm scope (Modules 1–4) named honestly; today is the last new content — media. ASK: "Questions on exam scope before we start — then none until the review slide." MISC: none. TRAN: "From characters to pixels."

## S2 · Today
- One digitization pipeline · raster vs vector · lossless vs lossy
**Notes:** [~3] TALK: promise the ladder vote — secret ballot, then argument. TRAN: the pipeline.

## S3 · The pipeline
- Sample → quantize → encode: images sample space, audio time, video both
**Notes:** [~10] TALK: one pipeline, three costumes (guide tip) — draw for audio, re-use for images/video. ASK: "What is the audio equivalent of a pixel?" MISC: none. TRAN: "The parameters."

## S4 · Fidelity parameters
- Resolution · sampling rate · bit depth · frame rate — the fidelity floor
**Notes:** [~8] TALK: each parameter named with its medium; the floor idea — below it, information is *gone*. ASK: "Which parameter did our projector fail at hall distance?" MISC: none. TRAN: "Two image tribes."

## S5 · Raster vs vector
- Grid of pixels vs redrawable geometry — the 800% zoom test
**Notes:** [~10] TALK: the logo demo (module guide) — SVG crisp, PNG blocks at 800%; ends the debate faster than definitions. ASK: "Which for the university logo? Which for the campus photo?" MISC: "PNG is higher quality than JPEG" — *lossless*, not *better*; format choice is per-use-case. TRAN: "Now compression."

## S6 · Lossless vs lossy
- Every bit vs what perception misses
**Notes:** [~10] TALK: the ladder's logic stated before the vote; lossy discards perceptually-missed information *by design*. ASK: "Which for the scanned transcript? Which for the podcast?" MISC: "compression creates information" — it only removes/rewrites; keep the boundary clean (module warning). TRAN: "Vote."

## S7 · Activity — Quality ladder (24 min)
Secret ballot per rung · then argument · tabulated vs file sizes
**Notes:** [~24] TALK: secret ballot *before* discussion (guide tip); tabulate votes against sizes on one slide; play the smallest audio rungs aloud. ASK (during): "What would make you accept a lower rung?" (Use case — bandage photo vs evidence photo.) MISC: anchoring on the first confident voice — the ballot exists to stop it. TROUBLE: projector can't show artefacts — the *file size* column carries the argument. TRAN: "Decisions, then."

## S8 · Format decisions, defended
- Four artefacts, four formats, four one-sentence justifications
**Notes:** [~10] TALK: the homework's format-court done live for two of four; photo→lossy, certificate→lossless, logo→vector, screenshot→lossless/light-lossy. ASK: "Defend the opposite choice for one of these." MISC: none. TRAN: "Check the module."

## S9 · Quick check
1. Pixel, sampling rate, frame — one line each.
2. Raster or vector for badge-to-banner scaling?
3. Lossless or lossy for the scanned transcript — why?
**Notes:** [~12] TALK: write-pair-resolve. MISC: Q2 — "both work" is evasion; the *justification* (resolution independence) is the answer. TRAN: "Summary — and exam scope."

## S10 · Summary
- One pipeline · parameters set the floor · formats are use-case decisions
**Notes:** [~6] TALK: exam skeleton; then the review slide: Modules 1–4, the check-question sets as the study spine, practice quizzes Q01–Q07. ASK: final scope questions. TRAN: exit ticket.

## S11 · Exit ticket
**One artefact from your own week (photo, scan, recording): name its right format and the one-line justification.**
**Notes:** [~5] TALK: any defensible format+justification pair earns credit; the justification is what you mark. Good luck on the midterm — say it once, mean it.
