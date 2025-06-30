"""Tests for handler module"""

from unittest.mock import AsyncMock

import pytest

from aind_tars_service_server.handler import SessionHandler


@pytest.mark.asyncio
class TestSessionHandler:
    """Test SessionHandler"""

    async def test_get_data(self, mock_get_prep_lot_multiple_pages: AsyncMock):
        """Tests get_data method."""
        session_handler = SessionHandler(
            client=mock_get_prep_lot_multiple_pages
        )
        query_params = {
            "pageSize": str(2),
            "order": "1",
            "orderBy": "id",
            "searchFields": "lot",
            "search": "VT321",
        }
        result = await session_handler.get_data(
            url="http://example.com", params=query_params
        )
        assert 2 == len(mock_get_prep_lot_multiple_pages.mock_calls)
        assert len(result) == 3

    async def test_get_data_with_limit(
        self, mock_get_prep_lot_multiple_pages: AsyncMock
    ):
        """Tests get_data method when limit is set."""
        session_handler = SessionHandler(
            client=mock_get_prep_lot_multiple_pages
        )
        query_params = {
            "pageSize": str(2),
            "order": "1",
            "orderBy": "id",
            "searchFields": "lot",
            "search": "VT321",
        }
        result = await session_handler.get_data(
            url="http://example.com", params=query_params, limit=1
        )
        assert 1 == len(mock_get_prep_lot_multiple_pages.mock_calls)
        assert len(result) == 1


if __name__ == "__main__":
    pytest.main([__file__])
