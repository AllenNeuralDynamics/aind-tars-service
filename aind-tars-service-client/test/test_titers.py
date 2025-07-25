# coding: utf-8

"""
    aind-tars-service

     ## aind-tars-service  Service to pull data from TARS.  

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from aind_tars_service_client.models.titers import Titers

class TestTiters(unittest.TestCase):
    """Titers unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Titers:
        """Test Titers
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Titers`
        """
        model = Titers()
        if include_optional:
            return Titers(
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                created_by = '',
                updated_by = '',
                id = '',
                notes = '',
                is_preferred = True,
                thawed_count = 56,
                result = 56,
                titer_type = None
            )
        else:
            return Titers(
        )
        """

    def testTiters(self):
        """Test Titers"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
