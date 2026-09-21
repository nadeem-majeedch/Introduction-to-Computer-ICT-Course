# Problem-Solving Case Bank — Level 3: Advanced

**25 cases** · PB-301–PB-325 · Now the progression demands **criteria-first justification**: multiple interacting constraints, quantified comparisons, defensible positions where reasonable people disagree, and trade-offs stated rather than hidden. Method and rubric: [bank index](index.md).

---

## PB-301 · Level 3 · Choosing the department's shared laptop pool

**Domain:** Personal computer selection (institutional scale) · **Related lectures:** L03, L06, L07, L08

**Scenario.** A small department wins a one-time grant for 10 shared laptops. Committee factions: "buy the cheapest decent machine ×10", "buy 6 good machines + keep 4 in reserve", "buy 8 mid-range + accessories". Usage: lab classes, student loans, staff presentations. Lifetime: 4 years expected. No IT staff beyond one keen technician.

**Problem statement.** Define explicit criteria, weigh them, and recommend one option with your scoring shown — including what would change your recommendation.

**Stakeholders.** Students (availability, performance); staff (presentations); the technician (maintenance load); the grant funder (value for money).

**Inputs:** grant budget (fixed); three options; usage profile; 4-year horizon. **Outputs:** criteria set → scored decision. **Constraints:** one-time purchase (no refresh budget); shared devices take abuse; spares strategy matters.

**Learning objectives.** Convert vague preferences into weighted criteria; show scoring transparently; state the decision's sensitivity.

**Available information.** Prices follow the pattern budget < mid-range < premium; mid-range machines historically survive shared use best; accessories (bags, locks, spare chargers) extend pool life; the technician can service one model faster than three.

**Student task.** Criteria list (≥5, with weights summing to 100%), the scored comparison table, the recommendation, and the one fact that would flip it.

**Suggested thinking time.** 20 minutes; then structured group defence.

**Expected solution characteristics.** Criteria likely: durability/uptime, maintenance simplicity (single model), student-hours delivered (count × reliability), spare availability, cost ceiling respected; the *single-model* argument (technician load) is the insight weak answers miss; 8+accessories usually scores best because accessories are reliability multipliers, but any well-argued option with honest scoring is defensible; the flip-fact: e.g., "if usage is mostly presentations, 6 premium machines win".

**Discussion questions.**

1. Which criterion did the "cheapest ×10" faction omit — and why does shared use amplify it?
2. What does "value" mean on a 4-year horizon that a purchase-price comparison cannot see?

**Extension challenge.** Rewrite your recommendation as the 150-word committee minute that survives a hostile question.

**References.** Course L03 (classes), L06–L08 (hardware reasoning); general PC procurement guides (instructor-provided).

---

## PB-302 · Level 3 · The department's drive fills every October

**Domain:** File and backup management · **Related lectures:** L08, L11

**Scenario.** A teaching department's shared drive hits capacity at the same time every year (new-cohort videos). The recurring fix — "delete stuff" — has started deleting things people need. Last year, a lecturer's old course archive vanished the week she needed it.

**Problem statement.** Diagnose the *systemic* cause (not "users keep files"), design a capacity policy that ends the October crisis, and handle the archival-loss question.

**Stakeholders.** Lecturers (their materials); students (access to past materials); the technician (storage admin); the department (budget for storage).

**Inputs:** the annual pattern; the deletion incident; storage growth trend. **Outputs:** root-cause analysis + policy design + the archive question. **Constraints:** minimal budget; compliance with any retention rules is *unknown* — flag it rather than assume.

**Learning objectives.** Distinguish capacity symptoms from governance causes; design a policy with named owners and triggers.

**Available information.** Videos dominate growth (10–100× documents); most annual content is superseded, not deleted-worthy; quotas per folder exist in the system; the vanished archive had no backup copy.

**Student task.** The root cause in one paragraph + the policy (three mechanisms, one per: prevention, triage, recovery) + how the policy would have saved the lecturer's archive.

**Suggested thinking time.** 20 minutes.

**Expected solution characteristics.** Root cause: capacity managed reactively, no ownership or lifecycle — "delete stuff" is a symptom-management ritual; policy: per-folder quotas with owners named (prevention), an annual *archival* tier (compressed, cold storage — triage), and versioned snapshots (recovery); the archive died because no tier existed between "live" and "delete"; flag the unknown: retention rules must be confirmed before any deletion policy is enforced — a good answer *asks*, it doesn't assume.

**Discussion questions.**

1. Why does "users keep too much" fail as a root cause — what would you measure to test it?
2. Which of your three mechanisms would you implement first, and why is it not the quota?

**Extension challenge.** Draft the one-page policy memo the technician can send to the head of department.

**References.** Course L08 (capacity), L11 (lifecycle); Bourgeois ch. 4 (course reference).

---

## PB-303 · Level 3 · The three-way format standoff

**Domain:** Data representation / Digital productivity · **Related lectures:** L15, L16, L20

**Scenario.** A research group must share a mixed archive (text reports, spreadsheets, photos) with three audiences: a funding body (wants PDFs), a partner lab (wants editable originals), and the university library (wants "preservation-grade" formats for a 20-year horizon). One drive, three expectations, no time for a media-archiving course.

**Problem statement.** Design the archive's format strategy: what to standardize, what to duplicate, and what to document — justified by the audiences' actual needs and the 20-year horizon.

**Stakeholders.** The funding body (reporting); the partner lab (reusability); the library (preservation); the group (maintenance effort).

**Inputs:** content types (text, tabular, images); three audience requirements; a 20-year access goal. **Outputs:** format strategy + duplication decision + documentation plan. **Constraints:** no conversion software beyond free tools; effort must be sustainable (annual, not weekly).

**Learning objectives.** Reason about format choice as a *stakeholder* decision; distinguish working formats from preservation formats; design documentation as an artefact.

**Available information.** Open formats (plain text/CSV, PDF/A, uncompressed or lossless images) outlive proprietary ones; originals have software dependencies; the library accepts submission packages with a simple README; conversions can be scripted annually.

**Student task.** The strategy table (content type → working format → share formats per audience) + what gets documented + the annual maintenance ritual.

**Suggested thinking time.** 25 minutes.

**Expected solution characteristics.** Strategy: keep *originals* as the editable master (partner lab's need), export PDFs for reporting, maintain a preservation copy in open formats (library's need) — duplication is deliberate, by audience, not accidental by history; documentation: README per package (formats, software expectations, dates) is what makes the 20-year goal credible — the *file without its context* is the real preservation risk; ritual: annual conversion + checksum/spot-open check; the insight that "preservation-grade" is mostly *open format + documentation*, not exotic tooling.

**Discussion questions.**

1. Which audience's requirement is cheapest to satisfy — and why did the group fear it most?
2. What dies first in a 20-year horizon: the file format, the software, or the README's context? What does that ordering imply?

**Extension challenge.** Write the README template (10 lines) that the library would accept.

**References.** Course L15–L16 (encoding, compression trade-offs); library digital-preservation guidance (instructor-provided).

---

## PB-304 · Level 3 · The exam-hall Wi-Fi that must not fail

**Domain:** Networking · **Related lectures:** L21, L22

**Scenario.** An exam hall (300 students, online quiz on own devices) has Wi-Fi that handles lectures fine but dropped 12% of connections last exam. The network team offers two fixes within budget: (a) more access points (spatial spread), (b) a wired-backhaul upgrade (throughput to the room). The exam uses mostly small bursts (answers), not big downloads.

**Problem statement.** Diagnose the likely failure mode from the evidence pattern, choose the fix with explicit criteria, and design the fallback plan that makes the chosen fix safe regardless.

