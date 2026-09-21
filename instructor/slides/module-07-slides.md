# Module 7 Slide Decks — L25–L28

**Format:** One `## S# · Title` per slide; `**Notes:**` carry [~minutes], TALK, ASK, MISC, DEMO, TRAN, EXT, TROUBLE cues. Run sheets allocate the full 120 minutes.

---

## L25 — Databases and Information Systems (Slides + Speaker Notes)

**Resources:** SQLite/DB browser on the projector (tested); clinic scenario cards; the duplicate-insert refusal demo queued.

### Run sheet (120 min)

| Block | Slides | Time |
|---|---|---|
| The spreadsheet pain + objectives | S1–S2 | 10 |
| Why databases exist | S3 | 10 |
| The relational model | S4–S6 | 22 |
| Reading SQL | S7–S8 | 14 |
| Activity: schema workshop | S9 | 28 |
| Concept check | S10 | 12 |
| Summary + exit ticket | S11–S12 | 12 |
| Buffer | — | 12 |

### Slides

# L25 · Databases and Information Systems
**Module 7 · Stage 1 · 2 hours**

## S1 · The shared-spreadsheet pain
**Notes:** [~7] TALK: two staff, one sheet, one save — changes vanish (guide tip); concurrency plus integrity is *why* this lecture exists. ASK: "Who has lived this? What broke exactly?" MISC: none. TRAN: "The machinery built to stop it."

## S2 · Today
- Data vs information, enforced · tables, keys, constraints · reading SQL
**Notes:** [~3] TALK: reading fluency only today — writing SQL is later courses (guide tip); say it to lower anxiety. TRAN: the model.

## S3 · Database vs DBMS
- The organized data · the software that keeps it true
**Notes:** [~10] TALK: the two nouns separated (guide answers); L01's data/information distinction returns as enforced integrity. ASK: "Which one would you call PostgreSQL?" MISC: "spreadsheets are databases" — module warning; the demo's refusal will settle it. TRAN: "The model."

## S4 · Tables and primary keys
- One kind of thing per table · PK = identity
**Notes:** [~8] TALK: the clinic schema grows on the board (guide plan); PK as the anchor that makes "this row" sayable. ASK: "What breaks if two patients share an ID?" MISC: none. TRAN: "The relationships."

## S5 · Foreign keys
- A column pointing at another table's PK — validity enforced
**Notes:** [~7] TALK: FK arrows drawn as students propose them; the appointment needs *both* FKs. ASK: "What should the DBMS do with an appointment for patient 9999?" MISC: none. TRAN: "The promises."

