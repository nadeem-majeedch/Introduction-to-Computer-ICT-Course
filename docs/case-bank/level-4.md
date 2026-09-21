# Problem-Solving Case Bank — Level 4: Expert

**25 cases** · PB-401–PB-425 · Expert cases layer **multiple interacting constraints** — budget, reliability, security, accessibility, scalability, privacy, maintainability, user needs, environmental impact — and demand design decisions justified by explicit criteria. None requires professional infrastructure; all require professional *reasoning*. Method and rubric: [bank index](index.md).

---

## PB-401 · Level 4 · Designing the campus lost-and-found system

**Domain:** Database and information organization / Public service systems · **Related lectures:** L11, L25, L30

**Scenario.** The students' union wins a small grant to digitize the campus lost-and-found (currently a cardboard box and a paper log). Constraints collide: privacy (found IDs, wallets, keys with addresses), verification (claimants must prove ownership), retention (uncollected items eventually donated), accessibility (the desk staffs itself with rotating volunteers, some with disabilities), scale (2,000 items/term), and a zero-run-rate budget after the grant. Volunteer turnover is monthly.

**Problem statement.** Design the system end-to-end: data model, claim verification flow, retention policy, and the volunteer-rotability requirement. Justify every major choice against a stated criterion, and name the constraint you knowingly under-serve.

**Stakeholders.** Finders and claimants (fairness, privacy); desk volunteers (usability, turnover); the union (liability, grant accountability); uncollected-item recipients (donation pipeline).

**Inputs:** the grant (one-time); the current paper process; the volume; the volunteer reality. **Outputs:** design document (model, flow, policy, rotability) + criteria table + the named under-served constraint. **Constraints:** all of: privacy, verification, retention, accessibility, scale, budget-zero-after-grant, monthly volunteer turnover.

**Learning objectives.** Design under genuinely interacting constraints; make trade-offs *explicit and ranked*; document a system for successors who don't exist yet.

**Available information.** The union has institutional accounts and a website; free database-tools exist; photos can be taken at intake; claim verification currently relies on description matching; legal duties (found property) are set by university policy (instructor provides excerpt).

**Student task.** The design (data model with entities/keys; claim flow with verification steps; retention timeline; volunteer interface choices), the criteria table mapping each choice → criterion, and the honest paragraph naming what your design under-serves and why.

**Suggested thinking time.** 30 minutes; then structured defence.

