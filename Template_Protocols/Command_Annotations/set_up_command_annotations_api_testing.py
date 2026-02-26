import httpx
import json
import sys

def set_step_grouping(base_url: str, enabled: bool = False):
    """
    Sets the allowStepGrouping setting on the local robot server.
    """
    url = f"{base_url}/settings"
    
    # Crucial: Opentrons-Version header is required by the robot-server
    headers = {"Opentrons-Version": "*"} 
    payload = {
        "id": "allowStepGrouping",
        "value": enabled
    }

    print(f"Sending POST to {url}...")
    
    try:
        with httpx.Client(headers=headers) as client:
            response = client.post(url, json=payload)
            
            if response.status_code == 200:
                print("✅ Success!")
                print(json.dumps(response.json(), indent=2))
            else:
                print(f"❌ Failed with status: {response.status_code}")
                print(f"Response text: {response.text}")
                
    except httpx.ConnectError:
        print("❌ Connection Error: Is your uvicorn server running on localhost:31950?")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Your uvicorn logs showed port 31950
    DEV_SERVER_URL = "http://localhost:31950"
    set_step_grouping(DEV_SERVER_URL, enabled=True)