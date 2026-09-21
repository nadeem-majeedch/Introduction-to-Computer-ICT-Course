---
quiz: Q03
covers: L05-L06
---

# Practice Q03 — L05–L06 (von Neumann · CPU)

## Q1

Draw (or list) the von Neumann components and the three kinds of signals the bus carries.

<details>
<summary>Self-check</summary>

CPU (control unit + ALU + registers), main memory (program + data together), I/O devices; bus carries **addresses** (where), **data** (what), **control** (when/who).
</details>

## Q2

What exactly did the 1945 stored-program proposal change about how machines are programmed?

<details>
<summary>Self-check</summary>

Before: programming = rewiring/patch-panels (ENIAC). After: the program is stored *in memory as data*, so changing behaviour = loading a different program — no physical reconfiguration. Software becomes a copyable artefact.
</details>

## Q3

Order these by speed and by size (both descending): L2 cache, registers, DRAM, SSD.

<details>
<summary>Self-check</summary>

Speed: registers > L2 cache > DRAM > SSD. Size: SSD > DRAM > L2 cache > registers — each level trades capacity/permanence for speed, which is the whole hierarchy argument.
</details>

## Q4

A friend's laptop has a 3.6 GHz chip but feels slower than your 2.4 GHz machine. Give three concrete causes.

<details>
<summary>Self-check</summary>

Any three of: different work-per-cycle (architecture), less/better cache, slower RAM or storage, fewer efficient cores under real load, thermal throttling, background load, older/slower SSD. Clock speed alone never predicts experience.
</details>

## Q5

In the fetch–decode–execute cycle, which register points to the next instruction, and what does the PC do *during* fetch?

<details>
<summary>Self-check</summary>

The **program counter (PC)**. During fetch its stored address is read out to fetch the instruction, and the PC then advances (typically by the instruction size) to point at the next one — jumps override this by writing a new PC value.
</details>
