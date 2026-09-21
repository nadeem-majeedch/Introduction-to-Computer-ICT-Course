---
quiz: Q08
covers: L13-L14
---

# Practice Q08 — L13–L14 (Number Systems · Numbers in Hardware)

## Q1

Convert 200 to binary, then to hex — show every step.

<details>
<summary>Self-check</summary>

200 ÷2 chain: remainders 0,0,1,0,0,0,1,1 → `11001000`. Hex by nibbles: `1100 1000` → C8, i.e. `0xC8`. Cross-check: 12×16+8 = 200. ✓
</details>

## Q2

Decode `1011 0110` as unsigned and as 8-bit two's complement.

<details>
<summary>Self-check</summary>

Unsigned: 128+32+16+4+2 = **182**. Signed (top bit negative-valued): −128+32+16+4+2 = **−74**. Same bits; the interpretation rule differs — that's two's complement in one line.
</details>

## Q3

Why is `#FF6600` orange? Answer in byte values and channel names.

<details>
<summary>Self-check</summary>

`FF`=255 red (full), `66`=102 green (~40%, adds yellow warmth), `00`=0 blue. RGB channels each take one unsigned byte (0–255), so hex pairs *are* the channel bytes — hex as a human view of binary, exactly L13's point.
</details>

## Q4

What is the largest 8-bit unsigned value and the smallest 8-bit signed value? Why the asymmetry?

<details>
<summary>Self-check</summary>

Unsigned max: 255 (`1111 1111`). Signed min: −128 (`1000 0000`, where the top bit is worth −128 and all lower bits are 0). Asymmetry: the two's-complement top bit *subtracts* 2^(n−1) rather than adding it, so the negative range reaches one further (−128) than the positive side (+127).
</details>

## Q5

Explain the 2038 problem in two sentences using the word "width."

<details>
<summary>Self-check</summary>

Many systems store time as **32-bit signed** seconds since 1970; that *width* caps the value at 2,147,483,647 seconds (January 2038). Beyond it, the counter wraps negative (overflow — L14 §14.3), which unpatched software will misinterpret — a width-choice bug waiting on the calendar.
</details>
