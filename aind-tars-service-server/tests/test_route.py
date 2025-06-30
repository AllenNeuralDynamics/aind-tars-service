"""Test routes"""

from typing import Any, Dict, List
from unittest.mock import MagicMock, call, patch

import pytest
from azure.core.credentials import AccessToken
from fastapi.testclient import TestClient

from aind_tars_service_server.configs import Settings
from aind_tars_service_server.route import (
    get_access_token,
)


@pytest.mark.asyncio
class TestRoutes:
    """Test responses in route module."""

    async def test_get_health(self, client: TestClient):
        """Tests a good response for healthcheck"""
        response = client.get("/healthcheck")
        assert 200 == response.status_code
        assert "OK" == response.json()["status"]

    @patch("aind_tars_service_server.route.ClientSecretCredential")
    async def test_get_access_token(self, mock_azure_credentials: MagicMock):
        """Tests get_access_token method"""
        mock_azure_credentials.return_value.get_token.return_value = (
            AccessToken(token="abc", expires_on=100)
        )
        token = await get_access_token(settings=Settings())
        mock_azure_credentials.assert_has_calls(
            [
                call(
                    tenant_id="tenant_id",
                    client_id="client_id",
                    client_secret="client_secret",
                ),
                call().get_token("http://example.com/scope"),
            ]
        )
        assert "abc" == token

    @patch("aind_tars_service_server.route.get_access_token")
    @patch("aind_tars_service_server.handler.SessionHandler.get_data")
    async def test_get_viral_prep_lot(
        self,
        mock_get_data: MagicMock,
        mock_get_access_token: MagicMock,
        client: TestClient,
        mock_prep_lot_data: List[Dict[str, Any]],
    ):
        """Tests get_viral_prep_lot route with successful response"""
        mock_get_access_token.return_value = "abc123"
        mock_get_data.return_value = mock_prep_lot_data

        response = client.get("/viral_prep_lots/VT3214g")

        assert 200 == response.status_code
        assert len(response.json()) == 1
        mock_get_access_token.assert_called_once()

    @patch("aind_tars_service_server.route.get_access_token")
    @patch("aind_tars_service_server.handler.SessionHandler.get_data")
    async def test_get_virus(
        self,
        mock_get_data: MagicMock,
        mock_get_access_token: MagicMock,
        client: TestClient,
        mock_virus_data: List[Dict[str, Any]],
    ):
        """Tests get_viral_prep_lot route with successful response"""
        mock_get_access_token.return_value = "abc123"
        mock_get_data.return_value = mock_virus_data

        response = client.get("/viruses/VIR300002_PHPeB")

        assert 200 == response.status_code
        assert len(response.json()) == 1
        mock_get_access_token.assert_called_once()

    @patch("aind_tars_service_server.route.get_access_token")
    @patch("aind_tars_service_server.handler.SessionHandler.get_data")
    async def test_get_molecules(
        self,
        mock_get_data: MagicMock,
        mock_get_access_token: MagicMock,
        client: TestClient,
        mock_molecule_data: List[Dict[str, Any]],
    ):
        """Tests get_viral_prep_lot route with successful response"""
        mock_get_access_token.return_value = "abc123"
        mock_get_data.return_value = mock_molecule_data

        response = client.get("/molecules/AiP1109")

        assert 200 == response.status_code
        assert len(response.json()) == 1
        mock_get_access_token.assert_called_once()


if __name__ == "__main__":
    pytest.main([__file__])
