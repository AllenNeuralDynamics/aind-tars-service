"""Tests configs module"""

import os
import unittest
from unittest.mock import patch

from aind_tars_service_server.configs import Settings


class TestSettings(unittest.TestCase):
    """Test methods in Settings Class"""

    @patch.dict(
        os.environ,
        {
            "TARS_TENANT_ID": "tenant_id",
            "TARS_CLIENT_ID": "client_id",
            "TARS_CLIENT_SECRET": "client_secret",
            "TARS_SCOPE": "scope",
            "TARS_RESOURCE": "resource",
        },
        clear=True,
    )
    def test_get_settings(self):
        """Tests settings can be set via env vars"""
        settings = Settings()
        expected_settings = Settings(
            tenant_id="tenant_id",
            client_id="client_id",
            client_secret="client_secret",
            scope="scope",
            resource="resource",
        )
        self.assertEqual(expected_settings, settings)


if __name__ == "__main__":
    unittest.main()
