---
activity: A4
title: Anatomy of a Web Request (Role-Play)
lecture: L22
duration: 30 minutes
---

# A4 — Anatomy of a Web Request

> **Lecture:** L22 · **Time:** 30 min · **Class:** 12+ role players, rest narrate and jury

## Goal

The full journey of `https://university.edu/courses` — performed by humans, so the *order and responsibility* of each hop sticks. This is Module 6's signature synthesis; the final exam's favourite scenario question grows from it.

## Role cards (distribute)

| Role | Holds | Says when hit |
|---|---|---|
| Browser | the URL | "resolve university.edu, then connect" |
| Resolver (ISP DNS) | cache | cache hit? "here's the IP" else "ask root" |
| Root server | TLD pointer | ".edu lives there" |
| TLD server (.edu) | authoritative pointer | "university.edu is served there" |
| Authoritative server | A record | "93.184.x.x" |
| Router ×3 | routing table | "not my network — next hop" |
| Server | page + certificate | "TCP OK → TLS OK → here's /courses" |
| Packet ×2 | data chunks | "route me; reorder me at the end" |
| Narrator/Jury | the script | verifies order, catches shortcuts |

## Round 1 — DNS walk (10 min)

Browser → resolver → (cache miss) → root → TLD → authoritative → back to resolver → IP to browser. Jury checks: *was the cache consulted first? who cached what?*

## Round 2 — The delivery (10 min)

TCP handshake (three exchanges), TLS nod (details are L23), HTTP GET, response packets — sent along **different router paths** to prove reassembly handles reordering. Jury checks: packets arrive out of order — who fixes the order, and how?

## Round 3 — Failure drills (5 min each, as time allows)

1. Root server "down": what still works, and for how long? (Caches.)
2. Router 2 dies mid-transfer: what happens to the packets in flight? (Rerouting — TCP retransmits.)
3. Someone swaps the server's certificate: which step refuses, and what does the user see?

## Debrief

Map the performed sequence onto L22's five-step journey, one line per step. The written exam version asks exactly this narration with named protocols.

## Solo variant (revision)

Write the journey as a numbered sequence naming protocol and role per step, then answer the three failure drills on paper.
