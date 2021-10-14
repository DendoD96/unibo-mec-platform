import logging
import os

import connexion
from flask_testing import TestCase
from flask import json

from swagger_server.encoder import JSONEncoder
from swagger_server.models.internal.applications_services_data import app_ids
from swagger_server.test.MEC011_service_management.utils.test_utilities import SERVICE_INFORMATIONS_TEMPLATE, \
	APP_INSTANCE_ID

SPECIFICATIONS_DIRECTORY = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'swagger'))


class BaseTestCase(TestCase):

	@classmethod
	def create_app(cls):
		logging.getLogger('connexion.operation').setLevel('ERROR')
		app = connexion.App(__name__, specification_dir=SPECIFICATIONS_DIRECTORY)
		app.app.json_encoder = JSONEncoder
		app_ids.clear()
		for filename in os.listdir(SPECIFICATIONS_DIRECTORY):
			if filename.endswith(".yaml"):
				app.add_api(filename, arguments={'title': f"ETSI GS ${filename.split('.')[0]} API"},
				            pythonic_params=True)
				continue
			else:
				continue
		return app.app

	def add_service(self, service_info, app_instance_id):
		return self.client.post(
			'/mec_service_mgmt/v1/applications/{appInstanceId}/services'.format(
				appInstanceId=app_instance_id),
			data=json.dumps(service_info),
			content_type='application/json')

	def app_ready(self, app_instance_id):
		return self.client.post(
			'/mec_app_support/v1/applications/{appInstanceId}/confirm_ready'.format(
				appInstanceId=app_instance_id),
			data=json.dumps({
				"indication": "READY"
			}),
			content_type='application/json')

	def register_app_and_add_service(self, service=None, app_instance_id=None):
		service_to_register = service if service is not None else SERVICE_INFORMATIONS_TEMPLATE
		app_instance_id_to_register = app_instance_id if app_instance_id is not None else APP_INSTANCE_ID
		response = self.app_ready(app_instance_id_to_register)
		self.check_status_code(204, response)
		response = self.add_service(service_info=service_to_register, app_instance_id=app_instance_id_to_register)
		self.check_status_code(201, response)
		return response

	def check_returned_service_informations(self, returned_service_informations, inserted_service=None):
		self.assertTrue('serInstanceId' in returned_service_informations)
		del returned_service_informations['serInstanceId']
		if inserted_service is None:
			self.assertTrue(returned_service_informations == SERVICE_INFORMATIONS_TEMPLATE)
		else:
			self.assertTrue(returned_service_informations == inserted_service)

	def check_returned_services_informations(self, returned_services_informations, inserted_services):
		def remove_key(dictionary: dict):
			dictionary.pop('serInstanceId', None)
			return dictionary

		self.assertTrue(
			any('serInstanceId' in service_informations for service_informations in returned_services_informations))
		returned_services_informations = list(map(remove_key, returned_services_informations))
		self.assertTrue(any(returned_service_information in inserted_services for returned_service_information in
		                    returned_services_informations))

	def check_status_code(self, status_expected, response, message=None):
		self.assertEqual(status_expected, response.status_code,
		                 msg=message)
