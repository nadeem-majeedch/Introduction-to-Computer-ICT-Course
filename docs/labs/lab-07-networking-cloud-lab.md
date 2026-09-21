---
lab: 7
title: Networking and Cloud Lab
assigned: L21
due: End of Week 13
---

# Lab 7 — Networking and Cloud Lab

> **Assigned:** L21 · **Due:** end of Week 13 · **Module 6**

## Purpose

You trace your own machine's network path end-to-end (L21–L23), inspect a real HTTPS exchange, and provision then *destroy* a free cloud VM (L24) — the full Module 6 arc on real infrastructure.

## Before you start

- 90–120 minutes; a browser and terminal.
- A free cloud account: use your institution's sanctioned platform if provided; otherwise a major free-tier provider (the LMS lists approved options). You will delete everything you create in Part 4 — cleanup is graded.
- **Authorization note:** all probing here is confined to *your own* machine and account. Scanning or probing systems you don't own is out of scope and off-limits (L29's boundary applies).

## Part 1 — Your network, mapped (20 min)

1. Record your private IP, gateway, and DNS servers (OS network settings; on Windows `ipconfig /all`, elsewhere `ip route` + `/etc/resolv.conf` or `scutil --dns`).
2. Your machine's *private* address (e.g., `192.168.x.x`) vs the *public* address a "what is my IP" service reports — why do they differ? (One sentence; L21's router role.)
3. Sketch your home/campus path: device → access point → router → ISP → internet, naming each hop's hardware.

## Part 2 — DNS and routes (25 min)

1. `nslookup your-university-domain.edu` (or `dig`): record the resolved IP and the responding server.
2. Repeat for a domain of your choice with a CDN — note how answers differ (cache proximity, L22's distributed DNS).
3. `tracert` (Windows) / `traceroute`/`mtr` (elsewhere) to your university: identify the first hop (gateway), your ISP's hop, and the destination; screenshot. Missing hops in output are *normal* (routers may not answer) — say why in one sentence rather than assuming failure.

## Part 3 — Inside HTTPS (25 min)

1. Open browser dev-tools → Network tab; load a news/university page.
2. Identify: the main document request (status 200?), three other resources, one redirect if any (301/302).
3. Confirm the padlock: view the certificate — record the domain it certifies and its expiry date; why does the padlock NOT tell you the site is *honest* (L23)?
4. Reload with cache disabled once — what changed in timing? (Connect to caching at *some* layer.)

## Part 4 — Cloud hands-on (30 min)

1. Create one free-tier VM (smallest size; Ubuntu or your choice); record region choice and why.
2. Connect (web console or SSH per provider instructions) and run `uname -a` — screenshot.
3. Stop AND delete the instance; confirm in the console; record the final state screenshot. *Running resources cost real money — teardown is part of the exercise.*

## Part 5 — Reflection questions

1. Which of L22's DNS server types did your resolver actually consult, per your Part 2 evidence?
2. What single fact from Part 3 best explains why free public Wi-Fi with HTTPS is *mostly* safe for passwords?
3. IaaS gave you an OS in minutes. Name one responsibility that remained yours (per L24's shared model) even before teardown.

## Expected observations and troubleshooting

**You should see:** a private address (`192.168.x.x` / `10.x.x.x` / `172.16–31.x.x`) vs a different public one; traceroute where hop 1 is your gateway and later hops may be `* * *` (routers declining to answer — normal, and your one-sentence why is graded); a certificate whose domain matches the site and an expiry date in the future; a VM lifecycle ending in a confirmed deletion.

**If something goes wrong:**
- *`nslookup` returns nothing* → try a second public resolver if your instructor approves, or record the failure itself — resolver behaviour is the topic, and a documented failure with analysis earns the marks.
- *No free-tier VM available in your region* → the provider's sandbox/Cloud-Shell environment is the accepted substitute; record `uname -a` from there and note the substitution. Cleanup duty transfers to whatever you create.
- *Teardown impossible right now* → stop the instance at minimum, screenshot the stopped state, and record the deletion plan with a date; running costs are real, so do not leave it running.
- *Campus network blocks traceroute* → run it on a home network or use the in-browser route-visualizer your instructor lists; blockage by policy is itself an observation worth a sentence.

**Accessibility alternative:** every terminal output can be captured as text instead of screenshots (screen readers work well with terminals); the certificate fields are readable text in the browser's security panel. If the cloud step is inaccessible, a documented walk-through of the provider's own tutorial with your analysis satisfies the learning outcome — the hands-on is preferred, the understanding is required.

## Submission checklist

- [ ] Network map + private/public IP explanation
- [ ] DNS/route screenshots with annotations
- [ ] HTTPS inspection answers + certificate record
- [ ] VM creation, use, and *teardown* screenshots
- [ ] Reflections; submitted via LMS

## Grading

Standard rubric ([labs index](index.md#how-labs-are-graded)); confirmed teardown is required for full marks.
