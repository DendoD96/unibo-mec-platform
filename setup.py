from setuptools import setup, find_packages

NAME = "unibo-mec-platform"
VERSION = "0.1.0"

REQUIRES = ["connexion", "python_dateutil", "setuptools"]

setup(
	name=NAME,
	version=VERSION,
	description="Unibo MEC Platform",
	author="Davide Borsatti, Daniele Rossi",
	author_email="davide.borsatti@unibo.it, daniele.rossi27@unibo.it",
	url="https://github.com/DendoD96/unibo-mec-platform",
	keywords=["Swagger", "MEC Platform"],
	install_requires=REQUIRES,
	packages=find_packages(exclude=['*.tests', '*.tests.*', 'tests.*', 'tests']),
	package_data={'': ['swagger/swagger.yaml']},
	include_package_data=True,
	entry_points={
		'console_scripts': ['swagger_server=swagger_server.__main__:main']},
	long_description="""\
    Unibo MEC Platform.
    """
)
