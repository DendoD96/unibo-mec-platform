#!/usr/bin/env python3
import logging
import threading

import connexion
import os

from swagger_server import encoder
from swagger_server.controllers.internal.subscription_manager import manager

SPECIFICATIONS_DIRECTORY = os.path.abspath(os.path.join(os.path.dirname(__file__), 'swagger'))
SUBSCRIPTION_MANAGER_NUMBER = 1


def main():
	app = connexion.App(__name__, specification_dir=SPECIFICATIONS_DIRECTORY, options={"swagger_ui": False})
	flask_app = app.app
	flask_app.json_encoder = encoder.JSONEncoder
	flask_app.logger.setLevel(logging.DEBUG)
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
