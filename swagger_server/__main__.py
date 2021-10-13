#!/usr/bin/env python3
import threading
from logging.config import dictConfig

import connexion
import os

import yaml

from swagger_server import encoder
from swagger_server.controllers.internal.subscription_manager import manager

SPECIFICATIONS_DIRECTORY = os.path.abspath(os.path.join(os.path.dirname(__file__), 'swagger'))
SUBSCRIPTION_MANAGER_NUMBER = 1
LOGGER_CONFIGURATION_PATH = '../logging.conf'


def main():
	app = connexion.App(__name__, specification_dir=SPECIFICATIONS_DIRECTORY, options={"swagger_ui": False})
	flask_app = app.app
	flask_app.json_encoder = encoder.JSONEncoder

	with open(LOGGER_CONFIGURATION_PATH, "r") as stream:
		try:
			dictConfig(yaml.safe_load(stream))
		except yaml.YAMLError:
			print("Unable to read logger configuration file")
			pass

	for filename in os.listdir(SPECIFICATIONS_DIRECTORY):
		if filename.endswith(".yaml"):
			app.add_api(filename, arguments={'title': f"ETSI GS ${filename.split('.')[0]} API"},
			            pythonic_params=True)
			continue
		else:
			continue
	for _ in range(SUBSCRIPTION_MANAGER_NUMBER):
		threading.Thread(target=manager, daemon=True).start()
	app.run(port=8080)


if __name__ == '__main__':
	main()
