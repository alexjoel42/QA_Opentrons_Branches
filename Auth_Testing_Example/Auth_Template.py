import json
import httpx
from pathlib import Path
from typing import Any, Dict, List, Optional

class OpentronsAuthClient:
    """
    Please reference the OpenAPI spec for the Opentrons Auth Server API to understand the available endpoints and their expected request/response formats.
    See the following URLs for more details:
    http://robot_ip:31950/openapi.json 

    http://robot_ip:31950/auth/openapi.json

    http://robot_ip:31950/system/openapi.json

    http://robot_ip:31950/update_server/openapi.json
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

    def _robot_api_headers(
        self, requires_auth: bool = True, opentrons_version: str = "*"
    ) -> Dict[str, str]:
        """Headers for main robot HTTP API routes (e.g. /protocols). Requires Opentrons-Version."""
        headers: Dict[str, str] = {
            "Accept": "application/json",
            "Opentrons-Version": opentrons_version,
        }
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

    # --- Robot HTTP API: protocols (see https://docs.opentrons.com/http/api_reference.html) ---

    def upload_protocol(
        self,
        protocol_path: str,
        *,
        labware_paths: Optional[List[str]] = None,
        protocol_kind: str = "standard",
        key: Optional[str] = None,
        run_time_parameter_values: Optional[Dict[str, Any]] = None,
        run_time_parameter_files: Optional[str] = None,
        requires_auth: bool = True,
        opentrons_version: str = "*",
        timeout: float = 120.0,
    ) -> Dict[str, Any]:
        """
        Upload a protocol via POST /protocols (multipart/form-data).

        Send one Python or JSON protocol file as ``protocol_path``; optional custom labware
        JSON files via ``labware_paths``. When access control is enabled, call ``get_token``
        first so ``protocols.write`` is authorized.

        ``run_time_parameter_values`` is sent as a JSON string in the form field, per API spec.
        """
        paths: List[str] = [protocol_path]
        if labware_paths:
            paths.extend(labware_paths)

        file_handles: List[Any] = []
        try:
            multipart_files: List[tuple] = []
            for p in paths:
                path = Path(p)
                fh = path.open("rb")
                file_handles.append(fh)
                multipart_files.append(("files", (path.name, fh)))

            data: Dict[str, str] = {"protocol_kind": protocol_kind}
            if key is not None:
                data["key"] = key
            if run_time_parameter_values is not None:
                data["run_time_parameter_values"] = json.dumps(run_time_parameter_values)
            if run_time_parameter_files is not None:
                data["run_time_parameter_files"] = run_time_parameter_files

            response = self.client.post(
                "/protocols",
                headers=self._robot_api_headers(
                    requires_auth=requires_auth, opentrons_version=opentrons_version
                ),
                files=multipart_files,
                data=data,
                timeout=timeout,
            )
            response.raise_for_status()
            return response.json()
        finally:
            for fh in file_handles:
                fh.close()