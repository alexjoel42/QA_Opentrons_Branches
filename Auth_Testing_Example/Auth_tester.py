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
        print("--- Fetching Current Settings ---")[-]
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

# --- EXECUTION BLOCK ---
if __name__ == "__main__":
    # You can call main() or user_flow_example() here depending on what you want to test!
    user_flow_example()