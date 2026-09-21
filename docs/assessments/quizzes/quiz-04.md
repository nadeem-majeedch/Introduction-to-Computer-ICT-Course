---
quiz: Q04
covers: L07-L08
---

# Practice Q04 — L07–L08 (Memory Hierarchy · Storage and Peripherals)

## Q1

Explain virtual memory in two sentences: what problem it solves and what it costs.

<details>
<summary>Self-check</summary>

It lets the OS extend RAM by moving less-used pages to disk, so machines survive workloads bigger than physical memory. Cost: every page fault pays the ~100× RAM↔disk speed gap — hence "thrashing" feels catastrophic rather than slightly slow.
</details>

## Q2

Why is SRAM used for cache despite costing far more per bit than DRAM?

<details>
<summary>Self-check</summary>

Speed and locality: SRAM's cell (six transistors, no refresh) answers in ~1–20 ns, and programs' temporal/spatial locality mean a small fast buffer near the core serves most accesses — a little of the right memory beats a lot of the far memory.
</details>

## Q3

A videographer's laptop stutters on 4-K editing though the CPU is fast. Which component is the suspect, and what two upgrades would you trial first?

<details>
<summary>Self-check</summary>

Storage (and/or RAM) — sustained video throughput. Trial: SSD with high sequential+random write speed, then more RAM (and the GPU for effects rendering; but the *stutter during editing* pattern points at storage first).
</details>

## Q4

Why is RAID 1 not a backup? Answer with the specific loss scenarios RAID 1 does not protect against.

<details>
<summary>Self-check</summary>

RAID guards against *disk failure only*: deletion (instantly mirrored), ransomware (encrypted copies mirrored), theft/fire (both units go), and user error are all replicated faithfully. Backups add *versions in time and offsite location* — different problems, different machinery.
</details>

## Q5

Classify these as input, output, or both, with the deciding property: touch screen, headset with mic, external SSD, barcode reader.

<details>
<summary>Self-check</summary>

Touch screen — both (touch in, display out); headset — both (mic in, speakers out); external SSD — both (reads and writes data; storage I/O); barcode reader — input only (one-way capture). The deciding property is the *direction* of information flow relative to the computer.
</details>
