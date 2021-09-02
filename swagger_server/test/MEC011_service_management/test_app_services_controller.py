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


class TestAppServicesController(BaseTestCase):
	"""AppServicesController integration test stubs"""

	def test_app_services_get(self):
		"""Test case for app_services_get


		"""
		query_string = [('ser_instance_id', 'ser_instance_id_example'),
		                ('ser_name', 'ser_name_example'),
		                ('ser_category_id', 'ser_category_id_example'),
		                ('consumed_local_only', True),
		                ('is_local', True),
		                ('scope_of_locality', 'scope_of_locality_example')]
		response = self.client.open(
			'/mec_service_mgmt/v1/applications/{appInstanceId}/services'.format(
				appInstanceId='app_instance_id_example'),
			method='GET',
			query_string=query_string)
		self.assert200(response,
		               'Response body is : ' + response.data.decode('utf-8'))

	def test_app_services_post(self):
		"""Test case for app_services_post


		"""
		body = ServiceInfoPost(ser_name="name", serializer="JSON", state="ACTIVE", version="2.0.0", transport_id="id")
		response = self.client.open(
			'/mec_service_mgmt/v1/applications/{appInstanceId}/services'.format(
				appInstanceId='app_instance_id_example'),
			method='POST',
			data=json.dumps(body),
			content_type='application/json')
		self.assert200(response,
		               'Response body is : ' + response.data.decode('utf-8'))

	def test_app_services_service_id_delete(self):
		"""Test case for app_services_service_id_delete


		"""
		response = self.client.open(
			'/mec_service_mgmt/v1/applications/{appInstanceId}/services/{serviceId}'.format(
				appInstanceId='app_instance_id_example', serviceId='service_id_example'),
			method='DELETE')
		self.assert200(response,
		               'Response body is : ' + response.data.decode('utf-8'))

	def test_app_services_service_id_get(self):
		"""Test case for app_services_service_id_get


		"""
		response = self.client.open(
			'/mec_service_mgmt/v1/applications/{appInstanceId}/services/{serviceId}'.format(
				appInstanceId='app_instance_id_example', serviceId='service_id_example'),
			method='GET')
		self.assert200(response,
		               'Response body is : ' + response.data.decode('utf-8'))

	def test_app_services_service_id_put(self):
		"""Test case for app_services_service_id_put


		"""
		body = ServiceInfo(ser_name="name", serializer="JSON", version="ServiceVersion1", state="ACTIVE",
		                   transport_info=TransportInfo(id="TransId12345", name="REST", type="REST_HTTP",
		                                                protocol="HTTP", version="2.0",
		                                                endpoint=EndPointInfoAddresses(
			                                                [EndPointInfoAddress(host="localhost", port=2234)]),
		                                                security=SecurityInfo()))
		response = self.client.open(
			'/mec_service_mgmt/v1/applications/{appInstanceId}/services/{serviceId}'.format(
				appInstanceId='app_instance_id_example', serviceId='service_id_example'),
			method='PUT',
			data=json.dumps(body),
			content_type='application/json')
		self.assert200(response,
		               'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
	import unittest

	unittest.main()
