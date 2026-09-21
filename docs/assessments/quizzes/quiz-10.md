---
quiz: Q10
covers: L17-L18
---

# Practice Q10 — L17–L18 (Boolean Logic · Logic Gates)

## Q1

Build the truth table for `(A OR B) AND (NOT B)`.

<details>
<summary>Self-check</summary>

A B | A∨B | ¬B | out — 00: 0,1,0 · 01: 1,0,0 · 10: 1,1,1 · 11: 1,0,0. Output is **A AND NOT B** — the table reveals the simplification (this expression *is* how "A but not B" formalises).
</details>

## Q2

Translate: "admission requires a pass mark and no outstanding dues." Then negate it with De Morgan (no NOT over the whole expression).

<details>
<summary>Self-check</summary>

Admit = Pass ∧ ¬Dues. Negation: ¬(Pass ∧ ¬Dues) = **¬Pass ∨ Dues** — "either no pass, or dues outstanding." De Morgan's flip: AND→OR when NOT distributes inside.
</details>

## Q3

Why is NAND universal? Show NOT, AND, OR from NANDs.

<details>
<summary>Self-check</summary>

NOT A = A NAND A (both inputs same → ¬A). AND = ¬(A NAND B) = (A NAND B) NAND (itself). OR = ¬A ∧¬B inverted via De Morgan → (A NAND A) NAND (B NAND B). Since NOT, AND, OR suffice for *any* Boolean function, NAND alone suffices: universality.
</details>

## Q4

The half adder: which gates, which outputs, and what can it *not* do that a full adder can?

<details>
<summary>Self-check</summary>

Sum = A XOR B; Carry = A AND B. It cannot accept an **incoming carry** from a previous column — multi-bit addition needs the full adder's third input (C-in), built from two half adders + an OR.
</details>

## Q5

A built circuit disagrees with its designed truth table on input row (1,1). Give a systematic debugging order.

<details>
<summary>Self-check</summary>

1. Re-derive the intended table (design error?). 2. Trace the row gate-by-gate on paper, labelling every wire. 3. Probe/verify each intermediate wire in the simulator against the paper values. 4. The first wire diverging from expectation localises the faulty gate/attachment. (Method — not rewiring at random.)
</details>
