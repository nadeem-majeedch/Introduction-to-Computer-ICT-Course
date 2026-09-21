# Teaching Guide — Module 5: Digital Logic and Productivity Tools

**Module 5** · Stage 3 · 4 lectures (L17–L20) · 8 contact hours
Companion to lecture pages `L17`–`L20` under `docs/lectures/`. **Not published.** Answers to exit tickets appear here and nowhere student-facing.

> Symbols: **[Slide]** projector visual · **[Board]** board work · **[Demo]** live demonstration · **[Discuss]** think-pair-share or open discussion.

## Before this module

- [ ] L17/L18 need a truth-table worksheet (blank 2- and 3-input tables); print or distribute digitally before class.
- [ ] Lab 5 (logic simulator) launches at L18: test the simulator on the lab image *and* confirm browser fallback works offline in the room.
- [ ] Lab 6 (spreadsheet) launches at L19: prepare the grade-book starter file with deliberately realistic data (some blanks, one typo) — cleaning is part of the point.
- [ ] L20's slide-makeover deck: build the deliberately awful 8-slide deck yourself (walls of text, colour-on-colour, no alt text); keep the "after" slides hidden.

## Misconception warnings (module level)

1. **"OR in logic means 'one or the other but not both'."** Everyday *or* is exclusive; logical OR is inclusive. L17 makes the distinction with XOR; police it forever.
2. **"Boolean logic is an abstract maths unit with no purpose."** The through-line is L17 → L18 (gates) → L19/L20 (IF functions and filters): the same operators decide spreadsheet rows, database queries (L25), and CPU arithmetic. Name the through-line at each lecture.
3. **"Spreadsheets are a data-science tool."** They are a *thinking* tool with hard limits; Module 7 deliberately shows where they end and databases begin.
4. **"Formatting is styling."** Structure (styles, headings, alt text) is semantic; formatting is visual. Accessibility (L20) lives entirely in the structural layer.

---

## L17 — Boolean Logic and Truth Tables

**Teaching tips:**
- Open with a *policy*, not a definition: "Students may register if they completed the prerequisite AND paid fees, OR have instructor permission." Let the class argue about edge cases — they are doing Boolean algebra before they know its name.
- Truth tables: enforce the 2ⁿ-row discipline mechanically (count-down binary ordering); the discipline prevents the most common exam error, incomplete tables.
- De Morgan's laws land best as "pushing NOT through a bracket flips the operator" — demonstrate, then let students *use* them the same hour; proofs belong to later courses.

**Board / projector plan:**
- [Board] The three-operator tables (AND, OR, NOT) built one row at a time from student examples; XOR added as the "everyday or" contrast.
- [Slide] The Mermaid decision diagram from the lecture page's "Visual explanation."
- [Board] One compound expression's full truth table, columns labelled operand-by-operand, left visible during guided practice.

