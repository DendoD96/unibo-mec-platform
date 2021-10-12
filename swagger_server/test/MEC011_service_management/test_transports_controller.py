# coding: utf-8

from __future__ import absolute_import

from swagger_server.test import BaseTestCase


class TestTransportsController(BaseTestCase):
	"""TransportsController integration test stubs"""

	def test_transports_get(self):
		"""Test case for transports_get


		"""
		response = self.client.open(
			'/mec_service_mgmt/v1/transports',
			method='GET')
		self.assert200(response,
		               'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
	import unittest

	unittest.main()
