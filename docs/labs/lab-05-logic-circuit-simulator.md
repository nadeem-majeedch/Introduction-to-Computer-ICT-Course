---
lab: 5
title: Logic Circuit Simulator Lab
assigned: L18
due: End of Week 10
---

# Lab 5 — Logic Circuit Simulator Lab

> **Assigned:** L18 · **Due:** end of Week 10 · **Module 5**

## Purpose

Truth tables describe; circuits compute. In a free browser-based logic simulator, you will build XOR from NANDs (universality, proven by your own hands) and assemble the half adder that L18 presented on paper.

## Before you start

- 60–75 minutes; a browser.
- Any free logic simulator (e.g., CircuitVerse or Logisim-evolution; your instructor pins the choice in class). Screenshots must show *your* circuit with all switches/LEDs visible.
- **Educational-use note:** the simulator is a sandbox; nothing here touches real hardware or networks.

## Part 1 — Gate warm-up (15 min)

Build and screenshot each with its truth table verified by toggling all inputs:

1. AND, OR, NOT from the palette (confirm the L17 table).
2. NAND and NOR (note the bubbles).

## Part 2 — Universality: XOR from NANDs (20 min)

1. On paper: sketch NOT, AND, OR built *only* from NAND gates (De Morgan does most of it).
2. In the simulator: build XOR from four NANDs; toggle all four input rows; verify against the L17 XOR table.
3. Screenshot with all four rows' outputs recorded on the image or beside it.

## Part 3 — The half adder (20 min)

1. Build: Sum = A XOR B, Carry = A AND B (from Part 1's gates).
2. Verify all four rows against the L18 table; screenshot each output pair.
3. Extend (optional, bonus): chain two half adders into a **full adder** (add the OR of the two carries) and verify all eight rows.

## Part 4 — Reflection questions

1. Where in your XOR-from-NAND build did De Morgan's law appear, in words?
2. Why does the half adder need *two* outputs? What does each represent for binary addition?
3. Your full adder's carry-out was wrong for one input row — describe a systematic way to find the faulty wire (method, not luck).

## Expected observations and troubleshooting

**You should see:** XOR-from-NAND outputs matching the L17 XOR table for all four rows; the half adder producing sum `0,1,1,0` and carry `0,0,0,1` as inputs count up; the paper sketch visibly preceding the build (that ordering is graded).

**If something goes wrong:**
- *A truth-table row is wrong* → systematic wire-tracing: feed the failing input row, follow the signal gate by gate against your sketch (the method reflection asks for exactly this).
- *The simulator won't load* → the browser-based fallback needs no install; if the network is down, the paper build with a gate-by-gate trace table satisfies Parts 2–3 (state the substitution on your submission).
- *Screenshots lack switch states* → most simulators toggle visually; ensure inputs are visibly set in every capture — invisible inputs make verification unverifiable.

**Accessibility alternative:** the paper-trace substitution above is fully screen-reader compatible; keyboard-only simulators exist and the lab accepts a complete trace table + sketch in place of screenshots. Colour-coded wires may be replaced by labelled wires.

## Submission checklist

- [ ] Part 1 verification screenshots
- [ ] Paper sketch + verified XOR-from-NAND circuit
- [ ] Half adder screenshots, all four rows
- [ ] Reflections; share-link or exported file via LMS

## Grading

Standard rubric ([labs index](index.md#how-labs-are-graded)); full-adder extension earns the remaining demonstration points (capped at 100%).
