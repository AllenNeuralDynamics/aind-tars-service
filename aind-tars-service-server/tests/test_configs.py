"""Tests configs module"""

import unittest

from aind_tars_service_server.configs import Settings


class TestSettings(unittest.TestCase):
    """Test methods in Settings Class"""

    def test_properties(self):
        """Tests properties get set properly"""
        settings = Settings(
            tenant_id="tenant_id",
            client_id="client_id",
            client_secret="client_secret",
            scope="http://example.com/scope",
            resource="http://example.com/resource",
        )
        self.assertEqual(
            "http://example.com/resource/api/v1/ViralPrepLots",
            settings.viral_prep_lots_url.unicode_string(),
        )
        self.assertEqual(
            "http://example.com/resource/api/v1/Viruses",
            settings.viruses_url.unicode_string(),
        )
        self.assertEqual(
            "http://example.com/resource/api/v1/Molecules",
            settings.molecules_url.unicode_string(),
        )

    def test_properties_no_path(self):
        """Tests properties get set properly when no path in resource"""
        settings = Settings(
            tenant_id="tenant_id",
            client_id="client_id",
            client_secret="client_secret",
            scope="http://example.com/scope",
            resource="http://example.com",
        )
        self.assertEqual(
            "http://example.com/api/v1/ViralPrepLots",
            settings.viral_prep_lots_url.unicode_string(),
        )
        self.assertEqual(
            "http://example.com/api/v1/Viruses",
            settings.viruses_url.unicode_string(),
        )
        self.assertEqual(
            "http://example.com/api/v1/Molecules",
            settings.molecules_url.unicode_string(),
        )


if __name__ == "__main__":
    unittest.main()
