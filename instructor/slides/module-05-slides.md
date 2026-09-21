# Module 5 Slide Decks — L17–L20

**Format:** One `## S# · Title` per slide; `**Notes:**` carry [~minutes], TALK, ASK, MISC, DEMO, TRAN, EXT, TROUBLE cues. Run sheets allocate the full 120 minutes.

---

## L17 — Boolean Logic and Truth Tables (Slides + Speaker Notes)

**Resources:** truth-table worksheets (blank 2- and 3-input tables, guide prep); spreadsheet with the registration-rule demo ready.

### Run sheet (120 min)

| Block | Slides | Time |
|---|---|---|
| Registration policy argument + objectives | S1–S2 | 12 |
| The operators | S3–S4 | 16 |
| Truth tables: the 2ⁿ discipline | S5–S6 | 16 |
| De Morgan | S7 | 10 |
| Activity: Truth-Table Design Sprint (A3) | S8 | 28 |
| Concept check | S9 | 12 |
| Summary + exit ticket | S10–S11 | 12 |
| Buffer | — | 14 |

### Slides

# L17 · Boolean Logic and Truth Tables
**Module 5 · Stage 1 · 2 hours**

## S1 · The registration policy
**Notes:** [~9] TALK: open with the policy, not the definition (guide tip): "Register if prerequisite AND fees, OR permission." Let the class argue edge cases — they are doing Boolean algebra unlabelled. ASK: "Who should be admitted? Defend one hard case." MISC: none. TRAN: "You've been doing this for ten minutes — here are its names."

## S2 · Today
- Two values, three operators (+XOR) · tables · De Morgan
**Notes:** [~3] TALK: smallest complete theory in the course — total verifiability. TRAN: operators.

## S3 · AND, OR, NOT
- Built from the room's own policy examples
**Notes:** [~10] TALK: three tables built row by row from *student* examples (guide plan). ASK: "OR: both true — true or false?" MISC: the exclusive-OR reflex — module warning #1; police it forever, name XOR next slide. TRAN: "The everyday 'or'."

## S4 · XOR: the everyday or
- Exactly one true — soup or salad
**Notes:** [~6] TALK: light pairs, turn signals; the two operators now have separate names. ASK: "Which operator is your phone's face-unlock-or-passcode?" (OR — either suffices.) MISC: none. TRAN: "Complete verification."

## S5 · Truth tables: 2ⁿ rows
- The count-down binary ordering — mechanically, every time
**Notes:** [~10] TALK: the discipline is mechanical (guide tip); incomplete tables are the classic exam error — the discipline prevents them. ASK: "Why does the third input double the rows?" MISC: "tables are busywork" — *complete verification by construction*; nothing escapes. TRAN: "One compound, together."

## S6 · Compound tables, worked
- A AND (NOT B) — all four rows, method visible
**Notes:** [~6] TALK: one full table left on the board through guided practice (guide plan). ASK: "Add the intermediate column — what does it buy?" MISC: none. TRAN: "Negation's grammar."

## S7 · De Morgan's laws
- NOT pushes through brackets and *flips* the operator
**Notes:** [~10] TALK: demonstrate-then-use same hour (guide tip); proofs belong to later courses. ASK: "Rewrite NOT(A OR B) your own way." MISC: NOT-distributes-without-flipping — drill one failing example on the board. TRAN: "Sprint time."

## S8 · Activity — Truth-Table Design Sprint (A3, 28 min)
Teams design a voting/eligibility rule · defend its table against attack cases
**Notes:** [~28] TALK: per the A3 handout; rival-team attack cases are the assessment engine. ASK (circulating): "Which row is your rule's weakness?" MISC: over-complex rules — simpler rules with *complete* tables score better; say the rubric. TROUBLE: stalled teams — offer the registrar's real rule as a starting artefact. EXT: express the rival's rule with De Morgan and show equivalence. TRAN: "Check yourselves."

## S9 · Quick check
1. Full table for A AND (NOT B).
2. Everyday "or" maps to which operator — and when does it not?
3. NOT (A OR B) = ? (De Morgan)
**Notes:** [~12] TALK: write-pair-resolve. MISC: Q2 — "always XOR" overshoot; exclusive *when both cannot hold* is the precise answer. TRAN: "Summary."

## S10 · Summary
- Two values, four operators, complete verification · De Morgan's flip
**Notes:** [~6] TALK: exam skeleton; name the through-line — L18 wires these into silicon, L19 puts them in spreadsheets, L25 into queries. TRAN: exit ticket.

## S11 · Exit ticket
**Write this as a Boolean expression and build its table: 'admitted if (prerequisite AND fees) OR permission.'**
**Notes:** [~6] TALK: the S1 policy, now formal — the loop closes; slips show whether the names stuck to the intuitions. 8 rows expected; missing rows are the discipline flag.

