---
quiz: Q11
covers: L19-L21
---

# Practice Q11 — L19–L21 (Productivity Tools · Networking)

## Q1

`=A1*$B$1` is copied two rows down and one column right. What does it become, and why?

<details>
<summary>Self-check</summary>

`=B3*$B$1`. Relative `A1` shifts with the copy (one right, two down → B3); absolute `$B$1` is pinned by the `$` signs (column *and* row locked). The mix is exactly how you build "each row × one fixed rate" tables.
</details>

## Q2

Write the IF formula: "Low" below 40, "OK" 40–69, "High" 70+.

<details>
<summary>Self-check</summary>

`=IF(B2<40,"Low",IF(B2<70,"OK","High"))` — nested IFs read top-down; the *order* matters (checking <70 after <40 means only 40–69 reaches it). Equivalent with ranges, wrong with reordered conditions — order and boundary logic is the real lesson.
</details>

## Q3

Which chart for "monthly rainfall across one year," and why is a pie chart wrong here?

<details>
<summary>Self-check</summary>

Line chart — the message is a *trend over ordered time*, which lines show and nothing else does as well. A pie shows parts of a *whole at one instant* (and 12 slices compare angles poorly); rainfall months are neither parts of a fixed whole nor few enough.
</details>

## Q4

Classify: Bluetooth keyboard link, university Wi-Fi, undersea cable network. Then name the device that joins the second to the third.

<details>
<summary>Self-check</summary>

PAN (personal, metres), LAN (local, building/campus), WAN (wide, regions/world). The **router** joins LAN to WAN (forwarding between networks by IP); the switch/AP stay inside the LAN.
</details>

## Q5

A video call stutters though speed tests show 200 Mbps. Bandwidth or latency — and which two home factors commonly cause it?

<details>
<summary>Self-check</summary>

Latency/jitter (and packet loss), not capacity — calls need *steady small packets in time*, not bulk throughput. Common causes: congested Wi-Fi (interference/distance — try wired), and bufferbloat on the home router under upload load. Speed tests measure bandwidth, which is why they pass while calls fail.
</details>