## S6 · Constraints are promises
- The demo: duplicate patient inserted — the DBMS *refuses*
**Notes:** [~7] TALK: the refusal demo (guide's demonstration) — one click, the lecture's thesis. ASK: "What did the refusal just buy the hospital?" MISC: "constraints are bureaucracy" — they are the difference between data and trustworthy data. TRAN: "Reading the language."

## S7 · SQL: SELECT, projected
- Columns, rows, conditions — reading order FROM → JOIN → WHERE
**Notes:** [~8] TALK: read two queries, annotated line by line (guide plan); reading fluency, not authoring. ASK: "In words, what does this return?" MISC: SQL anxiety — reading first lowers it; say so. TRAN: "One join."

## S8 · The JOIN, demystified
- Match rows where FK = PK — read two, fear dies
**Notes:** [~6] TALK: the JOIN sentence (guide warning); join patients to appointments live. ASK: "Which columns make the match?" MISC: "joins are advanced magic" — a match condition; twice-read kills the fear. TRAN: "Your schema."

## S9 · Activity — Schema design workshop (28 min)
Teams model the clinic · trade schemas · attack with bad data
**Notes:** [~28] TALK: per the lecture page's activity; the attack round (appointment with no patient; duplicate doctor) is the debrief's spine (guide tip). ASK (circulating): "Which constraint caught that attack — or should have?" MISC: appointment-as-table debates — allowed (guide prep); resolve by FK semantics. TROUBLE: teams over-modelling — three tables is the target scope. EXT: add a PRESCRIPTIONS table and its FKs. TRAN: "Check the model."

## S10 · Quick check
1. Database vs DBMS — one sentence each.
2. PK's job; FK's job.
3. What does a JOIN produce?
**Notes:** [~12] TALK: write-pair-resolve. MISC: Q2 — swapped jobs are common; re-run the appointment example to disambiguate. TRAN: "Summary."

## S11 · Summary
- Tables, keys, enforced promises · SQL read, not feared
**Notes:** [~6] TALK: exam skeleton; the tidy tables of L26 live in schemas like today's. TRAN: exit ticket.

## S12 · Exit ticket
**Name one bad record an unconstrained spreadsheet would accept that your clinic schema refuses — and name the refusing constraint.**
**Notes:** [~7] TALK: constraint-naming is the marked line; "the database stops it" without naming the constraint is half credit. Keep slips for L26's cleaning link.

---

## L26 — Data Science Foundations (Slides + Speaker Notes)

**Resources:** the dirty CSV loaded and tested (guide prep); CS-03 handout; the lifecycle drawn as a circle.

### Run sheet (120 min)

| Block | Slides | Time |
|---|---|---|
| Schema recap + objectives | S1–S2 | 8 |
| The lifecycle loop | S3 | 12 |
| Tidy data + the cleaning checklist | S4–S5 | 16 |
| Activity: clean the dirty dataset | S6 | 24 |
| Honest visualization + CS-03 | S7–S8 | 20 |
| Privacy: identifiability | S9 | 10 |
| Concept check | S10 | 10 |
| Summary + exit ticket | S11–S12 | 10 |
| Buffer | — | 10 |

### Slides

# L26 · Data Science Foundations
**Module 7 · Stage 1 · 2 hours**

## S1 · Yesterday's constraints, today's data
**Notes:** [~5] TALK: the clinic refused bad rows; today asks what *you* do when the data arrives already dirty. ASK: none. TRAN: "The field map."

## S2 · Today
- The lifecycle · cleaning · honest charts · identifiability — CS-03 today
**Notes:** [~3] TALK: the DS cohort's home lecture; every other student's data-defence course — say both. TRAN: lifecycle.

## S3 · The lifecycle is a loop
- Question → collect → clean → analyse → visualize → communicate → *back*
**Notes:** [~12] TALK: draw as a circle, not a line (guide tip); two feedback edges named — analysis exposes dirt, communication sharpens questions. ASK: "Which edge would surprise a 'one-pass project' planner?" MISC: "cleaning is a phase you finish" — the loop IS the rebuttal. TRAN: "The shape of clean data."

## S4 · Tidy data
- One observation per row · one variable per column
**Notes:** [~8] TALK: the definition, then one untidy example fixed live on the board. ASK: "What's the observation in the clinic's APPOINTMENTS table?" MISC: none. TRAN: "The species of dirt."

## S5 · The cleaning checklist
- Duplicates · sentinels · impossible values · inconsistencies · whitespace
**Notes:** [~8] TALK: each species with its standard check+fix (guide answers); the *species* matter more than volume. ASK: "Which species hides best from a quick glance?" (Sentinels — 999 looks like data.) MISC: none. TRAN: "Practice."

## S6 · Activity — Clean the dirty dataset (24 min)
Five checks in order · fix three species · log everything
**Notes:** [~24] TALK: the loaded CSV (guide prep); leave two species unfixed for the activity — unfinished on purpose. ASK (circulating): "What did you *keep* and why — did you log it?" MISC: silent fixing — the cleaning notebook is part of the skill (homework 1 mirrors it). TROUBLE: loading failure — the printed sample rows in the handout carry the exercise. TRAN: "Clean data, honest pictures."

## S7 · Honest visualization
- Chart choice is an argument — aggregation can hide subgroups
**Notes:** [~10] TALK: L19's craft plus ethics (module warning); the vaccination dashboard preview for CS-03. ASK: "What can an *average* hide that a distribution shows?" MISC: none. TRAN: "The case."

## S8 · Activity/Case — CS-03: Data-Driven Public Health (10 min brief + 10 debrief)
The dashboard's suspicious spike · what the chart hides · what you'd demand
**Notes:** [~20] TALK: per the CS-03 handout; teams decide what data they'd demand before recommending. ASK (debrief): "Which lifecycle stage does this case sit in — and which does it *feed back to*?" MISC: answer-first teams — demand-data-first is the discipline. TRAN: "Privacy in data form."

## S9 · Identifiability
- Rare combinations re-identify — privacy is a property of combinations
**Notes:** [~10] TALK: L26's §26.4; postal-code+birthdate+gender class of releases (homework extension previews). ASK: "Is 'no names' enough?" MISC: "anonymous = safe" — combinations betray; say it twice. TRAN: "Check the loop."

## S10 · Quick check
1. Six lifecycle stages, in order.
2. Three defect species and their fixes.
3. Why is identifiability a risk in "anonymous" data?
**Notes:** [~10] TALK: write-pair-resolve. MISC: Q1 — a *line* answer means the S3 circle didn't land; redraw with the two edges. TRAN: "Summary."

## S11 · Summary
- The loop · tidy structure · species-and-fixes · honest charts · combinations identify
**Notes:** [~5] TALK: exam skeleton; the project dataset inherits today's checklist directly. TRAN: exit ticket.

## S12 · Exit ticket
**Your project dataset: name one defect species you expect and the check that will catch it.**
**Notes:** [~5] TALK: species+check pairs are the marked line; slips seed the project's Milestone 2 data plan.

---

## L27 — AI Fundamentals (Slides + Speaker Notes)

**Resources:** the twelve system cards for the opener sort (guide prep); the spreadsheet trend-line predictor demo; exam-analogy board plan.

### Run sheet (120 min)

| Block | Slides | Time |
|---|---|---|
| Card sort: model or rules? + objectives | S1–S3 | 20 |
| AI and ML, defined | S4 | 10 |
| The training loop | S5–S6 | 20 |
| Demo: fit, predict, error | S7 | 12 |
| Rule-based vs learned boundary | S8 | 10 |
| Generative AI | S9 | 10 |
| Concept check | S10 | 12 |
| Summary + exit ticket | S11–S12 | 12 |
| Buffer | — | 14 |

### Slides

# L27 · AI Fundamentals
**Module 7 · Stage 1 · 2 hours**

## S1 · Sort first, define later
**Notes:** [~5] TALK: twelve cards on the tables *before* any definition (guide tip) — classification before terminology gives everyone stakes. ASK: none. TRAN: "Sort."

## S2 · Today
- AI vs ML · rule-based vs learned · the training loop · generative AI
**Notes:** [~3] TALK: L28 gets the ethics explicitly — say it now, defer it firmly. TRAN: sort.

## S3 · Activity (opener) — Model or rules? (15 min)
Twelve systems · sort and defend the two hardest
**Notes:** [~15] TALK: per the lecture page's activity; spell-check's two eras (rule → statistical) is the beautiful border case (guide answers). ASK (debrief): "Which card changed sides as you argued?" MISC: AI-means-robots reflex — the sort's evidence beats the reflex. TRAN: "The names."

## S4 · AI and ML, precisely
- AI: tasks needing intelligence when humans do them · ML: the learning subset
**Notes:** [~10] TALK: working definitions from the lecture page's 27.1; the subset relation drawn. ASK: "Is a chess engine with hand-tuned evaluation AI? ML?" MISC: "AI = the movies" — the working definition is the antidote. TRAN: "How learning happens."

## S5 · The training loop
- Data → model → prediction → loss → adjust → repeat
**Notes:** [~10] TALK: the exam-prep analogy, used three ways then retired (guide tip): practice questions, marking, study. ASK: "Map the analogy's parts onto the loop." MISC: "learning systems are just fancy if-statements" — there IS a real difference: behaviour *fitted*, not authored. TRAN: "Watch it fail usefully."

## S6 · Loss: how wrong, exactly?
- The loop's scoreboard — errors drive adjustment
**Notes:** [~10] TALK: loss as the measurable "wrongness" (guide answers); no loss, no learning. ASK: "What happens with no labels?" (Park — unsupervised is later courses.) MISC: none. TRAN: "Demo."

## S7 · Demo: fit, predict, error
- Trend line on visible points · predict the hidden one · reveal · then poison a point and re-fit
**Notes:** [~12] TALK: the guide's demo; the poisoned point makes data-quality→model-quality *visible*. ASK: "Which L26 defect species was that poison — and which arrow did it enter?" MISC: none. TRAN: "The boundary, honestly."

## S8 · The boundary, defended
- Rules where rules are knowable and stable · learning where patterns beat authoring
**Notes:** [~10] TALK: neither side wins; the card-sort's border cases were the preview. ASK: "Which of today's cards would you *move* after this slide?" MISC: "AI is always the right tool" — the boundary slide is the rebuttal. TRAN: "The loud sibling."

## S9 · Generative AI
- Predicting plausible continuations — powerful, unverified by nature
**Notes:** [~10] TALK: mechanism-honest per lecture page 27.3; the verification handoff to L28 is explicit (guide tip). ASK: "What does 'plausible' NOT mean?" MISC: none. TRAN: "Check the loop."

## S10 · Quick check
1. AI vs ML — one sentence each.
2. Name the training loop's four parts.
3. Rule-based vs learned — one defining difference.
**Notes:** [~12] TALK: write-pair-resolve. MISC: Q2 — "data, model, loss, adjustment" verbatim; "learning" alone is incomplete. TRAN: "Summary."

## S11 · Summary
- Definitions · the loop · the boundary · generation without verification
**Notes:** [~5] TALK: exam skeleton; the vocabulary today is L28's raw material — name the dependency. TRAN: exit ticket.

## S12 · Exit ticket
**Pick one familiar predictor (spam filter, autocomplete): write its data, model, and loss — one line each.**
**Notes:** [~6] TALK: three-line specificity is the marked line; vague "it learns from emails" answers get the loop-question back. Keep slips — L28 opens with one of them verified.

---

## L28 — Responsible AI Literacy (Slides + Speaker Notes)

**Resources:** the planted-error paragraph written the day before (guide prep; answer key stays here); the verification checklist diagram; project rubric for the disclosure link.

### Run sheet (120 min)

| Block | Slides | Time |
|---|---|---|
| Verify an exit slip + objectives | S1–S2 | 10 |
| Bias as a pipeline | S3–S4 | 18 |
| Hallucination, mechanistically | S5 | 10 |
| Activity: hallucination hunt | S6 | 28 |
| Provenance and privacy | S7–S8 | 14 |
| Disclosure and integrity | S9 | 12 |
| Concept check | S10 | 10 |
| Summary + exit ticket | S11–S12 | 10 |
| Buffer | — | 8 |

### Slides

# L28 · Responsible AI Literacy
**Module 7 · Stage 4 · 2 hours**

## S1 · Yesterday's slip, verified live
**Notes:** [~7] TALK: take one L27 exit slip's claim and verify it against course sources on the projector (guide's demonstration) — the *process* is the artefact. ASK: "What made that source check decisive?" MISC: none. TRAN: "The lecture's frame."

