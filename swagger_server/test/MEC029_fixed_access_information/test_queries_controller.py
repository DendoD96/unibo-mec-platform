# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.MEC029_fixed_access_information.cp_info import CpInfo  # noqa: E501
from swagger_server.test import BaseTestCase


class TestQueriesController(BaseTestCase):
    """QueriesController integration test stubs"""

    def test_device_info_get(self):
        """Test case for device_info_get

        retrieve information on the devices that are connected to a fixed access network.
        """
        query_string = [('gw_id', 'gw_id_example'),
                        ('device_id', 'device_id_example'),
                        ('device_status', 56)]
        response = self.client.open(
            '/fai/v1/queries/device_info',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_fa_info_get(self):
        """Test case for fa_info_get

        Retrieve information on the available fixed access networks.
        """
        query_string = [('customer_premises_info', CpInfo()),
                        ('last_mile_tech', 56),
                        ('interface_type', 56),
                        ('dsbw', 56),
                        ('usbw', 56),
                        ('latency', 56)]
        response = self.client.open(
            '/fai/v1/queries/fa_info',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
