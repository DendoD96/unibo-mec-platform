#!/usr/bin/env python3

import connexion
import os

from swagger_server import encoder

SPECIFICATIONS_DIRECTORY = os.path.abspath(os.path.join(os.path.dirname(__file__), 'swagger'))


def main():
	app = connexion.App(__name__, specification_dir=SPECIFICATIONS_DIRECTORY)
	app.app.json_encoder = encoder.JSONEncoder
	for filename in os.listdir(SPECIFICATIONS_DIRECTORY):
		if filename.endswith(".yaml"):
			app.add_api(filename, arguments={'title': f"ETSI GS ${filename.split('.')[0]} API"},
			            pythonic_params=True)
			continue
		else:
			continue
	app.run(port=8080)


if __name__ == '__main__':
	main()
