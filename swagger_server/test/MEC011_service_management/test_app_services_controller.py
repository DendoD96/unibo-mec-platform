# coding: utf-8

from __future__ import absolute_import

from flask import json

from swagger_server.models.MEC011_service_management.service_info import ServiceInfo  # noqa: E501
from swagger_server.test import BaseTestCase, APP_INSTANCE_ID

from swagger_server.test.MEC011_service_management.utils.test_utilities import get_service_info_post
from swagger_server.test.MEC011_service_management.utils.test_utilities import SERVICE_INFORMATIONS_TEMPLATE, SERVICE_ID


class TestAppServicesController(BaseTestCase):
	"""AppServicesController integration test."""

	def test_app_services_fail(self):
		"""Test case for app_services_get. Should return 404 because the application is not in READY state."""

		query_string = [('ser_instance_id', 'ser_instance_id_example'),
		                ('ser_name', 'ser_name_example'),
		                ('ser_category_id', 'ser_category_id_example'),
		                ('consumed_local_only', True),
		                ('is_local', True),
		                ('scope_of_locality', 'scope_of_locality_example')]

		response = self.client.get(
			'/mec_service_mgmt/v1/applications/{appInstanceId}/services'.format(
				appInstanceId=APP_INSTANCE_ID),
			query_string=query_string)
		self.check_status_code(status_expected=404, response=response,
		                       message="Should return 404 because the application is not in READY state.")

	def test_app_services_get(self):
		"""Test case for app_services_get. No filter query is passed in the request. Should return 200.
        The body contains the SERVICE_INFORMATIONS data with the addition of serInstanceId."""

		self.register_app_and_add_service()
		response = self.client.get(
			'/mec_service_mgmt/v1/applications/{appInstanceId}/services'.format(
				appInstanceId=APP_INSTANCE_ID))
		self.check_status_code(200, response)
		response_body_data = response.json
		self.assertTrue(len(response_body_data) == 1)
		self.check_returned_service_informations(response_body_data[0])

	def test_app_services_get_with_service_name_filter(self):
		"""Test case for app_services_get. Filter query is passed in the request and match the previous inserted service.
        Should return 200. The body contains the SERVICE_INFORMATIONS data with the addition of serInstanceId."""

		self.register_app_and_add_service()
		query_string = [('ser_name', 'name')]
		response = self.client.get(
			'/mec_service_mgmt/v1/applications/{appInstanceId}/services'.format(
				appInstanceId=APP_INSTANCE_ID),
			query_string=query_string)
		self.check_status_code(200, response)
		response_body_data = response.json
		self.assertTrue(len(response_body_data) == 1)
		self.check_returned_service_informations(response_body_data[0])

	def test_app_services_get_with_service_name_filter_empty(self):
		"""Test case for app_services_get. Filter query is passed in the request and match the previous inserted service.
        Should return 200 with an empty body."""

		self.register_app_and_add_service()
		query_string = [('ser_name', 'name1')]
		response = self.client.get(
			'/mec_service_mgmt/v1/applications/{appInstanceId}/services'.format(
				appInstanceId=APP_INSTANCE_ID),
			query_string=query_string)
		self.check_status_code(200, response)
		self.assertTrue(len(response.json) == 0)

	def test_app_services_get_with_combined_filters(self):
		"""Test case for app_services_get. Multiple filter query is passed in the request and match the previous
        inserted service. Should return 200. The body contains the SERVICE_INFORMATIONS data
        with the addition of serInstanceId."""

		self.register_app_and_add_service()
		query_string = [('ser_name', 'name'), ('consumed_local_only', True),
		                ('is_local', True)]
		response = self.client.get(
			'/mec_service_mgmt/v1/applications/{appInstanceId}/services'.format(
				appInstanceId=APP_INSTANCE_ID),
			query_string=query_string)
		self.check_status_code(200, response)
		response_body_data = response.json
		self.assertTrue(len(response_body_data) == 1)
		self.check_returned_service_informations(response_body_data[0])

	def test_app_services_post_fail(self):
		"""Test case for app_services_post. Should return 404 because the application is not in READY state."""

		response = self.add_service(service_info=get_service_info_post(), app_instance_id=APP_INSTANCE_ID)
		self.check_status_code(404, response,
		                       message="Should return 404 because the application is not in READY state.")

	def test_app_services_post(self):
		"""Test case for app_services_post. Should return 201. The body contains the SERVICE_INFORMATIONS data with
        the addition of serInstanceId."""
		response = self.register_app_and_add_service()
		response_body_data = response.json
		self.check_status_code(201, response)
		self.check_returned_service_informations(response_body_data)

	def test_app_services_service_id_delete_empty(self):
		"""Test case for app_services_service_id_delete. Should return 404 because the application is in READY state,
        but there is no service registered."""
		self.app_ready(app_instance_id=APP_INSTANCE_ID)
		response = self.client.delete(
			'/mec_service_mgmt/v1/applications/{appInstanceId}/services/{serviceId}'.format(
				appInstanceId=APP_INSTANCE_ID, serviceId=SERVICE_ID))
		self.check_status_code(404, response,
		                       message="Should return 404 because the application is in READY state, "
		                               "but there is no service registered.")

	def test_app_services_service_id_delete(self):
		"""Test case for app_services_service_id_delete.Should return 204 because the application is in READY state and
        there is a service registered that match the specified id."""

		added_service = self.register_app_and_add_service()

		response = self.client.delete(
			'/mec_service_mgmt/v1/applications/{appInstanceId}/services/{serviceId}'.format(
				appInstanceId=APP_INSTANCE_ID, serviceId=added_service.json['serInstanceId']))

		self.check_status_code(204, response)

	def test_app_services_service_id_get_not_found(self):
		"""Test case for app_services_service_id_get. Should return 404 because the application is in READY state,
        but there is no service registered."""
		self.app_ready(app_instance_id=APP_INSTANCE_ID)
		response = self.client.get('/mec_service_mgmt/v1/applications/{appInstanceId}/services/{serviceId}'.format(
			appInstanceId=APP_INSTANCE_ID, serviceId='service_id_example'))
		self.check_status_code(404, response,
		                       "Should return 404 because the application is in READY state, but there "
		                       "is no service registered.")

	def test_app_services_service_id_get(self):
		"""Test case for app_services_service_id_get. Should return 200 because the application is in READY state and
        there is a service registered that match the specified id. The body contains the SERVICE_INFORMATIONS data with
        the addition of serInstanceId."""

		added_service = self.register_app_and_add_service()

		response = self.client.get(
			'/mec_service_mgmt/v1/applications/{appInstanceId}/services/{serviceId}'.format(
				appInstanceId=APP_INSTANCE_ID, serviceId=added_service.json['serInstanceId']))
		self.check_status_code(200, response)
		response_body_data = response.json
		self.check_returned_service_informations(response_body_data)

	def test_app_services_service_id_put_not_found(self):
		"""Test case for app_services_service_id_put. Should return 404 because the application is in READY state,
        but there is no service registered."""

		self.app_ready(app_instance_id=APP_INSTANCE_ID)
		body = ServiceInfo.from_dict(SERVICE_INFORMATIONS_TEMPLATE)
		response = self.client.put(
			'/mec_service_mgmt/v1/applications/{appInstanceId}/services/{serviceId}'.format(
				appInstanceId=APP_INSTANCE_ID, serviceId=SERVICE_ID),
			data=json.dumps(body),
			content_type='application/json')
		self.check_status_code(404, response,
		                       message="Should return 404 because the application is in READY state, "
		                               "but there is no service registered.")

	def test_app_services_service_id_put(self):
		"""Test case for app_services_service_id_put. Should return 200 because the application is in READY state and
        there is a service registered that match the specified id. The body contains the updated service
        informations."""

		added_service_response = self.register_app_and_add_service()
		new_service_info = SERVICE_INFORMATIONS_TEMPLATE.copy()
		new_service_info['serName'] = 'new_name'

		response = self.client.put(
			'/mec_service_mgmt/v1/applications/{appInstanceId}/services/{serviceId}'.format(
				appInstanceId=APP_INSTANCE_ID, serviceId=added_service_response.json['serInstanceId']),
			data=json.dumps(new_service_info),
			content_type='application/json')

		self.check_status_code(200, response)
		self.assertTrue(response.json['serName'] == new_service_info['serName'])


if __name__ == '__main__':
	import unittest

	unittest.main()
