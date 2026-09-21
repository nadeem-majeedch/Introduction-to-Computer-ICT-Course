---
quiz: Q07
covers: L09-L12 (cumulative)
---

# Practice Q07 — Module 3 Cumulative (L09–L12)

## Q1

Tell the Module 3 story in five sentences: software layers → OS role → files → installation hygiene → troubleshooting method.

<details>
<summary>Self-check</summary>

Software layers from applications down through OS, drivers, and firmware to hardware (L09). The OS manages processes, memory, devices, files, and the interface (L10). File systems map that management onto the tree of paths and folders users live in (L11). Installing safely and patching promptly keeps the whole stack trustworthy (L12 §12.1–12.2). When anything fails, the structured isolate-and-test loop turns panic into diagnosis (L12 §12.3).
</details>

## Q2

A driver update breaks printing. Which two Module 3 concepts explain both the failure and the safe fix?

<details>
<summary>Self-check</summary>

Drivers (L09) — the translation layer between OS and device; a bad update breaks translation. Troubleshooting method (L12) — isolate (does the printer appear? other apps print?) then roll back the driver via the cheapest tested step rather than reinstalling the OS.
</details>

## Q3

Why does the course make you *write* paths (L11) in a course that uses GUIs everywhere?

<details>
<summary>Self-check</summary>

Paths are the address scheme every later module assumes: terminal work (Labs 3, 7), URLs' path structure (L23), cloud consoles and file stores (L24), and error messages that always name paths. GUIs hide the scheme; reading it is literacy, not nostalgia.
</details>

## Q4

Classify each permission red flag (L12 §12.1): a torch app requesting contacts; a map app requesting location; a PDF reader requesting microphone.

<details>
<summary>Self-check</summary>

Torch+contacts: red flag (no plausible purpose — data harvesting). Map+location: aligned with function (permission matches purpose). PDF reader+microphone: red flag (reading files needs no audio; purpose mismatch). The test is *purpose alignment*, per minimum-collection thinking (L26/L30 preview).
</details>

## Q5

You must hand a shared lab PC to next semester's student. Using Module 3 only, outline your sanitisation steps and one thing they *cannot* easily fix.

<details>
<summary>Self-check</summary>

Remove your accounts/data (deactivate, delete profile), uninstall personal software, check for synced credentials (browser accounts), factory-reset where supported. Cannot easily fix: remnants on storage below the OS (deleted-file recoverability, L11's misconception) — hence institutional wiping/disk-encryption standards, which is the real answer to hand over.
</details>
