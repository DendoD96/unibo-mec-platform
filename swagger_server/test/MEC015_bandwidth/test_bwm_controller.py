# coding: utf-8

from __future__ import absolute_import

from flask import json

from swagger_server.models.MEC015_bandwidth.bw_info import BwInfo  # noqa: E501
from swagger_server.models.MEC015_bandwidth.bw_info_deltas import BwInfoDeltas  # noqa: E501
from swagger_server.test import BaseTestCase


class TestBwmController(BaseTestCase):
    """BwmController integration test stubs"""

    def test_bandwidth_allocation_delete(self):
        """Test case for bandwidth_allocation_delete

        Remove a specific bandwidthAllocation
        """
        response = self.client.open(
            '/bwm/v1/bw_allocations/{allocation_id}'.format(allocation_id='allocation_id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_bandwidth_allocation_get(self):
        """Test case for bandwidth_allocation_get

        Retrieve information about a specific bandwidthAllocation
        """
        response = self.client.get('/bwm/v1/bw_allocations/allocation_id_example')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_bandwidth_allocation_list_get(self):
        """Test case for bandwidth_allocation_list_get

        Retrieve information about a list of bandwidthAllocation resources
        """
        query_string = [('app_instance_id', 'app_instance_id_example'),
                        ('app_name', 'app_name_example'),
                        ('session_id', 'session_id_example')]
        response = self.client.get(
            '/bwm/v1/bw_allocations',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_bandwidth_allocation_patch(self):
        """Test case for bandwidth_allocation_patch

        Modify the information about a specific existing bandwidthAllocation by sending updates on the data structure
        """
        body = BwInfoDeltas(app_ins_id="id", request_type="0")
        response = self.client.open(
            '/bwm/v1/bw_allocations/{allocation_id}'.format(allocation_id='allocation_id_example'),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_bandwidth_allocation_post(self):
        """Test case for bandwidth_allocation_post

        Create a bandwidthAllocation resource
        """
        body = BwInfo(allocation_direction="dir", app_ins_id="app_id", fixed_allocation="", request_type=1)
        response = self.client.open(
            '/bwm/v1/bw_allocations',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_bandwidth_allocation_put(self):
        """Test case for bandwidth_allocation_put

        Update the information about a specific bandwidthAllocation
        """
        body = BwInfo(allocation_direction="direction", app_ins_id="id", fixed_allocation="", request_type=1)
        response = self.client.open(
            '/bwm/v1/bw_allocations/{allocation_id}'.format(allocation_id='allocation_id_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