**Stakeholders.** Students (fair exam conditions); the invigilators (incident handling); the network team (budget, reputation); the exam board (integrity).

**Inputs:** failure pattern (dropouts, not slowness); 300 concurrent devices; bursty traffic profile; two fix options, one budget. **Outputs:** diagnosis + decision with criteria + fallback design. **Constraints:** exam cannot be postponed; the quiz must survive individual reconnects.

**Learning objectives.** Infer congestion *type* from symptoms (association airtime vs backhaul throughput); make a criteria-based choice under uncertainty; design graceful degradation.

**Available information.** 300 devices on lecture-tuned APs suggests airtime contention; burst traffic means backhaul is rarely the bottleneck; the quiz platform saves answers client-side and resyncs.

**Student task.** The diagnosis paragraph + the decision (a or b) with three named criteria + the fallback plan (three elements).

**Suggested thinking time.** 25 minutes.

**Expected solution characteristics.** Diagnosis: dropout pattern + device density + bursty traffic → airtime/association contention (more APs, spread channels), not backhaul starvation; decision: (a), criteria: symptom match, cost, deployment time before the exam; fallback: (1) quiz platform's offline save (already exists — verify), (2) invigilator protocol for reconnect stalls (patient, no mass-retry), (3) paper backup forms printed for a declared emergency; the *honest hedge*: if evidence later showed backhaul saturation, (b) wins — state the measurement that would decide (per-AP load logs).

**Discussion questions.**

1. What measurement would settle a-vs-b in one afternoon — and why wasn't it in the scenario?
2. Why does "the quiz saves locally" change the whole risk calculus?

**Extension challenge.** Draft the invigilator protocol card (5 lines) for the fallback.

**References.** Course L21 (medium contention), L22 (traffic patterns); generalized institutional scenario.

---

## PB-305 · Level 3 · The spreadsheet that runs the hostel

**Domain:** Database and information organization · **Related lectures:** L25; PB-207 is the beginner version

**Scenario.** A 200-bed hostel runs entirely on one spreadsheet: bookings, payments, maintenance requests, and staff shifts, shared by five staff. It works — until two staff edit simultaneously and overwrite each other, a double-booking happened last month, and the owner cannot answer "which rooms make money?" without a day of manual work.

**Problem statement.** Decide: keep the spreadsheet (with discipline) or migrate to a relational tool — justify with criteria, design the target schema, and plan the migration without a downtime window the business can afford.

**Stakeholders.** The owner (money, answers); staff (workflow disruption); guests (double-bookings affect them directly).

**Inputs:** the four data domains in one sheet; the concurrency failures; the owner's question. **Outputs:** decision with criteria + schema design + migration plan. **Constraints:** the hostel cannot stop operating; staff are spreadsheet-fluent but not database-fluent; budget minimal.

**Learning objectives.** Apply L25's relational decomposition to a *running* system; design a migration that respects business continuity; defend a decision with explicit criteria.

**Available information.** The data has natural entities (rooms, guests, bookings, payments, requests, shifts); free relational tools exist (including spreadsheet-adjacent ones); historical data must be preserved; staff training time ≈ one slow afternoon.

**Student task.** The decision + criteria table + the target schema (entities, keys, one relationship each) + the migration's phases.

**Suggested thinking time.** 25 minutes.

