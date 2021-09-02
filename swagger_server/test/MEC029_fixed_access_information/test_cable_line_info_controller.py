# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.MEC029_fixed_access_information.cp_info import CpInfo  # noqa: E501
from swagger_server.test import BaseTestCase


class TestCableLineInfoController(BaseTestCase):
    """CableLineInfoController integration test stubs"""

    def test_cable_line_info_get(self):
        """Test case for cable_line_info_get

        It Queries information about the cable line of a fixed access network.
        """
        query_string = [('customer_premises_info', CpInfo()),
                        ('cm_id', 'cm_id_example')]
        response = self.client.open(
            '/fai/v1/queries/cable_line_info',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
