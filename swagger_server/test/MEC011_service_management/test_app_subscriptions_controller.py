# coding: utf-8

from __future__ import absolute_import

from flask import json

from swagger_server.models.MEC011_service_management.ser_availability_notification_subscription import \
	SerAvailabilityNotificationSubscription  # noqa: E501
from swagger_server.test import BaseTestCase


class TestAppSubscriptionsController(BaseTestCase):
	"""AppSubscriptionsController integration test stubs"""

	def test_applications_subscription_delete(self):
		"""Test case for applications_subscription_delete


		"""
		response = self.client.open(
			'/mec_service_mgmt/v1/applications/{appInstanceId}/subscriptions/{subscriptionId}'.format(
				appInstanceId='app_instance_id_example', subscriptionId='subscription_id_example'),
			method='DELETE')
		self.assert404(response,
		               'Response body is : ' + response.data.decode('utf-8'))

	def test_applications_subscription_get(self):
		"""Test case for applications_subscription_get


		"""
		response = self.client.open(
			'/mec_service_mgmt/v1/applications/{appInstanceId}/subscriptions/{subscriptionId}'.format(
				appInstanceId='app_instance_id_example', subscriptionId='subscription_id_example'),
			method='GET')
		self.assert200(response,
		               'Response body is : ' + response.data.decode('utf-8'))

	def test_applications_subscriptions_get(self):
		"""Test case for applications_subscriptions_get


		"""
		response = self.client.open(
			'/mec_service_mgmt/v1/applications/{appInstanceId}/subscriptions'.format(
				appInstanceId='app_instance_id_example'),
			method='GET')
		self.assert200(response,
		               'Response body is : ' + response.data.decode('utf-8'))

	def test_applications_subscriptions_post(self):
		"""Test case for applications_subscriptions_post


		"""
		body = SerAvailabilityNotificationSubscription(subscription_type="SerAvailabilityNotificationSubscription",
		                                               callback_reference="callbackURI",
		                                               )
		response = self.client.open(
			'/mec_service_mgmt/v1/applications/{appInstanceId}/subscriptions'.format(
				appInstanceId='app_instance_id_example'),
			method='POST',
			data=json.dumps(body),
			content_type='application/json')
		self.assert200(response,
		               'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
	import unittest

	unittest.main()
