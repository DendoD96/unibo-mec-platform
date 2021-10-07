import logging

import connexion
import os

from flask_testing import TestCase

from swagger_server.encoder import JSONEncoder

SPECIFICATIONS_DIRECTORY = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'swagger'))


class BaseTestCase(TestCase):

	def create_app(self):
		logging.getLogger('connexion.operation').setLevel('ERROR')
		app = connexion.App(__name__, specification_dir=SPECIFICATIONS_DIRECTORY)
		app.app.json_encoder = JSONEncoder
		for filename in os.listdir(SPECIFICATIONS_DIRECTORY):
			if filename.endswith(".yaml"):
				app.add_api(filename, arguments={'title': f"ETSI GS ${filename.split('.')[0]} API"},
				pythonic_params=True)
				continue
			else:
				continue
		# app.add_api('MEC015_bandwidth.yaml')
		# app.add_api('MEC011_application_support.yaml')
		return app.app
