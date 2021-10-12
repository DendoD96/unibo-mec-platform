# coding: utf-8

from __future__ import absolute_import

from flask import json

from swagger_server.models.MEC028_wlan_access_information.ap_identity import ApIdentity
from swagger_server.models.MEC028_wlan_access_information.assoc_sta_subscription import AssocStaSubscription
from swagger_server.models.MEC028_wlan_access_information.measurement_config import MeasurementConfig  # noqa: E501
from swagger_server.models.MEC028_wlan_access_information.measurement_info import MeasurementInfo
from swagger_server.models.MEC028_wlan_access_information.sta_identity import StaIdentity
from swagger_server.test import BaseTestCase


class TestWaiController(BaseTestCase):
	"""WaiController integration test stubs"""

	def test_ap_info_get(self):
		"""Test case for ap_info_get

		Retrieve information on existing Access Points
		"""
		query_string = [('filter', 'filter_example'),
		                ('all_fields', 'all_fields_example'),
		                ('fields', 'fields_example'),
		                ('exclude_fields', 'exclude_fields_example'),
		                ('exclude_default', 'exclude_default_example')]
		response = self.client.open(
			'/wai/v2/queries/ap/ap_information',
			method='GET',
			query_string=query_string)
		self.assert200(response,
		               'Response body is : ' + response.data.decode('utf-8'))

	def test_measurement_link_list_measurements_get(self):
		"""Test case for measurement_link_list_measurements_get

		Retrieve information on measurements configuration
		"""
		response = self.client.open(
			'/wai/v2/measurements',
			method='GET')
		self.assert200(response,
		               'Response body is : ' + response.data.decode('utf-8'))

	def test_measurements_delete(self):
		"""Test case for measurements_delete

		Cancel a measurement configuration
		"""
		response = self.client.open(
			'/wai/v2/measurements/{measurementConfigId}'.format(measurementConfigId='measurement_config_id_example'),
			method='DELETE')
		self.assert200(response,
		               'Response body is : ' + response.data.decode('utf-8'))

	def test_measurements_get(self):
		"""Test case for measurements_get

		Retrieve information on an existing measurement configuration
		"""
		response = self.client.open(
			'/wai/v2/measurements/{measurementConfigId}'.format(measurementConfigId='measurement_config_id_example'),
			method='GET')
		self.assert200(response,
		               'Response body is : ' + response.data.decode('utf-8'))

	def test_measurements_post(self):
		"""Test case for measurements_post

		Create a new measurement configuration
		"""
		body = MeasurementConfig(measurement_id="measurement_id", measurement_info=MeasurementInfo(),
		                         sta_id=[StaIdentity(mac_id="mac_id")])
		response = self.client.open(
			'/wai/v2/measurements',
			method='POST',
			data=json.dumps(body),
			content_type='application/json')
		self.assert200(response,
		               'Response body is : ' + response.data.decode('utf-8'))

	def test_measurements_put(self):
		"""Test case for measurements_put

		Modify an existing measurement configuration
		"""
		body = MeasurementConfig(measurement_id="measurement_id", measurement_info=MeasurementInfo(),
		                         sta_id=[StaIdentity(mac_id="mac_id")])
		response = self.client.open(
			'/wai/v2/measurements/{measurementConfigId}'.format(measurementConfigId='measurement_config_id_example'),
			method='PUT',
			data=json.dumps(body),
			content_type='application/json')
		self.assert200(response,
		               'Response body is : ' + response.data.decode('utf-8'))

	def test_sta_info_get(self):
		"""Test case for sta_info_get

		Retrieve information on existing Stations
		"""
		query_string = [('filter', 'filter_example'),
		                ('all_fields', 'all_fields_example'),
		                ('fields', 'fields_example'),
		                ('exclude_fields', 'exclude_fields_example'),
		                ('exclude_default', 'exclude_default_example')]
		response = self.client.open(
			'/wai/v2/queries/sta/sta_information',
			method='GET',
			query_string=query_string)
		self.assert200(response,
		               'Response body is : ' + response.data.decode('utf-8'))

	def test_subscription_link_list_subscriptions_get(self):
		"""Test case for subscription_link_list_subscriptions_get

		Retrieve information on subscriptions for notifications
		"""
		query_string = [('subscription_type', 'subscription_type_example')]
		response = self.client.open(
			'/wai/v2/subscriptions',
			method='GET',
			query_string=query_string)
		self.assert200(response,
		               'Response body is : ' + response.data.decode('utf-8'))

	def test_subscriptions_delete(self):
		"""Test case for subscriptions_delete

		Cancel an existing subscription
		"""
		response = self.client.open(
			'/wai/v2/subscriptions/{subscriptionId}'.format(subscriptionId='subscription_id_example'),
			method='DELETE')
		self.assert200(response,
		               'Response body is : ' + response.data.decode('utf-8'))

	def test_subscriptions_get(self):
		"""Test case for subscriptions_get

		Retrieve information on current specific subscription
		"""
		response = self.client.open(
			'/wai/v2/subscriptions/{subscriptionId}'.format(subscriptionId='subscription_id_example'),
			method='GET')
		self.assert200(response,
		               'Response body is : ' + response.data.decode('utf-8'))

	def test_subscriptions_post(self):
		"""Test case for subscriptions_post

		Create a new subscription
		"""
		body = AssocStaSubscription(ap_id=ApIdentity(bssid="bssid"), subscription_type="subscription_type")
		response = self.client.open(
			'/wai/v2/subscriptions',
			method='POST',
			data=json.dumps(body),
			content_type='application/json')
		self.assert200(response,
		               'Response body is : ' + response.data.decode('utf-8'))

	def test_subscriptions_put(self):
		"""Test case for subscriptions_put

		Modify an existing subscription
		"""
		body = AssocStaSubscription(ap_id=ApIdentity(bssid="bssid"), subscription_type="subscription_type")
		response = self.client.open(
			'/wai/v2/subscriptions/{subscriptionId}'.format(subscriptionId='subscription_id_example'),
			method='PUT',
			data=json.dumps(body),
			content_type='application/json')
		self.assert200(response,
		               'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
	import unittest

	unittest.main()
