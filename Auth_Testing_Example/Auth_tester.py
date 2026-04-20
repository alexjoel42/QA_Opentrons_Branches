import os
import sys
import httpx
from dotenv import load_dotenv
from Auth_Template import OpentronsAuthClient

# Load variables from the .env file into the standard os environment
load_dotenv()

def get_required_env_var(var_name: str) -> str:
    """Helper to fetch env vars and fail cleanly if they are missing."""
    value = os.getenv(var_name)
    if not value:
        print(f"❌ Error: Missing required environment variable '{var_name}' in .env file.")
        sys.exit(1) # Stops the script immediately
    return value

def main():
    # Fetch from .env securely
    ROBOT_IP = get_required_env_var("ROBOT_IP")
    
    # Initialize the client
    client = OpentronsAuthClient(base_url=ROBOT_IP)
    
    try:
        # 1. Check current settings (Does not require auth)
        print("--- Fetching Current Settings ---")
        current_settings = client.get_settings()
        print(f"Initial State: {current_settings['data']}")
    except httpx.HTTPStatusError as e:
        print(f"HTTP error occurred: {e.response.status_code} - {e.response.text}")
    except httpx.ConnectError:
        print("Connection error: Is the robot server running and accessible?")
    except Exception as e:  
        print(f"An unexpected error occurred: {e}")
    finally:
        client.close()

def user_flow_example():
    """
    Example flow for user management and settings update using strictly .env variables.
    """
    # Fetch variables securely with NO hardcoded fallbacks
    ROBOT_IP = get_required_env_var("ROBOT_IP")
    ADMIN_USER = get_required_env_var("ROBOT_ADMIN_USER")
    ADMIN_PASS = get_required_env_var("ROBOT_ADMIN_PASS")

    # Initialize the synchronous client
    client = OpentronsAuthClient(base_url=ROBOT_IP)
    
    try:
        # 1. Login to get token (Must be done BEFORE updating settings)
        print("\n--- Authenticating ---")
        client.get_token(ADMIN_USER, ADMIN_PASS) # Fixed the Ruff F841 warning here!
        print("Successfully authenticated and obtained Bearer token.")

        # 2. Check and update settings
        print("\n--- Checking Access Control ---")
        settings = client.get_settings()
        
        if settings['data'].get('accessControlEnabled') is True:
            print("Access control is already enabled.")
        else:
            print("Access control is currently disabled. Enabling it now...")
            updated_settings = client.update_settings(access_control_enabled=True)
            print(f"Updated Settings: {updated_settings['data']}")

        # 3. Create a new user
        print("\n--- Creating User ---")
        new_user = client.create_user("scientist_1", "secure_pass", "Jane Doe", "user")
        print(f"Created user: {new_user['data']['userName']}")

    except httpx.HTTPStatusError as e:
        print(f"\n❌ HTTP Error: {e.response.status_code}")
        print(f"Details: {e.response.text}")
    except httpx.ConnectError:
        print("\n❌ Connection error: Is the robot server running and accessible?")
    except Exception as e:
        print(f"\n❌ An unexpected error occurred: {e}")
    finally:
        # Always close the connection
        client.close()


def protocol_upload_example():
    """
    Authenticate, then upload a protocol via POST /protocols (multipart).

    Requires in .env: ROBOT_IP, ROBOT_ADMIN_USER, ROBOT_ADMIN_PASS, PROTOCOL_PATH
    Optional: PROTOCOL_LABWARE_PATHS — comma-separated paths to extra labware JSON files.
    """
    ROBOT_IP = get_required_env_var("ROBOT_IP")
    ADMIN_USER = get_required_env_var("ROBOT_ADMIN_USER")
    ADMIN_PASS = get_required_env_var("ROBOT_ADMIN_PASS")
    PROTOCOL_PATH = get_required_env_var("PROTOCOL_PATH")

    labware_raw = os.getenv("PROTOCOL_LABWARE_PATHS", "").strip()
    labware_paths = [p.strip() for p in labware_raw.split(",") if p.strip()] or None

    client = OpentronsAuthClient(base_url=ROBOT_IP)

    try:
        print("\n--- Authenticating ---")
        client.get_token(ADMIN_USER, ADMIN_PASS)
        print("Successfully authenticated and obtained Bearer token.")

        print("\n--- Uploading protocol ---")
        print(f"File: {PROTOCOL_PATH}")
        if labware_paths:
            print(f"Extra labware files: {labware_paths}")

        result = client.upload_protocol(
            PROTOCOL_PATH,
            labware_paths=labware_paths,
        )
        data = result.get("data", result)
        protocol_id = data.get("id") if isinstance(data, dict) else None
        if protocol_id:
            print(f"Uploaded protocol id: {protocol_id}")
        print(f"Response: {result}")

    except httpx.HTTPStatusError as e:
        print(f"\n❌ HTTP Error: {e.response.status_code}")
        print(f"Details: {e.response.text}")
    except httpx.ConnectError:
        print("\n❌ Connection error: Is the robot server running and accessible?")
    except OSError as e:
        print(f"\n❌ File error (check PROTOCOL_PATH): {e}")
    except Exception as e:
        print(f"\n❌ An unexpected error occurred: {e}")
    finally:
        client.close()


# --- EXECUTION BLOCK ---
if __name__ == "__main__":
    # Pick one: main() | user_flow_example() | protocol_upload_example()
    user_flow_example()
    # protocol_upload_example()