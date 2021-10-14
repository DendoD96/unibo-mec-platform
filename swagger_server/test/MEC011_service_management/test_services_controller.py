# coding: utf-8

from __future__ import absolute_import

from swagger_server.test import BaseTestCase
from swagger_server.test.MEC011_service_management.utils.test_utilities import get_random_service_informations, \
	get_random_application_id, SERVICE_ID


class TestServicesController(BaseTestCase):
	"""ServicesController integration test stubs"""

	def test_services_get_empty(self):
		"""Test case for services_get with no app ready. Should return 200 with an empty list."""

		response = self.client.get('/mec_service_mgmt/v1/services')
		self.check_status_code(200, response)
		response_body_data = response.json
		self.assertTrue(len(response_body_data) == 0)

	def test_services_get(self):
		"""Test case for services_get with no app ready. Should return 200 with two services that were previously
		insert."""

		service_informations = [get_random_service_informations() for _ in range(2)]
		application_instance_ids = [get_random_application_id() for _ in range(2)]
		for index in range(2):
			self.register_app_and_add_service(service=service_informations[index],
			                                  app_instance_id=application_instance_ids[index])
		response = self.client.get('/mec_service_mgmt/v1/services')
		self.check_status_code(200, response)
		response_body_data = response.json
		self.assertTrue(len(response_body_data) == 2)
		self.check_returned_services_informations(returned_services_informations=response_body_data,
		                                          inserted_services=service_informations)

	def test_services_service_id_get_fail(self):
		"""Test case for services_service_id_get. Should return 404 because the application is not in READY state."""

		self.check_status_code(404, self.client.get(f"/mec_service_mgmt/v1/services/{SERVICE_ID}"))

	def test_services_service_id_get(self):
		"""Test case for services_service_id_get. Should return 200 because there is an app in ready state with a
		service registered whose id match with the provided one."""

		added_service = self.register_app_and_add_service()
		response = self.client.get(f"/mec_service_mgmt/v1/services/{added_service.json['serInstanceId']}")
		self.check_status_code(200, response)
		response_body_data = response.json
		self.check_returned_service_informations(response_body_data)


if __name__ == '__main__':
	import unittest

	unittest.main()
