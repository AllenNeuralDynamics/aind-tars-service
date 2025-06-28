"""Test routes"""

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
                call().get_token("scope"),
            ]
        )
        assert "abc" == token

    @patch("aind_tars_service_server.route.get_access_token")
    @patch("aind_tars_service_server.handler.SessionHandler.get_prep_lot_data")
    async def test_get_viral_prep_lot_200(
        self,
        mock_get_prep_lot_data: MagicMock,
        mock_get_access_token: MagicMock,
        client: TestClient,
        mock_get_raw_prep_lot_response: MagicMock,
    ):
        """Tests get_viral_prep_lot route with successful response"""
        mock_get_access_token.return_value = "abc123"
        mock_get_prep_lot_data.return_value = [
            {"lot": "VT3214g", "datePrepped": "2023-02-04T00:00:00Z"}
        ]

        response = client.get("/viral_prep_lot/VT3214g")

        assert 200 == response.status_code
        assert len(response.json()) >= 1
        mock_get_access_token.assert_called_once()
        mock_get_prep_lot_data.assert_called_once_with(prep_lot_id="VT3214g")

    @patch("aind_tars_service_server.route.get_access_token")
    @patch("aind_tars_service_server.handler.SessionHandler.get_molecule_data")
    async def test_get_molecule_data_200(
        self,
        mock_get_molecule_data: MagicMock,
        mock_get_access_token: MagicMock,
        client: TestClient,
        mock_get_raw_molecule_response: MagicMock,
    ):
        """Tests get_molecule_data route with successful response"""
        mock_get_access_token.return_value = "abc123"
        mock_get_molecule_data.return_value = [
            {
                "fullName": "pAAV-AiE2012m-minG-FlpO-WPRE-HGHpA",
                "sequence": "CATG",
            }
        ]

        response = client.get("/molecule/AiP1109")

        assert 200 == response.status_code
        assert len(response.json()) >= 1
        mock_get_access_token.assert_called_once()
        mock_get_molecule_data.assert_called_once_with(plasmid_name="AiP1109")

    @patch("aind_tars_service_server.route.get_access_token")
    @patch("aind_tars_service_server.handler.SessionHandler.get_virus_data")
    async def test_get_virus_data_200(
        self,
        mock_get_virus_data: MagicMock,
        mock_get_access_token: MagicMock,
        client: TestClient,
        mock_get_raw_virus_response: MagicMock,
    ):
        """Tests get_virus_data route with successful response"""
        mock_get_access_token.return_value = "abc123"
        mock_get_virus_data.return_value = [
            {
                "id": "virus-123",
                "aliases": [{"name": "AiV300024", "isPreferred": True}],
            }
        ]

        response = client.get("/virus/VIR300002_PHPeB")

        assert 200 == response.status_code
        assert len(response.json()) >= 1
        mock_get_access_token.assert_called_once()
        mock_get_virus_data.assert_called_once_with(
            virus_name="VIR300002_PHPeB"
        )


if __name__ == "__main__":
    pytest.main([__file__])
