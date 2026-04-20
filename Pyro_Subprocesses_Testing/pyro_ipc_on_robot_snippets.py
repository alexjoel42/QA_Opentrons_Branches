#!/usr/bin/env python3
"""
On-robot Pyro / protocol-subprocess QA helpers (httpx + commented shell).

Env (same idea as Auth_Testing_Example/no_auth_just_HTTP_API.py):
  ROBOT_BASE_URL  e.g. http://192.168.1.10:31950
  ROBOT_IP        used if ROBOT_BASE_URL unset (default 192.168.0.1)

Summary
  Goal                         On-robot approach
  Pyro/subprocess path         App or POST /protocols + POST /runs, enableProtocolSubprocess ON
  Server alive after faults    curl /health loop  ->  poll_health() below
  Evidence                     journalctl -u opentrons-robot-server (see comments)
  Raw motion (orthogonal)      opentrons_execute over SSH (not App/server subprocess path)
  Regression vs old path       Same protocol, flag OFF vs ON; compare time + logs
"""

from __future__ import annotations

import json
import os
import sys
import time
from pathlib import Path
from typing import Any

import httpx

# --- 1. Liveness / recovery (server wedging, zombie runs) ---


def _base_url() -> str:
    base = (os.environ.get("ROBOT_BASE_URL") or "").strip()
    if base:
        return base.rstrip("/")
    ip = (os.environ.get("ROBOT_IP") or "192.168.0.1").strip()
    return f"http://{ip}:31950"


def _robot_json_headers(*, opentrons_version: str = "*") -> dict[str, str]:
    """JSON bodies (POST /runs, /actions). Do not attach Content-Type to the Client used for multipart /protocols."""
    return {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Opentrons-Version": opentrons_version,
    }


def poll_health(
    *,
    interval_s: float = 5.0,
    prefix_utc: bool = True,
    max_chars: int = 200,
) -> None:
    """
    Mirrors integration RobotClient.get_health(): GET /health under load / after cancel / kill -9 / E-stop.

    Bash equivalent (from laptop):
      ROBOT_IP=192.168.x.x   # replace
      while true; do
        date -u
        curl -fsS "http://${ROBOT_IP}:31950/health" | head -c 200
        echo
        sleep 5
      done
    """
    base = _base_url()
    hdr = {"Accept": "application/json"}
    with httpx.Client(base_url=base, headers=hdr, timeout=30.0) as client:
        while True:
            if prefix_utc:
                print(time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), flush=True)
            r = client.get("/health")
            body = r.text[:max_chars] + ("…" if len(r.text) > max_chars else "")
            print(f"{r.status_code} {body}", flush=True)
            time.sleep(interval_s)


# --- 2. Logs on robot OS (commented — run over SSH) ---
#
# Gap: real IPC + ordering + operational errors mocks do not surface.
#
#   journalctl -u opentrons-robot-server -f --no-pager | rg -i 'pyro|protocol|subprocess|serpent|nameserver|traceback'
#   # or without rg:
#   journalctl -u opentrons-robot-server -n 500 --no-pager


# --- 3. opentrons_execute on robot (commented — orthogonal to App/server subprocess path) ---
#
#   ssh robot
#   opentrons_execute /data/my_protocol.py
#
# Docs: Python API CLI (advanced-control/command-line.md). Use for bare-metal motion;
# for Pyro IPC in App → robot-server → run, prefer POST /protocols + POST /runs or the App.


# --- 4. HTTP API run (same path as App when subprocess enabled on Flex) ---


def upload_protocol(
    client: httpx.Client,
    protocol_file: Path,
    *,
    protocol_kind: str = "standard",
    opentrons_version: str = "*",
) -> dict[str, Any]:
    """POST /protocols (multipart). Pattern matches Auth_Template.upload_protocol."""
    with protocol_file.open("rb") as fh:
        files = [("files", (protocol_file.name, fh))]
        data: dict[str, str] = {"protocol_kind": protocol_kind}
        r = client.post(
            "/protocols",
            headers={
                "Accept": "application/json",
                "Opentrons-Version": opentrons_version,
            },
            files=files,
            data=data,
            timeout=120.0,
        )
    r.raise_for_status()
    return r.json()