---

## L18 — Logic Gates and Simple Circuits (Slides + Speaker Notes)

**Resources:** Lab 5 simulator tested on lab image + offline browser fallback; gate-symbol gallery; NAND construction tree.

### Run sheet (120 min)

| Block | Slides | Time |
|---|---|---|
| Operators→symbols bridge + objectives | S1–S2 | 10 |
| Gate gallery | S3 | 12 |
| NAND universality | S4–S5 | 16 |
| Half adder | S6–S7 | 16 |
| Lab 5 = the activity | S8 | 30 |
| Concept check | S9 | 12 |
| Summary + exit ticket | S10–S11 | 12 |
| Buffer | — | 12 |

### Slides

# L18 · Logic Gates and Simple Circuits
**Module 5 · Stage 1 · 2 hours**

## S1 · Yesterday's tables, today in silicon
**Notes:** [~7] TALK: the bridge sentence — each table row now costs nanoseconds and silicon (guide tip); keep L17's operator tables visible beside the new symbols. ASK: "Predict: which operator computes 1+1 in binary?" MISC: none. TRAN: "The symbols."

## S2 · Today
- Gates · universality · the half adder — Lab 5 is the activity
**Notes:** [~3] TALK: promise that today's constructions are the lab's answer-key-in-spirit (never in handout). TRAN: gallery.

## S3 · The gate gallery
- AND, OR, NOT, XOR, NAND, NOR — symbols beside yesterday's tables
**Notes:** [~12] TALK: one-to-one placement (guide plan); NAND/NOR introduced as "the opposites". ASK: "Which symbol is yesterday's AND with a NOT glued on?" MISC: symbol confusion — shapes repeat; *the bubble* is the NOT. TRAN: "One gate to build them all."

## S4 · NAND is universal
- NOT from tied inputs · AND = NAND + NOT · OR via De Morgan
**Notes:** [~10] TALK: *show* the constructions (guide tip), never assert; the tree on the board. ASK: "Why would manufacturers love one-gate-suffices?" MISC: "universality is a party trick" — it's a manufacturing consequence; one process, any circuit. TRAN: "The payoff circuit."

## S5 · Universality, drawn
- NOT → AND → OR as nested NANDs — redraw from memory in the homework
**Notes:** [~6] TALK: leave the tree up; the homework asks for it from memory. ASK: none. MISC: none. TRAN: "Where arithmetic begins."

## S6 · The half adder
- Sum = XOR · Carry = AND — column addition in two gates
**Notes:** [~10] TALK: the module's best "oh" moment (guide tip) — yesterday's operators assemble L14's promise. ASK: "Which gate is the carry *and why*?" (Both-one-means-carry: AND.) MISC: "XOR is exotic" — it's the sum bit of every addition. TRAN: "Verify the promise."

## S7 · The adder keeps L14's promise
- Same circuit adds signed and unsigned — the two's-complement payoff, in silicon
**Notes:** [~6] TALK: connect explicitly to L14's exit ticket; the loop across four lectures closes. ASK: "What did the carry *mean* for unsigned? For signed?" (Overflow into the next column; wrap detection.) MISC: none. TRAN: "Lab 5."

## S8 · Activity — Lab 5 in session (30 min)
Build XOR-from-NANDs · half adder · verify every truth-table row
**Notes:** [~30] TALK: the lab *is* the activity (lecture page); students bring yesterday's 2ⁿ discipline. ASK (circulating): "Which row failed — and which wire owns it?" MISC: wiring-by-trial — require the drawn circuit *before* building. TROUBLE: simulator down — offline browser fallback from the prep list. EXT: full adder construction for fast pairs. TRAN: "Check the hour."

## S9 · Quick check
1. Half adder's outputs and their gates.
2. Why is NAND universal?
3. Combinational means…?
**Notes:** [~12] TALK: write-pair-resolve. MISC: Q3 — "no clock" is close; sharpen to *output depends only on current inputs*. TRAN: "Summary."

## S10 · Summary
- Gates embody operators · NAND suffices · the half adder computes
**Notes:** [~5] TALK: exam skeleton; name the module through-line once more (L17→L18→L19). TRAN: exit ticket.

## S11 · Exit ticket
**Draw the half adder from memory — two gates, two outputs, labelled.**
**Notes:** [~6] TALK: slips are the lab's readiness check; a missing carry is the diagnostic to note before the lab session proper.

---

## L19 — Productivity: Documents and Spreadsheets (Slides + Speaker Notes)

**Resources:** projector; grade-book starter file with realistic dirt (guide prep); one deliberately broken lookup for the live failure demo.

