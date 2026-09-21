# Teaching Guide — Module 8: Security, Society, and Synthesis

**Module 8** · Stage 4 · 4 lectures (L29–L32) · 8 contact hours
Companion to lecture pages `L29`–`L32` under `docs/lectures/`. **Not published.** Answers to exit tickets appear here and nowhere student-facing.

> Symbols: **[Slide]** projector visual · **[Board]** board work · **[Demo]** live demonstration · **[Discuss]** think-pair-share or open discussion.

## Before this module

- [ ] **Ethics and legality frame the whole module:** every activity is defensive, simulated, or first-person (protecting *your own* accounts and data). A5 uses fabricated phishing samples you provide — never harvested real ones; say so out loud, it is itself a teachable point.
- [ ] Lab 8 (security habits) runs alongside L29–L30: confirm password-manager/MFA guidance matches current institutional reality; update the handout's screenshots *this week*, not last month's.
- [ ] L31's flowchart clinic needs the syllabus grade-weight figures (project, quizzes best-10-of-14, labs, exams) — the chart they build must compute a real transcript.
- [ ] L32's showcase: book the room layout, prepare the peer-feedback slip template, test the projector switch-over timing between teams (8–10 min per team — rehearse the transitions once).

## Misconception warnings (module level)

1. **"Security is an antivirus product."** It is layered *habits* (updates, MFA, least privilege, backups — L11's 3-2-1 returns); products are one layer of many.
2. **"Privacy means having nothing to hide."** Reframe as *control over personal data* — purpose limitation and data minimization are design principles, not secrecy.
3. **"Hacking content is forbidden, so security is off-limits to learn."** The boundary is explicit and teachable: authorized, simulated, first-person defensive work only. Name the line in L29 and hold it all module.
4. **"Emerging tech is either hype or destiny."** L32's calibrated maturity talk and the L23/L28 toolkit land the middle path: evidence-based evaluation.

---

## L29 — Cybersecurity Fundamentals

**Teaching tips:**
- Open with the economics, not the fear: attacks are *businesses* with cost/benefit logic — which is why layered defence (raising attacker cost) works. Fear produces paralysis; economics produces habits.
- A5 (phishing audit) is the module's core activity: teams rank red flags, then draft the out-of-band verify reply — the *drafted reply* is the skill that transfers to their real inbox.
- Password guidance changes; teach the *properties* (unique per site, long, generated, stored by a manager, MFA on top) rather than current composition rules — the properties survive guideline updates.

**Board / projector plan:**
- [Board] The layered-defence stack drawn as castle layers: updates → unique passwords+manager → MFA → least privilege → backups; each layer gets its attack-class label.
- [Slide] The Mermaid phishing red-flag diagram from the lecture page's "Visual explanation."
- [Board] A5's ranking sheet skeleton: red flag → why it works → where in the layered stack it's stopped.

**Suggested demonstration:** The anatomy of one *fabricated* phishing email on the projector: annotate sender mismatch, urgency, lookalike domain, payload risk live; then show the out-of-band verification reply drafted in real time. (No live samples; no clicking; the sample never leaves your file.)

**Misconception warnings:**
- "I'm too small a target." Automated attacks sweep everyone; the economics don't check your follower count.
- "The padlock/branding proves authenticity" — L23's lesson returns with teeth: TLS ≠ trustworthiness; attackers have padlocks too.
- "Ransomware just encrypts, right?" Modern variants also exfiltrate; backups (3-2-1!) answer encryption, but not leak-only extortion — defence in depth again.

**Discussion prompts:**
1. Which of your daily accounts, if taken over, unlocks others? (Password reuse graphs — map two hops.)
2. Why do organisations still fall for phishing after years of training? (Attacks target *attention*, not ignorance; urgency defeats experts too.)
3. Where does Lab 8's MFA setup sit in the layered stack, and what residual risk remains?

**Exit-ticket questions (with answers):**
1. *Name four red flags in a phishing message.* — Sender/domain mismatch, urgency, unexpected payload/link, lookalike domain (accept others from A5's sheet).
2. *What is social engineering?* — Manipulating people (not machines) into disclosure or action — the human attack surface.
3. *Why unique-per-site passwords?* — Credential reuse turns one breach into many account takeovers (credential stuffing).
4. *MFA's added protection in one sentence.* — A stolen password alone no longer suffices; a second factor gates access.

---

## L30 — Privacy and Digital Citizenship

**Teaching tips:**
- The footprint self-audit is deliberately personal: students search themselves and review one platform's settings *live*. Prepare the room for someone discovering something uncomfortable — set the tone: curiosity, not shame; changes, not guilt.
- Tracking: teach the three mechanisms (cookies, fingerprinting, trackers) as *persistence strategies* — each answers "how does the tracker survive between my visits?" The question-first order keeps mechanisms memorable.
- Purpose limitation and data minimization are the lecture's exportable principles: students apply them to the university itself (what does the LMS need to know?) — institutional examples beat platform rants.

**Board / projector plan:**
- [Board] The three tracking mechanisms as three answers to one question written at the top: "how does tracking persist?"
- [Slide] The Mermaid data-flow diagram from the lecture page's "Visual explanation."
- [Board] Two principles in policy language: purpose limitation, data minimization — with a university-service example under each.

**Suggested demonstration:** The live settings review on the projector using *your own* account: walk one privacy settings page, narrate the trade-off you're making (convenience vs data), make one change. Modelling the decision — including its discomfort — is the demo.

**Misconception warnings:**
- "I deleted it, so it's gone." Deletion vs backup/archival/sync copies — L11's storage realities and L10's delete semantics return.
- "Incognito makes me anonymous." It changes *local* traces (history, cookies at rest); network observers and the sites still see you — precision here prevents false confidence.
- "Privacy settings are the whole answer." Settings reduce surface; behavioural choices (what to post, which apps get which permissions) dominate outcomes.

**Discussion prompts:**
1. Apply data minimization to a student club's membership form: which fields fail the test?
2. Who benefits when a "free" service's price is attention and data — and what exactly is the currency?
3. Which digital-citizenship norm from today should this university publish and enforce first?

**Exit-ticket questions (with answers):**
1. *Digital footprint in one sentence.* — The trail of data you leave (and that others leave about you) across online activity.
2. *Name two tracking mechanisms and their persistence strategy.* — Cookies (stored identifiers revisited to sites), fingerprinting (device-trait combination re-identification without storage), trackers (cross-site beacons) — any two.
3. *Purpose limitation in policy terms.* — Data collected for a stated purpose is not reused for incompatible ones without new consent.
4. *One difference between deleting content and it disappearing.* — Copies/backups/sync/archives persist; deletion is rarely global (accept reasoned examples).

---

## L31 — Computational Thinking

**Teaching tips:**
- This lecture is the course's *method exam in disguise*: the flowchart clinic computes a real transcript from syllabus weights — make the chart *run* with sample data until one planted bug surfaces. The bug-hunt is the point; plan which bug (an unanchored "best 10 of 14" is the classic).
- The four pillars must be *applied*, not defined: run the clinic explicitly through decomposition (grade components), pattern recognition (repeated course blocks), abstraction (the "score" node hides computation), algorithm design (the chart itself).
- Exit ticket is forward-looking by design: it primes the showcase and the synthesis. Leave 5 minutes for the project showcase logistics.

**Board / projector plan:**
- [Board] The four pillars as four labelled columns; the clinic's chart elements get tagged with which pillar produced them.
- [Slide] The Mermaid flowchart from the lecture page's "Visual explanation."
- [Board] The transcript computation written as both flowchart and pseudocode side by side — the translation is the skill.

**Suggested demonstration:** Trace one student's grades through the flowchart live (a volunteer's real quiz scores, anonymized on the board): the class executes the chart by hand — the flowchart is the CPU from L05, repurposed, and say so.

**Misconception warnings:**
- "Pseudocode is fake code." It is the *design language* — language-independent, reviewable, and what professionals write before code exists.
- "Efficiency means clever tricks." First correctness, then measurable inefficiency (the linear-vs-binary search demo) — cleverness without correctness is negative value.
- "Flowcharts are schoolwork." They are design artefacts in industry (process design, incident runbooks) — the chart they build today is the runbook shape they will write at work.

**Discussion prompts:**
1. Which pillar did today's clinic exercise most — and which pillar does your project need most?
2. Where did L05's cycle reappear inside your flowchart's execution?
3. What does "best 10 of 14" decompose into, as an algorithm?

**Exit-ticket questions (with answers):**
1. *Name the four pillars.* — Decomposition, pattern recognition, abstraction, algorithm design.
2. *Binary search's precondition.* — Sorted input (and random access — accept sorted as the key requirement).
3. *Flowchart vs pseudocode: one difference.* — Visual control-flow vs language-shaped text; both are design before code (accept reasoned pairs).
4. *Your transcript computation's most bug-prone node, and why.* — The best-10-of-14 node (sorting + truncation edge cases); accept any defended node.

---

## L32 — Emerging Technologies and Synthesis

**Teaching tips:**
- The showcase *is* the assessment event: enforce the 8–10 minute windows with a visible timer, collect peer-feedback slips after each team, and open one synthesis question per team — your facilitation, not a lecture, fills the gaps.
- The emerging-tech segment must stay *calibrated*: pair each technology (IoT, blockchain, quantum) with one real deployed use and one honest limitation. The L23/L28 toolkit does the evaluation work — students run it, you moderate.
- Close the course explicitly: the course-map slide from L01 returns, now annotated by the class naming what each module contributed. Full circle, deliberately.

**Board / projector plan:**
- [Board] Three-column maturity table: technology → deployed reality → honest limitation.
- [Slide] The course map from L01, re-projected for the synthesis close.
- [Board] Peer-feedback slip skeleton: two strengths, one question (the same slip the rubric references).

**Suggested demonstration:** The toolkit applied live: one current technology headline (this week's, whatever it is) run through L23's four credibility criteria and L28's verification loop on the projector — the course's methods meeting the news, in ten minutes.

**Misconception warnings:**
- "Quantum computers will replace ordinary ones." They are accelerators for narrow problem classes, not general successors — concept-level honesty per the lecture page.
- "Blockchain = trustworthy." It is tamper-evident *ledger* machinery; trust still depends on what's recorded and by whom (oracle problem — name it and move on).
- "The course is over, so the learning is filed." The synthesis close argues the opposite: the modules *compose* — say which two compose in your own work.

**Discussion prompts:**
1. Which project team's work most surprised you, and which module's concept did it use least predictably?
2. Pick this week's technology headline: which of L23's four criteria is hardest to satisfy from a news article alone?
3. Which single lecture would you teach to a younger student, and in one sentence, why?

**Exit-ticket questions (with answers):**
1. *One deployed reality and one limitation for IoT, blockchain, and quantum.* — IoT: sensors/automation everywhere, but security-patch debt; blockchain: tamper-evident ledgers in production, but oracle/governance limits; quantum: real hardware exists, but narrow algorithms, not general replacement (accept calibrated pairs).
2. *Name two course concepts your project used together.* — Any defensible pair traced to specific lectures (e.g., L11 conventions + L26 cleaning; L25 schema + L26 charts).
3. *What does "synthesis" mean in one sentence for this course?* — Using the modules together as one connected system rather than isolated topics — the course map read as a whole.
4. *Which toolkit will you keep using after this course, and on what?* — Any named tool (credibility criteria, verification loop, 3-2-1, troubleshooting method) with a concrete next use.
