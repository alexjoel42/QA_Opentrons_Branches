import httpx
from Auth_Template import OpentronsAuthClient

def main():
    # Replace with your actual robot's IP address
    ROBOT_IP = "http://10.14.19.198:31950"
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
    Example flow for user management and settings update.
    Uncomment and run this function in an async context if you want to test user creation and settings update.
    """
    import asyncio

    async def flow():
        async with OpentronsAuthClient(base_url="http://10.14.19.198:31950") as client:
            # 1. Check settings publicly
            settings = await client.get_settings()
            if settings['data']['accessControlEnabled'] == True:
                print("Access control is already enabled.")

            else:
                print("Access control is currently disabled. Enabling it now...")
                updated_settings = await client.update_settings(access_control_enabled=True)
                print(f"Updated Settings: {updated_settings['data']}")


            # 2. Login to get token
            token_data = await client.get_token("admin", "password123")
            print(f"Obtained Token: {token_data['access_token']}")

            # 3. Create a new user
            new_user = await client.create_user("scientist_1", "secure_pass", "Jane Doe", "user")
            print(f"Created user: {new_user['data']['userName']}")


# --- ADD THESE TWO LINES ---
if __name__ == "__main__":
    user_flow_example()