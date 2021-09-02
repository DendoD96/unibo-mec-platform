# coding: utf-8

from __future__ import absolute_import

from flask import json

from swagger_server.models.MEC016_device_application_interface.app_context import AppContext  # noqa: E501
from swagger_server.models.MEC016_device_application_interface.app_context_app_info import AppContextAppInfo
from swagger_server.models.MEC016_device_application_interface.app_context_app_info_user_app_instance_info import \
	AppContextAppInfoUserAppInstanceInfo
from swagger_server.models.MEC016_device_application_interface.application_location_availability import \
	ApplicationLocationAvailability  # noqa: E501
from swagger_server.models.MEC016_device_application_interface.application_location_availability_app_info import \
	ApplicationLocationAvailabilityAppInfo
from swagger_server.models.MEC016_device_application_interface.application_location_availability_app_info_available_locations import \
	ApplicationLocationAvailabilityAppInfoAvailableLocations
from swagger_server.test import BaseTestCase


class TestDevAppController(BaseTestCase):
	"""DevAppController integration test stubs"""

	def test_app_location_availability_post(self):
		"""Test case for app_location_availability_post

		Obtain the location constraints for a new application context.
		"""
		body = ApplicationLocationAvailability(
			app_info=ApplicationLocationAvailabilityAppInfo(app_d_version="1.0.0", app_name="app_name",
			                                                app_provider="app_provider", available_locations=[
					ApplicationLocationAvailabilityAppInfoAvailableLocations()]), associate_dev_app_id="dev_app_id")
		response = self.client.open(
			'/dev_app/v1/obtain_app_loc_availability',
			method='POST',
			data=json.dumps(body),
			content_type='application/json')
		self.assert200(response,
		               'Response body is : ' + response.data.decode('utf-8'))

	def test_dev_app_context_delete(self):
		"""Test case for dev_app_context_delete

		Deletion of an existing application context.
		"""
		response = self.client.open(
			'/dev_app/v1/app_contexts/{contextId}'.format(contextId='context_id_example'),
			method='DELETE')
		self.assert200(response,
		               'Response body is : ' + response.data.decode('utf-8'))

	def test_dev_app_context_put(self):
		"""Test case for dev_app_context_put

		Updating the callbackReference and/or appLocation of an existing application context.
		"""
		body = AppContext(app_info=AppContextAppInfo(app_d_version="1.0.0", app_name="app_name",
		                                             app_provider="app_provider", user_app_instance_info=[
				AppContextAppInfoUserAppInstanceInfo()]), associate_dev_app_id="dev_app_id")
		response = self.client.open(
			'/dev_app/v1/app_contexts/{contextId}'.format(contextId='context_id_example'),
			method='PUT',
			data=json.dumps(body),
			content_type='application/json')
		self.assert200(response,
		               'Response body is : ' + response.data.decode('utf-8'))

	def test_dev_app_contexts_get(self):
		"""Test case for dev_app_contexts_get

		Creation of a new application context.
		"""
		body = AppContext(app_info=AppContextAppInfo(app_d_version="1.0.0", app_name="app_name",
		                                             app_provider="app_provider", user_app_instance_info=[
				AppContextAppInfoUserAppInstanceInfo()]), associate_dev_app_id="dev_app_id")
		response = self.client.open(
			'/dev_app/v1/app_contexts',
			method='POST',
			data=json.dumps(body),
			content_type='application/json')
		self.assert200(response,
		               'Response body is : ' + response.data.decode('utf-8'))

	def test_me_app_list_get(self):
		"""Test case for me_app_list_get

		Get available application information.
		"""
		query_string = [('app_name', 'app_name_example'),
		                ('app_provider', 'app_provider_example'),
		                ('app_soft_version', 'app_soft_version_example'),
		                ('vendor_id', 'vendor_id_example'),
		                ('service_cont', 56)]
		response = self.client.open(
			'/dev_app/v1/app_list',
			method='GET',
			query_string=query_string)
		self.assert200(response,
		               'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
	import unittest

	unittest.main()
