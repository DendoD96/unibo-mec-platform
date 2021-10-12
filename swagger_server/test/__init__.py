import logging
import os

import connexion
from flask_testing import TestCase

from swagger_server.encoder import JSONEncoder
from swagger_server.models.internal.applications_services_data import app_ids

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
