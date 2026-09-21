# Teaching Guide — Module 6: Networks, Internet, and Cloud

**Module 6** · Stage 3 · 4 lectures (L21–L24) · 8 contact hours
Companion to lecture pages `L21`–`L24` under `docs/lectures/`. **Not published.** Answers to exit tickets appear here and nowhere student-facing.

> Symbols: **[Slide]** projector visual · **[Board]** board work · **[Demo]** live demonstration · **[Discuss]** think-pair-share or open discussion.

## Before this module

- [ ] Lab 7 (networking & cloud lab) runs this module: test the lab room's guest-network access in advance; the CLI exercises reuse L10's command fluency.
- [ ] A4 (anatomy of a web request) needs name tags or cards for the role-play: prepare resolver, root, TLD, authoritative, router, and endpoint cards — 8–10 roles for a typical section.
- [ ] CS-02 (university cloud migration) handout: confirm enough copies/digital access; pre-read the stakeholder list and pick your discussion devil's-advocate questions.
- [ ] L23's credibility gauntlet: pre-load the three same-claim pages (university, vendor, anonymous blog) in three browser tabs — never search live in class; results vary and derail timing.

## Misconception warnings (module level)

1. **"Wi-Fi is the internet."** Wi-Fi is the last-hop *access* technology; L21's campus-map activity exists to break this, and the L22 request journey finishes the job.
2. **"The cloud is a place / 'just someone else's computer'."** Both half-truths; the service-model ladder (L24) replaces them with IaaS/PaaS/SaaS precision.
3. **"A lock icon means the site is honest."** TLS authenticates the *connection to that domain*, not the domain's intentions; L23's credibility criteria are deliberately separate from the padlock.
4. **"Network problems are one thing."** The troubleshooting isolation from L12 returns here as layer-thinking: cable, LAN, DNS, or destination — name the layer before the fix.

---

## L21 — Networking Concepts

**Teaching tips:**
- Build the campus map activity *before* formal definitions: teams sketch the room's own network (their laptops → AP → switch → router → outside world), then the lecture supplies the official vocabulary for what they already drew. Ownership first, terminology second.
- Bandwidth vs latency is a *plumbing* intuition: pipe diameter vs water arrival delay. The video-call failure story (fat pipe, long queue) is the memorable case; tell it before the definitions.
- Protocol: introduce as "agreed message format + rules of exchange," then let students find its analogies (postage envelopes, airport procedures) — keep one analogy, drop the rest, they collide by 21.4.

**Board / projector plan:**
- [Board] The campus map from student teams, corrected in place with switch/router/AP labels as the segment proceeds.
- [Slide] The Mermaid topology diagram from the lecture page's "Visual explanation."
- [Board] PAN→LAN→MAN→WAN as nested boxes with one real example written inside each.

**Suggested demonstration:** Project the lecture-hall machine's network settings: IP address, gateway, DNS server — three numbers students will meet again in L22, seen live on the room's own network (no configuration changes; read-only).

**Misconception warnings:**
- "The router is the box with antennas." The AP does wireless; the router routes *between* networks; home boxes are three devices in one plastic shell — say so explicitly or the map activity mislabels everything.
- "More bandwidth fixes lag." Latency, queueing, and drops are separate axes; the call-freeze example separates them.
- "Wireless is just slower wired." Security exposure, interference, and shared-medium behaviour differ in kind, not just speed.

**Discussion prompts:**
1. Which single component's failure cuts the whole campus off the internet, and which failure touches one lab only?
2. Where does the university's Wi-Fi end and the "real" internet begin? (Trick — it's all networks; the distinction is administrative scope.)
3. Why do data centres still prefer cables for servers?

**Exit-ticket questions (with answers):**
1. *Order by scope: WAN, PAN, MAN, LAN.* — PAN < LAN < MAN < WAN.
2. *Switch vs router, one sentence each.* — Switch delivers frames within a network (by MAC); router moves packets between networks (by IP).
3. *Bandwidth vs latency in the video-call story.* — Bandwidth: capacity of the pipe; latency: delay per trip — a wide pipe with long queue still freezes calls.
4. *What makes something a protocol?* — An agreed format and exchange rules both sides follow.

---

## L22 — The Internet: How It Works

**Teaching tips:**
- A4 is the module's centrepiece activity and needs firm stage management: run it *once* slowly with narration, then once at speed; the class narrates the second run without notes. Appoint a "packet loss" heckler who removes one packet — TCP's re-request moment becomes theatre.
- Keep DNS to its question ("which IP is this name?") and defer resolver caching hierarchies to later courses; the *question-answer* shape matters, not the tree's pruning.
- The end-to-end trace (22.3) is the examinable centrepiece: students must reproduce it top-to-bottom on paper. Board it as a numbered sequence and leave it up through the activity.

**Board / projector plan:**
- [Board] The numbered request journey (name → IP → packets → hops → reassembly → response), written once, referenced all hour.
- [Slide] The Mermaid sequence diagram from the lecture page's "Visual explanation."
- [Board] One packet drawn with envelope fields (source IP, destination IP, sequence number) — the postal analogy grounded in real fields.

**Suggested demonstration:** In the read-only network-settings screen from L21, point at the DNS server number: "that is the resolver your machine will ask first" — yesterday's three numbers become today's cast.

**Misconception warnings:**
- "The internet is one big computer / one company." A federation of networks; no single owner — the packet-switching design is *why*.
- "Packets travel in order, together." Independent routing is the feature; TCP's reordering is the patch — the heckler demo shows it.
- "DNS looks up 'the' address." Names can map to many addresses; answers vary by location and time — accept that instability as design.

