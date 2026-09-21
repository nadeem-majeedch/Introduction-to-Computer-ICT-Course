# Module 6 Slide Decks — L21–L24

**Format:** One `## S# · Title` per slide; `**Notes:**` carry [~minutes], TALK, ASK, MISC, DEMO, TRAN, EXT, TROUBLE cues. Run sheets allocate the full 120 minutes.

---

## L21 — Networking Concepts (Slides + Speaker Notes)

**Resources:** projector; read-only network-settings screen on the hall machine (tested); campus-map drawing time for teams.

### Run sheet (120 min)

| Block | Slides | Time |
|---|---|---|
| Draw the room's network + objectives | S1–S3 | 18 |
| Official vocabulary, applied | S4–S5 | 14 |
| Bandwidth vs latency | S6–S7 | 14 |
| Protocols + layers | S8–S9 | 12 |
| Campus map annotated | S10 | 16 |
| Concept check | S11 | 12 |
| Summary + exit ticket | S12–S13 | 12 |
| Buffer | — | 22 |

### Slides

# L21 · Networking Concepts
**Module 6 · Stage 1 · 2 hours**

## S1 · You live inside a LAN
**Notes:** [~5] TALK: the frame — you've used this room's network all semester without seeing its shape; today you draw it first, vocabulary second (guide tip: ownership before terminology). ASK: none. TRAN: "Draw it."

## S2 · Today
- Networks by scale · hardware roles · bandwidth vs latency · protocols
**Notes:** [~3] TALK: promise the map annotation round. TRAN: draw.

## S3 · Activity (part 1) — Sketch the room's network
- Teams: every device → its box → the way out
**Notes:** [~10] TALK: five-minute sketch per team; wrong labels welcome — correction *is* the lesson. ASK (circulating): "What's the box with the antennas *doing*?" MISC: everyone labels the Wi-Fi box "router" — collect that; S5 re-labels it. TRAN: "The official version of your drawing."

## S4 · Networks by scale
- PAN · LAN · MAN · WAN — your sketch is a LAN
**Notes:** [~7] TALK: nested boxes (guide plan) with one real example each. ASK: "Where does your home network sit? The mobile network?" MISC: "Wi-Fi is the internet" — module warning #1; the sketch already shows the boundary. TRAN: "The boxes in your drawing."

## S5 · Hardware roles, corrected
- Switch keeps local traffic local · router is the door · AP bridges wireless to wired
**Notes:** [~7] TALK: re-label team sketches live; the home-box-is-three-devices speech (guide warning). ASK: "Which single failure silences the campus?" MISC: "the router is the box with antennas" — the AP does wireless; say it twice. TRAN: "Two numbers people confuse."

## S6 · Bandwidth vs latency
- Pipe diameter vs arrival delay — the video-call story
**Notes:** [~8] TALK: the fat-pipe-long-queue story *before* definitions (guide tip); plumbing intuition carries. ASK: "Can you have huge bandwidth and a frozen call?" MISC: "more bandwidth fixes lag" — latency, queueing, drops are separate axes. TRAN: "Measure them."

## S7 · Demo: the room's three numbers
- IP · gateway · DNS — read-only, from network settings
**Notes:** [~6] TALK: project the settings screen (read-only); three numbers students meet again in L22. ASK: "Which number is the door from S5?" MISC: none. TRAN: "Rules of exchange."

## S8 · Protocols
- Agreed format + rules — why heterogeneous devices cooperate
**Notes:** [~7] TALK: keep ONE analogy (postage envelopes), drop the rest before they collide (guide tip). ASK: "What breaks if two sides disagree on the format?" MISC: analogy soup — enforce the single one. TRAN: "Why layers?"

## S9 · Why layers?
- Each layer solves one problem for the one above — L09's stack, networked
**Notes:** [~5] TALK: the course's most reused idea returns — L09's stack, now networked; abstraction as engineering survival. ASK: none. MISC: none. TRAN: "Annotate your maps."

