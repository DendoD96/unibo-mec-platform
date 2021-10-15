# coding: utf-8

from __future__ import absolute_import

from swagger_server.test import BaseTestCase
from swagger_server.test.utils.test_utilities import SUBSCRIPTION_ID, APP_INSTANCE_ID, \
	get_service_availability_notification_subscription


class TestAppSubscriptionsController(BaseTestCase):
	"""AppSubscriptionsController integration test stubs"""

	def test_applications_subscription_delete_fail_for_app_id(self):
		"""Test case for applications_subscription_delete. Should return 404 because the application is not in READY state."""

		response = self.client.open(
			'/mec_service_mgmt/v1/applications/{appInstanceId}/subscriptions/{subscriptionId}'.format(
				appInstanceId=APP_INSTANCE_ID, subscriptionId=SUBSCRIPTION_ID),
			method='DELETE')
		self.check_status_code(404, response)

	def test_applications_subscription_delete_fail_for_subscription_id(self):
		"""Test case for applications_subscription_delete. Should return 404 because the application is in READY state,
        but there is no subscription registered."""

		self.app_ready(APP_INSTANCE_ID)
		response = self.client.open(
			'/mec_service_mgmt/v1/applications/{appInstanceId}/subscriptions/{subscriptionId}'.format(
				appInstanceId=APP_INSTANCE_ID, subscriptionId=SUBSCRIPTION_ID),
			method='DELETE')
		self.check_status_code(404, response)

	def test_applications_subscription_delete(self):
		"""Test case for applications_subscription_delete. There is no subscription registered."""
		inserted_subscription = self.register_app_and_add_subscription(
			get_service_availability_notification_subscription())
		response = self.client.open(
			'/mec_service_mgmt/v1/applications/{appInstanceId}/subscriptions/{subscriptionId}'.format(
				appInstanceId=APP_INSTANCE_ID,
				subscriptionId=inserted_subscription.json['serAvailabilityNotificationSubscriptionId']),
			method='DELETE')
		self.check_status_code(204, response)

	def test_applications_subscription_get_fail_for_app_id(self):
		"""Test case for applications_subscription_get. Should return 404 because the application is not in READY state."""

		response = self.client.open(
			'/mec_service_mgmt/v1/applications/{appInstanceId}/subscriptions/{subscriptionId}'.format(
				appInstanceId=APP_INSTANCE_ID, subscriptionId=SUBSCRIPTION_ID),
			method='GET')
		self.check_status_code(404, response)

	def test_applications_subscription_get_fail_for_subscription_id(self):
		"""Test case for applications_subscription_get. Should return 404 because the application is in READY state,
        but there is no subscription registered."""

		self.app_ready(APP_INSTANCE_ID)
		response = self.client.open(
			'/mec_service_mgmt/v1/applications/{appInstanceId}/subscriptions/{subscriptionId}'.format(
				appInstanceId=APP_INSTANCE_ID, subscriptionId=SUBSCRIPTION_ID),
			method='GET')
		self.check_status_code(404, response)

	def test_applications_subscription_get(self):
		"""Test case for applications_subscription_get."""
		inserted_subscription = self.register_app_and_add_subscription(
			get_service_availability_notification_subscription())
		response = self.client.open(
			'/mec_service_mgmt/v1/applications/{appInstanceId}/subscriptions/{subscriptionId}'.format(
				appInstanceId=APP_INSTANCE_ID,
				subscriptionId=inserted_subscription.json['serAvailabilityNotificationSubscriptionId']),
			method='GET')
		self.check_status_code(200, response)

	def test_applications_subscriptions_get_fail(self):
		"""Test case for applications_subscriptions_get


		"""
		response = self.client.open(
			'/mec_service_mgmt/v1/applications/{appInstanceId}/subscriptions'.format(
				appInstanceId='app_instance_id_example'),
			method='GET')
		self.check_status_code(404, response)

	def test_applications_subscriptions_get(self):
		"""Test case for applications_subscriptions_get


		"""
		self.app_ready(APP_INSTANCE_ID)
		response = self.client.open(
			'/mec_service_mgmt/v1/applications/{appInstanceId}/subscriptions'.format(
				appInstanceId='app_instance_id_example'),
			method='GET')
		self.check_status_code(200, response)

	def test_applications_subscriptions_post_fail(self):
		"""Test case for applications_subscriptions_post.
		Should return 404 because the application is not in READY state."""
		subscription_info = get_service_availability_notification_subscription()
		self.check_status_code(404, self.add_subscription(app_instance_id=APP_INSTANCE_ID,
		                                                  subscription_info=subscription_info))

	def test_applications_subscriptions_post(self):
		"""Test case for applications_subscriptions_post."""
		response = self.register_app_and_add_subscription(get_service_availability_notification_subscription())
		self.check_status_code(201, response)
		self.assertTrue(response.headers.get('Location'))


if __name__ == '__main__':
	import unittest

	unittest.main()
