---
quiz: Q09
covers: L15-L16
---

# Practice Q09 — L15–L16 (Character Encoding · Multimedia)

## Q1

State the ASCII codes for `A`, `a`, `0` and explain the design intent behind the gaps between them.

<details>
<summary>Self-check</summary>

`A`=65, `a`=97, `0`=48. Gaps are deliberate: lowercase = uppercase + 32 (case-folding becomes a single bit/offset operation), digits sit at 48–57 so the low nibble *is* the digit value (numeric conversion is a mask away).
</details>

## Q2

Your file shows `Ã©` where `é` belongs. Diagnose precisely: what bytes, what misread, what fix?

<details>
<summary>Self-check</summary>

`é` in UTF-8 is the two bytes `0xC3 0xA9`; the file was *displayed as Latin-1* (1 byte = 1 char), so `0xC3`→`Ã`, `0xA9`→`©`. The bytes are intact — re-decode the file as UTF-8 (and declare UTF-8 in the editor/HTML going forward).
</details>

## Q3

Why is a PNG preferred for screenshots while JPEG wins for photos? Answer with the lossy/lossless logic.

<details>
<summary>Self-check</summary>

Screenshots are flat colour, sharp edges, text — lossy JPEG's block/prediction artefacts *damage exactly those* (ringing around text). JPEG's trick (discard imperceptible detail) suits continuous-tone photos where the eye can't see the loss. Lossless preserves what's already simple; lossy compresses what's already complex.
</details>

## Q4

Compute raw size: 44,100 samples/s × 16 bits × 2 channels × 60 s. Give bytes and MB (one decimal).

<details>
<summary>Self-check</summary>

44,100 × 16 = 705,600 bits/s per channel → ×2 = 1,411,200 bits/s → ×60 = 84,672,000 bits = 10,584,000 bytes ≈ **10.6 MB** (or ~10.1 MiB). This is why CDs hold ~74–80 min uncompressed and why lossy codecs matter for streaming.
</details>

## Q5

Your logo must scale from a 16-px favicon to a 3-m banner. Raster or vector — and what happens if you choose wrong?

<details>
<summary>Self-check</summary>

Vector (SVG): the file stores drawing instructions, so any scale re-renders sharply. Wrong choice (raster): upscaling interpolates pixels — blur/softness at banner size; you'd need multiple resolutions for each size. Photos have no vector option (too complex), which is why both formats coexist.
</details>