**Expected solution characteristics.** Either decision can be defensible if argued honestly: migrate (concurrency + the owner's analytical question are structural) vs stay-with-discipline (staff fluency, budget) — the *criteria* matter more than the verdict; schema: ROOMS, GUESTS, BOOKINGS (guest_id, room_id, dates — the double-booking constraint lives here), PAYMENTS, REQUESTS, SHIFTS; migration: (1) freeze period for edits or single-writer rule, (2) export/reshape into entity tables, (3) run both in parallel for two weeks with the old sheet read-only, (4) cut over after reconciliation; the double-booking fix is *structural* (a constraint), not a training reminder — that distinction is the L25 core.

**Discussion questions.**

1. What makes the double-booking problem unfixable by "be careful"?
2. Which migration phase is riskiest — and what is your rollback if it fails?

**Extension challenge.** Write the query-shaped sentence for "which rooms make money" in your schema.

**References.** Course L25 (relational model, integrity); generalized business scenario.

---

## PB-306 · Level 3 · The phishing simulation dilemma

**Domain:** Cybersecurity and privacy / Ethical and societal implications · **Related lectures:** L29, L30

**Scenario.** A department wants to "train" staff with fake phishing emails. Two designs: (a) realistic fakes with individual failure-tracking and mandatory retraining for clickers; (b) consented, announced exercises with group-level (not individual) reporting. An earlier university elsewhere faced backlash when staff felt spied on; but real phishing doesn't announce itself.

**Problem statement.** Analyze both designs against training effectiveness *and* trust, take a position, and design the guardrails that keep your position ethical.

**Stakeholders.** Staff (trust, dignity, learning); the security team (real risk reduction); the department (compliance, morale); the university (reputation).

**Inputs:** two designs; the backlash precedent; real attackers' behaviour. **Outputs:** comparative analysis + position + guardrails. **Constraints:** the goal is *learning*, not surveillance; staff cannot opt out of employment.

**Learning objectives.** Apply L29/L30 reasoning to a defence-vs-trust tension; recognize that security measures are also *social* interventions; design proportionate guardrails.

**Available information.** Research on phishing exercises suggests punitive tracking can suppress reporting (people hide clicks); announced exercises reduce realism but raise engagement; reporting culture is the single strongest defence multiplier.

**Student task.** The two-design analysis (effectiveness, trust, harms) + your position (one paragraph, defended) + three guardrails.

**Suggested thinking time.** 25 minutes.

**Expected solution characteristics.** Analysis: (a) maximizes realism, risks chilling *reporting* — the very behaviour you want — and treats staff as suspects; (b) trades realism for consent and culture, may miss the complacency gap; either position defensible; guardrails regardless: no individual punishment for clicking (learning-focused), one-click *report* button celebrated, data aggregated not person-tracked, repeat exercises with varied difficulty; the deep insight: phishing training's true KPI is *report rate*, not click rate — optimize that and trust follows.

**Discussion questions.**

1. Why does click-shaming mechanically *suppress* the reporting you need?
2. Which design would you consent to as a staff member — and does your answer change your position?

**Extension challenge.** Write the staff-announcement text for your chosen design that builds participation instead of dread.

**References.** Course L29 (human factor), L30 (dignity, citizenship); CISA phishing guidance (course references); fictional department scenario.

---

## PB-307 · Level 3 · The 4-year-old phone decision

**Domain:** Sustainability / Personal computer selection · **Related lectures:** L03, L08, L12

**Scenario.** A student's 4-year-old phone: battery degrading, updates ending this year, camera fine, screen fine. Trade-in offers exist. The student's values: money tight, environmental concern real, but a failing battery in exam season is a genuine risk.

**Problem statement.** Build the decision framework: quantify the realistic options (keep-and-repair, replace-battery, buy used, buy new), decide, and defend against the strongest counter-argument.

**Stakeholders.** The student (money, reliability); the environment (e-waste); the manufacturer (update window); the second-hand market (its future user).

**Inputs:** device state; update timeline; repair costs (typical); trade-in offers. **Outputs:** options analysis (≥4) + decision + counter-argument defence. **Constraints:** exam-season reliability is non-negotiable; budget small.

**Learning objectives.** Quantify before deciding; separate *device* life from *update* life; argue a position against its best counter-case.

**Available information.** Battery replacement is cheap and extends life 2+ years; update-end is a security horizon, not an instant brick; used mid-range devices cost less than repair + future risk; e-waste footprint is dominated by manufacture, not use.

**Student task.** The four-option table (cost, reliability risk to exams, security horizon, environmental note) + decision + the strongest counter-argument and your reply.

**Suggested thinking time.** 20 minutes.

**Expected solution characteristics.** Options table with honest quantification (assumptions stated); strong answers decouple battery (repairable) from updates (security horizon) and note manufacture dominates footprint — so *extending* life helps most if reliability permits; common defensible decisions: replace battery now + plan used replacement when updates end (sequenced), or buy used now and trade the old one onward (its second life is the footprint argument); counter-argument handled head-on (e.g., "battery repair delays the inevitable" → sequencing answer: it buys exam security *and* time to buy well, not rush).

**Discussion questions.**

1. Which number in your analysis is least certain — and how would you find out?
2. Why does the manufacture-vs-use footprint fact make *timing* the environmental lever, not the purchase itself?

**Extension challenge.** Write the decision as a 100-word note your future self would thank you for.

**References.** Course L12 (update lifecycles), L03 (device classes); generalized consumer scenario.

---

## PB-308 · Level 3 · The group project with unequal laptops

**Domain:** Digital productivity / Accessibility and inclusive computing · **Related lectures:** L11, L20, L24

**Scenario.** A five-person group project: one member has an old laptop that can't run the presentation software smoothly, two have institutional accounts with cloud tools, one has only a phone, one has everything. The deliverable: slides + report + demo. Friction is rising; the strong laptop is becoming the single point of failure.

**Problem statement.** Design the collaboration architecture (tools, file structure, fallbacks) that makes every member productive, and specify the contingency for the day the strong laptop dies.

**Stakeholders.** The five members (unequal resources); the course (deliverable quality); the instructor (fair assessment of individuals).

**Inputs:** the device/account inventory; three deliverable types; the deadline. **Outputs:** architecture design + role design + contingency. **Constraints:** zero budget; tools must be free-tier; individual contributions must stay visible for fair grading.

**Learning objectives.** Design workflows around the *weakest* link deliberately; separate documents from devices; build redundancy into collaboration.

**Available information.** Cloud editors run in browsers (old laptop and phone included); version history attributes edits; the phone can present and review but not author comfortably; a shared folder structure exists on the institutional cloud.

**Student task.** The architecture (which tool per deliverable per member-class) + the file-structure convention + the strong-laptop contingency (three steps).

**Suggested thinking time.** 20 minutes.

**Expected solution characteristics.** Architecture: browser-based editors for text/slides (weak laptop + phone can *review and comment* if not author), cloud folder with per-section files (attributable edits via version history), the phone member gets reviewing/testing roles early plus authoring sprints on campus machines; convention: numbered files, one owner each, dates in names; contingency: everything already lives in the cloud (devices are terminals), any member's account can present, a USB export is refreshed before each milestone — the design insight: **the architecture already survived the laptop dying because no deliverable lived on it**.

**Discussion questions.**

1. Which design choice made the contingency almost trivial — and why do groups usually skip it?
2. How does your file convention protect fair grading without surveillance?

**Extension challenge.** Write the group's one-page working agreement this design implies.

**References.** Course L20 (workflows), L24 (cloud semantics), L11 (versioning).

---

## PB-309 · Level 3 · The smart-meter data request

**Domain:** AI literacy / Data science workflows · **Related lectures:** L26, L28, L30

**Scenario.** An energy utility (fictional) plans an ML model to predict household peak usage from smart-meter data, to target efficiency advice. The data is granular (15-minute intervals). A pilot showed accuracy the team celebrates; a privacy review notes that 15-minute load profiles can reveal when nobody is home. Legal says "anonymized is fine"; the data scientist is not so sure.

**Problem statement.** Evaluate the anonymization claim, identify the real re-identification risk in this data type, and propose the data-minimization design that keeps the project's value.

**Stakeholders.** Households (privacy, benefit); the utility (service quality, legal standing); the data science team (project viability); regulators (eventual arbiters).

**Inputs:** data granularity; the pilot's success; the legal opinion; the load-profile research context. **Outputs:** risk evaluation + minimization design + the go/no-go framing. **Constraints:** the advice service must still work (that's the point); no fabricating compliance claims.

**Learning objectives.** Apply L26/L28/L30 to a realistic data-science ethics case; understand why "anonymous" granularity is a claim to test, not a label to trust; design trade-offs as *parameters*, not verdicts.

**Available information.** Research has shown granular consumption profiles can be linked to occupancy patterns; coarser aggregation reduces but doesn't eliminate inference; the model's actual need (peak *timing patterns*) may not require household-level 15-minute data; differential-privacy-style aggregation exists conceptually.

**Student task.** The evaluation (why "anonymized" is insufficient here — mechanism, not slogan) + the minimization design (at least two levers) + the go/no-go conditions.

**Suggested thinking time.** 25 minutes.

**Expected solution characteristics.** Evaluation: granularity itself is the identifier — occupancy is inferable from load shape even without names, so "no names attached" ≠ anonymous (linkability via address + profile); levers: temporal aggregation (hourly or daily peaks may suffice for advice), spatial aggregation (neighbourhood-level targeting), purpose limitation (retention, no secondary uses); go/no-go conditions framed as testable thresholds (e.g., "if advice quality at daily aggregation ≥ X% of pilot quality, choose the coarser tier"); the honest boundary: students flag what a real deployment would need (DPIA, regulator engagement) without pretending to specify it.

**Discussion questions.**

1. Why does the *shape* of electricity use identify a household more than its meter number?
2. Which lever (temporal, spatial, retention) costs the project most — and who decides that trade?

**Extension challenge.** Draft the 3-row table: data tier → advice capability → privacy exposure.

**References.** Course L26 (data ethics), L28 (responsible AI), L30 (minimization); smart-meter privacy literature (instructor-provided); fictional utility scenario.

---

## PB-310 · Level 3 · The open-book exam under a proctoring tool

**Domain:** Education technology / Ethical and societal implications · **Related lectures:** L27, L30

**Scenario.** A course proposes AI-based remote proctoring (camera + screen monitoring) for open-book exams. Students split: some welcome flexibility (no travel to halls), others fear false flags (movement differences, eye-gaze variance, room diversity) and constant surveillance. The instructor's dilemma: integrity, equity, and trust in one policy.

**Problem statement.** Structure the decision: what the tool can and cannot validly detect, where false-positive risk concentrates, and the policy design (with appeals) you would defend to both student factions.

**Stakeholders.** Students (equity, privacy, anxiety); the instructor (integrity, fairness); the university (policy, liability); the vendor (claims).

**Inputs:** the tool's mechanism (behavioural flags); the open-book format; diverse exam environments. **Outputs:** capability analysis + policy design + the appeal path. **Constraints:** the policy must be *explainable* to students in advance; false accusations are the worst failure mode.

**Learning objectives.** Reason about AI detection limits (L27/L28 false positives); design policy where the cost of error is asymmetric; balance flexibility against surveillance harm.

**Available information.** Behavioural flags have documented false-positive issues across neurodivergence, environments, and camera quality; flag ≠ proof; the alternative (in-person halls) has its own equity costs (travel, health); appeals processes exist but are slow.

**Student task.** The capability/false-positive analysis (three failure modes) + your policy (what the tool may decide, what requires human review) + the appeal design (two properties that make it fair).

**Suggested thinking time.** 25 minutes.

