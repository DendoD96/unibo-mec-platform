# coding: utf-8

from __future__ import absolute_import

from flask import json

from swagger_server.models.MEC029_fixed_access_information.onu_alarm_subscription import OnuAlarmSubscription
from swagger_server.models.MEC029_fixed_access_information.onu_alarm_subscription_filter_criteria_onu_alarm import \
	OnuAlarmSubscriptionFilterCriteriaOnuAlarm
from swagger_server.test import BaseTestCase


class TestSubscriptionController(BaseTestCase):
	"""SubscriptionController integration test stubs"""

	def test_individual_subscription_delete(self):
		"""Test case for individual_subscription_delete

		Used to cancel the existing subscription.
		"""
		response = self.client.open(
			'/fai/v1/subscriptions/{subscriptionId}'.format(subscriptionId='subscription_id_example'),
			method='DELETE')
		self.assert200(response,
		               'Response body is : ' + response.data.decode('utf-8'))

	def test_individual_subscription_get(self):
		"""Test case for individual_subscription_get

		Retrieve information about this subscription.
		"""
		response = self.client.open(
			'/fai/v1/subscriptions/{subscriptionId}'.format(subscriptionId='subscription_id_example'),
			method='GET')
		self.assert200(response,
		               'Response body is : ' + response.data.decode('utf-8'))

	def test_individual_subscription_put(self):
		"""Test case for individual_subscription_put

		Used to update the existing subscription.
		"""
		body = OnuAlarmSubscription(callback_reference="callbackURI", subscription_type="subscriptionType",
		                            filter_criteria_onu_alarm=OnuAlarmSubscriptionFilterCriteriaOnuAlarm(
			                            onu_id=["onu_id1"]))
		response = self.client.open(
			'/fai/v1/subscriptions/{subscriptionId}'.format(subscriptionId='subscription_id_example'),
			method='PUT',
			data=json.dumps(body),
			content_type='application/json')
		self.assert200(response,
		               'Response body is : ' + response.data.decode('utf-8'))

	def test_sub_get(self):
		"""Test case for sub_get

		request information about the subscriptions for this requestor.
		"""
		query_string = [('subscription_type', 'subscription_type_example')]
		response = self.client.open(
			'/fai/v1/subscriptions',
			method='GET',
			query_string=query_string)
		self.assert200(response,
		               'Response body is : ' + response.data.decode('utf-8'))

	def test_sub_post(self):
		"""Test case for sub_post

		 create a new subscription to FAI notifications.
		"""
		body = OnuAlarmSubscription(callback_reference="callbackURI", subscription_type="subscriptionType",
		                            filter_criteria_onu_alarm=OnuAlarmSubscriptionFilterCriteriaOnuAlarm(
			                            onu_id=["onu_id1"]))
		response = self.client.open(
			'/fai/v1/subscriptions',
			method='POST',
			data=json.dumps(body),
			content_type='application/json')
		self.assert200(response,
		               'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
	import unittest

	unittest.main()
