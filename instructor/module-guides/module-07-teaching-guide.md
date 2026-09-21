# Teaching Guide — Module 7: Data, Databases, and Intelligent Systems

**Module 7** · Stage 4 · 4 lectures (L25–L28) · 8 contact hours
Companion to lecture pages `L25`–`L28` under `docs/lectures/`. **Not published.** Answers to exit tickets appear here and nowhere student-facing.

> Symbols: **[Slide]** projector visual · **[Board]** board work · **[Demo]** live demonstration · **[Discuss]** think-pair-share or open discussion.

## Before this module

- [ ] This is the DS cohort's home module and the CS cohort's systems preview — calibrate emphasis per section, but teach *both* halves of each lecture.
- [ ] L25's schema workshop needs the clinic scenario cards (patients, doctors, appointments) prepared; decide in advance whether you allow "appointments as table" vs "appointments as association" debates — they will happen.
- [ ] L26's dirty dataset: prepare the small CSV (duplicates, one impossible date, a 999 sentinel value, mixed-case categories, trailing spaces) and test it loads in the tooling students have.
- [ ] L28's hallucination-hunt paragraph: write it the day before with planted errors (one fake citation, one wrong date, one plausible-but-false claim); keep your answer version here, never in the deck.

## Misconception warnings (module level)

1. **"A spreadsheet is a database."** Scale, concurrent multi-user integrity, constraints, and queryability separate them; L25's clinic schema makes the difference concrete.
2. **"AI understands."** L27's training intuition (data → model → loss → adjustment) exists precisely to replace anthropomorphism with mechanism; L28 exploits the gap.
3. **"Charts speak for themselves."** L26's honest-visualization segment is where Module 5's chart skills meet data ethics; aggregating away subgroups is the classic sin.
4. **"Verification is distrust of technology."** Frame L28's habits as *professional* practice — the same isolation-and-evidence discipline as L12, applied to probabilistic systems.

---

## L25 — Databases and Information Systems

**Teaching tips:**
- Open with the spreadsheet-limit story: two staff editing "the same" sheet, one saves, the other's changes vanish. Concurrency plus integrity is *why* databases exist — let the pain motivate the machinery.
- The schema workshop's trading phase is where learning happens: teams attack each other's designs with bad data (appointment with no patient; duplicate doctor). Constraints catching or missing is the debrief's spine.
- SQL: read-only today. SELECT, projection, filter, one JOIN — reading fluency, not authoring. Writing SQL is later courses' business.

**Board / projector plan:**
- [Board] The clinic schema growing on the board: PATIENTS, DOCTORS, APPOINTMENTS boxes; PK/FK arrows drawn as students propose them.
- [Slide] The Mermaid ER-style diagram from the lecture page's "Visual explanation."
- [Board] One SELECT with a JOIN, annotated line by line (FROM → JOIN → WHERE → what comes back).

**Suggested demonstration:** Any SQLite/DB browser: create the three tables live with one constraint (PK), attempt to insert a duplicate patient — the constraint *refuses*; that refusal is the lecture's thesis in one click.

**Misconception warnings:**
- "Rows are records, so spreadsheets are databases." Without enforced keys and constraints, nothing stops contradictions; the demo's refusal is the difference.
- "Joins are advanced magic." A JOIN is just "match rows where the FK equals the PK" — read two and the fear dies.
- "Data integrity is an IT department concern." Bad rows cost *analysts* truth; integrity is a data-user's own interest.