**Expected solution characteristics.** Analysis: flags are *indicators*, not evidence; false positives concentrate in movement/gaze variance and non-standard rooms; cost asymmetry (a false accusation harms far more than a missed violation) demands human-in-the-loop; policy: tool flags → human review of flagged segments only → no automated penalties; appeal: fast (days, not weeks) and evidence-disclosing (students see the flagged basis) — those two properties are the fairness core; honest boundary: acknowledge no policy eliminates the tension — the design *allocates* it.

**Discussion questions.**

1. Why is "the AI is 95% accurate" the wrong frame for this decision?
2. Which faction's strongest concern does your appeal design *not* fully answer — and why accept that residual?

**Extension challenge.** Write the pre-exam notice paragraph that explains the policy honestly, including its limits.

**References.** Course L27 (limits), L30 (surveillance ethics); proctoring-false-positive reporting (instructor-provided); fictional course scenario.

---

## PB-311 · Level 3 · The library's dying catalogue terminal

**Domain:** Public service systems / Operating systems · **Related lectures:** L03, L10, L12

**Scenario.** A public library's catalogue terminal runs an OS past its update end. It works, patrons use it daily, and replacing it competes with the book budget. The technician proposes three options: (a) replace hardware now, (b) isolate the terminal (no external network, catalogue app only), (c) install a lighter OS on the same hardware. Risk appetites differ: the head librarian fears downtime; the city IT officer fears the unpatched OS.

**Problem statement.** Evaluate the three options against stated criteria (security, downtime, cost, longevity), recommend, and design the transition so the head librarian's fear is addressed in the plan itself.

**Stakeholders.** Patrons (access); the head librarian (downtime fear); the city IT officer (security mandate); the book budget (competitor for funds).

**Inputs:** three options; usage pattern (catalogue lookups only); the update-end date. **Outputs:** criteria-based evaluation + recommendation + transition plan. **Constraints:** no budget invention; patrons cannot lose access for more than a day.

**Learning objectives.** Evaluate under conflicting risk appetites; recognize isolation as a legitimate third strategy; design transitions that address the *human* objection.

**Available information.** The terminal's only network use is the catalogue server; a spare similar machine exists for staging; lighter OSes run fine on old hardware; catalogue usage peaks after school hours.

**Student task.** The criteria table (weights shown) + recommendation + the transition plan that answers the librarian's downtime fear directly.

**Suggested thinking time.** 25 minutes.

**Expected solution characteristics.** Evaluation: (b) isolation is defensible *short-term* (removes the remote-attack surface) but decays as the OS ages and if the app needs updates; (c) maximizes longevity per dollar but needs staging time; (a) costs book-budget money but ends the problem; common strong answers: (c) staged on the spare machine with (b)-style isolation as the interim hardening — but *any* criteria-argued choice passes; transition: stage on spare → parallel-run one week → cutover in a low-peak window with the old terminal kept as fallback for a month (this is what answers the librarian — *her* fear is designed against, not dismissed).

**Discussion questions.**

1. Why does "isolate it" decay as a strategy — what changes over time?
2. Which stakeholder's risk perception was *factually* wrong, and how does your plan correct it without confrontation?

**Extension challenge.** Draft the one-paragraph budget request that makes the book-budget trade-off explicit and fair.

**References.** Course L10/L12 (OS lifecycle), L03 (hardware classes); fictional library scenario.

---

## PB-312 · Level 3 · The club treasury handover that lost everything

**Domain:** File and backup management / University administration · **Related lectures:** L11, L19

**Scenario.** A student club's treasurer graduates; the handover is a verbal tour of "where things are" — a personal cloud account, a laptop, a USB stick, and a group chat with receipts. Two months later, the new treasurer finds the personal cloud locked (dormant-account policy), the laptop formatted, and the chat history expiring. The club's financial history is largely gone.

**Problem statement.** Diagnose the handover's failure modes (ownership, locations, format, expiry), design the handover protocol, and specify what must exist *before* anyone graduates.

**Stakeholders.** The new treasurer (inheritance); the club (continuity, audits); the university's societies office (accountability); the departing treasurer (goodwill — this wasn't malice).

**Inputs:** the four locations; the expiry mechanisms; the club's need (audit-ready history). **Outputs:** failure-mode analysis + handover protocol + the standing state. **Constraints:** no budget; must survive *successive* handovers, not just this one.

**Learning objectives.** Design for continuity of *institutional* (not personal) data; anticipate expiry as a failure mode; make protocol that survives goodwill lapses.

**Available information.** Institutional accounts exist for societies; the chat platform has an export feature; the university requires societies to file a year-end summary; the USB stick is medium-lived.

**Student task.** The failure-mode table (each location → how it failed) + the protocol (who does what, when) + the standing state (what always exists, where).

**Suggested thinking time.** 20 minutes.

**Expected solution characteristics.** Failure modes: personal ownership (dormancy lock), device-bound data (formatting), ephemeral chat (expiry), verbal-only knowledge (walked out the door); protocol: at year-end — export chat, consolidate to the *institutional* account, one dated archive + a README index, walk-through recorded in writing; standing state: the institutional account always holds current books + last 3 years' archives; the deep principle: club data must never live where a *person's* lifecycle can delete it — design for the role, not the officeholder.

**Discussion questions.**

1. Why is "the treasurer was careless" the wrong root cause — whose design failure was it, really?
2. Which of the four failures is *hardest* to prevent with protocol alone, and what handles it instead?

**Extension challenge.** Write the handover checklist (6 items) as the societies-office template for all clubs.

**References.** Course L11 (3-2-1), L19 (documentation as workflow); fictional club scenario.

---

## PB-313 · Level 3 · The bandwidth auction (a network policy case)

**Domain:** Networking / University administration · **Related lectures:** L21, L22

**Scenario.** A hall of residence has finite bandwidth. Policy options: (a) flat per-user cap, (b) time-of-day shaping (slow bulk traffic at peak), (c) application classes (study tools prioritized, streaming deprioritized). Last term, evening lectures streamed live lagged while 200 devices streamed entertainment. The housing office wants "fair"; the IT team wants "manageable"; students want "fast".

**Problem statement.** Define "fairness" operationally for this setting (it is contested), evaluate the three policies against your definition, and recommend with the enforcement honesty each requires.

**Stakeholders.** Students (streamers, streamers-of-lectures, gamers, all); IT (manageability); the housing office (complaint reduction); the university (educational mission).

**Inputs:** finite shared capacity; the lecture-lag incident; three policy families. **Outputs:** fairness definition + policy evaluation + recommendation. **Constraints:** policies must be explainable to residents; enforcement must be technically realistic.

**Learning objectives.** Make a contested value ("fairness") operational; evaluate network policies with mechanism honesty; recommend under stakeholder conflict.

**Available information.** Lecture streaming is schedulable (known times); entertainment is elastic (deferrable); per-user caps are simple but blunt; app classification is imperfect (encrypted traffic, VPNs); capacity grows only with money.

**Student task.** Your fairness definition (one sentence + justification) + the three-policy evaluation table + recommendation + one enforcement honesty note.

**Suggested thinking time.** 25 minutes.

**Expected solution characteristics.** Definitions vary and that's the point — e.g., "equal *opportunity* for educational use first, best-effort for the rest" vs "equal share, period" — each implies different policies; evaluation: (a) simple/blunt (hurts light users, easy evasion), (b) time-shaping matches deferrable demand to off-peak (smart but needs user communication), (c) mission-aligned but classification is leaky (honesty: encrypted/VPN traffic evades it); strong answers often combine (b)+(c) with scheduled lecture priority *by whitelist* (deterministic, not classification-dependent); honesty note: any choice needs published rules or it reads as arbitrary throttling.