## S10 · Activity (part 2) — Annotate the campus map
- What breaks if each single component fails?
**Notes:** [~16] TALK: per the lecture page's activity; failure annotation on the *corrected* sketches. ASK (circulating): "Which failure is *silent* — works, but slowly?" MISC: single-point-of-failure hunting only — ask for the partial-degradation cases too. TROUBLE: teams done early — add the server room. TRAN: "Check the map."

## S11 · Quick check
1. Order by scope: WAN, PAN, MAN, LAN.
2. Switch vs router — one sentence each.
3. Bandwidth vs latency in the call story.
**Notes:** [~12] TALK: write-pair-resolve. MISC: Q2 — swapped answers mean the S5 relabel didn't land; fix before summary. TRAN: "Summary."

## S12 · Summary
- Scale classes · three hardware roles · two independent axes · protocols
**Notes:** [~6] TALK: exam skeleton; Lab 7 continues the CLI+network thread. TRAN: exit ticket.

## S13 · Exit ticket
**On your annotated map: mark one failure that cuts the whole campus off, and one that only slows one lab.**
**Notes:** [~6] TALK: expected: router/uplink vs one switch/AP; slips show map comprehension. Keep for L22's resilience discussion.

---

## L22 — The Internet: How It Works (Slides + Speaker Notes)

**Resources:** A4 role-play cards (resolver, root, TLD, authoritative, routers, endpoints — guide prep); the "packet-loss heckler" recruit; L21's three numbers.

### Run sheet (120 min)

| Block | Slides | Time |
|---|---|---|
| Three numbers recap + objectives | S1–S2 | 8 |
| Packet switching | S3–S4 | 16 |
| Naming: DNS | S5 | 10 |
| TCP's patch | S6 | 8 |
| Activity: A4 role-play | S7 | 30 |
| The end-to-end trace | S8–S9 | 16 |
| Concept check | S10 | 10 |
| Summary + exit ticket | S11–S12 | 12 |
| Buffer | — | 10 |

### Slides

# L22 · The Internet: How It Works
**Module 6 · Stage 1 · 2 hours**

## S1 · Yesterday's three numbers
**Notes:** [~5] TALK: IP, gateway, DNS on the board — today they become the cast of a planetary delivery system. ASK: "Which one turns names into addresses?" MISC: none. TRAN: "The core idea."

## S2 · Today
- Packet switching · DNS · TCP · the full request journey — A4 today
**Notes:** [~3] TALK: promise the role-play; recruit the heckler now (quietly). TRAN: packets.

