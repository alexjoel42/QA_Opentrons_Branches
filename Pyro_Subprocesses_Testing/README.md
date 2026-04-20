# Pyro / protocol-subprocess QA (this folder)

This folder tracks **manual and protocol-driven validation** for the Opentrons Flex path where user protocol code runs in a **separate process** and talks to robot-server over **Pyro-style IPC**. The product question is: *does real user code, peripherals, and run lifecycle behave correctly across that boundary—not only in unit tests?*

---

## What we are trying to prove (feature level)

| Area | Why it matters | What “good” looks like | Typical gap if weak |
|------|----------------|-------------------------|---------------------|
| **Serialization / type registry** | Objects (commands, liquids, module handles, results) cross the protocol ↔ server boundary; bad types can **crash, error, or silently corrupt** after round-trip | Long and varied protocols complete; App/run state matches expectations; no mystery wrong motion or wrong numbers | Failures only on odd workloads; sim passes but hardware fails on large or weird types |
| **Run lifecycle** | Subprocess path must create, run, stop, and clean up runs reliably | Cancel ends run cleanly; new run can start; no stuck “running” in App | Zombie runs, server wedged, or run queue confusion after cancel / fault |
| **Throughput & scheduling** | Subprocess startup and real hardware contention differ from CI | **Same protocol** with flag OFF vs ON: acceptable time-to-start and wall time; stable over **N repeats** | Only happy-path tested once; surprises under load (e.g. eager subprocess cost vs production scheduling) |
| **Peripherals & large payloads** | Camera, plate reader, stackers, TC lids stress **bigger RPC payloads and timing** than pipette-only smokes | Devices complete; CSV/exports legible; no chronic timeouts vs baseline | Mock/sim-only validation; bandwidth or firmware timing bugs on real hardware |
| **Resilience** | Field robots see faults | After **E-stop**, **kill -9** on protocol child, or **mid-run cancel**, robot-server **stays up** and `/health` stays healthy; logs explain failure | “Works until it doesn’t”—hangs, orphaned runs, or opaque logs under fault |

---

## How this splits from automated CI

- **CI** is strong on correctness of many surfaces but **cannot** replace: 24/7 scheduling contention, real USB/CAN/device timing, or “server still alive” under faults.
- **On-robot** work here combines: (1) **template protocols** elsewhere in `QA_Opentrons_Branches/Template_Protocols/` (see the plan file), (2) **this folder’s** dedicated stress script and HTTP helpers, and (3) **manual** checks (health loop, `journalctl`, optional `opentrons_execute` as an orthogonal motion check—not the App subprocess path).

---

## What’s in this folder

| Artifact | Audience | Purpose |
|----------|-----------|---------|
| [`pyro_ipc_protocol_qa_b47a1b1c.plan.md`](pyro_ipc_protocol_qa_b47a1b1c.plan.md) | QA + eng | P0 / P1 / P2 **protocol matrix** (what to run from templates and why); serialization note; environment matrix (flag ON/OFF, sim vs HW). |
| [`lots_of_camera_pyro.py`](lots_of_camera_pyro.py) | HW run | **Single Flex protocol** stressing camera volume, gripper, temperature module concurrent tasks, on-robot CSV I/O, and plate reader single→multi—in one repeatable file. |
| [`pyro_ipc_on_robot_snippets.py`](pyro_ipc_on_robot_snippets.py) | Field / automation | **httpx** helpers: `GET /health` loop, `POST /protocols` + `POST /runs` (+ play)—same structural idea as the App; comments for `journalctl`, SSH, and fault-injection **evidence**. |

---

## Priority snapshot (aligned with the plan)

- **P0 — Release gate:** Short Flex smokes, RTP-heavy and command-heavy templates, cancel/crash behavior, subprocess ON.

- **P1 — Peripherals:** Camera-heavy, plate reader (including error paths), TC lid / stacker smokes—on **real** hardware.

- **P2 — PD / analysis / viz:** PD-sourced and command-annotation-heavy protocols; compare outputs to baseline when subprocess is ON.

- **Explicit non-protocol gates:** E-stop during motion, `kill -9` on protocol subprocess, REPL/threading edge cases—these are **manual or separate harnesses**, not replaced by normal `run()` protocols.

---

## For managers: quick “gap finder”

Use this list to see what is **not** fully covered if the only thing executed was a short smoke or sim run.

- **Flag A/B:** Same representative protocol with **enableProtocolSubprocess OFF vs ON** (time, stability, logs) not compared.
- **Faults:** No **cancel mid-run**, **E-stop**, or **process kill** evidence paired with **`/health`** and **`journalctl`**.
- **Soak:** No **multi-repeat** or long **camera / command-list** stress on hardware.
- **Peripherals:** No **camera / plate reader / stacker / TC** runs on a real deck (bandwidth and timing).
- **Server vs CLI:** Only **`opentrons_execute`** on device was run (moves motors but **not** the App ⇄ robot-server ⇄** subprocess** path).
- **Analysis:** PD/run export or internal tooling not compared to a **baseline** with subprocess ON.

If any row in the first table is “unknown” for your release candidate, treat it as a **coverage gap** until addressed with the approaches in this folder and the plan.
