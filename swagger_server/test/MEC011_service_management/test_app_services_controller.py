# coding: utf-8

from __future__ import absolute_import

from flask import json

from swagger_server.models.MEC011_service_management.end_point_info_address import EndPointInfoAddress
from swagger_server.models.MEC011_service_management.end_point_info_addresses import EndPointInfoAddresses
from swagger_server.models.MEC011_service_management.security_info import SecurityInfo
from swagger_server.models.MEC011_service_management.service_info import ServiceInfo  # noqa: E501
from swagger_server.models.MEC011_service_management.service_info_post import ServiceInfoPost  # noqa: E501
from swagger_server.models.MEC011_service_management.transport_info import TransportInfo
from swagger_server.test import BaseTestCase


def get_service_info_post():
	return ServiceInfoPost(ser_name="name", serializer="JSON", state="ACTIVE", version="2.0.0",
	                       consumed_local_only=True, is_local=True,
	                       transport_info=TransportInfo(id="TransId12345", name="REST", type="REST_HTTP",
	                                                    protocol="HTTP", version="2.0",
	                                                    endpoint=EndPointInfoAddresses(
		                                                    [EndPointInfoAddress(host="localhost", port=2234)]),
	                                                    security=SecurityInfo()))


class TestAppServicesController(BaseTestCase):
	"""AppServicesController integration test stubs"""

	def add_service(self, app_instance_id, service_info):
		return self.client.post(
			'/mec_service_mgmt/v1/applications/{appInstanceId}/services'.format(
				appInstanceId=app_instance_id),
			data=json.dumps(service_info),
			content_type='application/json')

	def test_app_services_get_empty_list(self):
		"""Test case for app_services_get"""

		query_string = [('ser_instance_id', 'ser_instance_id_example'),
		                ('ser_name', 'ser_name_example'),
		                ('ser_category_id', 'ser_category_id_example'),
		                ('consumed_local_only', True),
		                ('is_local', True),
		                ('scope_of_locality', 'scope_of_locality_example')]

		response = self.client.get(
			'/mec_service_mgmt/v1/applications/{appInstanceId}/services'.format(
				appInstanceId='app_instance_id_example'),
			query_string=query_string)
		self.assert200(response,
		               'Response body is : ' + response.data.decode('utf-8'))
		self.assertTrue(len(response.json) == 0)

	def test_app_services_get(self):
		"""Test case for app_services_get"""

		app_instance_id = 'app_instance_id_example'
		self.add_service(app_instance_id=app_instance_id, service_info=get_service_info_post())
		response = self.client.get(
			'/mec_service_mgmt/v1/applications/{appInstanceId}/services'.format(
				appInstanceId=app_instance_id))
		self.assertTrue(len(response.json) == 1)
		self.assert200(response,
		               'Response body is : ' + response.data.decode('utf-8'))

	def test_app_services_get_with_service_name_filter(self):
		"""Test case for app_services_get"""

		app_instance_id = 'app_instance_id_example'
		self.add_service(app_instance_id, get_service_info_post())
		query_string = [('ser_name', 'name')]
		response = self.client.get(
			'/mec_service_mgmt/v1/applications/{appInstanceId}/services'.format(
				appInstanceId=app_instance_id),
			query_string=query_string)
		self.assertTrue(len(response.json) == 1)
		self.assert200(response,
		               'Response body is : ' + response.data.decode('utf-8'))

	def test_app_services_get_with_service_name_filter_empty(self):
		"""Test case for app_services_get"""

		app_instance_id = 'app_instance_id_example'
		self.add_service(app_instance_id, get_service_info_post())
		query_string = [('ser_name', 'name1')]
		response = self.client.get(
			'/mec_service_mgmt/v1/applications/{appInstanceId}/services'.format(
				appInstanceId=app_instance_id),
			query_string=query_string)
		self.assertTrue(len(response.json) == 0)
		self.assert200(response,
		               'Response body is : ' + response.data.decode('utf-8'))

	def test_app_services_get_with_combined_filters(self):
		"""Test case for app_services_get"""

		app_instance_id = 'app_instance_id_example'
		self.add_service(app_instance_id, get_service_info_post())
		query_string = [('ser_name', 'name'), ('consumed_local_only', True),
		                ('is_local', True)]
		response = self.client.get(
			'/mec_service_mgmt/v1/applications/{appInstanceId}/services'.format(
				appInstanceId=app_instance_id),
			query_string=query_string)
		self.assertTrue(len(response.json) == 1)
		self.assert200(response,
		               'Response body is : ' + response.data.decode('utf-8'))

	def test_app_services_post(self):
		"""Test case for app_services_post"""

		response = self.client.post(
			'/mec_service_mgmt/v1/applications/{appInstanceId}/services'.format(
				appInstanceId='app_instance_id_example'),
			data=json.dumps(get_service_info_post()),
			content_type='application/json')
		response_body_data = response.json
		self.assertTrue(response.status_code == 201)
		self.assertTrue('serInstanceId' in response_body_data and
		                response_body_data['serName'] == 'name' and
		                response_body_data['serializer'] == "JSON" and response_body_data['state'] == "ACTIVE" and
		                response_body_data['version'] == "2.0.0")

	def test_app_services_service_id_delete_empty(self):
		"""Test case for app_services_service_id_delete"""
		response = self.client.delete(
			'/mec_service_mgmt/v1/applications/{appInstanceId}/services/{serviceId}'.format(
				appInstanceId='app_instance_id_example', serviceId='service_id_example'))
		self.assert404(response)

	def test_app_services_service_id_delete(self):
		"""Test case for app_services_service_id_delete"""

		app_instance_id = 'app_instance_id_example'
		added_service = self.add_service(app_instance_id, get_service_info_post())

		response = self.client.delete(
			'/mec_service_mgmt/v1/applications/{appInstanceId}/services/{serviceId}'.format(
				appInstanceId=app_instance_id, serviceId=added_service.json['serInstanceId']))

		self.assertTrue(response.status_code == 204)

	def test_app_services_service_id_get_not_found(self):
		"""Test case for app_services_service_id_get"""
		response = self.client.get('/mec_service_mgmt/v1/applications/{appInstanceId}/services/{serviceId}'.format(
			appInstanceId='app_instance_id_example', serviceId='service_id_example'))
		self.assert404(response)

	def test_app_services_service_id_get(self):
		"""Test case for app_services_service_id_get"""

		app_instance_id = 'app_instance_id_example'
		added_service = self.add_service(app_instance_id, get_service_info_post())

		response = self.client.get(
			'/mec_service_mgmt/v1/applications/{appInstanceId}/services/{serviceId}'.format(
				appInstanceId=app_instance_id, serviceId=added_service.json['serInstanceId']))
		self.assert200(response)

	def test_app_services_service_id_put_not_found(self):
		"""Test case for app_services_service_id_put"""

		body = ServiceInfo(ser_name="name", serializer="JSON", version="ServiceVersion1", state="ACTIVE",
		                   transport_info=TransportInfo(id="TransId12345", name="REST", type="REST_HTTP",
		                                                protocol="HTTP", version="2.0",
		                                                endpoint=EndPointInfoAddresses(
			                                                [EndPointInfoAddress(host="localhost", port=2234)]),
		                                                security=SecurityInfo()))
		response = self.client.put(
			'/mec_service_mgmt/v1/applications/{appInstanceId}/services/{serviceId}'.format(
				appInstanceId='app_instance_id_example', serviceId='service_id_example'),
			data=json.dumps(body),
			content_type='application/json')
		self.assert404(response)

	def test_app_services_service_id_put(self):
		"""Test case for app_services_service_id_put"""

		body = get_service_info_post()
		app_instance_id = 'app_instance_id_example'
		added_service_response = self.client.post(
			'/mec_service_mgmt/v1/applications/{appInstanceId}/services'.format(
				appInstanceId=app_instance_id),
			data=json.dumps(body),
			content_type='application/json')

		added_service = ServiceInfo.from_dict(added_service_response.json)
		added_service.ser_name = "name1"

		response = self.client.put(
			'/mec_service_mgmt/v1/applications/{appInstanceId}/services/{serviceId}'.format(
				appInstanceId=app_instance_id, serviceId=added_service.ser_instance_id),
			data=json.dumps(body),
			content_type='application/json')

		self.assert200(response)
		self.assertTrue(response.json['serName'] == body.ser_name)


if __name__ == '__main__':
	import unittest

	unittest.main()