**Discussion prompts:**
1. Where in the clinic schema would "the patient's age" cause trouble, and what stores better? (Derived data — store date of birth.)
2. Why do hospitals still run systems designed decades ago? (Integrity and continuity beat novelty — link to L03's mainframe reliability.)
3. What would you lose if the university stored grades in spreadsheets per instructor?

**Exit-ticket questions (with answers):**
1. *Database vs DBMS in one sentence each.* — Database: organized data itself; DBMS: the software managing storage, integrity, queries.
2. *Primary key's job.* — Uniquely identifies each row; no duplicates/nulls — the anchor for relationships.
3. *Foreign key's job.* — A column referencing another table's PK; enforces the relationship's validity.
4. *What does a JOIN produce?* — Rows combined across tables where the FK–PK match holds.

---

## L26 — Data Science Foundations

**Teaching tips:**
- The lifecycle (question → collect → clean → analyse → visualize → communicate) must be *drawn as a loop*, not a line — analysis results send you back to re-question. Students who see a line think cleaning is a phase you finish.
- The dirty-dataset exercise is deliberately small (a few dozen rows); the *species* of dirtiness matters more than the volume: duplicates, sentinels, impossible dates, case inconsistencies, whitespace.
- Honest visualization: connect backward to L19's chart choice, then escalate to aggregation ethics — the vaccination dashboard in CS-03 hides subgroups; that is an ethics failure, not a style failure.

**Board / projector plan:**
- [Board] The lifecycle as a circle with the six stages; the "clean" node gets a "return here always" arrow from analyse.
- [Slide] The Mermaid lifecycle diagram from the lecture page's "Visual explanation."
- [Board] The dirty-data checklist as a two-column tally: defect species → which rows.

**Suggested demonstration:** Load the dirty CSV live; run the five checks in order; fix two defect species in front of the room and leave two for the activity — unfinished on purpose, because the activity is the practice.

**Misconception warnings:**
- "Cleaning is menial." It is the stage where truth is defended; downstream conclusions inherit every skipped check.
- "Aggregates are neutral." Averages hide distributions; the dashboard case shows aggregation as an *argument* — sometimes an unfair one.
- "More data beats bad data." Bad rows propagate; volume amplifies rather than repairs.

**Discussion prompts:**
1. Which lifecycle stage fails most often in student projects, and what does it cost? (Cleaning; silently wrong results.)
2. When is a pie chart defending a lie? (Many categories / non-additive shares — L19's rule now with ethical stakes.)
3. Your project dataset: name one defect species you have already met and your planned fix.

**Exit-ticket questions (with answers):**
1. *List the six lifecycle stages in order.* — Question, collect, clean, analyse, visualize, communicate (loop back).
2. *Tidy data in one sentence.* — One observation per row, one variable per column, one table per kind of observation.
3. *Name three defect species and their fixes.* — Duplicates→deduplicate; sentinel 999→treat as missing/recode; mixed case/whitespace→normalize (accept others from the exercise).
4. *Why is identifiability a privacy risk in "anonymous" data?* — Rare-value combinations re-identify individuals even without names (link to L30).

---

## L27 — AI Fundamentals

**Teaching tips:**
- The model-or-rules card sort is the lecture's opener, not closer: classification *before* definitions gives every student stakes in the boundary discussion. Defend the two hardest cards (spell-check's rule era vs statistical era is a beautiful case).
- Training intuition: use the exam-prep analogy — many practice questions (data), the student's mental model improves against marked answers (labels), errors guide study (loss). One analogy, used three ways, then retired.
- Generative AI: keep the mechanism honest (predicting plausible continuations from patterns) and *explicitly defer* the ethics to L28 — say so, or the class derails early.

**Board / projector plan:**
- [Board] Rule-based vs learned split: two columns, the twelve cards sorted live, border cases left hanging deliberately.
- [Slide] The Mermaid training-loop diagram from the lecture page's "Visual explanation."
- [Board] The exam-prep analogy mapped explicitly: practice questions=training data, marking=labels/loss, study=adjustment.

**Suggested demonstration:** A spreadsheet predictor: fit a "model" (trend line) on visible points, hide the next point, let the class predict, reveal — prediction from pattern, error visible. Then add a misleading point and re-fit: data quality → model quality, visually.

**Misconception warnings:**
- "AI = robots/movies." Working definition: systems performing tasks that need intelligence when humans do them; the card sort gives the operative boundary.
- "Learning systems are just fancy if-statements." There IS a real difference: behaviour is *fit* from data, not authored rule by rule — consequences explored in L28.
- "The model is right because it's confident." Confidence and correctness are different axes; L28's hallucination hunt exists for this.

**Discussion prompts:**
1. Your phone's autocomplete: learned or rules? What data did it learn from — and what does that imply about its errors?
2. Where in Module 6's web did the training data for today's models come from?
3. Which of your daily apps got *better* the more you used it? That curve is learning.

**Exit-ticket questions (with answers):**
1. *AI vs ML in one sentence each.* — AI: systems doing tasks needing intelligence when humans do them; ML: the subset that learns patterns from data rather than fixed rules.
2. *Rule-based vs learned: one defining difference.* — Authored rules vs behaviour fitted from data.
3. *Name the training loop's four parts.* — Data, model, loss, adjustment.
4. *Why does more data of the right kind help learning?* — More pattern coverage; less overfitting to quirks (accept intuition-level).

---

## L28 — Responsible AI Literacy

**Teaching tips:**
- The hallucination hunt must use *your* planted paragraph, not a live-generated one — planted errors let you verify every team's find. Keep your key here only; teams report, you confirm.
- Bias: teach the *mechanism* (skewed data → fitted model → skewed outcomes), one concrete domain each run (hiring filters, credit scoring, or facial analysis — pick per cohort), and resist both doom and dismissal; literacy sits between.
- Close the module by connecting L28's verification habit back to L23's credibility criteria and L12's evidence discipline — the course's through-line made explicit: "same method, new objects."

**Board / projector plan:**
- [Board] The bias pipeline: data → model → outcome, with the skew arrow drawn in red at each stage.
- [Slide] The Mermaid verification checklist from the lecture page's "Visual explanation."
- [Board] Disclosure template skeleton: tool, what it did, what I verified, what I changed.

**Suggested demonstration:** Verification live: take one claim from the hunt paragraph and verify it against the course's own reference sources on the projector — the *process* (search the index, check provenance, check date) is the teachable artefact, not the verdict.

**Misconception warnings:**
- "Bias means the programmers were biased." Mostly it is *data* bias — history's patterns learned faithfully; the mechanism matters because the fixes differ (data curation vs intent).
- "Hallucinations are random glitches." They are the mechanism working as designed: plausible continuation without a truth-check — hence verification is structural, not optional.
- "Disclosure weakens work." It strengthens it: provenance is quality assurance, mirroring citation practice; the rubric (project, CLO-10) rewards it.

**Discussion prompts:**
1. Which of L23's credibility criteria applies unchanged to AI outputs, and which needs adaptation? (Evidence/currency/purpose still apply; "authority" becomes provenance.)
2. Should an AI-assisted medical triage tool disclose its confidence to patients? Use the bias pipeline to argue.
3. Write the one-sentence integrity rule you would post above your own desk.

**Exit-ticket questions (with answers):**
1. *Trace bias through the pipeline.* — Unrepresentative/skewed training data → model fits the skew → outcomes reproduce or amplify it.
2. *What is hallucination, mechanistically?* — Confident output not grounded in training data or reality; plausible pattern continuation without truth-checking.
3. *Name two checks before using an AI tool on course work.* — Provenance of its data/outputs (verify against sources) and privacy of what you submit (no personal/third-party data into tools you don't control).
4. *The disclosure template's four parts.* — Tool, what it did, what you verified, what you changed.
