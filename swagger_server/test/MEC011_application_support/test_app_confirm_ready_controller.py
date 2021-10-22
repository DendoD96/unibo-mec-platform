# coding: utf-8

from __future__ import absolute_import

from flask import json

from swagger_server.models.MEC011_application_support.app_ready_confirmation import AppReadyConfirmation  # noqa: E501
from swagger_server.test import BaseTestCase
from swagger_server.test.utils.test_utilities import APP_INSTANCE_ID


class TestAppConfirmReadyController(BaseTestCase):
	"""AppConfirmReadyController integration test stubs"""

	def test_applications_confirm_ready_post(self):
		"""Test case for applications_confirm_ready_post"""

		body = AppReadyConfirmation(indication="READY")
		response = self.client.open(
			'/mec_app_support/v1/applications/{appInstanceId}/confirm_ready'.format(
				appInstanceId=APP_INSTANCE_ID),
			method='POST',
			data=json.dumps(body),
			content_type='application/json')
		self.check_status_code(204, response)


if __name__ == '__main__':
	import unittest

	unittest.main()