## S2 · Today
- Bias mechanisms · hallucination · provenance · disclosure — the course's ethical centrepiece
**Notes:** [~3] TALK: the graded-disclosure promise named now (rubric link). TRAN: bias.

## S3 · Bias: data → model → outcome
- Skew in, skew out — mechanism, not malice
**Notes:** [~10] TALK: the pipeline with red arrows (guide's board plan); one concrete domain per cohort (hiring/credit/facial — pick one, don't tour). ASK: "Which arrow does 'delete the biased column' attack — and why might it fail?" (Proxies.) MISC: "bias means biased programmers" — module warning; *data* bias dominates, and the fixes differ. TRAN: "Why confidence lies."

## S4 · Bias case, mapped
- One real reported case, run through the three arrows
**Notes:** [~8] TALK: keep to the mapped case; tour-de-bias derails the hour. ASK: "At which arrow would your fix begin?" MISC: doom-or-dismiss spirals — literacy sits between; say it. TRAN: "The hallucination mechanism."

## S5 · Hallucination: the mechanism working
- Plausible continuation without a truth-check — *unassigned truth value*
**Notes:** [~10] TALK: the module warning verbatim-ish: not random glitches — designed behaviour minus truth-checking; "unassigned truth value" is the phrase of the day. ASK: "So is verification optional or structural?" MISC: none. TRAN: "Hunt."

