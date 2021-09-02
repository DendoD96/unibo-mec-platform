# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.MEC011_application_support.current_time import CurrentTime  # noqa: E501
from swagger_server.models.problem_details import ProblemDetails  # noqa: E501
from swagger_server.models.MEC011_application_support.timing_caps import TimingCaps  # noqa: E501
from swagger_server.test import BaseTestCase


class TestTimingController(BaseTestCase):
    """TimingController integration test stubs"""

    def test_timing_caps_get(self):
        """Test case for timing_caps_get

        
        """
        response = self.client.open(
            '/mec_app_support/v1/timing/timing_caps',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_timing_current_time_get(self):
        """Test case for timing_current_time_get

        
        """
        response = self.client.open(
            '/mec_app_support/v1/timing/current_time',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