**Discussion questions.**

1. Whose definition of fairness won in your analysis — and what does that reveal about "neutral" technical policy?
2. Why is whitelist-by-schedule more robust than app-classification for the lecture-stream case?

**Extension challenge.** Draft the resident-facing announcement of your policy in 80 words, honest about what gets slowed.

**References.** Course L21 (capacity/contention), L22 (traffic shaping concept); generalized residence scenario.

---

## PB-314 · Level 3 · The dataset that changed meaning mid-project

**Domain:** Data science workflows · **Related lectures:** L19, L26

**Scenario.** A student team analyses two years of a city's published air-quality data. Midway, they discover the city *changed sensor locations* in year two — and, quietly, the sensor model. Downstream, a neighbourhood "improved" 30%. The team's draft conclusion: successful policy. The change note exists, buried in a PDF appendix.

**Problem statement.** Diagnose every way the change threatens the analysis, redesign the methodology to salvage the project honestly, and decide what the "improvement" claim may now assert.

**Stakeholders.** The team (their conclusions, their grade); the city (its published record); anyone acting on the result (residents, journalists).

**Inputs:** the sensor change; the buried note; two years of data; the draft conclusion. **Outputs:** threat analysis + methodology redesign + the defensible claim. **Constraints:** no new sensors can be deployed; the change note is legitimate metadata, not deception — but discoverability was poor.

**Learning objectives.** Treat data provenance changes as first-class analysis threats; redesign methodology rather than abandon it; calibrate claims to evidence.

**Available information.** Overlap periods may exist (old and new sensors running together); neighbouring cities' data offers comparison; the change note specifies dates and models; standard practice treats such series breaks with break-point methods (concept level).

**Student task.** The threat list (≥3, each mechanism explained) + the redesigned methodology + the sentence of claim the evidence now supports.

**Suggested thinking time.** 25 minutes.

**Expected solution characteristics.** Threats: location change breaks spatial comparability (the "improvement" may be sensor-placement artefact), model change breaks instrument comparability, trend claims conflate policy effect with measurement change; redesign: restrict analysis to overlap windows / use neighbours as controls / report both raw and break-adjusted series / state limitations prominently; claim: at most "a change coinciding with the sensor transition is observed; attribution to policy is not supported by comparable measurements" — the calibration of claim to evidence *is* the grade; meta-lesson: discoverability of metadata is a data-quality issue the team should note in their report.

**Discussion questions.**

1. Which threat would a careless team never notice — and why does it produce *confident* wrongness?
2. How would you redesign the city's publishing so the next team doesn't nearly miss this?

**Extension challenge.** Write the limitations section's three opening sentences.

**References.** Course L26 (provenance, honesty); instructor-provided readings on sensor-series breaks.

---

## PB-315 · Level 3 · The password policy that made everything worse

**Domain:** Cybersecurity · **Related lectures:** L29

**Scenario.** An institution enforces: 12+ characters, four character classes, 60-day rotation, no reuse of last 12 passwords. Consequences: sticky notes, pattern-game passwords (Winter2026!, Winter2027!…), help-desk reset floods, and user research suggesting reuse across *external* sites too. Security leadership wants "stronger enforcement"; the analyst proposes the opposite.

**Problem statement.** Diagnose which requirement causes which harm (mechanism, not vibe), design the replacement policy, and defend it against the "we'd look soft" objection with evidence-class reasoning.

**Stakeholders.** Users (burden, workarounds); the help desk (flood); security leadership (mandate, optics); the institution (real risk).

**Inputs:** the four requirements; observed workarounds; modern guidance direction. **Outputs:** harm-requirement mapping + replacement policy + defence. **Constraints:** replacement must be implementable with common systems (no exotic tooling assumed); the policy must be *explainable* in one screen.

**Learning objectives.** Trace policy requirements to behavioural mechanisms; redesign toward practices evidence supports (length, uniqueness, MFA, breached-password checks); argue against a mandate without dismissing its fear.

**Available information.** Rotation *without* suspicion drives predictable patterns (documented in guidance literature); length and uniqueness are the load-bearing requirements; MFA absorbs far more risk than rotation; breached-password screening exists in common systems.

**Student task.** The harm map (requirement → mechanism → observed behaviour) + replacement policy (four elements) + the defence paragraph.

**Suggested thinking time.** 25 minutes.

**Expected solution characteristics.** Harm map: rotation → patterned increments; class rules → predictable transforms; no-reuse lists → cross-site reuse; the combination → sticky notes; replacement: long passphrases, unique per site, no scheduled rotation (rotate on suspicion/breach), MFA everywhere, breached-password screening; defence: reframe — the mandate optimizes *compliance optics*, the redesign optimizes *attacker cost*; cite-class reasoning: attackers don't brute-force 60-day-old passwords, they use breached lists (screening) and reuse (uniqueness); the honest limit: change needs leadership sponsorship and a transition plan — name it.

**Discussion questions.**

1. Which requirement is *cheapest to drop* and most harmful to keep — why that combination?
2. What would you measure six months after the switch to know it worked?

**Extension challenge.** Write the one-screen replacement policy as users would actually read it.

**References.** Course L29; NIST SP 800-63B (course references — its rotation guidance is the evidence anchor).

---

## PB-316 · Level 3 · The family history project and the 40-year-old disk

**Domain:** Data representation / File and backup management · **Related lectures:** L15, L16, L11

**Scenario.** A student's family asks them (the "computer one") to rescue a relative's archive: 5.25-inch floppies (1980s), a Zip disk, a phone with a dead charging port, printed photos, and a shoebox of undeveloped film. Mixed formats, unknown encodings, one shot at some media.