### Run sheet (120 min)

| Block | Slides | Time |
|---|---|---|
| Operators→functions bridge + objectives | S1–S2 | 8 |
| Documents: styles beat formatting | S3–S4 | 18 |
| Spreadsheets: references and functions | S5–S7 | 24 |
| Charts: honest pictures | S8–S9 | 12 |
| Lab 6 launch activity | S10 | 28 |
| Concept check | S11 | 12 |
| Summary + exit ticket | S12–S13 | 12 |
| Buffer | — | 6 |

### Slides

# L19 · Productivity: Documents and Spreadsheets
**Module 5 · Stage 1 · 2 hours**

## S1 · Yesterday's operators, in your spreadsheet
**Notes:** [~5] TALK: AND/OR/NOT are *literal spreadsheet functions* — the bridge from theory to the tools your degree is written in. ASK: "Where did you last use AND in real life?" TRAN: "Documents first."

## S2 · Today
- Structure beats formatting · references and functions · honest charts — Lab 6 launches
**Notes:** [~3] TALK: split the hour cleanly (guide tip): 35/45/15 + launch. TRAN: styles.

## S3 · Styles are the document
- One style edit restyles everything — watch the ToC update itself
**Notes:** [~10] TALK: the restyle demo (guide's S3 demo); the room notices the ToC. ASK: "What did formatting *cost* you before styles?" MISC: "styling is the document" — styles are; formatting is the costume. TRAN: "The machinery."

## S4 · ToC, tracked changes
- Automatic structure · attribution and audit trail
**Notes:** [~8] TALK: tracked changes as the semantic-layer audit (module warning); link to L20's versioning. ASK: "What does tracked changes change about group work?" MISC: none. TRAN: "The grid."

## S5 · References: the grammar
- Relative moves with you · absolute ($A$1) stays pinned
**Notes:** [~10] TALK: the fixed-address-vs-moving-street picture (guide's board plan); where marks are won and lost in Lab 6. ASK: "Which reference kind for a tax-rate cell?" MISC: "absolute references are for perfectionists" — they're the difference between correct copies and silent corruption. TRAN: "The core functions."

## S6 · Functions: SUM, AVERAGE, IF, lookup
- Compose them — the operators from L17 live here
**Notes:** [~7] TALK: IF as the decision function (L17 bridge); lookup against the grading table. ASK: "Which function turns a score into pass/fail?" MISC: none. TRAN: "Watch me fail."

## S7 · Demo: the deliberate failure
- Unanchored lookup dragged wrong — read the error aloud
**Notes:** [~7] TALK: the planned failure (guide tip) — leave it on screen; the fix with `$` lands harder. ASK: "What exactly went wrong, in reference terms?" MISC: none. TRAN: "Charts."

## S8 · Charts are arguments
- Bar for comparison · line for trend · the pie's narrow domain
**Notes:** [~7] TALK: chart-choice discipline from the lecture page's 19.3; bring the dishonest twin (truncated axis) for contrast. ASK: "When is a pie chart *right*?" (Few categories, sums to 100% — rare but real.) MISC: "the chart shows what the data shows" — choice *is* an argument. TRAN: "Lab 6."

## S9 · Lab 6 briefing
- Grade-book: references, IF, lookups, one defensible chart
**Notes:** [~5] TALK: point at the handout; the starter file's dirt is deliberate. ASK: none. TRAN: activity.

## S10 · Activity — Lab 6 in session (28 min)
Build through the IF stage · bring one failure to next class
**Notes:** [~28] TALK: in-lecture portion per the lab handout; the graded skill is the reference discipline. ASK (circulating): "Show me your `$` and tell me why it's there." MISC: formatting-first students — data first, costume later. TROUBLE: starter file won't load — the CSV fallback in the lab's prep notes. EXT: the lookup stage early for fast pairs. TRAN: "Check the tools."

## S11 · Quick check
1. Relative vs absolute — one sentence each.
2. The pass/fail function?
3. Line or bar for monthly rainfall — why?
**Notes:** [~12] TALK: write-pair-resolve. MISC: Q3 — "either" is evasion; *time trend* is the argument. TRAN: "Summary."

## S12 · Summary
- Styles carry meaning · references are the grammar · charts argue
**Notes:** [~5] TALK: exam skeleton; the failure demo is the homework story — bring your own. TRAN: exit ticket.

## S13 · Exit ticket
**Your grade-book needs the grading scale (in H2:H6) used in every student's row. Absolute or relative — and what breaks if you choose wrong?**
**Notes:** [~7] TALK: expected: absolute; relative *shifts the scale* row by row — silent corruption. The exact failure class from the S7 demo; keep slips for the lab session.

---

## L20 — Productivity: Presentations and Workflows (Slides + Speaker Notes)

**Resources:** the deliberately awful 8-slide deck (built per guide prep); accessibility checker ready; project brief/milestones pages projected for the announcement.

### Run sheet (120 min)

| Block | Slides | Time |
|---|---|---|
| Lab 6 harvest + objectives | S1–S2 | 8 |
| Slides: three principles | S3–S4 | 16 |
| Activity: slide makeover | S5 | 26 |
| Accessibility as habit | S6–S7 | 14 |
| Workflows: versioning + sync | S8–S9 | 14 |
| Project announcement | S10 | 12 |
| Concept check | S11 | 12 |
| Summary + exit ticket | S12–S13 | 12 |
| Buffer | — | 6 |

### Slides

# L20 · Productivity: Presentations and Workflows
**Module 5 · Stage 1 · 2 hours**

## S1 · Lab 6's failures, harvested
**Notes:** [~5] TALK: read one `\$`-less failure aloud (anonymized); references discipline carried. ASK: none. TRAN: "Today: slides — and your project begins."

## S2 · Today
- Three principles · accessibility · workflows · **project announcement**
**Notes:** [~3] TALK: flag the announcement at S10 so energy paces itself. TRAN: principles.

## S3 · The deck supports the speaker
- Contrast · hierarchy · one message per slide
**Notes:** [~9] TALK: the rubric strip (guide's board plan); wall-of-text slides *compete* with you for the audience's reading attention. ASK: "Recall the worst deck you've endured — which principle died first?" MISC: "slides are the script" — the module-level warning; say it as a design sentence. TRAN: "Prove it."

## S4 · The awful deck
- Eight slides of everything wrong — name the sins before the fix
**Notes:** [~7] TALK: project the awful deck; class names violations per slide, rapid-fire. ASK: "Score it: which slide is worst?" MISC: none. TRAN: "Fix it."

## S5 · Activity — Slide makeover (26 min)
Pairs rebuild two slides · before/after deltas in 90 seconds
**Notes:** [~26] TALK: per the lecture page's activity; give pairs *only* the before-deck and the three principles — your "after" pair ends the debate with evidence (guide tip). ASK (circulating): "Which principle is your hardest fix?" MISC: decoration-first fixes — contrast and hierarchy are the graded axes. TRAN: "The principles have teeth: accessibility."

## S6 · Accessibility as a habit
- Alt text · real structure · contrast — design quality for *everyone*
**Notes:** [~8] TALK: captions in noisy rooms, alt text in broken images; the course site's validators enforce this spirit — now applied by you. ASK: "What does alt text owe: the image's *decoration* or its *meaning*?" MISC: "accessibility is for others" — module warning; it is design quality. TRAN: "Watch the tools agree."

## S7 · Demo: the checker agrees
- Run the accessibility checker on the awful deck — warnings light up
**Notes:** [~6] TALK: the guide's demo; tools corroborate principles. ASK: "Which warning maps to which principle?" MISC: none. TRAN: "Files that don't collapse."

## S8 · Versioning beats hope
- draft-v01 → review-v02 → final-v03 — history preserved
**Notes:** [~8] TALK: L11's conventions scale to teams; "never overwrite a draft" as the rule. ASK: "What does v03 know that v01 forgot?" MISC: none. TRAN: "And sync?"

## S9 · Sync ≠ versioning
- Sync mirrors the latest state · versioning keeps history
**Notes:** [~6] TALK: the distinction that matters in team projects (module warning); mistakes propagate through sync too. ASK: "Which layer answers 'who changed what when'?" MISC: "cloud sync = version control" — name the two different fears they answer. TRAN: "Your project."

## S10 · The integrated project
- Brief · milestones · rubric — pair choice due L… per schedule
**Notes:** [~12] TALK: walk the three pages projected; today's skills are the project's deliverables (charter draft is homework). ASK: "Which milestone frightens you most?" MISC: pairing anxiety — the rubric supports individual work too (OQ-10); say so. TRAN: "Check the toolkit."

## S11 · Quick check
1. The three principles.
2. Alt text's job, one sentence.
3. Sync vs versioning — one difference.
**Notes:** [~12] TALK: write-pair-resolve. MISC: Q2 — "describe the image" is incomplete; *conveys meaning* to non-sight. TRAN: "Summary."

## S12 · Summary
- Three principles · accessibility habits · versioned + synced workflows · project live
**Notes:** [~5] TALK: exam skeleton; the module closes — logic to productivity, one through-line. TRAN: exit ticket.

## S13 · Exit ticket
**Write the first line of your team charter: your naming convention for project files.**
**Notes:** [~6] TALK: expected: pattern with version/date slots (L11 convention applied); slips seed Milestone 1's charter — keep them.
