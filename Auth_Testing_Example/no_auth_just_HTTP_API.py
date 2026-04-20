#!/usr/bin/env python3
"""HTTP API (no auth): get currently attached pipettes.

Env:
- ROBOT_BASE_URL: e.g. http://10.14.19.73:31950
- ROBOT_IP: used if ROBOT_BASE_URL is not set (defaults to 10.14.19.73)
- PIPETTES_REFRESH: if "true", pass refresh=true to GET /pipettes (OT-2 only; default false)

Docs: https://docs.opentrons.com/http/api_reference.html#tag/Pipettes/operation/get_pipettes
"""

from __future__ import annotations

import json
import os

import httpx

def _robot_base_url() -> str:
    """
    Prefer explicit ROBOT_BASE_URL; otherwise build from ROBOT_IP.

    Default port 31950 matches robot-server HTTP API.
    """
    base = (os.environ.get("ROBOT_BASE_URL") or "").strip()
    if base:
        return base.rstrip("/")
    ip = (os.environ.get("ROBOT_IP") or "10.14.19.73").strip()
    return f"http://{ip}:31950"


BASE = _robot_base_url().rstrip("/")
PIPETTES_REFRESH = (os.environ.get("PIPETTES_REFRESH") or "false").strip().lower() in (
    "1",
    "true",
    "t",
    "yes",
    "y",
    "on",
)

HDR = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Opentrons-Version": "*",
}


def _print(title: str, payload: object) -> None:
    print(f"\n=== {title} ===\n{json.dumps(payload, indent=2)}")


def _try_get_json(client: httpx.Client, path: str, *, params: dict | None = None) -> dict:
    r = client.get(path, params=params)
    out: dict = {"path": path, "status_code": r.status_code, "params": params or {}}
    try:
        out["json"] = r.json()
    except Exception:
        out["text"] = r.text
    return out


def main() -> None:
    with httpx.Client(base_url=BASE, headers=HDR, timeout=120.0) as c:
        print(f"Target: {BASE}")
        path = "/pipettes"
        params = {"refresh": "true"} if PIPETTES_REFRESH else None
        _print(f"GET {path}", _try_get_json(c, path, params=params))


if __name__ == "__main__":
    main()