**Problem statement.** Plan the rescue: triage by fragility, choose capture methods (with the honesty of what's infeasible for a student), and design the *output* archive so this never recurs.

**Stakeholders.** The family (memories); the relative (consent over personal records); future family members (accessibility in 30 years).

**Inputs:** the media inventory; unknown encodings; one-shot risk. **Outputs:** triage plan + capture methods + output archive design. **Constraints:** student budget; some media may need specialist services (identify which honestly); consent needed for personal content.

**Learning objectives.** Reason about media longevity and format obsolescence (L15/L16 applied across decades); triage by *loss risk*; design archives for the next handover (PB-312's lesson, decades scale).

**Available information.** Floppy drives are rare but obtainable; Zip disks die suddenly (sticky-shed/click issues); film development is a commercial service; photos need scanning at chosen resolution; file formats from the era may need identification.

**Student task.** The triage order (most at risk first, with why) + capture method per medium (name what's realistically DIY vs specialist) + the output archive's design (formats, documentation, copies).

**Suggested thinking time.** 25 minutes.

**Expected solution characteristics.** Triage: film first (chemical degradation is time-critical, commercial service exists), then the dead-port phone (data extraction via repair or chip-off is specialist — honest boundary), then Zip (sudden-death risk), then floppies (stable-ish but drive availability), photos last (stable paper); capture: name DIY (floppy drive + imaging tools) vs specialist (film lab, phone repair) without inventing prices; output: open formats, plain-text inventory with context (who/what/when — the README *is* the preservation), 3-2-1 copies, and a named successor owner; the meta-lesson: every archive is a future PB-312 unless designed not to be.

**Discussion questions.**

1. Why does film outrank the floppies in urgency despite floppies being "older"?
2. What single documentation habit most increases the archive's 30-year survivability?

**Extension challenge.** Write the inventory template (5 columns) for the archive README.

**References.** Course L15–L16 (obsolescence), L11 (3-2-1); digital-preservation guides (instructor-provided); fictional family scenario.

---

## PB-317 · Level 3 · The lecture-recording consent standoff

**Domain:** Digital citizenship / Education technology · **Related lectures:** L20, L30

**Scenario.** A course wants to record lectures for revision access. A student refuses recording (privacy: their questions, health disclosures in class). Another faction needs recordings (commuting, illness, second-language processing). The instructor proposes recording with student questions cut; a student objects that *being visibly absent from the recording* outs them as the questioner.

**Problem statement.** Map all the privacy harms in this design space (not just the obvious one), evaluate the proposed mitigations, and design the consent architecture the course should adopt.

**Stakeholders.** The refusing student (dignity, outing risk); recording-dependent students (access); the instructor (teaching flow, policy); the university (policy compliance).

**Inputs:** the cutting proposal; the outing objection; access needs. **Outputs:** harm map + mitigation evaluation + consent architecture. **Constraints:** access must be genuinely preserved (token access fails); design must be explainable on day one.

**Learning objectives.** Enumerate privacy harms beyond the obvious (inference, absence-as-signal); design consent as architecture, not checkbox; balance access and dignity without dismissing either.

**Available information.** Recordings can pause for questions (latency acceptable); audio-only versions reduce visual exposure; the university has consent guidelines; absence-pattern inference is a real re-identification vector.

**Student task.** The harm map (≥4 harms, including non-obvious) + the evaluation of "cut questions" as mitigation + your architecture.

**Suggested thinking time.** 25 minutes.

**Expected solution characteristics.** Harm map: direct capture (voice/face), absence-as-signal (being the only gap), inference (health/guardianship disclosures), scope creep (recordings reused beyond course); evaluation: cutting questions *reduces* direct capture but *creates* the absence signal — partial fix that shifts harm; architecture: pause-and-resume for Q&A (everyone's gap, not targeted), audio-only alternative channel, day-one explanation, retention limit stated, and *opt-out of appearing* available to all (normalizing gaps) — dignity preserved by making absence uninformative; access preserved because content recording continues.

**Discussion questions.**

1. Why is "we cut the questions" a privacy *improvement and a new harm* simultaneously?
2. Which harm does your architecture not solve — and why is naming it better than pretending?

**Extension challenge.** Write the day-one course-policy paragraph implementing your architecture.

**References.** Course L30 (consent, inference harms); fictional course scenario.

---

## PB-318 · Level 3 · The hospital's tablet rollout (conceptual)

**Domain:** Healthcare information systems (conceptual) · **Related lectures:** L10, L24, L30

**Scenario.** A fictional hospital pilots tablets for ward round notes. Benefits: instant records at bedside. Risks discussed in the pilot: battery deaths mid-round, screen-sharing shoulder-surfing in corridors, autopsy-grade cleaning regimes, and nurses reporting the tablets *slow them down* (login friction) while doctors love them.

**Problem statement.** Structure the pilot evaluation: what to measure (efficiency vs role), the security/flow tensions, and the go/no-go criteria with the stakeholder whose voice the data would otherwise erase.

**Stakeholders.** Patients (privacy, care quality); nurses (workflow, the slow-down claim); doctors (enthusiasm); IT (management, cleaning compliance).

**Inputs:** pilot observations; the role-split sentiment; the cleaning/security requirements. **Outputs:** measurement plan + tension analysis + go/no-go criteria. **Constraints:** conceptual — no real hospital data; the evaluation must surface role-differential effects explicitly.

**Learning objectives.** Design evaluations that detect *differential* effects across roles (aggregation danger, L26); reason about security-flow tensions in care settings; set criteria before seeing results.

**Available information.** Sentiment is split by role; login friction is the nurses' named cause; cleaning regimes are non-negotiable; battery/privacy issues are engineering-solvable but flow friction may be structural.

**Student task.** The measurement plan (per-role metrics, not averages) + the two tensions analyzed + three go/no-go criteria set *in advance*.

**Suggested thinking time.** 25 minutes.

**Expected solution characteristics.** Measurement: time-per-note by role, error/omission rates, login-frequency counts, patient-facing privacy incidents — *never* averaged across roles (the nurse slow-down would vanish into doctor enthusiasm); tensions: security (lock, shoulder-surf) vs flow (re-login per room) — solvable via proximity/auth design trade-offs to be named, not assumed; cleaning-as-security (hygiene is also an availability issue); criteria: e.g., "no role's task time worsens >X%", "privacy incidents zero-tolerance", "cleaning compliance measurable" — set pre-hoc to resist enthusiasm after the fact; the erased-stakeholder framing: averages would have erased the nurses — the same aggregation ethics as PB-209 at institutional scale.

**Discussion questions.**

1. Why would a mean across roles have hidden the pilot's most important finding?
2. Which go/no-go criterion is hardest to measure honestly — and how would you audit it?

**Extension challenge.** Draft the pilot's one-page evaluation plan header (metrics table, three rows).

**References.** Course L24 (device management), L26 (aggregation), L30 (health privacy); conceptual scenario — no real clinical data or claims.

---

## PB-319 · Level 3 · The open-source dependency you didn't choose

**Domain:** Software installation / Small business ICT · **Related lectures:** L09, L12

**Scenario.** A small web agency's site uses a free plugin; the plugin's maintainer announces abandonment. Options: (a) freeze (works today), (b) fork it (needs skills they lack), (c) migrate to an alternative (redesign work), (d) pay a commercial replacement. The plugin handles contact forms and has 40k downloads — popular, but that's not maintenance.

**Problem statement.** Evaluate the four options with criteria that include *time* (the risk is future, not present), recommend, and design the monitoring that would have caught this earlier.

**Stakeholders.** The agency (clients' sites, reputation); clients (their forms keep working); the plugin's community (its ecosystem); future maintainers.

**Inputs:** four options; the agency's skills reality; the popularity-vs-maintenance distinction. **Outputs:** criteria evaluation + recommendation + monitoring design. **Constraints:** no security team; the decision must be explainable to non-technical clients.

**Learning objectives.** Reason about dependency risk as time-decaying (L09/L12); evaluate with maintenance criteria, not feature lists; design early-warning monitoring.

**Available information.** Unmaintained plugins accrue security holes as the platform evolves; forks need ongoing skills; alternatives exist with migration cost; commercial support exists at cost; the site's forms are lead-generation (business-critical).

**Student task.** The criteria table (include a "risk over 12 months" row) + recommendation + the monitoring design (three signals).

**Suggested thinking time.** 25 minutes.

**Expected solution characteristics.** Criteria: maintenance outlook, migration cost, skill fit, client impact, risk trajectory (freeze's risk *grows* — the row weak answers omit); recommendation varies by argued skills reality — commonly (c) with a staged migration or (d) if revenue justifies; freeze is defensible only with a sunset date; monitoring: release-activity signals (commit/review cadence), platform-compatibility advisories, security-announce subscription — designed to catch the *next* dependency before abandonment is announced; the distinction: popularity is not maintenance (40k downloads don't fix bugs).

**Discussion questions.**

1. Why does "it works today" actively mislead in this decision class?
2. Which monitoring signal would have warned you six months before the announcement?

**Extension challenge.** Write the client-explanation paragraph for your recommendation (no jargon, no panic).

**References.** Course L09 (software sourcing), L12 (maintenance); generalized agency scenario.

---

## PB-320 · Level 3 · The translation model in the university clinic (conceptual)

**Domain:** AI literacy / Healthcare information systems (conceptual) · **Related lectures:** L27, L28, L30

**Scenario.** A fictional university clinic proposes an AI translation aid for patient-intake conversations in three minority languages. Accuracy testing shows 85% sentence-level adequacy in benchmarks; staff anecdote says it helps; a community advocate warns that *systematic* errors in intake (allergies, medications) are precisely where 85% average is dangerous. The clinic has no budget for professional interpreters beyond emergencies.

**Problem statement.** Analyze where average accuracy misleads (error distribution, consequence asymmetry), design the deployment constraints that would make the tool acceptable, and specify what must be measured with the community, not about them.

**Stakeholders.** Patients (safety, dignity, language access); clinicians (workflow, liability); the communities (language equity); the clinic (legal/ethical standing).

**Inputs:** benchmark accuracy; the advocate's critique; the no-budget reality. **Outputs:** accuracy critique + deployment constraints + community-involvement measurement. **Constraints:** status quo (no interpreter) has its own harm — the tool isn't against a perfect baseline; no fabricated claims about the model's internals.

**Learning objectives.** Apply L27/L28: average metrics vs error distributions and consequence asymmetry; design constraints (scope, human roles) around known limitations; involve affected communities as evaluators, not subjects.

**Available information.** Intake hinges on a small set of high-consequence facts (allergies, medications, conditions); benchmarks aggregate sentence types; the community advocate represents speakers; professional interpreters are emergency-only here.

**Student task.** The accuracy critique (why 85% average is the wrong number) + deployment constraints (≥3) + the community-measurement design.

**Suggested thinking time.** 25 minutes.

**Expected solution characteristics.** Critique: error distribution matters (if the 15% concentrates in drug names/doses, the tool is unusable for intake regardless of average); consequence asymmetry (a mistranslated allergy is catastrophic; a mistranslated hobby is not) demands per-category metrics; constraints: scope-limited (triage/orientation, *not* clinical facts without human verification), mandatory human confirmation for the high-consequence set, visible failure-honesty signage, staff escalation path; community measurement: co-designed error taxonomies, speaker-panel review of real (anonymized) usage, grievance channel — *with* the community, not about them; the baseline honesty: no-interpreter status quo harms too, so the comparison is against *current* reality, not perfection.

**Discussion questions.**

1. Why is sentence-level benchmarking structurally blind to this clinic's real risk?
2. What does "human confirmation" cost the workflow — and who bears that cost?

**Extension challenge.** Draft the three-line intake-form protocol where the tool may and may not be trusted.

**References.** Course L27 (limits), L28 (evaluation, stakeholders), L30 (equity); fictional clinic; no real clinical claims.

---

## PB-321 · Level 3 · The energy dashboard that changed behaviour (and then didn't)

**Domain:** Sustainability / Data science workflows · **Related lectures:** L19, L26

**Scenario.** A university dorm piloted a live energy dashboard per floor. Usage dropped 9% in month one, then decayed to baseline by month three. The pilot report recommends *expanding* the dashboard. A student analyst asks whether the report measured the right thing.

**Problem statement.** Diagnose the decay (novelty effect vs other explanations), evaluate the expansion recommendation, and design the intervention that targets the decay mechanism rather than the symptom.

**Stakeholders.** Residents (behaviour, bills); the sustainability office (targets, budget); the analyst (methodology); future dorms (the expansion decision).

**Inputs:** the 9%→baseline curve; the expansion recommendation; the dashboard's design (passive display). **Outputs:** decay diagnosis + recommendation evaluation + intervention design. **Constraints:** interventions must be cheap; measurement honesty over advocacy.

**Learning objectives.** Distinguish competing explanations for a time-series pattern; evaluate recommendations against the diagnosed mechanism; design behaviour interventions with *feedback loops*, not information dumps.

**Available information.** Novelty decay is common in passive displays; the dorm has floor-level (not individual) data; comparisons between floors exist; the sustainability office has a small events budget; exams/seasons confound.

**Student task.** The diagnosis (≥3 candidate mechanisms, with the test that discriminates) + the evaluation of "expand" + your intervention design.

**Suggested thinking time.** 25 minutes.

**Expected solution characteristics.** Mechanisms: novelty decay (classic), confounds (season/exams — test against weather-normalized, non-pilot dorms), feedback absence (display shows numbers but no *actionable* loop); evaluation: expansion replicates the *input* (a display) without addressing the mechanism — likely replicates the decay too; intervention: social comparison (floor-vs-floor with a light goal), actionable framing ("tonight vs your floor's average"), periodic re-engagement events; honest boundary: behaviour effects are hard to sustain — set the *measurement plan* before expansion, so the next report can't fool itself either.

**Discussion questions.**

1. Which confound could masquerade as decay — and what data separates them?
2. Why does "more dashboards" satisfy the office's need to act while solving nothing?

**Extension challenge.** Write the three-line measurement plan that would settle expansion after one term.

**References.** Course L19 (design), L26 (confounds, honest measurement); fictional dorm scenario.

---

## PB-322 · Level 3 · The accessibility retrofit deadline

**Domain:** Accessibility and inclusive computing · **Related lectures:** L20; Lab 8 adjacent

**Scenario.** A student-built course-portal project (used by 400 students) fails key accessibility checks: no keyboard navigation for its quiz viewer, colour-only status coding, unlabeled form fields. A retrofit must ship in three weeks with one developer. The course owner proposes: fix everything; the developer proposes: fix the quiz viewer (highest-use path) + add a text-status channel + document the rest as known issues.

**Problem statement.** Evaluate both plans against user impact, effort realism, and honest communication; recommend; and design the *regression guard* so fixed things stay fixed.

**Stakeholders.** Students using assistive tech (immediate access); the course owner (compliance, optics); the developer (feasibility); future cohorts (the portal persists).

**Inputs:** the three defects; usage distribution; three-week window; one developer. **Outputs:** plan evaluation + recommendation + regression guard. **Constraints:** partial fixes are acceptable if *communicated* and prioritized by impact; standards (WCAG-class) name the targets.

**Learning objectives.** Prioritize accessibility fixes by user impact, not defect count; design honest partial-remediation communication; build regression guards into maintenance.

**Available information.** The quiz viewer is the highest-traffic component; form fields' labels are quick wins (high impact, low effort); colour-coding has a trivial text-status fix; full keyboard nav of the viewer is the big item; usage data exists.

**Student task.** The evaluation (both plans: impact, realism, communication) + recommendation + the regression guard (two mechanisms).

**Suggested thinking time.** 20 minutes.

**Expected solution characteristics.** Evaluation: "fix everything" ignores effort realism and likely delivers nothing finished in three weeks; the developer's plan is impact-ordered — but the *communication* component (published known-issues + alternative access path) is what makes it ethical rather than just pragmatic; recommendation: developer's plan plus immediate quick wins (labels, text-status — cheap, high-impact) and a stated schedule for the keyboard nav; regression guard: automated accessibility checks in the project's test routine (the repo's own validator culture, applied) + a manual screen-reader pass per release; the principle: accessibility is maintenance, not a one-time audit.

**Discussion questions.**

1. Why are the two quick wins non-negotiable even in a constrained plan?
2. What does your regression guard catch that a three-week sprint never could?

**Extension challenge.** Write the known-issues notice students would actually read (5 lines).

**References.** Course L20 (accessibility), Lab 8 (habits); WCAG quick-reference (instructor-provided); fictional portal scenario.

---

## PB-323 · Level 3 · The dual-supplier cloud dilemma

**Domain:** Cloud computing / Small business ICT · **Related lectures:** L24, L07

**Scenario.** A small e-learning startup runs entirely on one cloud provider. A competitor's major outage last year (a famous one) prompts the board to demand "no single point of failure." Engineering proposes three responses: (a) full multi-cloud deployment (both providers run everything), (b) warm standby on a second provider (data replicated, minimal runtime), (c) documented fast-exit plan (portability work + rehearsal, no second deployment). Budget: modest.

**Problem statement.** Evaluate the three architectures against outage risk, cost, complexity, and the failure modes of each *plan itself*; recommend; and name the risk your recommendation accepts.

**Stakeholders.** Learners (continuity); the board (risk optics, budget); engineering (complexity burden); the provider (relationship).

**Inputs:** three architectures; modest budget; the board's mandate. **Outputs:** evaluation + recommendation + accepted-risk statement. **Constraints:** the company is small — complexity kills startups too; the board's mandate ("no SPOF") may be infeasible literally.

**Learning objectives.** Evaluate resilience architectures at appropriate scale; recognize each plan's *own* failure modes; communicate accepted risk upward honestly.

**Available information.** Multi-cloud doubles operational surface (skills, incidents, cost); warm standby halves that but still needs sync + failover testing; fast-exit is cheapest but exit takes hours–days; the famous outage lasted hours, not days; data egress costs matter.

**Student task.** The evaluation (each option: protection level, cost, complexity, own failure mode) + recommendation + the accepted-risk sentence for the board.

**Suggested thinking time.** 25 minutes.

**Expected solution characteristics.** Evaluation: (a) maximum protection, but the complexity itself becomes the outage source for a small team — its own failure mode is *chronic*; (b) strong for data durability, failover still untested-until-tested — its failure mode is *stale/untested standby*; (c) cheap, but its failure mode is *the plan rotting* (unrehearsed, egress blocked by cost); common strong recommendation: (b)+(c) hybrid — standby for data, rehearsed-exit for runtime, with failover drills scheduled; accepted-risk statement: "brief (minutes-to-hours) runtime loss during regional outages is accepted; total data loss and multi-day exit are designed against" — the honesty of *naming* what's accepted is the senior move.

**Discussion questions.**

1. Why can the *solution to outages* cause outages — which option is most guilty?
2. What would you test quarterly to keep your chosen plan real rather than decorative?

**Extension challenge.** Write the board-slide headline (one sentence) + the accepted-risk footnote.

**References.** Course L24 (cloud semantics), L07 (capacity); generalized startup scenario.

---

## PB-324 · Level 3 · The course-recommendation algorithm (conceptual)

**Domain:** AI literacy / University administration · **Related lectures:** L26, L27, L28

**Scenario.** A university pilots a system recommending elective courses using past students' grades and enrolment patterns. Early evidence: recommendations correlate with prior programme (CS students get more CS), and the pilot cohort's satisfaction is high. A dean worries the system narrows exploration for first-generation students who already under-elect outside their programme. The vendor calls the system "bias-free because it uses only grades."

**Problem statement.** Analyze the vendor's claim (mechanism, not slogans), design the fairness evaluation (what to measure, on whom), and propose the pilot-extension rules that would satisfy both the dean and the satisfied majority.

**Stakeholders.** Students (exploration, outcomes — especially first-generation); the dean (equity); the pilot's satisfied users; the vendor (claims); the university (admissions fairness reputation).

**Inputs:** the correlation evidence; satisfaction data; the vendor's claim; the dean's concern. **Outputs:** claim analysis + fairness evaluation design + pilot rules. **Constraints:** the system uses only grades *as features* — the claim's truth depends on what grades *encode*; evaluation must be feasible for a pilot.

**Learning objectives.** See how "neutral" features encode history (L26/L28); design fairness evaluation with *populations*, not averages; propose operational rules that constrain without killing the pilot.

**Available information.** Grades reflect prior schooling, programme structures, and advice networks; the pilot cohort is self-selected; exploration breadth is measurable (elective diversity); first-generation status is available as a cohort marker (aggregate use only).

**Student task.** The claim analysis (what grades encode, mechanism) + the fairness evaluation design (metrics, populations) + three pilot rules.

**Suggested thinking time.** 25 minutes.

**Expected solution characteristics.** Claim analysis: "only grades" smuggles in *everything grades correlate with* — school effects, programme sorting, advice networks; the model doesn't need a protected-attribute input to produce correlated outputs; evaluation: recommendation diversity by cohort (aggregate, privacy-respecting), *outcome* follow-up (do recommended electives lead to grades/satisfaction comparable to self-chosen?), subgroup performance gaps; rules: exploration floor (some non-programme suggestions), opt-out honoured and easy, aggregate fairness reporting per term, no use for gating (advice only); the satisfied majority is honored by keeping the tool advisory — the dean's ask is constraints, not cancellation.

**Discussion questions.**

1. Why does removing protected attributes from inputs fail to remove bias from outputs?
2. Which of your rules would the vendor resist most — and why is that resistance informative?

**Extension challenge.** Draft the one-paragraph pilot report header that states fairness findings honestly.

**References.** Course L26–L28; NIST AI RMF (course references); conceptual scenario.

---

## PB-325 · Level 3 · The club's old projector and the new lecture

**Domain:** Hardware troubleshooting / Education technology · **Related lectures:** L03, L08, L16

**Scenario.** A society borrows a department's 8-year-old projector for a public lecture in a 150-seat hall. Test in a small room: fine. On the night: dim image, washed colours, audience complaints, a laptop HDMI handshake failure at the worst moment. The society's committee debates: never borrow old projectors / always test in the actual hall / buy their own projector (budget!).

**Problem statement.** Diagnose each failure from first principles (lumens vs room, colour shift vs surface, handshake vs cable/version), design the testing protocol that would have caught them, and decide the committee question with criteria.

**Stakeholders.** The society (reputation, budget); the audience (experience); the department (equipment loans); future speakers.

**Inputs:** three failure symptoms; the small-room test's inadequacy; three committee options. **Outputs:** per-failure diagnosis + protocol + decision. **Constraints:** budget small; the department loan remains available; lectures vary in venue.

**Learning objectives.** Connect display physics (L16) and interface realities (L08) to event failure; design *venue-realistic* testing; make an equipment-ownership decision with criteria.

**Available information.** Projector brightness is rated in lumens against screen size and ambient light; old lamps dim (the 8-year figure matters); colour shifts with surface and lamp age; HDMI handshake failures trace to cable/version/EDID quirks; halls differ wildly.

**Student task.** The three diagnoses (mechanism each) + the testing protocol (venue-realistic elements) + the committee decision with criteria.

**Suggested thinking time.** 20 minutes.

**Expected solution characteristics.** Diagnoses: lamp-age dimming × hall size/ambient light → insufficient lumens for the space (small-room test couldn't see it); colour wash → aged lamp spectrum + screen surface; handshake → cable/version/EDID negotiation — classic transient, solved by tested spares; protocol: test *in the venue* at talk-time lighting, full-sized content, measured from the back row, spare cable + second device rehearsed; decision varies with argued criteria (rental-quality loans per-event vs a mid-range owned unit amortized vs protocol-only) — the criterion that decides: venue variability (owned unit doesn't fix a new hall's lighting; protocol travels); strong answers often choose protocol + keep borrowing, *not* the purchase.

**Discussion questions.**

1. Why did the small-room test actively mislead rather than merely under-inform?
2. Which committee option treats the symptom while the protocol treats the cause?

**Extension challenge.** Write the society's "event AV checklist" card (6 lines, laminated in spirit).

**References.** Course L03/L08 (display hardware), L16 (light/sampling); vendor lumen guidance (instructor-provided); fictional event scenario.
