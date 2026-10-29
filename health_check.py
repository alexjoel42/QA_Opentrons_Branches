from opentrons import protocol_api

metadata = {
    "protocolName": "Dump hardware serial numbers",
    "author": "QA",
    "description": (
        "On-robot: GET /health, /instruments, /pipettes, /modules and print serials. "
        "Uses requests against localhost:31950 (httpx is not on the robot)."
    ),
}

requirements = {
    "robotType": "Flex",
    "apiLevel": "2.28",
}

BASE_URL = "http://localhost:31950"
HEADERS = {
    "Accept": "application/json",
    "Opentrons-Version": "*",
}


def _get_json(path, *, quiet=False):
    """GET path on local robot-server; return parsed JSON or None."""
    import requests

    url = f"{BASE_URL}{path}"
    try:
        r = requests.get(url, headers=HEADERS, timeout=15)
    except requests.RequestException as e:
        if not quiet:
            print(f"GET {path} failed: {e}")
        return None
    if r.status_code != 200:
        if not quiet:
            print(f"GET {path} -> {r.status_code}: {r.text[:200]}")
        return None
    try:
        return r.json()
    except ValueError:
        if not quiet:
            print(f"GET {path} -> non-JSON body")
        return None


def _collect_lines():
    lines = []
    seen = set()

    def add(line, key=None):
        dedupe = key or line
        if not line or dedupe in seen:
            return
        seen.add(dedupe)
        lines.append(line)

    health = _get_json("/health")
    if health:
        for key in ("robot_serial", "serial", "serialNumber"):
            if health.get(key):
                add(f"robot: {health[key]}", key=f"robot:{health[key]}")
                break

    # Flex: /instruments (includes 96-channel on left, gripper on extension)
    instruments = _get_json("/instruments", quiet=True)
    if instruments:
        for item in instruments.get("data") or []:
            serial = item.get("serialNumber") or item.get("id")
            if not serial:
                continue
            mount = item.get("mount") or "?"
            kind = (item.get("instrumentType") or "instrument").lower()
            model = item.get("instrumentModel") or item.get("instrumentName") or ""
            if kind in ("pipette", "gripper"):
                label = f"{mount}"
                if model:
                    label = f"{mount} ({model})"
                add(f"{label}: {serial}", key=f"mount:{mount}")
            else:
                add(str(serial), key=f"instrument:{serial}")

    # OT-2 style /pipettes (also useful as fallback)
    pipettes = _get_json("/pipettes", quiet=True)
    if pipettes:
        for mount in ("left", "right"):
            info = pipettes.get(mount)
            if not isinstance(info, dict):
                continue
            serial = info.get("id") or info.get("serialNumber")
            if not serial:
                continue
            model = info.get("model") or info.get("name") or ""
            label = f"{mount}"
            if model:
                label = f"{mount} ({model})"
            add(f"{label}: {serial}", key=f"mount:{mount}")

    modules = _get_json("/modules")
    if modules:
        for item in modules.get("data") or []:
            serial = item.get("serialNumber") or item.get("id")
            if not serial:
                continue
            model = item.get("moduleModel") or item.get("moduleType") or "module"
            add(f"{model}: {serial}", key=f"module:{serial}")

    return lines


def run(protocol: protocol_api.ProtocolContext):
    if protocol.is_simulating():
        protocol.comment("Simulation: skipping HTTP serial dump")
        return

    lines = _collect_lines()
    if not lines:
        protocol.comment("No serial numbers found")
        print("No serial numbers found")
        return

    protocol.comment("--- Hardware serial numbers ---")
    print("--- Hardware serial numbers ---")
    for line in lines:
        protocol.comment(line)
        print(line)
