"""Tests for handler module"""

from unittest.mock import MagicMock

import pytest
from requests import Response

from aind_tars_service_server.configs import Settings
from aind_tars_service_server.handler import SessionHandler
from aind_tars_service_server.models import (
    MoleculeData,
    MoleculeResponse,
    PrepLotData,
    PrepLotResponse,
    Virus,
    VirusResponse,
)


class TestSessionHandler:
    """Test SessionHandler"""

    def test_sanitize_input(self):
        """Tests _sanitize_input method strips whitespaces"""
        output_str = SessionHandler._sanitize_input(" ABC123\t\n")
        assert output_str == "ABC123"

    def test_get_raw_prep_lot_response(self):
        """Tests _get_raw_prep_lot_response method"""
        # Create mock response directly for raw response check
        mock_response = MagicMock(spec=Response)
        mock_response.json.return_value = {
            "data": [
                {"lot": "VT3214g", "datePrepped": "2023-02-04T00:00:00Z"}
            ],
            "search": "VT3214g",
            "searchFields": "lot",
            "totalCount": 1,
            "pageSize": 1,
        }

        mock_session = MagicMock()
        mock_session.get.return_value = mock_response
        handler = SessionHandler(
            session=mock_session,
            bearer_token="abc-123",
            settings=Settings(),
        )
        response = handler._get_raw_prep_lot_response(
            prep_lot_id="VT3214g", page_size=1
        )
        mock_session.get.assert_called_once()
        args, kwargs = mock_session.get.call_args

        assert "ViralPrepLots" in kwargs["url"]
        assert kwargs["params"]["search"] == "VT3214g"
        assert kwargs["params"]["searchFields"] == "lot"
        assert kwargs["params"]["pageSize"] == "1"
        assert isinstance(response, Response)
        response_json = response.json()
        assert response_json["search"] == "VT3214g"
        assert response_json["searchFields"] == "lot"

    def test_get_prep_lot_response(self, mock_get_raw_prep_lot_response):
        """Tests _get_prep_lot_response method when 200 response returned"""
        handler = SessionHandler(
            session=MagicMock(fetch=mock_get_raw_prep_lot_response),
            bearer_token="abc-123",
            settings=Settings(),
        )
        response = handler._get_prep_lot_response(prep_lot_id="VT3214g")
        assert isinstance(response, PrepLotResponse)
        assert len(response.data) >= 0
        print(response.data)

    def test_get_prep_lot_data(self, mock_get_raw_prep_lot_response):
        """Tests get_prep_lot_data method"""
        handler = SessionHandler(
            session=MagicMock(fetch=mock_get_raw_prep_lot_response),
            bearer_token="abc-123",
            settings=Settings(),
        )
        data = handler.get_prep_lot_data(prep_lot_id="VT3214g")
        assert isinstance(data, list)
        if len(data) > 0:
            assert isinstance(data[0], PrepLotData)

    def test_get_raw_molecule_response(self):
        """Tests _get_raw_molecule_response method"""
        mock_response = MagicMock(spec=Response)
        mock_response.json.return_value = {
            "search": "AiP1109",
            "searchFields": "name",
        }

        mock_session = MagicMock()
        mock_session.get.return_value = mock_response

        handler = SessionHandler(
            session=mock_session,
            bearer_token="abc-123",
            settings=Settings(),
        )

        _ = handler._get_raw_molecule_response(plasmid_name="AiP1109")
        mock_session.get.assert_called_once()
        args, kwargs = mock_session.get.call_args

        assert "Molecules" in kwargs["url"]
        assert kwargs["params"]["search"] == "AiP1109"
        assert kwargs["params"]["searchFields"] == "name"

    def test_get_molecule_response(self, mock_get_raw_molecule_response):
        """Tests _get_molecule_response method"""
        handler = SessionHandler(
            session=MagicMock(fetch=mock_get_raw_molecule_response),
            bearer_token="abc-123",
            settings=Settings(),
        )
        response = handler._get_molecule_response(plasmid_name="AiP1109")
        assert isinstance(response, MoleculeResponse)
        assert len(response.data) >= 0

    def test_get_molecule_data(self, mock_get_raw_molecule_response):
        """Tests get_molecule_data method"""
        handler = SessionHandler(
            session=MagicMock(fetch=mock_get_raw_molecule_response),
            bearer_token="abc-123",
            settings=Settings(),
        )
        data = handler.get_molecule_data(plasmid_name="AiP1109")
        assert isinstance(data, list)
        if len(data) > 0:
            assert isinstance(data[0], MoleculeData)

    def test_get_raw_virus_response(self):
        """Tests _get_raw_virus_response method"""
        mock_response = MagicMock(spec=Response)
        mock_response.json.return_value = {
            "search": "VIR300002_PHPeB",
            "searchFields": "aliases.name",
        }

        mock_session = MagicMock()
        mock_session.get.return_value = mock_response

        handler = SessionHandler(
            session=mock_session,
            bearer_token="abc-123",
            settings=Settings(),
        )

        _ = handler._get_raw_virus_response(virus_name="VIR300002_PHPeB")
        mock_session.get.assert_called_once()
        args, kwargs = mock_session.get.call_args

        assert "Viruses" in kwargs["url"]
        assert kwargs["params"]["search"] == "VIR300002_PHPeB"
        assert kwargs["params"]["searchFields"] == "aliases.name"

    def test_get_virus_response(self, mock_get_raw_virus_response):
        """Tests _get_virus_response method"""
        handler = SessionHandler(
            session=MagicMock(fetch=mock_get_raw_virus_response),
            bearer_token="abc-123",
            settings=Settings(),
        )
        response = handler._get_virus_response(virus_name="VIR300002_PHPeB")
        assert isinstance(response, VirusResponse)
        assert len(response.data) >= 0

    def test_get_virus_data(self, mock_get_raw_virus_response):
        """Tests get_virus_data method"""
        handler = SessionHandler(
            session=MagicMock(fetch=mock_get_raw_virus_response),
            bearer_token="abc-123",
            settings=Settings(),
        )
        data = handler.get_virus_data(virus_name="VIR300002_PHPeB")
        assert isinstance(data, list)
        if len(data) > 0:
            assert isinstance(data[0], Virus)


if __name__ == "__main__":
    pytest.main([__file__])