## S6 · Activity — Hallucination hunt (28 min)
The planted paragraph · find, verify, correct · write the disclosure that would have made it acceptable
**Notes:** [~28] TALK: *your* planted paragraph, never live-generated (prep note) — every team find is verifiable; the answer key stays in this folder. ASK (circulating): "Which source decides your fake-citation case?" MISC: teams stopping at the fake citation — two errors remain; push. TROUBLE: a team finds an *unplanted* error — verify publicly; that's a bonus, celebrate it. TRAN: "Before you even use the tool."

## S7 · Provenance before use
- What trained it · what you submit · who sees the result
**Notes:** [~7] TALK: the three pre-use questions (lecture page 28.3); L26's identifiability is the privacy engine. ASK: "Which of your three most recent tool uses fails a question?" MISC: none. TRAN: "The habit you'll be graded on."

## S8 · Disclosure as quality assurance
- Tool · role · verification · changes — the rubric's line
**Notes:** [~7] TALK: the four-part template (guide's board plan); disclosure strengthens work — provenance mirrors citation practice. ASK: "What does your disclosure template owe a reader who wants to *re-check*?" MISC: "disclosure weakens work" — module warning; the rubric rewards it. TRAN: "Check the toolkit."

## S9 · Quick check
1. Trace bias through the pipeline.
2. Hallucination, mechanistically.
3. The disclosure template's four parts.
**Notes:** [~10] TALK: write-pair-resolve. MISC: Q3 — "say I used AI" is one part of four; the template has teeth. TRAN: "Summary."

## S10 · Summary
- Bias is a pipeline · hallucination is designed behaviour · verify structurally · disclose as QA
**Notes:** [~5] TALK: exam skeleton; the through-line made explicit — L12's evidence discipline, L23's credibility criteria, today's verification loop: one method, new objects (guide tip). TRAN: exit ticket.

## S11 · Exit ticket
**Draft your project's disclosure block skeleton — four parts, one line each.**
**Notes:** [~6] TALK: skeletons seed Milestone 2's workshop; slips showing only "I used ChatGPT" get the four-part question back. Module 7 closes — the toolkits carry forward.
