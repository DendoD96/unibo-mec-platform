# coding: utf-8

from __future__ import absolute_import

from flask import json

from swagger_server.models.MEC014_ue_identity.ue_identity_tag_info import UeIdentityTagInfo  # noqa: E501
from swagger_server.test import BaseTestCase


class TestUeIdentityTagInfoController(BaseTestCase):
	"""UeIdentityTagInfoController integration test stubs"""

	def test_ue_identity_tag_info_get(self):
		"""Test case for ue_identity_tag_info_get


		"""
		query_string = [('ue_identity_tag', 'ue_identity_tag_example')]
		response = self.client.open(
			'/ui/v1/{appInstanceId}/ue_identity_tag_info'.format(appInstanceId='app_instance_id_example'),
			method='GET',
			query_string=query_string)
		self.assert_401(response,
		                'Response body is : ' + response.data.decode('utf-8'))

	def test_ue_identity_tag_info_put(self):
		"""Test case for ue_identity_tag_info_put


		"""
		body = UeIdentityTagInfo()
		response = self.client.open(
			'/ui/v1/{appInstanceId}/ue_identity_tag_info'.format(appInstanceId='app_instance_id_example'),
			method='PUT',
			data=json.dumps(body),
			content_type='application/json')
		self.assert_401(response,
		                'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
	import unittest

	unittest.main()
