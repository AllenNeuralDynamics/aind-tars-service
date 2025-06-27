"""Tests session module"""

import pytest
from requests import Session

from aind_tars_service_server.session import get_session


class TestSession:
    """Test methods in Session Class"""

    def test_get_session(self):
        """Tests get_session method"""

        session = next(get_session())
        assert session is not None
        assert isinstance(session, Session)


if __name__ == "__main__":
    pytest.main([__file__])
