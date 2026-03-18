import httpx
from typing import Any, Dict, Optional

class OpentronsAuthClient:
    """
    Synchronous client for the Opentrons Auth Server API.
    Handles OAuth2 authentication, user management, and system settings.
    """

    def __init__(self, base_url: str = "http://localhost:31950"):
        self.base_url = base_url.rstrip("/")
        self.client = httpx.Client(base_url=self.base_url)
        self.token: Optional[str] = None

    def close(self):
        """Close the underlying HTTP client session."""
        self.client.close()

    def _get_headers(self, requires_auth: bool = True) -> Dict[str, str]:
        """Helper to construct headers with the Bearer token if required."""
        headers = {"Accept": "application/json"}
        if requires_auth and self.token:
            headers["Authorization"] = f"Bearer {self.token}"
        return headers

    # --- OAuth2 Endpoints ---

    def get_token(self, username: str, password: str) -> Dict[str, Any]:
        """
        The OAuth 2 token endpoint (RFC 6749).
        Exchanges credentials for a token and stores it in the client.
        """
        data = {
            "grant_type": "password_credentials",
            "username": username,
            "password": password,
            "scope": "auth_settings.write protocols.write restart.write robot_control.write robot_settings.write run_data.write ssh_keys.write updates.write users.read users.write"
        }
        # OAuth2 token requests typically use form-encoded data
        response = self.client.post("/auth/oauth2/token", data=data, headers=self._get_headers(requires_auth=False))
        response.raise_for_status()
        
        token_data = response.json()
        self.token = token_data.get("access_token")
        return token_data

    def introspect_token(self, token_to_check: str) -> Dict[str, Any]:
        """The OAuth 2 token introspection endpoint (RFC 7662)."""
        response = self.client.post(
            "/auth/oauth2/introspect", 
            data={"token": token_to_check}, 
            headers=self._get_headers()
        )
        response.raise_for_status()
        return response.json()

    # --- Settings Endpoints ---

    def get_settings(self) -> Dict[str, Any]:
        """Get the current authorization and authentication settings."""
        response = self.client.get("/auth/settings", headers=self._get_headers(requires_auth=False))
        response.raise_for_status()
        return response.json()

    def update_settings(self, access_control_enabled: bool) -> Dict[str, Any]:
        """Change authorization and authentication settings. Returns the new settings."""
        payload = {"data": {"accessControlEnabled": access_control_enabled}}
        response = self.client.patch("/auth/settings", json=payload, headers=self._get_headers())
        response.raise_for_status()
        return response.json()

    def reset_settings(self) -> Dict[str, Any]:
        """Reset authorization and authentication settings to their defaults."""
        response = self.client.delete("/auth/settings", headers=self._get_headers())
        response.raise_for_status()
        return response.json()

    # --- User Management Endpoints ---

    def create_user(self, user_name: str, password: str, full_name: str, account_type: str = "user") -> Dict[str, Any]:
        """Create a new user."""
        payload = {
            "data": {
                "userName": user_name,
                "password": password,
                "fullName": full_name,
                "accountType": account_type
            }
        }
        response = self.client.post("/auth/users", json=payload, headers=self._get_headers())
        response.raise_for_status()
        return response.json()

    def get_user(self, user_name: str) -> Dict[str, Any]:
        """Get a specific user by its unique identifier."""
        response = self.client.get(f"/auth/users/{user_name}", headers=self._get_headers())
        response.raise_for_status()
        return response.json()

    def update_user(self, user_name: str, **kwargs) -> Dict[str, Any]:
        """Update a specific user. Pass fields like password, fullName, accountType as kwargs."""
        payload = {"data": kwargs}
        response = self.client.patch(f"/auth/users/{user_name}", json=payload, headers=self._get_headers())
        response.raise_for_status()
        return response.json()

    def delete_user(self, user_name: str) -> None:
        """Delete a specific user by its unique identifier."""
        response = self.client.delete(f"/auth/users/{user_name}", headers=self._get_headers())
        response.raise_for_status()