**Suggested demonstration:** Spreadsheet live: `=AND(B2>50, C2="yes")` filled down a column; then filter the sheet by TRUE — the truth table visibly becomes a query. (Spreadsheets as the operators' first home; Lab 6 deepens this.)

**Misconception warnings:**
- "OR is exclusive" — the module-level warning; use XOR's name when students mean it.
- "A truth table is busywork." It is *complete verification*: exhaustive by construction — the first formal tool they own that leaves nothing untested.
- "NOT can be distributed without flipping." De Morgan's flip is the trap; drill one failing example.

**Discussion prompts:**
1. Your phone unlocks with face OR passcode. Under what condition does it open — and which operator models it?
2. Where did you use exclusive-OR today without noticing? (Light pairs, turn signals, "soup or salad".)
3. Why does 3 inputs force 8 rows? (Each new input doubles the cases — connect to binary counting.)

**Exit-ticket questions (with answers):**
1. *Truth table for A AND (NOT B), all four rows.* — A=1,B=0 → 1; all other rows 0.
2. *Everyday "or" maps to which operator?* — XOR (exactly-one semantics), when both cannot hold.
3. *Rewrite NOT (A OR B) using De Morgan.* — (NOT A) AND (NOT B).
4. *Why 2ⁿ rows for n inputs?* — Each input independently true/false; binary counting enumerates all combinations.

---

## L18 — Logic Gates and Simple Circuits

**Teaching tips:**
- The bridge from L17 is physical embodiment: "each table row now costs nanoseconds and silicon." Keep yesterday's operators on the board and add the gate symbols beside them.
- NAND-universality: *show* the constructions (NOT from tied NAND inputs; AND as NAND+NOT; OR via De Morgan) rather than asserting; the lab then makes students build XOR from four NANDs — the hour's payoff.
- Half adder: carry *is* AND, sum *is* XOR — the module's best "oh" moment, because yesterday's operators assemble yesterday's arithmetic promise (L13–L14).

**Board / projector plan:**
- [Board] Gate-symbol gallery beside the L17 operator tables, one-to-one.
- [Slide] The Mermaid half-adder diagram from the lecture page's "Visual explanation."
- [Board] NAND constructions tree: NOT → AND → OR drawn as nested NANDs.

**Suggested demonstration:** Simulator (or the lab image): toggle inputs on the half adder while the class calls the truth-table row from L17's discipline — the table *predicts* the silicon; then break one wire and watch a row fail.

**Misconception warnings:**
- "Gates are tiny switches and that's all." They are switches *whose patterns compute*; the adder is the existence proof.
- "XOR is exotic." It's the sum bit of every addition; half the adder is XOR.
- "Circuits are wired by hand per expression." Universality means *one* gate type suffices — manufacturing consequence worth a sentence.

**Discussion prompts:**
1. Why does a computer's adder not care whether inputs are signed (link L14)? — Two's complement's design promise, now visibly kept.
2. Where does the "carry" of your column addition live in the half adder? — The AND output.
3. Why do chipmakers prefer one repeated gate to many gate types?

**Exit-ticket questions (with answers):**
1. *Half adder's two outputs and their gates.* — Sum = XOR of inputs; carry = AND of inputs.
2. *Why is NAND universal?* — NOT, AND, OR (hence any Boolean function) can be built from NAND alone.
3. *XOR from NANDs needs how many gates (standard construction)?* — Four.
4. *Combinational means…?* — Output depends only on current inputs (no memory/state).

---

## L19 — Productivity: Documents and Spreadsheets

**Teaching tips:**
- Split the hour cleanly: ~35 min documents (styles → ToC → tracked changes), ~45 min spreadsheets (references → functions → honest charts), ~15 min lab launch. The references segment (relative vs absolute) is where most marks are won and lost in Lab 6.
- "Structure beats formatting" is the thesis: demonstrate by restyling a whole document with one style edit — the ToC updates itself, the room notices.
- Spreadsheet demo must *fail once* on purpose: an unanchored lookup dragged wrong. The error teaches more than the success; leave it on screen.

**Board / projector plan:**
- [Board] Document anatomy: styles → outline → ToC → citations; one arrow "one edit restyles everything."
- [Slide] The Mermaid chart-choice diagram from the lecture page's "Visual explanation."
- [Board] The grid with `$A$1` vs `A1` semantics drawn as "fixed address vs street that moves with you."

**Suggested demonstration:** Live grade-book: SUM/AVERAGE over a column; IF for pass/fail; VLOOKUP-style lookup against a grading table; then the deliberate drag-error; then fix with `$`. Close: two honest charts of the same data (bar for comparison, line for trend) and one dishonest truncated-axis twin for contrast.

**Misconception warnings:**
- "The chart shows what the data shows." Chart choice *is* an argument; truncation and dual axes can lie — bring the dishonest twin.
- "Absolute references are for perfectionists." They are the difference between correct copies and silent corruption.
- "Styling is the document." Styles are the document; formatting is its costume — and tracked changes only work on the semantic layer.

**Discussion prompts:**
1. Which spreadsheet mistakes scale invisibly (copy-error classes) vs visibly (formula error)? — Invisibility is the danger; anchoring discipline is the defence.
2. When is a pie chart the *right* answer? — Few categories, parts-of-a-whole that sums to 100%; rare but real.
3. What does tracked changes change about group work? — Attribution and audit trail; bridges to L20's versioning.

**Exit-ticket questions (with answers):**
1. *Relative vs absolute reference in one sentence each.* — Relative shifts with the formula's new position; absolute stays pinned (`$`).
2. *Which function turns a numeric score into pass/fail?* — IF (with a comparison condition).
3. *Line vs bar chart: which for monthly rainfall, which for city populations?* — Line for time-trend (rainfall); bar for category comparison (populations).
4. *Why styles before formatting?* — Consistency, automatic ToC/navigation, accessibility — structure carries meaning.

---

## L20 — Productivity: Presentations and Workflows

**Teaching tips:**
- The slide-makeover is the assessment-style activity: give pairs *only* the before-deck and the three principles; the reveal of your "after" pair ends the debate with evidence rather than taste.
- Alt text practice happens *here*, on real decks — the accessibility validator's spirit made human. Require one alt-texted image per rebuilt slide.
- Workflow segment: file versioning (`v01`, dates, ISO order), naming conventions (L11 callback), cloud sync vs version control distinction. The project (brief, milestones) is announced here per the schedule — keep 5 minutes for it.

**Board / projector plan:**
- [Board] The three slide principles as a rubric strip: contrast, hierarchy, one message per slide.
- [Slide] The Mermaid workflow diagram from the lecture page's "Visual explanation."
- [Board] Versioning timeline: `draft-v01` → `review-v02` → `final-v03` with the "never overwrite a draft" arrow.

**Suggested demonstration:** The makeover reveal: before/after pairs projected side by side; then the accessibility checker run live on the awful deck (contrast warnings light up) — tools corroborate principles.

**Misconception warnings:**
- "Slides are the script." The deck supports the speaker; wall-of-text slides compete with the speaker for the audience's reading attention.
- "Accessibility is a nicety for others." It is design quality for everyone (captions in noisy rooms; alt text in broken images) — and checked tooling in this course.
- "Cloud sync = version control." Sync replicates the latest state (and mistakes propagate); versioning keeps history — the distinction matters in team projects.

**Discussion prompts:**
1. Recall the worst slide deck you have endured: which principle did it violate first?
2. In your project team, who owns the naming convention, and what happens without one?
3. Why does "one message per slide" also serve accessibility?

**Exit-ticket questions (with answers):**
1. *Name the three slide principles.* — Contrast, hierarchy, one message per slide.
2. *Alt text's job in one sentence.* — Conveys the image's meaning to those who cannot see it (screen readers, broken images) — semantic, not decorative description.
3. *Sync vs versioning distinction.* — Sync mirrors current state; versioning preserves history for recovery and accountability.
4. *Where do project milestones live?* — The course website's project section (brief/milestones/rubric pages).
