#!/usr/bin/env python3
import pathlib
import threading
from logging.config import dictConfig

import connexion
import os
import argparse
import yaml

from swagger_server import encoder
from swagger_server.controllers.internal.subscription_manager import manager

SPECIFICATIONS_DIRECTORY = os.path.join(pathlib.Path(__file__).parent.resolve(), 'swagger')
SUBSCRIPTION_MANAGER_NUMBER = 1
LOGGER_CONFIGURATION_PATH = os.path.join(pathlib.Path(__file__).parents[1], 'logging.conf')
LOG_FILE_PATH = os.path.join(pathlib.Path(__file__).parents[1], 'mec_platform.log')


def main():
	app = connexion.App(__name__, specification_dir=SPECIFICATIONS_DIRECTORY, options={"swagger_ui": False})
	flask_app = app.app
	flask_app.json_encoder = encoder.JSONEncoder

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
	with open(LOGGER_CONFIGURATION_PATH, "r") as stream:
		try:
			argument_parser = argparse.ArgumentParser()
			argument_parser.add_argument('--debug-level', help="set the debug output level", type=int,
			                             choices=[0, 1, 2, 3, 4, 5])
			argument_parser.add_argument('--debug-type', help="set the debug type", type=str,
			                             choices=['file', 'console'])
			arguments = argument_parser.parse_args()
			logger_config = yaml.safe_load(stream)
			debug_level = arguments.debug_level
			debug_type = arguments.debug_type
			if debug_level is not None and debug_level != 1:
				logger_config['root']['level'] = debug_level * 10
			if debug_type is not None and debug_type != 'console':
				logger_config['root']['handlers'] = [debug_type]
				logger_config['handlers']['file']['filename'] = os.path.join(pathlib.Path(__file__).parents[1],
				                                                             'mec_platform.log')
			dictConfig(logger_config)
		except yaml.YAMLError:
			print("Unable to read logger configuration file")
	main()