**Discussion prompts:**
1. Why did packet switching beat dedicated circuits for bursty data? (Idle circuits waste; bursts share.)
2. What exactly breaks if one core router dies mid-transfer? (Reroute; TCP re-requests; the transfer survives — resilience by design.)
3. Your university's names and numbers: which campus system is your resolver?

**Exit-ticket questions (with answers):**
1. *Packet switching in one sentence.* — Messages are split into packets routed independently and reassembled at the destination.
2. *DNS's job; TCP's job.* — DNS: resolve names to IP addresses; TCP: ordered, reliable delivery with retransmission of losses.
3. *What does a hop count?* — One router-to-router leg of a packet's journey.
4. *Why is the internet resilient?* — Many alternative paths; packets reroute around failures (no single mandatory route).

---

## L23 — The Web: HTTP, Browsers, and Search

**Teaching tips:**
- URL dissection should happen on *real* URLs from the students' own contexts (course site, a government portal, a shortened link) — parse one on the board into protocol, domain, path, query, fragment, and never accept "the link" as a unit again.
- The padlock conversation must be unambiguous: TLS protects the *pipe* to the named domain; it says nothing about the domain's honesty. Bridge immediately into the credibility gauntlet.
- The gauntlet needs scoring discipline: the four criteria on the board, each page scored 0–2 per criterion, totals defended by teams — structure beats vibes.

**Board / projector plan:**
- [Board] One URL dissected with labelled arrows; keep it up while the gauntlet runs.
- [Slide] The Mermaid rendering pipeline from the lecture page's "Visual explanation."
- [Board] The four credibility criteria as scoring columns for the gauntlet.

**Suggested demonstration:** Live browser DevTools on the course site, Network tab: reload once, point at the first request line — method, status 200, and the cascade of dependent requests. Real HTTP, no configuration, permanent impact. (Read-only inspection only.)

**Misconception warnings:**
- "The browser downloads 'the page'." It fetches HTML + dozens of assets and *renders* them through parse → DOM → style → paint; the view is a construction, not a copy.
- "Search finds pages." Search finds *index entries*, ranked by ranking systems — the index is the searchable thing, not the live web.
- "HTTPS = safe to click." TLS ≠ trustworthiness; phishing sites have padlocks — the gauntlet's whole point.

**Discussion prompts:**
1. What does the browser do first with an unfamiliar domain, and which L22 actor answers?
2. Why does a page half-load when its images fail but not vice versa? (HTML is the dependency root — rendering order.)
3. Which credibility criterion is hardest to automate, and why? (Purpose/bias — judgement; automation handles metadata better than intent.)

**Exit-ticket questions (with answers):**
1. *Parse `https://university.edu/admissions/apply?year=2027` into parts.* — Protocol https; domain university.edu; path /admissions/apply; query year=2027.
2. *What does HTTPS add over HTTP?* — TLS: encryption of the pipe + authentication of the domain (integrity too).
3. *Order: crawler, index, ranking.* — Crawler discovers → indexer stores/organizes → ranking orders results per query.
4. *Name the four credibility criteria.* — Authority, evidence, currency, purpose (accept the lecture page's exact four).

---

## L24 — Cloud Computing and Virtualization

**Teaching tips:**
- Open with services students *already* pay for (mail, storage, streaming) and let them place each on the IaaS/PaaS/SaaS ladder themselves — the ladder lands better as recognition than as definition.
- Virtualization needs one clean image: hypervisor slices one physical machine into many virtual ones; containers share the host kernel and start like processes. Stop at the intuition — later courses go deep.
- CS-02 debate: assign stakeholders (CIO, finance, IT staff, faculty, students) and *require* each team to voice one stakeholder's cost argument. The capex/opex distinction becomes personal, and the "no wrong answer" trade-off framing must be explicit.

**Board / projector plan:**
- [Board] The responsibility ladder drawn as stacked strips: "who manages what" moving down from apps (SaaS) to silicon (IaaS); students place the university's systems on it.
- [Slide] The Mermaid stack diagram from the lecture page's "Visual explanation."
- [Board] Capex vs opex as a two-column ledger for the CS-02 finance stakeholder.

**Suggested demonstration:** A timed container-vs-VM startup comparison if the lab image allows; otherwise the projector screenshot pair (hypervisor console listing VMs; container runtime listing containers) with the boot-time figures annotated.

**Misconception warnings:**
- "Cloud = someone else's computer." True but empty: the *service model* — elastic, measured, on-demand — is the substance (and the economics).
- "Containers are tiny VMs." Different mechanism: containers share the host OS kernel; VMs virtualize hardware with guest OSes.
- "Cloud is always cheaper." At steady load, owned hardware can win; elasticity is what you pay for — CS-02's finance argument made honestly.

**Discussion prompts:**
1. The university's email, LMS, and the physics department's compute cluster: which service model is each, and why did they likely differ?
2. What must be true about a workload for elasticity to actually save money? (Variable demand; idle time to shed.)
3. Which L22 concept does a multi-region cloud deployment reuse? (Networks of data centres — traffic routed as always; regions are just far hops.)

**Exit-ticket questions (with answers):**
1. *Match: renting raw servers; renting a managed database platform; using webmail.* — IaaS; PaaS; SaaS.
2. *VM vs container, one difference.* — VM: full guest OS on a hypervisor; container: processes sharing the host kernel (lighter, faster start).
3. *Elasticity in one sentence.* — Capacity scales with demand automatically; you pay for what you use.
4. *Capex vs opex in the CS-02 debate.* — Capex: capital purchase of owned machines; opex: operational rental of cloud capacity — the debate is cash-flow and control vs flexibility.