## S3 · Packet switching
- Split, route independently, reassemble — shared links beat circuits
**Notes:** [~9] TALK: bursty-data economics (guide's discussion answers); resilience is a *consequence* of the design. ASK: "Why did this beat dedicated circuits?" MISC: "the internet is one big computer/one company" — module warning; a federation, by design. TRAN: "The envelope."

## S4 · The packet, drawn
- Source IP · destination IP · sequence number — postal fields, real ones
**Notes:** [~7] TALK: the envelope fields (guide's plan); sequence number earns its keep at S6. ASK: "What does the sequence number *anticipate*?" MISC: none. TRAN: "Names first."

## S5 · DNS: the phone book
- Which IP is this name? — resolver, hierarchy, one question
**Notes:** [~10] TALK: keep DNS to its question (guide tip); defer resolver-caching hierarchies to later courses. ASK: "What if DNS lies — or dies?" MISC: "DNS looks up 'the' address" — many answers, varying by place/time; instability is design. TRAN: "Losses happen."

## S6 · TCP: order and re-requests
- Best-effort IP + TCP's bookkeeping = reliable delivery
**Notes:** [~8] TALK: the patch metaphor — IP loses things; TCP notices and re-asks. ASK: "Which packet field does TCP use to reassemble?" MISC: "packets travel together in order" — independent routing is the feature; TCP is the patch. TRAN: "You are the network now."

## S7 · Activity — A4: Anatomy of a Web Request (30 min)
Students play every role · one pass slow with narration · one at speed · the heckler strikes
**Notes:** [~30] TALK: per the A4 handout and guide's stage-management; second run narrated by the class *without notes*. ASK (after the heckler): "Who noticed, who fixed it, how long did it take?" MISC: skipping the DNS step because "we know it" — no; run every hop. TROUBLE: odd numbers of students — instructor plays the resolver (best seat in the house). EXT: a second heckler drops a *different* packet mid-flight. TRAN: "The journey on paper."

## S8 · The end-to-end trace
- Name → IP → packets → hops → reassembly → response — the examinable centrepiece
**Notes:** [~10] TALK: the numbered sequence (guide's board plan); students must reproduce it top-to-bottom — say it's examinable. ASK: "Where in the sequence did the heckler's packet return?" MISC: none. TRAN: "One word about resilience."

## S9 · Why the internet survives backhoes
- Many paths; packets reroute; TCP re-requests — resilience by design
**Notes:** [~6] TALK: the homework's resilience story set up; L21's map annotations were the local version. ASK: "What DOES hurt badly?" (DNS/CDN-scale failures — homework's extension.) MISC: none. TRAN: "Check the journey."

## S10 · Quick check
1. Packet switching in one sentence.
2. DNS's job; TCP's job.
3. What does a hop count?
**Notes:** [~10] TALK: write-pair-resolve. MISC: Q3 — "a website" answers; a hop is one *router-to-router leg*. TRAN: "Summary."

## S11 · Summary
- Packets, names, re-requests — and the full journey as one reusable trace
**Notes:** [~6] TALK: exam skeleton; the trace returns in L23 as the HTTP conversation's stage. TRAN: exit ticket.

## S12 · Exit ticket
**Write the eight-step journey of your most-visited site, from typing the name.**
**Notes:** [~7] TALK: eight numbered steps expected (guide's homework); missing-DNS journeys are the diagnostic. Keep slips — L23 opens with one of them dissected.

---

## L23 — The Web: HTTP, Browsers, and Search (Slides + Speaker Notes)

**Resources:** DevTools Network tab on the hall machine (tested); three same-claim pages pre-loaded in tabs (guide prep: never search live); gauntlet scoring sheet.

### Run sheet (120 min)

| Block | Slides | Time |
|---|---|---|
| An exit-ticket journey, dissected | S1–S2 | 8 |
| URL anatomy | S3–S4 | 16 |
| HTTP(S): the conversation | S5–S6 | 14 |
| Rendering: construction, not copy | S7 | 10 |
| Search: crawler → index → ranking | S8 | 10 |
| Activity: credibility gauntlet | S9 | 26 |
| Concept check | S10 | 12 |
| Summary + exit ticket | S11–S12 | 12 |
| Buffer | — | 12 |

### Slides

# L23 · The Web: HTTP, Browsers, and Search
**Module 6 · Stage 1 · 2 hours**

## S1 · One of your journeys, dissected
**Notes:** [~5] TALK: project one L22 exit slip (anonymized, a good one); today adds the *conversation* on top of its packets. ASK: none. TRAN: "The address."

## S2 · Today
- URLs · HTTP(S) · rendering · search — and a credibility gauntlet
**Notes:** [~3] TALK: the gauntlet is scored — 0–2 per criterion, totals defended (guide tip). TRAN: URL.

## S3 · URL anatomy
- Protocol · domain · path · query · fragment — dissected live
**Notes:** [~10] TALK: parse a real URL from *their* context (guide tip); never accept "the link" as a unit again. ASK: "Which part tells your browser *how* to talk?" MISC: none. TRAN: "The safety reading."

## S4 · Read URLs like a skeptic
- Lookalike domains · path tricks · shorteners — Module 8's first line of defence
**Notes:** [~6] TALK: the URL as safety skill; L29 will inherit this directly. ASK: "What's suspicious about `university-portal.com` when your university is `.edu`?" MISC: none. TRAN: "The conversation."

## S5 · HTTP: request/response
- Methods, status codes — the web's grammar
**Notes:** [~8] TALK: DevTools demo now or at S6 (guide's plan allows either); GET and 200 named, the rest later courses'. ASK: "What does 404 actually mean, in one word?" (Missing.) MISC: none. TRAN: "What the S adds."

## S6 · HTTPS = HTTP + TLS
- The *pipe* is encrypted and authenticated — the domain's honesty is a separate question
**Notes:** [~6] TALK: the padlock conversation must be unambiguous (guide tip); TLS ≠ trustworthiness — bridge into the gauntlet. ASK: "Does the padlock vouch for the *content*?" MISC: "lock icon means safe" — module warning #3; attackers have padlocks. TRAN: "What the browser builds."

## S7 · Rendering: a construction
- Fetch HTML → DOM → style → scripts → paint
**Notes:** [~10] TALK: the view is a construction, not a copy (module warning); half-loaded pages make sense. ASK: "Why does a page half-appear while images lag?" MISC: none. TRAN: "How search finds things."

## S8 · Search: crawler → index → ranking
- You query the index, not the live web
**Notes:** [~10] TALK: the pipeline; ranking as the algorithmic gatekeeper — Module 7 previews its bias questions. ASK: "Why might two people see different results for the same query?" MISC: "search finds pages" — it finds *index entries*. TRAN: "The gauntlet."

## S9 · Activity — Credibility gauntlet (26 min)
Three same-claim pages · score 0–2 per criterion · defend the ranking
**Notes:** [~26] TALK: per the lecture page's activity; four criteria on the board as scoring columns (guide plan); tabs pre-loaded — *never* search live (prep note). ASK (circulating): "Which criterion is your lowest score — why?" MISC: vibes-based ranking — the scores must cite the criteria. TROUBLE: a page fails all four — that's a fine outcome; the defence is the grade. TRAN: "Check the hour."

## S10 · Quick check
1. Parse the projected URL into its five parts.
2. What does HTTPS add — and what does it *not* vouch for?
3. Order: crawler, index, ranking.
**Notes:** [~12] TALK: write-pair-resolve. MISC: Q2 — "safety" answers are the S6 conflation; re-run the padlock sentence. TRAN: "Summary."

## S11 · Summary
- URLs dissected · the padlock's real promise · rendering as construction · the index
**Notes:** [~6] TALK: exam skeleton; the gauntlet's four criteria are the course's credibility toolkit — L28 inherits them. TRAN: exit ticket.

## S12 · Exit ticket
**Score your most-visited site 0–2 on the four criteria — one justification for your lowest score.**
**Notes:** [~6] TALK: self-audits are harder than stranger-audits — that's the point; lowest-score-justification is the marked line. Keep slips for L28's criteria-transfer discussion.

---

## L24 — Cloud Computing and Virtualization (Slides + Speaker Notes)

**Resources:** CS-02 handout count confirmed (guide prep); service-ladder strips for the board; VM/container screenshot pair (or timed demo if lab image allows).

### Run sheet (120 min)

| Block | Slides | Time |
|---|---|---|
| Services you already pay for + objectives | S1–S2 | 10 |
| What "cloud" means | S3 | 10 |
| IaaS / PaaS / SaaS ladder | S4–S5 | 16 |
| Virtualization: VMs and containers | S6–S7 | 16 |
| Activity: CS-02 case study | S8 | 30 |
| Cloud vs on-premises + concept check | S9–S10 | 14 |
| Summary + exit ticket | S11–S12 | 12 |
| Buffer | — | 12 |

### Slides

# L24 · Cloud Computing and Virtualization
**Module 6 · Stage 1 · 2 hours**

## S1 · You already rent the cloud
**Notes:** [~7] TALK: mail, storage, streaming on the board from the class's own list (guide tip) — recognition before definition. ASK: "What do you *actually* pay for?" MISC: none. TRAN: "The definition."

## S2 · Today
- The cloud defined · the service ladder · virtualization · CS-02 debate
**Notes:** [~3] TALK: promise the debate with named stakeholders. TRAN: definition.

## S3 · Cloud, defined
- On-demand · self-service · elastic · measured — a model, not a place
**Notes:** [~10] TALK: NIST-flavoured characteristics (lecture page's 24.1); "someone else's computer" is true but empty (module warning) — the *service model* is the substance. ASK: "Which characteristic would you miss first if it vanished?" MISC: none. TRAN: "The ladder."

## S4 · The responsibility ladder
- IaaS: you manage OS-upward · PaaS: app+data · SaaS: nothing
**Notes:** [~9] TALK: the stacked strips (guide's board plan); place the university's mail, LMS, and physics cluster *with the class*. ASK: "Which rung for the library catalogue?" MISC: rung confusion — the *who patches the OS* question settles it. TRAN: "The enabling trick."

## S5 · Demo: who manages what
- One scenario, walked down the ladder — control grows as burden shifts
**Notes:** [~7] TALK: short walk-through rather than new content; the ladder internalized. ASK: none. MISC: none. TRAN: "How one machine becomes many."

## S6 · Virtual machines
- Hypervisor slices hardware; guest OS each — heavy, isolated
**Notes:** [~8] TALK: the one clean image (guide tip); stop at intuition — later courses go deep. ASK: "Why would a data centre *want* many guests per host?" MISC: none. TRAN: "The lighter sibling."

## S7 · Containers
- Share the host kernel — light, fast, portable
**Notes:** [~8] TALK: VM-vs-container screenshot pair with boot times (guide prep); "tiny VMs" is the warning — mechanism differs. ASK: "Which would you start 300 of, and why?" MISC: "containers are tiny VMs" — shared kernel vs virtualized hardware; say the mechanism. TRAN: "The debate."

## S8 · Activity — CS-02: A University Moves to the Cloud (30 min)
Stakeholder teams · cost arguments required · recommendation written
**Notes:** [~30] TALK: per the CS-02 handout; each team voices one stakeholder's cost argument (guide tip) — capex/opex becomes personal. ASK (circulating): "Which stakeholder did your team *dismiss* too fast?" MISC: verdict-first teams — require the stakeholder arguments before any recommendation. TROUBLE: finance stall — the ledger two-column from the guide's plan unblocks. TRAN: "The honest trade-off."

## S9 · Cloud vs on-premises: a trade-off, not a verdict
- Elastic demand favours rent · steady load can favour owning
**Notes:** [~7] TALK: the "no wrong answer" framing made explicit (guide tip); the homework's elasticity-maths previews it. ASK: "Which workload class still buys machines?" MISC: "cloud is always cheaper" — module warning; elasticity is what you pay for. TRAN: "Check the ladder."

## S10 · Quick check
1. Match: raw servers / managed platform / webmail.
2. VM vs container — one mechanism difference.
3. Elasticity in one sentence.
**Notes:** [~7] TALK: write-pair-resolve. MISC: Q2 — "size" answers; the *kernel-sharing* is the mechanism. TRAN: "Summary."

## S11 · Summary
- The cloud is a model · the ladder allocates responsibility · virtualization enables elasticity · trade-offs decide
**Notes:** [~6] TALK: exam skeleton; Module 6 closes — the network stack is now end-to-end legible. TRAN: exit ticket.

## S12 · Exit ticket
**Your five-sentence CS-02 recommendation — which stakeholder's objection was hardest to dismiss, and why?**
**Notes:** [~6] TALK: the *objection-naming* is the marked line (guide's homework); slips feed the project's cloud-migration option discussions.