**Expected solution characteristics.** Model: ITEMS (id, category, found-location, photo, intake-date, status), CLAIMS (item_id, claimant-contact, description-match, verified-date) — verification by *specific detail* (what's engraved in the wallet) rather than identity documents (privacy at intake); retention: 1-term hold → donation, with personal-data purge at disposition (minimization); rotability: simple state-machine statuses, no free text required, photo-first records (a volunteer with any device can intake in 90 seconds); the under-served constraint varies — commonly scalability of photo storage on a zero budget, or verification strength vs privacy (photo-of-item vs photo-of-contents) — *naming* it, with the reasoning, is the expert move.

**Discussion questions.**

1. Which constraint pair fights hardest (privacy vs verification? accessibility vs security?) — and how did your design pace that fight?
2. What happens to your system on the first malicious claim attempt — is the failure graceful?

**Extension challenge.** Write the volunteer's one-page intake procedure your design implies — no jargon, monthly-replaceable.

**References.** Course L25 (data design), L30 (minimization), L11 (retention); fictional union scenario.

---

## PB-402 · Level 4 · The clinic's offline-first records problem (conceptual)

**Domain:** Healthcare information systems (conceptual) / Cloud computing · **Related lectures:** L07, L24, L30

**Scenario.** A fictional rural clinic network (four sites, unreliable internet: hours-long outages weekly) pilots digital patient records. Requirements collide: availability during outages (care continues offline), consistency (the same patient's record at two sites), privacy (health data on shared infrastructure), auditability (who saw what), maintenance (one part-time technician), and hardware realities (dust, heat, power cuts). The vendor proposes a cloud-only system; a student intern proposes local servers; the technician proposes "cloud with local caching" without being able to specify it.

**Problem statement.** Design the architecture options properly (cloud-only, local-first with sync, hybrid-caching), evaluate against the named constraints with explicit criteria, recommend, and design the failure-mode story for the outage your recommendation will meet first.

**Stakeholders.** Patients (care continuity, privacy); clinicians (workflow during outages); the technician (maintenance load); the network's funder (cost); auditors (accountability).

**Inputs:** four sites; outage pattern; one technician; the three architecture families; audit requirement. **Outputs:** options analysis (criteria-weighted) + recommendation + first-outage narrative. **Constraints:** reliability during outages is non-negotiable; privacy and audit must survive the architecture; budget modest; skills constrained.

**Learning objectives.** Architect for *availability under partition* at student scale (the CAP intuition, conceptual); evaluate architectures where every constraint interacts; narrate failure modes before they occur.

**Available information.** Conflict rates (two sites editing one record) are low but non-zero; the technician can maintain one well-documented system, not two clever ones; audit logs must exist offline too; power cuts add hardware risk to local servers; the funder's budget covers either modest local hardware or cloud subscription, not both at scale.

**Student task.** The three-option evaluation table (each constraint × each option, with the interaction notes) + recommendation + the first-outage narrative (what happens, what the user sees, what recovers when connectivity returns).

**Suggested thinking time.** 30 minutes.

**Expected solution characteristics.** Strong answers surface the *interactions*: local-first maximizes availability but multiplies privacy surface and technician load; cloud-only maximizes maintainability but fails the non-negotiable; hybrid-caching is the honest frontier (write locally, queue, sync on reconnect) but its consistency story (conflicting edits) must be *designed*: last-writer-wins with audit trail, or field-level merge for low-conflict entities — either defensible if named; recommendation usually hybrid with scope control (offline cache only for that site's active patients — minimization again); the first-outage narrative must include audit logging offline and the sync-conflict path; the technician-load criterion usually decides scope (one system, documented, boring).

**Discussion questions.**

1. Why is "sync on reconnect" the easy half and "conflicting edits" the design's real test?
2. Which constraint did the vendor's cloud-only proposal treat as invisible — and why do vendors do that?

**Extension challenge.** Write the technician's runbook header (what breaks, what to check, what to never touch).

**References.** Course L24 (cloud semantics), L30 (health privacy); conceptual scenario — no real clinical systems specified.

---

## PB-403 · Level 4 · The exam-grade data pipeline for 8,000 students

**Domain:** Data science workflows / University administration · **Related lectures:** L19, L25, L26

**Scenario.** The registry assembles final grades from 200 course spreadsheets (lecturers' own formats), applies exam-board rules (scaling, resit caps, progression thresholds), publishes within 72 hours, and must survive: one lecturer's late submission, one format surprise, one rule change decided *during* assembly, and one student's grade-correction arriving mid-pipeline. Currently this is three staff with manual reconciliation and a heroics culture. The registry asks a student consulting team (you) for the design.

**Problem statement.** Design the pipeline: ingestion (heterogeneous inputs), rule application (versioned, auditable), publication (privacy, timing), and exception handling (late/corrected/changing inputs). Justify with criteria; specify what is *rejected* rather than silently fixed.

**Stakeholders.** Students (correct, timely, private grades); lecturers (their formats, their deadlines); registry staff (the 72 hours, their sanity); exam board (rule integrity); auditors (traceability).

**Inputs:** 200 heterogeneous spreadsheets; rule set (with in-flight changes); the 72-hour window; the exception classes. **Outputs:** pipeline design + criteria justification + the rejection policy. **Constraints:** privacy (per-student data through every stage); auditability (every grade's provenance); heterogeneity (lecturers won't standardize by decree); the human reality (late submissions happen).

**Learning objectives.** Design data pipelines with provenance and explicit rejection; handle schema heterogeneity by contract, not hope; make rules versioned artifacts, not tribal knowledge.

**Available information.** Most lecturers can export CSV from any tool; the rule set changes rarely but unpredictably; publication is per-student portal + registry archive; a correction mid-pipeline is a *re-run* question; staff time is the scarcest resource.

**Student task.** The pipeline design (stages, contracts, provenance markers, exception queues) + criteria table + the rejection policy (three things the pipeline must *refuse* rather than fix, and why).

**Suggested thinking time.** 30 minutes.

**Expected solution characteristics.** Design: (1) export contract (a simple template + validator at submission — heterogeneity handled by *feed-in* format, not by decree), (2) staging with provenance (every grade traceable to file+row+rule-version), (3) rules as versioned config (the mid-flight change becomes a *new version* applied to a named boundary — auditable, not retroactive chaos), (4) exception queues (late file → re-run affected course only; correction → targeted re-run with both versions archived); rejections: silently-coerced types (a "grade" of "pass???" must halt, not guess), duplicated student IDs, and cross-file aggregate mismatches — each rejection reason: silent fixing *destroys auditability*, the pipeline's core duty; privacy: per-student records through staging, no bulk spreadsheets emailed (L30); the expert note: the design must make the *honest path easier than the heroics* — contracts that validate early.

**Discussion questions.**

1. Why must the pipeline reject rather than coerce ambiguous values — connect to auditability explicitly.
2. Which is harder: the format contract or the mid-flight rule change? What makes each survivable?

**Extension challenge.** Draft the export-contract instruction sheet a busy lecturer reads in two minutes.

**References.** Course L25 (integrity), L26 (provenance), L19 (structured data); fictional registry scenario.

---

## PB-404 · Level 4 · Security, sustainability, and the 300-seat lab refresh

**Domain:** Sustainability / Hardware / University administration · **Related lectures:** L03, L07, L10, L12

**Scenario.** A faculty plans its 300-seat computer-lab refresh. Cross-pressures: sustainability mandate (the university's carbon plan), security patching (lab machines are shared, semi-public), budget (once per ~6 years), accessibility (some seats need specific adaptations), and utilization data showing 40% idle capacity (booking patterns). Four candidate strategies: (a) replace all hardware now (current default), (b) thin clients (longer life, server dependency), (c) staggered refresh of the most-used 60%, (d) hybrid: thin clients for general use + 20 full machines for specialist software. The carbon plan's fine print: *embodied* emissions dominate, so buying less matters more than efficiency ratings.

**Problem statement.** Model the strategies against all constraints (carbon including embodied, security posture, accessibility, cost-per-student-hour, resilience to vendor/update lifecycles), recommend with your weighting shown, and design the first-year security-operations plan for your choice.

**Stakeholders.** Students (availability, performance, adapted seats); the faculty (budget, carbon targets); IT operations (patching 300 seats); the sustainability office (the mandate's integrity); the accessibility service (adaptation requirements).

**Inputs:** utilization data; four strategies; the carbon plan's embodied-emissions principle; refresh history. **Outputs:** weighted evaluation + recommendation + year-one security-ops plan. **Constraints:** all six named constraints interact — e.g., thin clients reduce embodied carbon but add server dependency (availability risk); staggered refresh reduces waste but complicates patching (mixed fleet).

**Learning objectives.** Design under interacting institutional constraints; apply embodied-carbon reasoning to procurement (not just power ratings); write a security-operations plan proportionate to the chosen architecture.

**Available information.** Utilization shows booking clusters (peak hours, dead zones); thin-client lifespans historically exceed full PCs (less local failure); specialist software (engineering, data science) needs real compute for a subset of seats; patching 300 mixed-OS seats is the ops burden; accessibility adaptations ride on specific hardware (adjustable desks, specific peripherals).

**Student task.** The evaluation matrix (strategies × constraints, with interaction notes where two constraints fight) + weighted recommendation + year-one security-ops plan (patch cadence, imaging, incident scope).

**Suggested thinking time.** 35 minutes.

**Expected solution characteristics.** The interactions are the exam: (a) is defensible on simplicity but fails embodied-carbon and the utilization data; (b) minimizes embodied carbon and ops (one gold image) but the *server dependency* fails availability during server incidents and specialist seats still need real machines; (c) matches spend to use but mixed-fleet patching burden and the *visible inequality* of new-vs-old labs are real costs; (d) usually wins on the interactions (thin clients where general, real machines where measured need) but requires honest ops math — and the weighting must be *shown*; year-one security-ops: one gold image, scheduled patch window (L12's deliberate patching), lab-isolated network segment, incident scope = re-image (shared machines assume compromise — least-trust posture), adaptation seats inventoried in the image plan; the expert note: the carbon plan's embodied principle flips the default — the *best* environmental machine is the one not manufactured.

**Discussion questions.**

1. Which two constraints produce the sharpest fight in your matrix — and which one did you let win, at what cost?
2. Why does "40% idle" not simply mean "buy 60% less"? What does utilization data *not* tell you?

**Extension challenge.** Write the 150-word committee recommendation with your weights stated inline.

**References.** Course L03/L07/L10/L12; embodied-carbon ICT literature (instructor-provided); fictional faculty scenario.

---

## PB-405 · Level 4 · The city's open-data portal (conceptual)

**Domain:** Public service systems / Data science workflows · **Related lectures:** L22, L25, L26, L30

**Scenario.** A fictional city publishes open data (transport, budgets, air quality, service requests). Adoption is low, but one journalist's analysis of the service-request data caused a minor scandal (response-time disparities by district). The city now debates: (a) pause publication pending review, (b) publish everything faster (the open-by-default position), (c) a middle path with quality tiers and publication review. Cross-pressures: transparency's public value, data quality (districts enter data inconsistently), privacy (service-request narratives sometimes contain personal details), re-identification risk in aggregate data, and the city's capacity (two staff).

**Problem statement.** Design the publication policy: quality tiers, privacy review process (proportionate to two staff), the re-identification assessment method, and the response to the scandal dynamic (publication as accountability vs publication as risk). Justify against criteria; name the position's residual risk.

**Stakeholders.** Residents and journalists (accountability, access); district staff (data-entry reality); the two-person open-data team (capacity); vulnerable individuals in narratives (privacy); the city leadership (scandal exposure).

**Inputs:** the scandal episode; the quality inconsistency; the privacy incidents; two staff. **Outputs:** policy design + criteria justification + residual-risk statement. **Constraints:** transparency value is real (name it, don't dismiss); privacy review must scale to two staff; quality tiers must not become a censorship mechanism; re-identification risk is dataset-specific.

**Learning objectives.** Balance transparency, privacy, and quality as *policy design*, not vibes; design proportionate review processes; treat re-identification as a dataset-specific assessment, not a checkbox.

**Available information.** Narrative fields carry most privacy risk (they can be dropped or generalized); numeric/response-time fields are lower-risk but quality-varied; the journalist's method (comparative district analysis) was legitimate; k-anonymity-class thinking applies to published aggregates (concept level); the team can automate format validation but not content review.

**Student task.** The tiered policy (which data classes get which treatment) + the privacy-review process (proportionate to two staff) + the re-identification assessment method + the residual-risk paragraph.

**Suggested thinking time.** 30 minutes.

**Expected solution characteristics.** Tiers: automated publication for structured/low-risk fields (transport, budgets) — open-by-default where risk is low; standardized-review class for narrative-bearing data (strip/replace free text, delay publication by one cycle for review); paused class only for demonstrated re-identification risk (assessed per dataset, published criteria — the *published criteria* are what stop tiers becoming censorship); review process: intake checklist + automation (field-type validation) + a named second reviewer for the narrative class; re-identification method: enumerate the linking datasets that exist (other open data, electoral registers) and test the specific dataset's uniqueness on plausible joins (concept-level, documented); residual risk honestly named: small cells + creative linking will sometimes re-identify — the policy's delay-and-review reduces but never eliminates, and the *response protocol* (who to notify, correction path) is part of the design; the scandal framing: the disparity analysis was *the portal working* — the answer to accountability journalism is data quality, not data suppression.

**Discussion questions.**

1. Why must the tier criteria be published — what does an unpublished tier list become?
2. Which is more dangerous to the city: the next journalist's analysis, or the perception that pausing is easy?

**Extension challenge.** Write the two-page policy's opening "principles" section (5 principles, one sentence each).

**References.** Course L26 (open data ethics), L30 (privacy); open-data guides (instructor-provided); fictional city scenario.

---

## PB-406 · Level 4 · The family's digital estate plan

**Domain:** Cybersecurity and privacy / Ethical and societal implications · **Related lectures:** L11, L29, L30

**Scenario.** A student's family asks them to organize "what happens to our digital stuff" after a relative's sudden illness made it urgent: two adults' accounts (email, banking, cloud photos, subscriptions, a small business's social accounts), shared devices, and no documentation anywhere. Legal context (generalized): access after death varies by service and jurisdiction; recovery by guessing passwords is neither reliable nor necessarily permitted. The family wants dignity, access, and security simultaneously.

**Problem statement.** Design the digital-estate plan: the inventory method, the access-transfer mechanisms (per account class), the security of the plan itself, and the boundaries (what the plan must *not* try to do). Justify with criteria; flag where professional advice (legal) is required rather than attempted.

**Stakeholders.** The relatives (access, dignity); the plan's executor (clarity under stress); the services (their own policies); the small business (continuity); future family members (the photos).

**Inputs:** the account inventory classes; the urgency; the generalized legal context. **Outputs:** estate plan design + criteria table + the boundaries section. **Constraints:** the plan must survive being *unused for years then needed suddenly*; it must not become a security liability itself; legal specifics vary — the design must degrade gracefully to "consult a professional."

**Learning objectives.** Design for low-frequency, high-stakes events; balance access against security in a plan that outlives its author's presence; know the boundary between design and professional territory.

**Available information.** Major services offer legacy/inactive-account mechanisms (named generally in course references); password managers support emergency access; the small business's accounts may be transferable via business tools; the family shares trust but not technical fluency; the plan will live on paper + a sealed location (their choice).

**Student task.** The inventory method (how to enumerate, how to store) + per-class access mechanisms (email/financial/subscriptions/photos/business) + the plan's own security design + the boundaries paragraph.

**Suggested thinking time.** 30 minutes.

**Expected solution characteristics.** Inventory: classified list (account, class, recovery mechanism, notes), stored encrypted (password-manager secure note) with a paper *pointer* (not passwords) in the sealed location; mechanisms: built-in legacy tools first (designed for this), manager emergency-access for credentials, business-tool transfer for the commercial accounts, financial institutions routed through their documented processes (never password-sharing for banks — both unreliable and policy-violating); plan security: the pointer reveals nothing without the manager's emergency access (which requires the service's own dead-man verification); boundaries: no jurisdiction-specific legal claims, no circumvention of service terms, no assuming today's mechanisms persist — annual review is part of the design; the dignity thread: the plan is drafted *with* the relatives (their wishes recorded), not imposed on them.

**Discussion questions.**

1. Why is a paper list of passwords the classic wrong answer — and what property does your design preserve that it loses?
2. Which account class has the *worst* transfer mechanism in your research, and how does the plan cope?

**Extension challenge.** Write the one-page "letter to the executor" template the plan implies.

**References.** Course L11 (documentation), L29 (credential hygiene), L30 (data lifecycle); service legacy-account documentation (instructor-provided, generalized); fictional family scenario.

---

## PB-407 · Level 4 · The lecture-capture system with a maintenance cliff

**Domain:** Education technology / Cloud computing · **Related lectures:** L10, L20, L24

**Scenario.** A university's lecture-capture system (recordings in faculty rooms, published to a portal) runs on aging custom software; the vendor is sunsetting it. Migration options: (a) vendor's new cloud product (subscription, data residency questions), (b) open-source self-hosted recording pipeline (capability exists, one admin), (c) minimal pivot: low-cost recording + existing video platform (loses room-automation integration). Cross-pressures: 400 hours of existing recordings (continuity), data-residency policy (recordings include student voices), accessibility requirements (captions — currently manual and backlog-growing), the one-admin reality, and cost visibility (subscription vs hidden self-host labour).

**Problem statement.** Design the decision: evaluation criteria (including *true* cost and the caption debt), the migration plan for continuity (400 hours + in-flight semester), and the accessibility trajectory under your choice. Name the risk your choice accepts and the tripwire that would reverse it.

**Stakeholders.** Students (access, captions, continuity); lecturers (workflow); the admin (maintenance reality); the university (residency policy, cost); accessibility service (caption debt).

**Inputs:** three options; the recording archive; the caption backlog; one admin; residency policy. **Outputs:** criteria-weighted decision + migration plan + accessibility trajectory + tripwire. **Constraints:** continuity through a semester boundary; captions are a *debt* that compounds; hidden labour must be costed honestly; residency constraints bind.

**Learning objectives.** Compare total cost of ownership honestly (subscription vs labour); plan migrations under continuity constraints; treat accessibility debt as a first-class decision input.

**Available information.** The cloud product handles captions via machine transcription + human correction tier; self-hosted pipelines exist but captions remain manual there too; the video platform (option c) has machine captions; the archive can be bulk-transferred in all options; residency policy requires regional hosting (the cloud product offers a region — verify); the admin can maintain either self-hosted or vendor-managed, not both.

**Student task.** The criteria table (with the caption-debt row and the true-cost row made explicit) + decision + migration plan (three phases, semester-boundary aware) + tripwire.

**Suggested thinking time.** 30 minutes.

**Expected solution characteristics.** Criteria include: continuity risk, true cost (subscription fee vs admin-hours × salary — shown, not asserted), caption trajectory (machine-first with correction workflow beats a growing manual backlog — the debt shrinks only where automation + correction exists), residency compliance (verify region, don't assume), single-admin sustainability; decision commonly (a) if residency verifies, (b) if it doesn't — but *the verification step must precede the decision* (the expert discipline); migration: phase 1 dual-run on new system for one course, phase 2 bulk archive transfer + redirect links, phase 3 in-flight semester cut over at the boundary; tripwire: e.g., "if the vendor's regional hosting lapses or caption quality degrades below X, re-open decision" — naming the reversal condition is what makes the choice a decision rather than a bet.

**Discussion questions.**

1. Why is the caption backlog a *decision input* rather than an operational detail?
2. What does "true cost" hide in each option that a fees-vs-licence comparison misses?

**Extension challenge.** Write the one-slide summary for the budget committee: costs, risks, tripwire.

**References.** Course L20 (accessibility), L24 (cloud), L07 (capacity); fictional university scenario.

---

## PB-408 · Level 4 · The neighborhood mesh network proposal (conceptual)

**Domain:** Networking / Sustainability / Public service systems · **Related lectures:** L21, L22, L30

**Scenario.** A student volunteer group proposes a community Wi-Fi mesh for a neighbourhood with poor affordable internet. The proposal document assumes: donated routers on rooftops, volunteer maintenance, and "the internet is a right." Cross-pressures the proposal ignores: security (open mesh = shared risk; who is responsible for abuse on the exit node), sustainability (volunteer burnout, hardware death), legality/policy (some ISPs' terms restrict sharing; liability questions), privacy (traffic transiting neighbours' equipment), and honest capacity (mesh backhaul is slower than the marketing suggests). The group asks you to make the proposal *survive contact with reality*.

**Problem statement.** Redesign the proposal: architecture (mesh topology vs distributed individual shares), governance (who is liable, who maintains, exit plan), security posture (exit-node responsibility, user education), and the sustainability plan (hardware lifecycle, volunteer succession). Justify with criteria; keep the mission while naming what the mission must give up.

**Stakeholders.** Residents (access, cost); volunteers (burnout, liability); ISPs (their terms); abuse victims (if the exit node is misused); the neighbourhood (trust once broken is not rebuilt).

**Inputs:** the proposal's assumptions; the constraint list; small budget; volunteer enthusiasm. **Outputs:** redesigned architecture + governance + security posture + sustainability plan. **Constraints:** all five cross-pressures; the mission (affordable access) must survive the redesign recognizably.

**Learning objectives.** Convert an idealistic proposal into a survivable design; assign responsibility for shared infrastructure explicitly; design volunteer-system succession (PB-312's lesson at infrastructure scale).

**Available information.** Individual-share architectures (each home shares its own subscription under its own name) distribute liability more cleanly than a collective exit node; mesh backhaul degrades with hops; router hardware dies in 3–5 years outdoors; abuse-responsibility defaults to the subscription holder; ISP terms vary (instructor provides generalized guidance).

**Student task.** The redesign (architecture choice + governance model + security posture + succession plan) + criteria table + the mission paragraph (what the redesign preserves and what it explicitly gives up).

**Suggested thinking time.** 35 minutes.

**Expected solution characteristics.** Architecture: typically *distributed individual shares* (each host shares under their own subscription, mesh only for dead zones) over a collective exit — liability and abuse-responsibility stay local and attributable, the model's biggest survival property; governance: a named small committee, simple rules (who may host, what happens on abuse report), and a written exit/wind-down plan (the mesh's death is a *planned event*, not a decay); security: guest-network isolation per host, no transit of host-family traffic through guest VLANs, exit-node abuse protocol (suspend → investigate → document), user education at onboarding; sustainability: hardware lifecycle fund (small monthly seed), spares pool, volunteer *pairing* (no single points of human failure — PB-312 again); mission paragraph: preserves affordable access where feasible; gives up "free for all" (hosted shares have limits) and "no rules" (rules are what make it last); the honest capacity note: mesh hops throttle backhaul — dead zones get coverage, not speed.

**Discussion questions.**

1. Why does the collective exit node concentrate the proposal's fatal risk — trace the abuse scenario end to end.
2. Which constraint does the original proposal's "internet is a right" framing obscure — and how does your redesign honor the value without the slogan?

**Extension challenge.** Write the host-family's one-page "what you're agreeing to" document.

**References.** Course L21 (mesh/topology), L30 (shared infrastructure ethics); generalized ISP-term guidance (instructor-provided); fictional neighbourhood scenario.

---

## PB-409 · Level 4 · The AI TA at exam scale (conceptual)

**Domain:** AI literacy / Education technology · **Related lectures:** L27, L28, L30

**Scenario.** A course with 1,200 students pilots an AI teaching assistant answering course questions 24/7. Pilot results (one section, 80 students): high satisfaction, three documented hallucination incidents (one confidently wrong about an exam rule), instructor time saved ~4 hours/week. Scaling to 1,200 collides with: hallucination stakes (exam-rule errors propagate at scale), the equity question (students with AI access skills extract more value), disclosure and data policy (student questions contain personal context), and the illusion of coverage (instructors may skip office hours, assuming the TA covers gaps it doesn't). The dean wants scale; the instructor wants guardrails.

**Problem statement.** Design the scale decision: capability boundaries (what the TA may answer, how it declines), the error-rate monitoring design, the equity and disclosure mechanisms, and the office-hours interaction (what human coverage must remain regardless). Justify with criteria; specify the *pilot evidence that does not transfer* to scale.

**Stakeholders.** Students (accurate help, equity, privacy); instructors (time saved, accuracy accountability); the dean (scale economics); the vendor (claims); students who distrust AI (their access path too).

**Inputs:** pilot metrics; the three incidents; the scale factor (15×); the constraint list. **Outputs:** capability-boundary design + monitoring plan + equity/disclosure mechanisms + human-coverage floor. **Constraints:** hallucination stakes rise with scale; equity must be designed, not assumed; disclosure must be honest without poisoning usage; the office-hours floor must be argued, not asserted.

**Learning objectives.** Distinguish pilot-transferable from pilot-misleading evidence; design AI deployment boundaries (scope, refusal, disclosure); protect non-user populations in AI rollouts.

**Available information.** Exam-rule questions are rare but high-stakes — a curated FAQ layer can handle them deterministically; question logs can be monitored for hallucination *classes*; usage data shows some students never use the tool; office hours at scale are imperfect anyway; the vendor supports scoped answers (course-material grounding) with citations.

**Student task.** The boundary design (allowed/declined/question-types, with the citation-grounding rule) + monitoring plan (what's logged, what triggers review) + equity/disclosure mechanisms + the human floor (what office hours must still cover and why).

**Suggested thinking time.** 30 minutes.

**Expected solution characteristics.** Boundaries: course-material-grounded answers with citations (hallucination class 1 addressed), deterministic FAQ layer for exam/assessment rules (class 2 — never let a generative answer near policy), graceful refusal outside scope (class 3) with human-redirect; monitoring: sampled answer audits + incident reports + question-class logs (the three pilot incident classes each get a tripwire); equity: use-data reviewed per cohort *by access pattern* (not demographics), alternative paths kept equivalent (the same FAQ published to all, not only in the TA), and the disclosure that normalizes both use and non-use; human floor: office hours remain for *ambiguity, appeals, and the questions the TA refuses* — the floor's argument is the refusal class, not sentimentality; non-transferable evidence: satisfaction and time-saved from a self-selected pilot cohort of 80 (enthusiasts, small-N incidents) do not predict 1,200-user behaviour — name this explicitly.

**Discussion questions.**

1. Why is the exam-rule incident the most important of the three — what does its *class* tell you about boundaries?
2. Which pilot metric is most misleading at 15× scale, and why did it look so good?

**Extension challenge.** Write the students' announcement: what the TA is, isn't, and when to see a human.

**References.** Course L27/L28 (limits, grounding), L30 (equity, disclosure); fictional course scenario.

---

## PB-410 · Level 4 · The four-year phone-lab sustainability project

**Domain:** Sustainability / Education technology / Hardware · **Related lectures:** L03, L08, L12, L24

**Scenario.** A department designs a four-year teaching lab for app-development and data-science courses using smartphones (students' own or lab units). The sustainability office requires: minimum embodied carbon, maximum lifespan, and a credible end-of-life path. Cross-pressures: OS update horizons (security), hardware heterogeneity (teaching against 20 device models is chaos), student ownership equity (not all students own capable devices), software requirements (some courses need specific OS versions), and the e-waste reality (lab units retired while functional are the exact waste the policy targets). Four strategies on the table: (a) BYOD with minimum-spec published, (b) department buys a standard lab unit ×80, (c) BYOD + a small loaner pool for equity, (d) BYOD + refurbished devices purchased second-hand for the pool.

**Problem statement.** Evaluate the four strategies against the full constraint set (carbon, lifespan, equity, heterogeneity, update horizons, e-waste), recommend with weights shown, and design the end-of-life path for your choice (what happens to each device class, when, and to whose benefit).

**Stakeholders.** Students (equity, learning experience); the sustainability office (mandate integrity); instructors (heterogeneity chaos); IT (security updates on lab units); the refurbishment sector (a real partner or a wish).

**Inputs:** four strategies; the constraint set; four-year horizon. **Outputs:** weighted evaluation + recommendation + end-of-life design. **Constraints:** equity is a hard constraint (a student must never be unable to participate); update horizons bound usable life; e-waste policy targets *functional devices retired* — the design must not create that waste.

**Learning objectives.** Apply lifecycle thinking (embodied carbon, update horizons, second life) as design constraints; resolve equity through architecture rather than exception-handling; design end-of-life as part of procurement, not afterthought.

**Available information.** Refurbished devices cost ~40–60% of new and carry no new embodied carbon; OS support horizons vary by vendor class (flagship > budget); a minimum-spec document (RAM, OS version, years of updates remaining) is enforceable at purchase-time but decays; loaner pools of ~10% cohort size historically suffice; local refurbishers exist but require relationship-building.

**Student task.** The evaluation matrix (strategies × constraints with interaction notes) + weighted recommendation + the end-of-life path (per device class: teaching life → second life → disposal, with timelines and partners).

**Suggested thinking time.** 35 minutes.

**Expected solution characteristics.** Evaluation tensions: (a) BYOD is cheapest-carbon but fails equity hard-constraint without a pool; (b) 80 new units is the worst embodied-carbon outcome and creates the exact retire-functional-devices waste the policy names; (c) fixes equity but pool of new devices repeats (b)'s carbon; (d) — BYOD + refurbished loaners — usually wins: equity served, near-zero new embodied carbon, refurbishment sector strengthened, end-of-life easier (already once-cycled devices); weights must be shown; end-of-life design: teaching life (4y) → loaner downgrade (1–2y) → accredited refurbisher/reseller (second life) → certified recycler only at true end-of-life, with data-wipe certificate at every transition (security constraint persists past use); update-horizon rule: devices enter the pool only with ≥3 years of updates remaining (the *purchase filter* that makes (d) survive the security constraint); heterogeneity handled by the minimum-spec + emulator for edge cases rather than fleet standardization.

**Discussion questions.**

1. Why does the e-waste policy point *against* the strategy everyone finds simplest (buy new, one model)?
2. Which constraint would break strategy (d) first if the refurbisher relationship failed — and what's the fallback?

**Extension challenge.** Write the minimum-spec one-pager students receive before the semester.

**References.** Course L03/L08 (hardware), L12 (update horizons); embodied-carbon smartphone literature (instructor-provided); fictional department scenario.

---

## PB-411 · Level 4 · The hospital's alert-fatigue problem (conceptual)

**Domain:** Healthcare information systems (conceptual) / AI literacy · **Related lectures:** L27, L28, L30

**Scenario.** A fictional hospital's monitoring systems generate 200+ alerts per nurse per shift; 85–90% are actionable-but-minor or false positives. The predictable human result: alert desensitization — and the near-miss where a real critical alert was dismissed as noise. A vendor proposes an AI triage layer that suppresses low-priority alerts (projected 60% reduction). The nursing lead's fear: "the suppressed alert will be the one that matters." The safety officer wants the near-miss investigated before anything changes.

**Problem statement.** Structure the problem: the fatigue mechanism (why 200 alerts produce worse outcomes than 40), the AI layer's risk profile (what suppression optimizes vs what safety needs), the investigation design for the near-miss, and the implementation path (if any) with the monitoring that could detect a suppressed-alert disaster before it compounds.

**Stakeholders.** Nurses (workload, moral weight of dismissal decisions); patients (the alerts exist for them); the vendor (claims); the safety officer (systemic view); hospital leadership (liability, costs).

**Inputs:** the alert statistics; the near-miss; the vendor's proposal; the nursing lead's objection. **Outputs:** mechanism analysis + risk profile + investigation design + implementation path/monitoring. **Constraints:** doing nothing is also a decision (fatigue has casualties); suppression errors are catastrophic-rare — the monitoring must catch the rare; conceptual scenario — no real clinical protocol specified.

**Learning objectives.** Analyze alarm fatigue as a systems problem (signal-to-noise, human factors) rather than a volume problem; evaluate AI safety layers by their *failure distribution*, not their average; design pre-implementation monitoring for catastrophic-rare failures.

**Available information.** Alert fatigue research (concept level) shows desensitization scales with false-positive rate; critical alerts are a small minority of volume; the AI's projected suppression is *low-priority* classes — but priority labels come from the same noisy system; the near-miss involved a misclassified-priority alert; incident-reporting culture varies by unit.

**Student task.** The fatigue mechanism analysis (why the 200-alert stream degrades decisions) + the AI layer's risk profile (error distribution, what suppression optimizes) + the near-miss investigation design + the implementation path with monitoring.

**Suggested thinking time.** 35 minutes.

**Expected solution characteristics.** Mechanism: constant low-grade interrupts deplete attention; sensitivity to *rare* critical signals decays with exposure to noise (the boy-who-cried-wolf dynamics, formalized); the system's failure is not volume but *signal-to-noise with human cost on both sides*; AI-layer risk profile: suppression optimizes average workload, but its errors concentrate exactly where the human has been desensitized (the suppressed alert meets an inattentive nurse — errors *compound*); investigation design: the near-miss gets a systemic analysis (not blame — the priority label came from the system), tracing the misclassification source, reporting-culture review; implementation path: staged (shadow mode first — AI classifies but doesn't suppress, human disagreement logged as training/monitoring data; then narrow-class suppression with hard floors — certain alert classes never suppressible), monitoring: weekly disagreement audits, suppressed-alert outcome tracing (every suppressed alert whose patient later deteriorates gets review — the tripwire), and a standing nurse escalation path that requires no justification; the honest framing: the vendor's 60% number is an *average* claim — safety needs the tail.

**Discussion questions.**

1. Why does suppression-error × desensitization compound rather than merely add — express the mechanism.
2. What does "shadow mode first" buy that a pilot-with-suppression does not?

**Extension challenge.** Write the one-paragraph stance a nursing union representative could read aloud: conditions under which the layer is acceptable.

**References.** Course L27/L28 (AI limits, evaluation); alarm-fatigue literature (instructor-provided, concept level); fictional hospital scenario.

---

## PB-412 · Level 4 · The archive of a closed social platform

**Domain:** Data representation / Ethical and societal implications / File and backup management · **Related lectures:** L15, L16, L11, L30

**Scenario.** A fictional social platform for a niche research community announces closure in 90 days: 15 years of public discussions, shared datasets, and project pages. A member consortium wants to preserve it. Cross-pressures: consent (members posted under one privacy regime; closure changes the context), scope (15 years × multimedia × linked resources — what's *worth* preserving), format (platform-proprietary structures, embedded media, dead links), law (generalized: copyright of posts vs platform ownership of the corpus), and curation labour (volunteers, 90 days). The platform offers a full database export — 400 GB, undocumented schema.

**Problem statement.** Design the preservation project: consent framework (what may be preserved, under what notice), scope policy (what's in, what's out, by what criteria), technical approach (export → browsable archive: formats, structure, link-rot strategy), and the sustainability handover (PB-312 at corpus scale). Justify with criteria; name what is knowingly lost.

**Stakeholders.** Community members (their contributions, their consent); researchers (future corpus); the platform (its obligations); the consortium volunteers (labour, liability); posterity (the 15 years).

**Inputs:** the 90-day window; the export offer; the consent regime's terms; volunteer capacity. **Outputs:** consent framework + scope policy + technical approach + handover design. **Constraints:** consent changes with context (closure makes posts permanently public in new ways); the export is undocumented; 90 days bounds ambition; copyright boundaries are generalized — the design flags rather than resolves legal questions.

**Learning objectives.** Design preservation under consent and context-collapse constraints; make scope decisions by explicit criteria under time pressure; document an archive for users who don't exist yet.

**Available information.** The platform's terms (instructor-provided excerpt) govern corpus ownership; members can be notified in-app; the export's schema is inferable from content; static-site generation and format conversion are feasible with the group's skills; the community has one professional archivist (advising, not doing).

**Student task.** The four-part design + criteria table + the knowingly-lost paragraph (what your scope policy excludes and why that loss is accepted).

**Suggested thinking time.** 35 minutes.

**Expected solution characteristics.** Consent: notification + opt-out window (posts removed on request — the *right to object* matters more than perfect consent, which is unattainable retroactively), context statement published with the archive ("preserved because the platform closed; not for new distribution"); scope: criteria-based — full text + images by default, embedded third-party media by *link inventory only* (dead links documented — honest link-rot accounting), private/deleted content excluded absolutely; technical: export → schema inference (documented as inferred, not authoritative) → conversion to open formats (plain text + standard image formats) → static browsable archive + checksummed preservation masters; handover: three institutional copies (3-2-1), a named steward organization, an annual fixity check ritual, and a README in the PB-316 tradition — the archive's context is its survival; knowingly-lost: dynamic features (search-as-was, threaded notifications), some dead embedded media, and any post whose author opts out — each loss named with the criterion that accepted it.

**Discussion questions.**

1. Why does closure change consent even when no post's *content* changes — express the context-collapse mechanism.
2. Which scope criterion was hardest to write — and what does your excluded class cost posterity?

**Extension challenge.** Write the archive's front-page statement: what this is, what it isn't, how to request removal.

**References.** Course L15/L16 (formats), L30 (consent, context); digital-preservation guidance (instructor-provided); fictional platform scenario.

---

## PB-413 · Level 4 · The exam-portal rewrite under a live semester

**Domain:** Small business ICT / Web technologies · **Related lectures:** L09, L22, L25, L29

**Scenario.** A small ed-tech firm's exam portal (30 institutional clients, 200k exam-takes/year) needs a rewrite: the codebase is 8 years old, one departing developer holds tribal knowledge, security patches land slowly, and clients demand features the architecture resists. The semester is live — no downtime window exists. Three approaches: (a) big-bang rewrite then cutover (classic, risky), (b) strangler migration (new system grows around the old, routes shift gradually), (c) hardening-first (fix security/perf on the old code, defer the rewrite a year). Cross-pressures: the departing developer's knowledge (capture it or lose it), security exposure during migration (the old system runs months longer), client trust (one failed exam window ends the firm), and the firm's runway (12 months).

**Problem statement.** Design the migration: approach choice with criteria, the knowledge-capture plan (what must exist before the developer leaves), the security posture during the transition, and the cutover safety net (what makes an exam-window failure recoverable). Name the failure mode that kills the firm under your plan — and its specific mitigation.

**Stakeholders.** Exam-takers (integrity, availability); client institutions (trust, features); the firm (survival, runway); the departing developer (knowledge, goodwill); the new developers (the codebase they inherit).

**Inputs:** three approaches; the timeline; the runway; the live-semester constraint. **Outputs:** approach decision + knowledge-capture plan + transition security posture + cutover safety net. **Constraints:** zero downtime tolerance during exams; knowledge walks out the door on a known date; security debt compounds during any long transition; runway bounds team size.

**Learning objectives.** Choose between rewrite strategies under operational constraints; capture expert knowledge as a deadline-bound artifact; design cutover safety nets where failure is existential.

**Available information.** The old system's exam-window behaviour is battle-tested (its *reliability* is an asset the rewrite must match, not assume); the departing developer will document if asked properly (their exit is 6 weeks out); the strangler pattern allows per-feature routing (new exam-booking first, grading last); a parallel-run option exists for read paths; the runway supports 3 developers.

**Student task.** The four-part design + criteria table + the firm-killing failure mode named with its mitigation.

**Suggested thinking time.** 35 minutes.

**Expected solution characteristics.** Approach: (b) strangler usually wins — big-bang (a) bets the firm on a single cutover with unproven reliability at exam scale; hardening-first (c) is defensible if runway were longer, but defers the structural problems clients already feel; knowledge-capture: the departing developer writes the *operations* doc (deployment, failure modes, exam-window runbook, the undocumented quirks — "the Tuesday deploy rule" class of knowledge) as their final deliverable, pair-documented, reviewed by the new team *while they can still ask*; security posture during transition: the old system's patching accelerates (it runs longer — the transition must not become a security holiday), auth migration early (credentials handled once, carefully), the exam window's WAF/monitoring unchanged; cutover safety net: per-feature flags (instant rollback per feature, not per system), parallel-run verification for grading (both systems compute, compare, alert), and the exam-window freeze ritual (no migrations inside exam windows — scheduled around the client calendar); firm-killing failure mode: the first exam window on the new booking path failing at load — mitigation: load-test at 3× last year's peak, feature-flag rollback rehearsed, and the *old path kept warm* (not deleted) for two full exam cycles.

**Discussion questions.**

1. Why is the old system's reliability an asset that a rewrite must *earn*, not assume?
2. What makes the knowledge-capture doc different from ordinary documentation — and why does the deadline change its content?

**Extension challenge.** Write the exam-window runbook's table of contents (10 entries) — the departing developer's outline.

**References.** Course L09 (software lifecycle), L22 (load), L29 (patching); generalized migration-pattern literature (instructor-provided); fictional firm scenario.

---

## PB-414 · Level 4 · The two-town broadband decision (conceptual)

**Domain:** Public service systems / Networking / Sustainability · **Related lectures:** L21, L22, L04

**Scenario.** A fictional regional government must choose a broadband intervention for two towns: Town A (dense, aged copper, 5,000 households, two ISPs willing to invest with subsidy), Town B (scattered, 800 households, no commercial interest, existing community-broadband initiative that collapsed in debt). Total budget covers one town properly or both badly. Cross-pressures: equity (both towns have unserved people), sustainability (infrastructure lifespan, power), deliverability (the collapsed initiative poisoned trust in B), economics (A's density promises returns), and the digital-divide mandate (the programme's *purpose* is the unserved, and B's unserved rate is higher).

**Problem statement.** Design the decision: the evaluation criteria (including the trust-damage variable, which resists measurement), the intervention design per town (they may legitimately differ), the sustainability plan (power, maintenance, lifespan), and the political-economy answer (how the decision survives being the town that lost). Justify with criteria; state what the budget constraint *forces* rather than pretends it away.

**Stakeholders.** Residents of both towns (access now, trust, bills); ISPs (investment cases); the regional government (mandate, precedent); the community initiative's remnants (their credibility); future programmes (the precedent this sets).

**Inputs:** town profiles; the budget reality; the trust history; the mandate text. **Outputs:** criteria framework + per-town intervention design + sustainability plan + the loser-town answer. **Constraints:** the budget forces a real trade — the design must name it; trust damage in B is a constraint *on* intervention design, not merely a fact; the mandate's equity purpose must survive the economics.

**Learning objectives.** Design infrastructure decisions where equity and economics genuinely conflict; treat trust as an engineering constraint; design political survival for difficult allocations.

**Available information.** A's density supports fixed-line economics with modest subsidy; B's scatter raises per-household cost 3–5×; fixed-wireless (tower-based) suits B's geography at lower cost; the collapsed initiative's debt poisoned B's willingness to pre-pay anything; A has commercial pull (ISPs will co-invest); the mandate's text defines success as unserved-households-connected, not total connections.

**Student task.** The criteria framework (with how trust-damage is operationalized) + per-town design (they may differ — different technologies are legitimate) + sustainability plan + the political-economy answer (three elements: transparency, sequencing, the B-commitment instrument).

**Suggested thinking time.** 35 minutes.

**Expected solution characteristics.** Criteria: unserved-households per unit subsidy (the mandate's own metric), deliverability risk, trust-adjusted adoption (B's discount), sustainability cost, precedent value; per-town: A = subsidized fixed-line via ISP co-investment (density does the work; subsidy per household is low); B = community-owned fixed-wireless *with the governance reforms the collapse implies* (no pre-payment — grant-funded build, public accounts, elected oversight — the trust-damage variable shapes the *design*, not just the risk score); sustainability: tower power (solar+grid mix), maintenance funded by a ring-fenced operations line (not the capital budget — the collapse died of operations starvation), hardware lifecycle plan; political-economy: full criteria transparency (both towns see the same math), explicit sequencing commitment (B in year 1 — *because* its need is higher, the mandate says so — with A's co-investment timeline independent), and the commitment instrument (B's year-2 tranche contractually reserved, so the promise survives election cycles); the forced-trade honesty: A's service *quality* (gigabit) exceeds B's (reliable 100 Mbps-class fixed-wireless) — named, justified by geography, and paired with the access-floor guarantee (every household in both towns above a service floor).

**Discussion questions.**

1. How did trust damage change B's *design* (not just its probability) — and what would have happened if it hadn't?
2. Which criterion would the ISP lobby attack first — and does your framework survive the attack?

**Extension challenge.** Write the two-town announcement's 150-word statement — honest about the quality difference, committed to the floor.

**References.** Course L21/L22 (networking), L04 (divide); broadband-policy literature (instructor-provided); fictional towns scenario.

---

## PB-415 · Level 4 · The museum's interactive exhibit for every visitor

**Domain:** Accessibility and inclusive computing / Hardware / Public service systems · **Related lectures:** L03, L16, L20

**Scenario.** A fictional museum commissions a flagship interactive exhibit (a local-history timeline) with hard requirements: usable by wheelchair users, blind and low-vision visitors, deaf visitors, children, and visitors with cognitive disabilities — *simultaneously popular* (it must not become the exhibit where queues form because interactions are slow), within a mid-range budget, and maintainable by two technicians. The interactive-design firm proposes a 55-inch touchscreen with an audio handset. The access group's review is scathing: single-user assumption, no non-visual pathway, no caption default, and the queue-failure mode (one user monopolizes; others wait, watch, leave).

**Problem statement.** Redesign the exhibit interaction: the multi-modal design (what channel serves whom without segregating), the throughput design (why queues are an accessibility failure, mechanically), the maintenance plan, and the evaluation protocol (how the museum will know it succeeded, with whom). Justify against the requirements; name what the budget forces you to cut.

**Stakeholders.** The full visitor spectrum (dignity, access, enjoyment); the museum (attendance, reputation, budget); the access group (their review must be answered, not managed); the two technicians (maintenance reality); the design firm (their proposal's salvage).

**Inputs:** the firm's proposal; the access review; the requirement list; the budget class. **Outputs:** redesigned interaction + throughput analysis + maintenance plan + evaluation protocol. **Constraints:** accessibility must be *integrated* (segregated "accessibility mode" is a failure); throughput failures disproportionately harm disabled visitors (who can least afford the queue); maintenance fits two technicians.

**Learning objectives.** Design accessibility as integrated multi-modal experience, not an add-on mode; treat throughput as an equity variable; design evaluations that measure success for disabled visitors specifically.

**Available information.** Multi-modal patterns (concept level): parallel independent stations beat one shared screen; audio induction loops serve hearing-aid users; tactile + audio description layers serve blind visitors; captions-by-default serve deaf visitors *and* noisy halls; children need physical reach ranges and simple interaction depth; the timeline content decomposes into per-era standalone units (which is what enables parallelism).

**Student task.** The redesign (interaction architecture, per-modality provision, reach/range specs) + the throughput analysis (why the single screen queues and the redesign doesn't) + maintenance plan + evaluation protocol.

**Suggested thinking time.** 35 minutes.

**Expected solution characteristics.** Architecture: decompose the timeline into 5–6 parallel era-stations (each self-contained, 2–3 minutes interaction), rather than one serial mega-screen — parallelism is the accessibility-throughput unlock; per-station: tactile timeline strip + audio description (handset or loop), captions-by-default on all audio, high-contrast large-type mode, seated reach ranges (per access-standards guidance — heights stated), and a physical *or* touch-free trigger for each interaction (hygiene and motor-diversity); throughput: the single screen's failure is serial dependency — average interaction 4–6 min × popularity = queues where disabled visitors bear the wait penalty (their alternative is leaving); parallel stations cut expected wait by the station count and *equalize* it; maintenance: commodity hardware per station (one spare per five stations), content updates via standard files (the technicians' skill level respected), a daily power-cycle ritual; evaluation: observation study with disabled visitors *recruited* (not incidental), task-completion and dwell-time per modality, the queue-time distribution (not average — the tail is where equity dies), and the access group's sign-off as a gate; budget cut, named: probably the bespoke custom housing (standard enclosures instead) and one station's interactivity depth — cut *depth*, never a modality.

**Discussion questions.**

1. Why is "accessibility mode" on the single screen a design failure even if every feature exists within it?
2. What does the queue-time *distribution* show that the average hides — and who lives in the tail?

**Extension challenge.** Write the exhibit's one-panel orientation card: what's here, how each modality works, where help is.

**References.** Course L16/L20 (multimodal, accessibility); museum-accessibility standards (instructor-provided); fictional museum scenario.

---

## PB-416 · Level 4 · The university's AI-policy design (conceptual)

**Domain:** AI literacy / Ethical and societal implications / Education technology · **Related lectures:** L27, L28, L30

**Scenario.** A university drafts its first AI-use policy for coursework. The draft (from legal + one committee) bans "AI-generated submissions" and requires "disclosure when AI was used." Two semesters of reality: detection tools misfire (flagging honest students), "AI-generated" is undefinable at the margin (grammar tools, autocomplete, code assistants), disclosure rates are ~8% (nobody believes the rule), and departments differ wildly (a coding course encourages AI; an essay course bans it; a translation course is undecided). The policy is failing by its own terms. The Provost asks a student-faculty working group (including you) to redesign it.

**Problem statement.** Diagnose why the draft fails (each mechanism, not generically), design the replacement policy architecture (what's university-level vs course-level, what's assessed, what's disclosed), the enforcement design (what happens on suspected misuse, given detection-tool error rates), and the review cycle (how the policy learns). Justify with criteria; state what the policy *cannot* achieve.

**Stakeholders.** Students (fair assessment, clarity, the misfired-accusation risk); instructors (enforceability, departmental diversity); the university (integrity, legal exposure); the detection vendors (claims); the assessment's actual purpose (learning).

**Inputs:** the failing draft; the two semesters of evidence; departmental divergence; detection-tool error reality. **Outputs:** diagnosis + policy architecture + enforcement design + review cycle. **Constraints:** the policy must be enforceable *and* fair at scale; it cannot define "AI-generated" precisely (the design must work around that); departmental diversity is a feature to accommodate, not a bug to flatten.

**Learning objectives.** Design policy where the core definition is impossible — by restructuring what's asked; set enforcement defaults around error-asymmetric tools; build learning cycles into policy.

**Available information.** Detection tools have documented false-positive rates (and biases across language backgrounds); process evidence (drafts, version history, oral defence) is more reliable than output-detection; disclosure rates track rule credibility; course-level authority exists (module handbooks); the university's integrity framework already handles evidence standards.

**Student task.** The four-part design + criteria table + the "cannot achieve" paragraph.

**Suggested thinking time.** 35 minutes.

**Expected solution characteristics.** Diagnosis: the ban fails because (1) "AI-generated" has no defensible boundary (the definition problem — grammar checkers are AI), (2) detection errors punish the innocent asymmetrically (non-native speakers flagged more — an equity failure), (3) an unenforceable rule with 8% compliance teaches rule-contempt — the integrity harm the policy meant to prevent; architecture: university level sets *principles* (honest process, no misrepresentation, disclosure by course rule) and the evidence standard; course level sets the *rules* (per-assessment AI stance from a defined menu: required / permitted-with-disclosure / restricted / barred, each with its evidence expectations) — diversity accommodated by design; enforcement: suspicion triggers *process* evidence review (drafts, history, structured oral check) rather than detector scores alone — detector output may *prompt* review, never *constitute* proof (the error-asymmetry default); review cycle: annual, with disclosure-rate and accusation-appeal data reviewed, course-rule menu revised — the policy is versioned like the code in PB-413; cannot-achieve paragraph: the policy cannot prevent every misuse, cannot define the boundary perfectly, and cannot substitute for assessment design that makes AI use visible (redesigning assessment *is* the long-term answer the policy can only nudge).

**Discussion questions.**

1. Why does moving rules to course level *strengthen* rather than weaken university integrity?
2. What does the 8% disclosure rate tell you about rule credibility — and how does your design spend that credibility differently?

**Extension challenge.** Write the assessment-menu card (four stances, one line each) instructors would actually use.

**References.** Course L27/L28 (AI literacy), L30 (integrity, equity); detection-tool error literature (instructor-provided); fictional university scenario.

---

## PB-417 · Level 4 · The dam-monitoring upgrade (conceptual)

**Domain:** Public service systems / Networking / Data science workflows · **Related lectures:** L21, L24, L26

**Scenario.** A fictional water authority monitors 12 aging dams with 1990s-era sensors (water level, seepage, movement) reporting over radio to a control room. Budget exists for a partial modernization. The engineering choices: (a) modernize the two highest-risk dams fully (new sensors, redundant links, cloud analytics), (b) modernize all 12 minimally (better telemetry, basic analytics), (c) hybrid — full at the two highest-risk, telemetry-upgrade at the rest, plus a shared analytics layer. Cross-pressures: sensor validation (new sensors need *calibration history* — a new sensor on an old dam has no baseline; the old sensors' quirk-knowledge lives in one retiring engineer), connectivity (dams are remote; radio vs cellular vs satellite), fail-safe design (monitoring must fail *loudly* — silence must be an alarm, not an absence), and the analytics temptation (a vendor offers AI "anomaly detection" trained on... what baseline?).

**Problem statement.** Design the decision: risk-ranking method (what makes a dam high-risk — define it, don't assert it), the architecture choice with criteria, the sensor-transition plan (baseline continuity across the swap), the fail-safe requirements, and the honest evaluation of the AI-anomaly offer. Justify with criteria; specify what must be true for the retiring engineer's knowledge to survive.

**Stakeholders.** Downstream communities (the alerts exist for them); the authority (liability, budget); the control-room operators (alarm quality); the retiring engineer (their knowledge, the transition); the vendor (claims).

**Inputs:** 12 dams, partial budget; the sensor-baseline problem; the connectivity constraints; the vendor offer. **Outputs:** risk-ranking method + architecture choice + transition plan + fail-safe spec + AI-offer evaluation. **Constraints:** monitoring failure must be loud; calibration baselines must survive the hardware swap; the knowledge walkout is date-bound; the AI offer must be evaluated against its training-data reality.

**Learning objectives.** Rank risk by explicit method (not intuition); design instrument transitions that preserve baseline continuity; evaluate AI offers against their training-data honesty; specify fail-safe (fail-loud) monitoring.

**Available information.** Risk drivers are documentable (downstream population, structural age, inspection history, seepage trends); old sensors have known quirks (documented only in the engineer's experience — the transition plan must extract it); radio coverage exists at all sites; cellular is partial; satellite is possible at cost; the AI vendor's models were trained on *other* dams' data — transferability to these instruments is unproven.

**Student task.** The five-part design + criteria table + the knowledge-survival specification.

**Suggested thinking time.** 35 minutes.

**Expected solution characteristics.** Risk ranking: a scored method (downstream population × structural condition × trend data × inspection findings), weights set by a panel *before* seeing the per-dam numbers (pre-registration discipline — prevents post-hoc rationalization of the two favourites); architecture: (c) — full redundancy where risk justifies (redundant links, local buffering, fail-loud watchdogs), telemetry upgrades elsewhere, shared analytics only after baseline continuity exists; transition plan: parallel-running old and new sensors per dam (weeks-to-months for calibration crossover — budget for it), the engineer's quirk-log extracted as a structured document *with recorded walkthroughs* (the knowledge survival spec: written + verbal + a named successor shadowing one calibration cycle); fail-safe: heartbeat-based alarms (silence = alarm), power-fail behaviour specified, control-room alert-quality audited (alarm fatigue is PB-411's problem — the spec caps operator alert load); AI-offer evaluation: honest — models trained on other dams' instruments lack baseline transfer without local training data, so the offer is *pilotable later* (shadow classification against operator judgement), not contractable now; the criteria table names what each choice protects and accepts.

**Discussion questions.**

1. Why must the risk weights be fixed before the per-dam data is examined — what failure does pre-registration prevent?
2. What makes silence-as-alarm the *opposite* of the vendor's anomaly framing — and which does safety need?

**Extension challenge.** Write the engineer's quirk-log template (10 fields) that the transition plan depends on.

**References.** Course L21 (telemetry), L26 (baselines), L27 (AI honesty); dam-safety monitoring guidance (instructor-provided, generalized); fictional authority scenario.

---

## PB-418 · Level 4 · The code club's device fleet across four years

**Domain:** Education technology / Sustainability / Small business ICT · **Related lectures:** L03, L10, L12, L24

**Scenario.** A volunteer code club (30 children/week, ages 9–13) runs on donated laptops of wildly varying age and state. Four-year realities: devices die (donations become e-waste the club must dispose of responsibly), OS support ends (some machines can't run the teaching tools safely), volunteer IT skill is thin, child-safety constraints (network isolation, no personal accounts), and funding is zero-regular. The club's founder asks for a *fleet strategy*, not another donation drive: what to accept, what to refuse, how to image, when to retire, and how to dispose.

**Problem statement.** Design the fleet strategy: the acceptance policy (what donations help and what burden them), the imaging/maintenance design (thin volunteer skill, child-safety constraints), the retirement criteria (functional-vs-unsupportable), and the disposal chain (responsible e-waste with data sanitation). Justify with criteria; design for the founder's succession (the club outlives them — PB-312's law).

**Stakeholders.** The children (working, safe machines); volunteer IT leads (burnout); donors (their goodwill and their expectations); the club's future (succession); the e-waste chain (legal and ethical disposal).

**Inputs:** the donation reality; the constraint set; zero regular funding; thin IT skill. **Outputs:** acceptance policy + imaging/maintenance design + retirement criteria + disposal chain + succession note. **Constraints:** child-safety (isolated network, managed accounts) is non-negotiable; donations that create maintenance burden are *net negative* — the policy must refuse gracefully; the strategy must outlive its author.

**Available information.** Standard lightweight OSes (course-adjacent: Linux distributions) revive old hardware for browser-based teaching tools; child-safe profiles exist in mainstream OSes; a single standard image per device-class beats per-device care; refurbishers and e-waste programmes exist regionally (instructor provides generalized pointers); data-sanitation tools are standard.

**Learning objectives.** Design an acceptance policy that prices donation burden honestly; choose maintenance patterns compatible with thin volunteer skill (image-as-repair); set retirement criteria from support horizons rather than breakage; build succession so the strategy outlives its author.

**Student task.** The five-part strategy + criteria table + the succession design.

**Suggested thinking time.** 30 minutes.

**Expected solution characteristics.** Acceptance: a published spec (device classes accepted, minimum specs, what's declined — CRTs, broken screens, anything pre-dating the standard image) with the graceful-refusal script (donations that burden volunteers are refused *with reasons and alternatives*); imaging: one standard image per device class (browser-based curriculum, local child accounts, network isolation at the router — no per-child accounts, no per-device customizing), a "re-image, don't repair" maintenance rule (thin-skill compatible — the image *is* the repair), and a loaner buffer (3–5 ready spares so a dead machine never stops a lesson); retirement criteria: when the device can't run the standard image's security updates (not when it *breaks* — support-horizon is the trigger, PB-407's cliff); disposal: wipe-certified handoff to accredited refurbisher (still-usable devices get second lives — the PB-410 chain) or certified e-waste recycling for true end-of-life, with the certificate filed; succession: the strategy *is* a document (acceptance spec, image recipe, retirement rule, disposal contacts) plus a two-deep volunteer rule — the fleet outlives the founder because the strategy, not the person, holds the knowledge.

**Discussion questions.**

1. Why is "accept everything, sort later" the donation-policy that kills volunteer clubs?
2. What makes "re-image, don't repair" the right rule for thin IT skill — and what does it give up?

**Extension challenge.** Write the donor-facing acceptance one-pager (spec + why + the refusal script's first line).

**References.** Course L10/L12 (OS lifecycle), L03 (hardware classes); e-waste guidance (instructor-provided); fictional club scenario.

---

## PB-419 · Level 4 · The open-data research replication crisis (conceptual)

**Domain:** Data science workflows / Public service systems · **Related lectures:** L19, L26

**Scenario.** A fictional research group's influential paper (on district-level education outcomes using published government data) is challenged: two re-analyses reach different conclusions from the same sources. The group's own materials reveal why — their download scripts hit data that was *silently revised* mid-project (a methodology note changed a definition), their joins assumed stable identifiers (some district codes were re-used), and their README says "data from govt portal" with a date that no longer resolves to the same files. The journal asks the group to respond; the group's junior researcher (who built the pipeline) must write the response.

**Problem statement.** Write the case as the group's response design: the provenance audit (what exactly went wrong, mechanically), the re-analysis protocol (how to make the result reproducible or honestly withdrawn), the correction/erratum strategy (what the paper should now claim), and the pipeline redesign so the group's *next* project is immune. Justify with criteria; state what the response must *not* do.

**Stakeholders.** The research community (replication trust); the junior researcher (career, authorship fairness); policymakers who cited the paper (decisions in flight); the journal (correction integrity); the data publisher (revision practices).

**Inputs:** the failed joins; the silent revision; the unresolvable README; the two re-analyses. **Outputs:** provenance audit + re-analysis protocol + erratum strategy + pipeline redesign. **Constraints:** the response must be honest about the pipeline's failures without the junior researcher becoming the scapegoat (the failures were systemic — no provenance tooling existed); the erratum must calibrate claims to what survives re-analysis.

**Learning objectives.** Audit provenance failure mechanically (which link broke, when); design reproducibility as artifact-freezing, not documentation aspiration; write corrections that calibrate claims without theatrical self-flagellation.

**Available information.** The portal's revision history exists in archived snapshots (third-party archives); the definition change affected one sub-population's comparability; district-code re-use affects ~3% of rows; the paper's headline claim rests on the affected comparison; the junior researcher's scripts are deterministic given the inputs — the *inputs* were the problem.

**Student task.** The four-part response design + criteria table + the must-not paragraph.

**Suggested thinking time.** 35 minutes.

**Expected solution characteristics.** Provenance audit: three mechanical failures named — silent upstream revision (no snapshot pinning), identifier re-use (no referential validation of joins), unresolvable README (documentation pointed at a *portal*, not an *artifact*); re-analysis protocol: freeze artifacts (the archived snapshots + the current portal data as *separate named datasets*), run the pipeline on both, report the delta — if the headline claim survives the frozen-data version, say so with the revision-sensitivity quantified; if it doesn't, the claim retreats (the erratum states which comparison is unsupported); erratum strategy: calibrated language ("the district-level comparison is sensitive to the 2019 definition revision; the directional finding holds under snapshot X but not snapshot Y" — or the honest withdrawal of the affected claim), *no* blame language toward the junior researcher — the systemic frame (no tooling existed) is also the true frame; pipeline redesign: snapshot-pinned ingestion (every download archived with hash), identifier validation gates (reject joins on re-used codes rather than merge silently), and a README that *names artifacts by hash* — reproducibility as engineering, not virtue; must-not paragraph: must not re-run until the inputs are pinned (re-running on drifting data manufactures false precision), must not attribute the failure to individual carelessness, and must not let the erratum's caution leak into claiming the *opposite* conclusion (absence of support ≠ evidence of reverse).

**Discussion questions.**

1. Why is "the scripts are deterministic" no defence — and what exactly does artifact-freezing buy that determinism doesn't?
2. Which of the three mechanical failures would your pipeline redesign have caught *earliest* — and at what stage cost?

**Extension challenge.** Write the erratum's three-sentence summary for the journal.

**References.** Course L26 (provenance, replication); replication-crisis literature (instructor-provided, concept level); fictional research scenario.

---

## PB-420 · Level 4 · The bookstore that must move online in ten weeks

**Domain:** Small business ICT / Cloud computing · **Related lectures:** L08, L11, L24, L25

**Scenario.** A campus bookstore's building is reclaimed by the university with ten weeks' notice; the owner must move sales online or close. Reality: 40,000 titles in a hand-maintained spreadsheet and paper cards, a 30-year customer base with course-text lists held as *paper photos on the owner's phone*, no e-commerce anything, one staff member (the owner's nephew, tech-comfortable), a small budget (the closure compensation), and the seasonal crunch (semester start is in week 6 of the ten). The nephew proposes a mainstream hosted e-commerce platform; the owner fears losing the personal relationships that are the store's actual moat.

**Problem statement.** Design the migration: what launches in ten weeks vs what waits (the scope cut, by criteria), the catalogue strategy (40,000 titles cannot be hand-entered — what's the realistic data path), the customer-relationship transfer (the paper photos, the personal moat), the operations design (one-and-a-half staff), and the risk plan for the week-6 semester crunch. Justify with criteria; name what the store's online identity must preserve to stay *this* store.

**Stakeholders.** The owner (livelihood, identity, the moat); the nephew (capability, burnout); customers (course texts at semester start, the relationship); publishers (terms); the university (the displaced tenant's continuity).

**Inputs:** the ten weeks; the catalogue state; the photo-list problem; the budget; the crunch timing. **Outputs:** scope decision + catalogue data path + relationship transfer + operations design + crunch risk plan. **Constraints:** the crunch is immovable; hand-entry of 40k titles is impossible in the window; the moat (personal service) must survive digitization; the staff is 1.5 people.

**Learning objectives.** Cut scope by explicit criteria under a hard deadline; find the data path that makes an impossible catalogue feasible; digitize a *relationship* without destroying it.

**Available information.** Publishers provide title databases (ISBN-keyed) on request; ISBN lookup services exist; course lists can be prioritized (maybe 2,000 titles are course-critical); hosted platforms handle inventory, payment, tax; the paper photos are transcribable but slowly — the *course list* is the priority set; the customer base is reachable via an email list the owner has kept for decades.

**Student task.** The five-part design + criteria table + the identity paragraph.

**Suggested thinking time.** 35 minutes.

**Expected solution characteristics.** Scope: launch = course-text pre-orders (the ~2k priority set) + top-selling general categories + pickup-by-appointment for the local base; the full 40k catalogue is *not* launched hand-entered — it loads via publisher feeds + ISBN lookup over the following term (criteria: what the crunch needs, what staff-hours allow, what revenue depends on); catalogue path: publisher title feeds + ISBN-keyed import + the photo lists transcribed *only* for the course-critical set (with a verification pass by the owner — their knowledge is the QA); relationship transfer: the email list is the moat's spine (a personal note from the owner announcing the move, course-list service preserved as a *human* step — students send their list, the owner replies with availability; the store's identity is the reply, not the checkout), plus local pickup keeping the face-to-face alive; operations: hosted platform (build-vs-buy is not close at 1.5 staff), simple order states, the nephew's week structured (morning orders, afternoon imports), and the owner protected from tech-burden; crunch risk plan: pre-orders open week 3 (before the crunch), pickup capacity capped and booked (no walk-in surprises), a failure mode for each week (platform slow → stock-answer + callback list; photo transcription behind → phone orders take priority, transcribe after); identity paragraph: what must survive is the owner's knowledge answering *your* list personally — the design routes around anything that would replace that with a search box.

**Discussion questions.**

1. Why is "launch the full catalogue" the scope failure here — what does the crunch actually pay for?
2. What does the moat analysis tell you about which *features* matter — and which mainstream-platform defaults would quietly kill the store's identity?

**Extension challenge.** Write the owner's announcement email (150 words) — the move, the course-list promise, the pickup option.

**References.** Course L08/L25 (requirements, data), L24 (hosted platforms); fictional bookstore scenario.

---

## PB-421 · Level 4 · The whistleblower's data dilemma (conceptual)

**Domain:** Cybersecurity and privacy / Ethical and societal implications · **Related lectures:** L29, L30

**Scenario.** A fictional NGO's finance officer discovers expense records suggesting systematic misuse of grant funds by a senior manager. The NGO's own policy requires reporting to the board; the officer fears retaliation (the manager chairs the policy committee), and the *evidence* is a copy of internal financial files taken without authorization (policy technically violated in the copying, though the records relate to the officer's own duties). The officer asks a friend (a student, you) for guidance on handling the evidence: how to preserve it credibly, whether to return the copies, how to document the discovery timeline, and what not to do.

**Problem statement.** Design the guidance (as the friend's honest advice, knowing your limits): the evidence-integrity options (hashing, dated statements, what establishes credibility vs what only *claims* it), the legal/policy territory map (what needs a lawyer vs what the friend can say), the retaliation-risk mitigations (documentation, channels), and the ethical boundaries of the advice itself (what the friend should decline to decide for the officer). Justify with criteria; be explicit about uncertainty.

**Stakeholders.** The officer (career, integrity, safety); the NGO (its funds, its governance); the board (its duty); the manager (due process — presumption applies); the friend (the limits of their role); the grant funder (its money).

**Inputs:** the discovery; the copying's technical policy violation; the retaliation fear; the friendship. **Outputs:** guidance design + integrity-options analysis + territory map + the friend's boundary statement. **Constraints:** the advice must not itself create new wrongs (spreading allegations, insecure storage of sensitive files); due process for the manager must be preserved (the evidence is *allegation*, not verdict); the friend is not a lawyer and must not act as one; the scenario is conceptual — no real persons.

**Learning objectives.** Reason about evidence integrity (hashing, timestamps, chain of custody intuition) at a layperson's honest level; map advice territory (what belongs to professionals); balance loyalty, ethics, and due process under uncertainty.

**Available information.** File hashes and dated statements are standard integrity tools (course-reachable: L29's hashing); NGOs vary in whistleblower protections (jurisdiction-dependent — flag, don't resolve); secure storage (the officer's personal encrypted space) exists; anonymous reporting channels exist but weaken evidence credibility trade-offs; the friend's proper role is *information and options*, not decisions.

**Student task.** The guidance design (options, not orders) + the integrity analysis (what hashing/dating establishes and what it doesn't) + the territory map (lawyer-now items vs discussable items) + the boundary statement.

**Suggested thinking time.** 30 minutes.

**Expected solution characteristics.** Guidance shape: options with consequences, never the decision ("here are the paths; you choose; here's what each costs"); integrity: hashing the files + a dated written account *now* (memories decay before processes move) establishes *consistency over time* — it does not prove authenticity or origin, and the advice says so plainly (credibility ≠ proof); territory map: lawyer-now (the unauthorized copying's legal exposure, jurisdiction's whistleblower protections, employment risk), board-policy-now (the reporting duty — the policy exists and using it is both required and protective), friend-discussable (storage hygiene, documentation habits, emotional load); retaliation mitigations: contemporaneous written record, reporting through the *policy channel* (which timestamps the disclosure — protective), a trusted person informed of the timeline (not the contents), and no publication/allegation-spreading (which would surrender legal protections and harm due process); the boundary statement: the friend declines to decide whether to report, declines to store the evidence, declines legal opinions — and says why (the stakes exceed the friendship's competence, and *saying so is the help*); the ethical spine: due process for the manager and protection for the officer are *both* preserved by channel-and-document discipline, and both fail if the officer improvises.

**Discussion questions.**

1. What does hashing establish, precisely — and why is the gap between "consistent" and "authentic" the crux of the advice?
2. Why does *using the policy channel* protect the officer more than bypassing it, even when the policy's chair is the suspect?

**Extension challenge.** Write the friend's four-sentence opening reply that sets the role boundary without abandoning the person.

**References.** Course L29 (hashing, integrity), L30 (whistleblower protections — generalized); fictional NGO scenario; no real persons or cases.

---

## PB-422 · Level 4 · The exam-schedule optimization with human constraints (conceptual)

**Domain:** University administration / Computational thinking · **Related lectures:** L22, L31

**Scenario.** A fictional university's exam scheduling is a manual ordeal: 900 exams, 12,000 students, rooms of varying capacity and accessibility, invigilator availability (academic staff, bounded hours), and the constraint web: students in concurrent programmes must not have clashes, back-to-back exam equity (nobody should face three exams in 24 hours), accessible-room proximity for students with accommodations, and room-turnover cleaning windows. The registry proposes buying scheduling software; a CS senior proposes the registry's problem is a constraint-optimization case the university could model itself (course project scale). The registry's counter: "software doesn't know that Professor X cannot invigilate Fridays for religious observance, and the last consultant didn't either."

**Problem statement.** Design the modelling approach: what the decision variables, hard constraints, and soft constraints are (from the narrative — extract them; the narrative is the spec), how the "human knowledge" objection is answered (constraint elicitation as a design phase, not a limitation), the validation design (how a generated schedule is checked before humans trust it), and the recommendation (buy, build as a course project, or hybrid — with criteria). Justify with criteria; name the constraint the narrative *implies* but doesn't state (finding it is part of the task).

**Stakeholders.** Students (clash-free, humane spacing, accommodation proximity); invigilators (bounded, fair assignments); the registry (feasibility, their manual expertise); the accommodations service (their students' needs); the senior (their proposal's fate).

**Inputs:** the narrative's constraint list (explicit and implied); the buy/build/hybrid question. **Outputs:** model design (variables, hard/soft constraints) + elicitation plan + validation design + recommendation. **Constraints:** the model must serve humans under their real constraints, not optimize a toy; unmodelled constraints are the known killer — elicitation is the design core; validation must precede trust.

**Learning objectives.** Extract a formal model from a messy narrative (computational thinking at system scale); classify constraints (hard vs soft, stated vs implied); design validation that earns human trust; make a buy/build/hybrid call with criteria.

**Available information.** Standard exam-timetabling is a known hard problem (NP-hard class — course-appropriate to *name* without solving); commercial tools exist with elicitation support; the university teaches optimization in year 2+ (the senior's project would be a prototype, not production); the registry's manual expertise is itself a constraint corpus (their yearly fixes encode the unwritten rules).

**Student task.** The model design + elicitation plan + validation design + recommendation.

**Suggested thinking time.** 35 minutes.

**Expected solution characteristics.** Model: variables (exam→slot+room+invigilators assignments), hard constraints (no student clash, room capacity+accessibility match, invigilator availability incl. religious observance, cleaning windows), soft constraints (24-hour spacing, accommodation proximity, invigilation fairness, back-to-back minimization) with weights; the *implied* constraint (the extraction test): e.g., invigilator assignments must respect that the same invigilator cannot cover two simultaneous exams (stated nowhere but load-bearing), or room accessibility must match *assigned* accommodations (not just "accessible rooms exist") — naming an implied constraint and defending its necessity is the expert marker; elicitation: the registry's past-three-years manual fix logs mined for unwritten rules, structured interviews per constraint class, and a "constraint backlog" reviewed after each prototype run (elicitation as ongoing phase); validation: constraint-checker report per generated schedule (every hard constraint verified, soft-constraint scores shown), registry walkthrough of the ten worst soft-constraint violations, and a one-semester shadow run (generated schedule compared against the manual one, divergences reviewed) before any live use; recommendation: hybrid usually — commercial tool for the solving core (buying NP-hard solvers is rational) *with* the elicitation layer and checker built in-house (the human knowledge is the moat), the senior's course-project energy pointed at the checker and the elicitation tooling rather than the solver; criteria shown for the call.

**Discussion questions.**

1. Which constraint in your model would the registry describe as "obviously" — and why is "obvious" the enemy of modelling?
2. Why is the shadow-run semester the trust instrument — what does it demonstrate that a constraint-report cannot?

**Extension challenge.** Write the constraint-elicitation interview guide (6 questions) for the registry's schedulers.

**References.** Course L31 (decomposition, modelling); timetabling literature (instructor-provided, concept level); fictional university scenario.

---

## PB-423 · Level 4 · The smart-campus energy system (conceptual)

**Domain:** Sustainability / Cloud computing / AI literacy · **Related lectures:** L21, L24, L26, L27

**Scenario.** A fictional university proposes an integrated smart-campus energy system: sensors (occupancy, temperature, power) feeding a central platform that optimizes HVAC and lighting, with a dashboard for sustainability reporting. The proposal's assumptions: occupancy sensing improves comfort *and* savings, ML optimization beats schedule-based control, and the dashboard drives behaviour. Cross-pressures: privacy (occupancy sensing in study spaces —attendance inference, individual tracking potential), the ML baseline problem (savings claims need *honest* baselines — weather and occupancy confound everything), fail-safe control (the optimizer must not make buildings unusable when it errs), vendor lock-in (the platform's data format), and the behaviour question (dashboards historically decay — PB-321's lesson at institutional scale).

**Problem statement.** Design the evaluation-before-deployment plan: the privacy architecture (what occupancy data is collected, minimized, retained — at design time), the ML-claim evaluation protocol (baselines, confounds, the honest experiment), the fail-safe control spec, and the lock-in mitigations. Justify with criteria; state which proposal assumption you'd test first and why it's load-bearing.

**Stakeholders.** Building users (comfort, privacy); the sustainability office (savings, reporting); facilities management (control, maintainability); the university (investment, claims integrity); the vendor (the sale).

**Inputs:** the proposal's three assumptions; the constraint set; the PB-321 precedent (dashboard decay). **Outputs:** privacy architecture + ML evaluation protocol + fail-safe spec + lock-in mitigations. **Constraints:** privacy must be *architectural* (minimization at collection), not policy-bolted; savings claims must survive confound analysis (the university will publish them); control failure must degrade to safe schedules, not to a hot office; lock-in must be mitigated before signing, not after.

**Learning objectives.** Design privacy into sensing architecture (collection-time minimization); demand honest baselines for ML control claims (the confound discipline); spec fail-safe automation; mitigate lock-in contractually and technically.

**Available information.** Occupancy sensing can be coarse (presence counts) or fine (identity-linked); HVAC control has safe-mode schedules (the fallback exists in every building — the spec formalizes it); savings claims in vendor materials rarely state baselines; the platform's API openness varies by vendor (negotiable pre-contract); weather normalization is standard in energy analysis (course-adjacent: PB-321's confound discipline).

**Student task.** The four-part plan + criteria table + the load-bearing assumption argument.

**Suggested thinking time.** 35 minutes.

**Expected solution characteristics.** Privacy architecture: presence-count sensors (no identity), retention days-not-months, no occupancy data joined to individuals, dashboard aggregates only — collection-time minimization (the design question is *what not to sense*); ML evaluation protocol: shadow mode first (optimizer proposes, humans follow or not, disagreements logged), honest baseline = weather-normalized + occupancy-adjusted consumption of comparable buildings or prior periods, savings claimed only for the *delta the shadow run validates*, published with method (the claims-integrity constraint); fail-safe spec: bounded action ranges (optimizer may adjust setpoints within a defined band, never outside), automatic reversion to schedule on sensor staleness or model-confidence lapse, and a manual override that always wins (the hot-office failure mode designed against); lock-in mitigations: data-export guarantee in open formats (contractual, tested before signing), sensor-hardware separability from the platform (replaceable head-ends), and the exit-cost line-item in the business case; load-bearing assumption: ML-beats-schedules — because the *entire* control layer depends on it, and the honest experiment (shadow mode) tests it before any control authority transfers; occupancy-sensing comfort is secondary (schedules + manual adjustment already deliver most of it), and the dashboard assumption is PB-321-decayed on arrival (plan for re-engagement, not launch spikes).

**Discussion questions.**

1. Why is "what not to sense" the first privacy decision rather than "how to protect what we sense"?
2. What does the shadow-mode protocol prove that a vendor's reference-customer visit cannot?

**Extension challenge.** Write the one-slide "claims we will and won't make" for the university's announcements.

**References.** Course L24/L26/L27; energy-analytics baselining guidance (instructor-provided); fictional campus scenario.

---

## PB-424 · Level 4 · The open-source student project going production

**Domain:** Small business ICT / Education technology / Web technologies · **Related lectures:** L09, L12, L22, L29

**Scenario.** A final-year student team's course project (a departmental room-booking web app) unexpectedly succeeds: three other departments want it, a student society offers to host it "properly," and the team graduates in eight months. The project was built with course-level practices (no tests beyond demos, secrets in the repo history, one database, no monitoring, README written for markers). Cross-pressures: security (multi-department = real user data, real attack surface; the repo's secret history), sustainability (who maintains it after graduation — PB-312's law again, now with a server attached), the data-protection line (booking data is personal data), scope control (three departments' feature requests now), and the handover cliff (the team's expiry date is known and near).

**Problem statement.** Design the production-readiness plan: the security triage (what must be fixed before *any* new department onboards, ranked), the infrastructure and data-protection baseline (hosting, backups, access, retention), the governance/handover design (who owns it post-graduation, how decisions get made), and the scope gate (how feature requests are triaged against the runway). Justify with criteria; specify the *do-not-launch trigger* — the finding that would stop the expansion entirely.

**Stakeholders.** The using departments (availability, their data); students (the service); the university IT (who should probably own this); the team (their legacy, their time-to-exams); future maintainers (the codebase they inherit).

**Inputs:** the project's practice level; the expansion demand; the graduation timeline. **Outputs:** security triage + infrastructure/DP baseline + governance design + scope gate + do-not-launch trigger. **Constraints:** eight months bounds ambition; the secret history is a known unknown (rotation is cheaper than archaeology); personal data changes the legal class of the project; governance must survive the founders (the handover cliff is the *primary* risk — more than any bug).

**Learning objectives.** Triage security debt by exposure order (what must precede first new user); design governance that survives founder departure; set scope gates under runway pressure; define kill criteria before launch.

**Available information.** Institutional hosting exists (and IT ownership solves governance *and* infrastructure if the project meets the bar); secrets rotation is standard; backup/access/retention patterns are course-reachable (L11, L29, L30); the departments' requests can be ranked by their actual need vs the core booking loop.

**Student task.** The five-part plan + criteria table + the do-not-launch trigger.

**Suggested thinking time.** 35 minutes.

**Expected solution characteristics.** Security triage (pre-onboarding order): (1) secrets rotation + history scrub *or* clean-rebuild decision (cheap, non-negotiable), (2) auth hardening (multi-department = shared admin model redesign — per-department scoping), (3) input validation / injection review on the booking core, (4) dependency audit (L09's unmaintained-dependency check, PB-319's lesson); infrastructure/DP baseline: institutional hosting first (IT ownership solves backups, monitoring, and the governance question simultaneously — the pitch to IT *is* the governance move), data protection: booking data minimized (purpose-bound fields), retention policy (past-term bookings purged), access logged, backup-tested (L11's "a backup is a restore that has worked"); governance: university-IT ownership with the team as documented handover (operations doc in PB-413's tradition — deployment, runbook, decision log), a named faculty sponsor, and the module-instructor loop for future student maintainers (the succession pipeline); scope gate: core-loop-first triage — requests scored on (need × users) / maintenance-cost, new departments onboarded only after the current one runs one full term incident-light; do-not-launch trigger: if the auth redesign cannot land before the first new department's real users, or if university IT declines ownership and no institutional host exists (student-society hosting of personal data is the line — declined), the expansion stops — the app stays single-department and the honest answer to the other departments is "not yet, and here's what must be true first."

**Discussion questions.**

1. Why does "who owns the server" outrank any individual security fix in this case — trace the failure if ownership stays with graduating students?
2. What does the do-not-launch trigger reveal about the difference between a project that *works* and a service that can be *responsible* for data?

**Extension challenge.** Write the one-page pitch to university IT: what the app is, what ownership would entail, what the team hands over.

**References.** Course L09/L12/L22/L29/L30; fictional project scenario.

---

## PB-425 · Level 4 · The capstone: design the course's own problem bank

**Domain:** University administration / Education technology / Ethical and societal implications · **Related lectures:** all — this case is the course looking at itself

**Scenario.** The course team decides next year's problem-solving strand should use a *student-maintained* case bank: each cohort contributes new cases (from their own experience of the course's domains), the best are curated in, and the bank evolves. You are designing the system that makes this work. Cross-pressures: quality control (student cases will vary wildly in realism and solvability), consent and privacy (cases drawn from experience may embed real people, employers, institutions), answer-key integrity (curated solutions must not leak — the course's own leak-guard problem), metadata discipline (level, domain, lecture-links must stay consistent or the bank's progression map dissolves), volunteer-curatorial labour (a TA plus rotating students), and the pedagogical inversion (students *designing* problems may learn differently — and better — than solving them; but only if the design task is scaffolded, not assigned naked).

**Problem statement.** Design the system: the case-contribution specification (template, level criteria, the "solvable-and-grounded" test), the consent/sanitization protocol (what must be fictionalized, how it's checked), the curation workflow (submission → review → integration, with metadata discipline), the leak-prevention design (solutions' separation, the bank's own validator), and the pedagogical scaffold (what students get *taught* about case design before they attempt it). Justify with criteria; name the failure mode that would most likely kill the system in year two — and its prevention.

**Stakeholders.** Future students (the bank's users); contributing students (their ideas, their privacy, their learning); curators (TA + rotating students — the labour reality); the course team (quality, integrity); the bank's continuity (the succession problem, encountered at meta scale).

**Inputs:** the existing bank's conventions (levels, IDs, fields); the cross-pressure list; the labour reality. **Outputs:** contribution spec + consent protocol + curation workflow + leak-prevention design + pedagogical scaffold. **Constraints:** the system must run on thin labour; consent must be structural (not honor-system); the metadata discipline must be machine-checkable (this repo's own validator culture — the design should assume validation exists); the pedagogical scaffold must make design-task learning real.

**Learning objectives.** Design a *contributory* system under quality/privacy/labour constraints; apply the course's own principles (separation, validation, succession) to the course's own artefact; scaffold a design task so students learn from designing, not just producing.

**Available information.** The existing bank's structure (levels, ID scheme, the 22-field template, the validator); sanitization practice exists in this bank's own scenarios (fictional institutions, named as fictional); the leak-guard tooling pattern (structure-based checks, not trust); curricular space exists in the final module for a case-design mini-unit.

**Student task.** The five-part design + criteria table + the year-two failure-mode analysis.

**Suggested thinking time.** 35 minutes.

**Expected solution characteristics.** Contribution spec: the existing template *as the submission format* (fields enforced by validator — students learn the discipline by using it), with the solvability test (a case is acceptable iff a competent peer can produce a defensible answer from the stated information alone — no insider knowledge required) and the grounded-realism rubric (constraints must interact; a case with one obvious answer is a quiz, not a case); consent/sanitization: structural rules — real institutions/persons/employers must be fictionalized (the bank's own convention: "fictional" markers), identifying details stripped, and a *sanitization checklist* reviewed at curation (structural, not honor-system); curation workflow: submission via validator-checked template → curator triage (rubric-scored: realism, solvability, level-fit, domain-fit) → revision loop with the contributor (authorship retained — name in the case's credits) → integration with ID assignment and lecture-link mapping; leak-prevention: solutions in the private tree only, structural validator extends to new cases (public files must not contain the solution-bearing fields — machine-checked, the repo's own pattern applied to the bank itself); pedagogical scaffold: a case-design mini-unit (what makes a problem *good* — constraints that interact, information that suffices, stakeholders with legitimate conflicts), worked examples *from the bank's own rejected-cases pile* (the failures teach most), and the design task framed as "write the case you wish you'd had"; year-two failure mode: metadata decay + curator burnout — new cases drift from the level scheme, the progression map dissolves, curation backlog grows, contributions stop (the system dies of maintenance, not policy); prevention: machine-checkable metadata (the validator refuses unmapped cases), a *curator rota with two-deep staffing* (PB-312's law), and a modest but real incentive structure (credit-bearing curation roles — the labour must be resourced, not wished for).

**Discussion questions.**

1. Why is the "solvable-and-grounded" test the heart of the contribution spec — what fails without it?
2. How does this design apply the course's own principles back onto the course — and what does that recursion teach that a lecture cannot?

**Extension challenge.** Write the case-design mini-unit's assessment brief (one page) — the task, the rubric, the consent rules.

**References.** Course-wide (all modules); the bank's own conventions (index, template, validator); fictional course-team scenario.
