#!/usr/bin/env python3
"""HTTP API Stress Test: Uncapped 2000 concurrent requests to Opentrons Flex."""

from __future__ import annotations
import os
import asyncio
import collections
import httpx

def _robot_base_url() -> str:
    base = (os.environ.get("ROBOT_BASE_URL") or "").strip()
    if base:
        return base.rstrip("/")
    ip = (os.environ.get("ROBOT_IP") or "10.14.19.194").strip()
    return f"http://{ip}:31950"

BASE = _robot_base_url()
HDR = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Opentrons-Version": "*",
}

stats = collections.Counter()

async def send_request(client: httpx.AsyncClient, request_id: int):
    """Sends a single request concurrently and tracks the outcome."""
    try:
        response = await client.get("health")
        stats[f"Status {response.status_code}"] += 1
        if request_id % 50 == 0:
            print(".", end="", flush=True)
    except httpx.PoolTimeout:
        stats["Error: Local Client Pool Timeout"] += 1
    except httpx.ConnectTimeout:
        stats["Error: Connection Timeout (Robot Handshake)"] += 1
    except httpx.ReadTimeout:
        stats["Error: Read Timeout (Robot took too long to reply)"] += 1
    except httpx.ConnectError:
        stats["Error: Connection Refused/Dropped by Robot"] += 1
    except Exception as e:
        stats[f"Error: {type(e).__name__}"] += 1

async def main():
    # Configure UNLIMITED concurrent connections locally
    unlimited_limits = httpx.Limits(max_connections=None, max_keepalive_connections=None)
    
    async with httpx.AsyncClient(
        base_url=BASE, 
        headers=HDR, 
        timeout=30.0, 
        limits=unlimited_limits
    ) as client:
        total_requests = 2000
        print(f"Target: {BASE}")
        print(f"Launching UNCAPPED flood attack of {total_requests} requests ", end="")
        
        tasks = [send_request(client, i) for i in range(total_requests)]
        await asyncio.gather(*tasks)
        
        print("\n\n=== STRESS TEST RESULTS ===")
        print(f"Total Requests Sent: {total_requests}")
        print("---------------------------")
        for outcome, count in stats.items():
            print(f"{outcome}: {count}")
        print("===========================")

if __name__ == "__main__":
    asyncio.run(main())