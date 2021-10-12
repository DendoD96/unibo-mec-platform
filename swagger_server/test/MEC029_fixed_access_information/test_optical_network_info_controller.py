# coding: utf-8

from __future__ import absolute_import

from swagger_server.test import BaseTestCase


class TestOpticalNetworkInfoController(BaseTestCase):
	"""OpticalNetworkInfoController integration test stubs"""

	def test_optical_network_info_get(self):
		"""Test case for optical_network_info_get

		used to query information about the optical network.
		"""
		query_string = [('ponYsId', 'pon_ys_id_example'),
		                ('onuId', 'onu_id_example')]
		response = self.client.open(
			'/fai/v1/queries/optical_network_info',
			method='GET',
			query_string=query_string)
		self.assert200(response,
		               'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
	import unittest

	unittest.main()
