---
quiz: Q12
covers: L22-L24
---

# Practice Q12 — L22–L24 (Internet · Web · Cloud)

## Q1

List, in order, the four DNS server types consulted for an uncached lookup — and name the step that usually makes repeats instant.

<details>
<summary>Self-check</summary>

Resolver (ISP) → root server → TLD server (.edu) → authoritative server for the domain. **Caching** at the resolver (and your OS/browser) is what makes repeat visits skip the whole walk.
</details>

## Q2

What does TCP add over IP, and what happens to your download's packets when one router on the path dies mid-transfer?

<details>
<summary>Self-check</summary>

TCP adds reliability: ordering, acknowledgment, and retransmission over IP's best-effort routing. Dying router: in-flight packets are lost; the endpoints retransmit, and remaining packets route around the failure — the download slows, doesn't corrupt. (Different routes → reordering is normal; sequence numbers fix it.)
</details>

## Q3

Parse `https://results.example.edu/2026/spring?dept=cs` into its four parts.

<details>
<summary>Self-check</summary>

Protocol `https` (secure HTTP); domain `results.example.edu` (DNS resolves it); path `/2026/spring` (resource address); query `?dept=cs` (parameters for the resource).
</details>

## Q4

HTTPS proves the server's identity and encrypts the conversation. What does it *not* tell you — and how does A5's message 2 exploit the gap?

<details>
<summary>Self-check</summary>

It does not tell you the site is **honest** — a phishing site can hold a perfectly valid certificate for its own (fraudulent) domain. A5's "bank" used a real certificate on a lookalike domain: the padlock secured the *connection to the impostor*.
</details>

## Q5

Classify: (a) hourly-rented Linux VM, (b) Google Docs, (c) managed web-app hosting. For (c), name one thing you still own.

<details>
<summary>Self-check</summary>

(a) IaaS — you manage the OS up; (b) SaaS — provider runs everything, you manage data/settings; (c) PaaS — you deploy code, provider runs runtime/scaling. Even in (c) you own **your code's security and your data/access control** — shared responsibility never fully transfers.
</details>