def create_run_for_protocol(
    client: httpx.Client,
    protocol_id: str,
    *,
    opentrons_version: str = "*",
) -> dict[str, Any]:
    """POST /runs with protocolId (RobotClient-style)."""
    payload = {"data": {"protocolId": protocol_id}}
    r = client.post(
        "/runs",
        json=payload,
        headers=_robot_json_headers(opentrons_version=opentrons_version),
        timeout=60.0,
    )
    r.raise_for_status()
    return r.json()


def play_run(
    client: httpx.Client,
    run_id: str,
    *,
    opentrons_version: str = "*",
) -> dict[str, Any]:
    """POST /runs/{id}/actions — start execution (typical after create)."""
    payload = {"data": {"actionType": "play"}}
    r = client.post(
        f"/runs/{run_id}/actions",
        json=payload,
        headers=_robot_json_headers(opentrons_version=opentrons_version),
        timeout=60.0,
    )
    r.raise_for_status()
    return r.json()


def upload_protocol_create_run_and_play(
    protocol_path: str | Path,
    *,
    opentrons_version: str = "*",
    do_play: bool = True,
) -> dict[str, Any]:
    """
    End-to-end: upload → create run → optional play.

    If access control is on, add Bearer tokens to the same routes (see Auth_Testing_Example/Auth_Template.py).

    curl sketch (headers/auth per your site; structure is the canonical bit):
      curl -fsS -X POST "http://$ROBOT_IP:31950/protocols" -H 'Opentrons-Version: *' ...multipart...
      curl -fsS -X POST "http://$ROBOT_IP:31950/runs" -H 'Content-Type: application/json' -H 'Opentrons-Version: *' \\
        -d '{\"data\":{\"protocolId\":\"<id>\"}}'
    """
    path = Path(protocol_path)
    base = _base_url()
    out: dict[str, Any] = {"base_url": base}
    # No default Content-Type: multipart POST /protocols must set boundary itself.
    with httpx.Client(base_url=base, timeout=120.0) as c:
        uploaded = upload_protocol(c, path, opentrons_version=opentrons_version)
        out["upload_response"] = uploaded
        pid = (uploaded.get("data") or {}).get("id")
        if not pid:
            raise RuntimeError(f"Unexpected POST /protocols response: {uploaded}")
        run = create_run_for_protocol(c, pid, opentrons_version=opentrons_version)
        out["run_response"] = run
        rid = (run.get("data") or {}).get("id")
        if not rid:
            raise RuntimeError(f"Unexpected POST /runs response: {run}")
        if do_play:
            out["play_response"] = play_run(c, rid, opentrons_version=opentrons_version)
        out["protocol_id"] = pid
        out["run_id"] = rid
    return out


# --- 5. Feature-flag A/B (manual — no code substitute) ---
#
# Same QA protocol, enableProtocolSubprocess OFF vs ON (Flex internal setting).
# Compare: time to start, wall time, App run state, journalctl noise.
# CI cannot reproduce 24s eager subprocess vs production scheduling contention.


# --- 6. Fault injection (manual — supervision semantics) ---
#
# - Cancel from App or API mid-run → run ends; GET /health still OK; new run can start.
# - kill -9 protocol child (PID from ps/logs) → run fails; server stays up.
# - E-stop during motion → recovery, no permanent hang.
# Use poll_health() + journalctl as evidence; do not fully automate across sites.


# --- 7. Peripherals (hardware only for bandwidth/firmware timing) ---
#
# Camera, plate reader, stacker: run the same template protocols on deck, not in sim.
# See pyro_ipc_protocol_qa_*.plan.md P1 table.


def main() -> None:
    if len(sys.argv) < 2:
        print(
            "Usage:\n"
            "  python pyro_ipc_on_robot_snippets.py health [interval_seconds]\n"
            "  python pyro_ipc_on_robot_snippets.py run <path/to/protocol.py>\n",
            file=sys.stderr,
        )
        sys.exit(2)
    cmd = sys.argv[1].lower()
    if cmd == "health":
        interval = float(sys.argv[2]) if len(sys.argv) > 2 else 5.0
        poll_health(interval_s=interval)
    elif cmd == "run":
        if len(sys.argv) < 3:
            print("run requires a protocol file path", file=sys.stderr)
            sys.exit(2)
        result = upload_protocol_create_run_and_play(sys.argv[2])
        print(json.dumps(result, indent=2))
    else:
        print(f"Unknown command: {cmd}", file=sys.stderr)
        sys.exit(2)


if __name__ == "__main__":
    main()
