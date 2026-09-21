---
case-study: CS-01
title: Moore's Law and the Smartphone
lecture: L06 (debrief L08)
duration: 30 minutes
---

# CS-01 — Moore's Law and the Smartphone

> **Lecture:** L06 (debrief in L08) · **Duration:** 30 min · **Format:** stakeholder debate + structured decision

## The scenario

It is 2015. A phone manufacturer's product committee must decide the flagship phone's direction for 2016. Transistor scaling is still delivering gains, but each generation costs more to develop, battery chemistry is improving only slowly, and rival phones compete on cameras and screens.

The committee hears from three voices:

- **Engineering lead:** "Transistor budgets are best spent on efficiency (smaller process node) — speed is already 'enough'; battery life is the real constraint."
- **Marketing lead:** "Consumers buy clock-speed numbers. Spend the budget on raw performance we can print on the box."
- **Product strategist:** "Spend on the camera pipeline and on-machine AI acceleration (a neural chip) — differentiation that specs can't easily copy."

## Guiding questions

1. **Trend analysis:** State Moore's observation precisely (doubling period, quantity). Which committee assumptions *depend* on the trend continuing — and which survive its slowdown?
2. **Spec literacy (L06):** Why is "clock speed on the box" a weak predictor of phone experience? Name two chip properties the box hides.
3. **Constraint reasoning (L07–L08):** In a phone, rank the pressure on: die area, power/heat, memory bandwidth. Justify each ranking in one sentence.
4. **Decision:** Which voice do you fund, and what one benchmark would you demand *before* mass production to test the claim?
5. **Hindsight (debrief in L08):** Which voice did the industry effectively follow in the late 2010s (specialised NPUs, camera silicon)? What does that imply about where Moore's-law headroom went?

## The framework applied

This case rehearses the *requirements → components* method from L08 §8.3, run backwards: given component trends, which *product bets* become possible? The exam version asks you to argue a spec decision from workload requirements — same skill, opposite direction.

## Debrief notes for self-study

- Moore's law is an empirical industry trend (G. Moore, 1965), not physics — see [L06](../lectures/L06-cpu-instruction-execution.md) references.
- The smartphone is the era's proof-by-artefact: ENIAC-to-pocket compression is the Module 1 → Module 2 bridge in one object.
