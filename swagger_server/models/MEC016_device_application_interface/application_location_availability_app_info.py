# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.MEC016_device_application_interface.application_location_availability_app_info_available_locations import ApplicationLocationAvailabilityAppInfoAvailableLocations  # noqa: F401,E501
from swagger_server import util


class ApplicationLocationAvailabilityAppInfo(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, app_d_version: str=None, app_description: str=None, app_name: str=None, app_package_source: str=None, app_provider: str=None, app_soft_version: str=None, available_locations: List[ApplicationLocationAvailabilityAppInfoAvailableLocations]=None):  # noqa: E501
        """ApplicationLocationAvailabilityAppInfo - a model defined in Swagger

        :param app_d_version: The app_d_version of this ApplicationLocationAvailabilityAppInfo.  # noqa: E501
        :type app_d_version: str
        :param app_description: The app_description of this ApplicationLocationAvailabilityAppInfo.  # noqa: E501
        :type app_description: str
        :param app_name: The app_name of this ApplicationLocationAvailabilityAppInfo.  # noqa: E501
        :type app_name: str
        :param app_package_source: The app_package_source of this ApplicationLocationAvailabilityAppInfo.  # noqa: E501
        :type app_package_source: str
        :param app_provider: The app_provider of this ApplicationLocationAvailabilityAppInfo.  # noqa: E501
        :type app_provider: str
        :param app_soft_version: The app_soft_version of this ApplicationLocationAvailabilityAppInfo.  # noqa: E501
        :type app_soft_version: str
        :param available_locations: The available_locations of this ApplicationLocationAvailabilityAppInfo.  # noqa: E501
        :type available_locations: List[ApplicationLocationAvailabilityAppInfoAvailableLocations]
        """
        self.swagger_types = {
            'app_d_version': str,
            'app_description': str,
            'app_name': str,
            'app_package_source': str,
            'app_provider': str,
            'app_soft_version': str,
            'available_locations': List[ApplicationLocationAvailabilityAppInfoAvailableLocations]
        }

        self.attribute_map = {
            'app_d_version': 'appDVersion',
            'app_description': 'appDescription',
            'app_name': 'appName',
            'app_package_source': 'appPackageSource',
            'app_provider': 'appProvider',
            'app_soft_version': 'appSoftVersion',
            'available_locations': 'availableLocations'
        }
        self._app_d_version = app_d_version
        self._app_description = app_description
        self._app_name = app_name
        self._app_package_source = app_package_source
        self._app_provider = app_provider
        self._app_soft_version = app_soft_version
        self._available_locations = available_locations

    @classmethod
    def from_dict(cls, dikt) -> 'ApplicationLocationAvailabilityAppInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ApplicationLocationAvailability_appInfo of this ApplicationLocationAvailabilityAppInfo.  # noqa: E501
        :rtype: ApplicationLocationAvailabilityAppInfo
        """
        return util.deserialize_model(dikt, cls)

    @property
    def app_d_version(self) -> str:
        """Gets the app_d_version of this ApplicationLocationAvailabilityAppInfo.

        Identifies the version of the application descriptor. It is equivalent to the appDVersion defined in clause 6.2.1.2 of ETSI GS MEC 0102 [1].  # noqa: E501

        :return: The app_d_version of this ApplicationLocationAvailabilityAppInfo.
        :rtype: str
        """
        return self._app_d_version

    @app_d_version.setter
    def app_d_version(self, app_d_version: str):
        """Sets the app_d_version of this ApplicationLocationAvailabilityAppInfo.

        Identifies the version of the application descriptor. It is equivalent to the appDVersion defined in clause 6.2.1.2 of ETSI GS MEC 0102 [1].  # noqa: E501

        :param app_d_version: The app_d_version of this ApplicationLocationAvailabilityAppInfo.
        :type app_d_version: str
        """
        if app_d_version is None:
            raise ValueError("Invalid value for `app_d_version`, must not be `None`")  # noqa: E501

        self._app_d_version = app_d_version

    @property
    def app_description(self) -> str:
        """Gets the app_description of this ApplicationLocationAvailabilityAppInfo.

        Human readable description of the MEC application. The length of the value shall not exceed 128 characters.  # noqa: E501

        :return: The app_description of this ApplicationLocationAvailabilityAppInfo.
        :rtype: str
        """
        return self._app_description

    @app_description.setter
    def app_description(self, app_description: str):
        """Sets the app_description of this ApplicationLocationAvailabilityAppInfo.

        Human readable description of the MEC application. The length of the value shall not exceed 128 characters.  # noqa: E501

        :param app_description: The app_description of this ApplicationLocationAvailabilityAppInfo.
        :type app_description: str
        """

        self._app_description = app_description

    @property
    def app_name(self) -> str:
        """Gets the app_name of this ApplicationLocationAvailabilityAppInfo.

        Name of the MEC application. The length of the value shall not exceed 32 characters.  # noqa: E501

        :return: The app_name of this ApplicationLocationAvailabilityAppInfo.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name: str):
        """Sets the app_name of this ApplicationLocationAvailabilityAppInfo.

        Name of the MEC application. The length of the value shall not exceed 32 characters.  # noqa: E501

        :param app_name: The app_name of this ApplicationLocationAvailabilityAppInfo.
        :type app_name: str
        """
        if app_name is None:
            raise ValueError("Invalid value for `app_name`, must not be `None`")  # noqa: E501

        self._app_name = app_name

    @property
    def app_package_source(self) -> str:
        """Gets the app_package_source of this ApplicationLocationAvailabilityAppInfo.

        URI of the application package. Shall be included in the request. The application package shall comply with the definitions in clause 6.2.1.2 of ETSI GS MEC 0102 [1].  # noqa: E501

        :return: The app_package_source of this ApplicationLocationAvailabilityAppInfo.
        :rtype: str
        """
        return self._app_package_source

    @app_package_source.setter
    def app_package_source(self, app_package_source: str):
        """Sets the app_package_source of this ApplicationLocationAvailabilityAppInfo.

        URI of the application package. Shall be included in the request. The application package shall comply with the definitions in clause 6.2.1.2 of ETSI GS MEC 0102 [1].  # noqa: E501

        :param app_package_source: The app_package_source of this ApplicationLocationAvailabilityAppInfo.
        :type app_package_source: str
        """

        self._app_package_source = app_package_source

    @property
    def app_provider(self) -> str:
        """Gets the app_provider of this ApplicationLocationAvailabilityAppInfo.

        Provider of the MEC application. The length of the value shall not exceed 32 characters.  # noqa: E501

        :return: The app_provider of this ApplicationLocationAvailabilityAppInfo.
        :rtype: str
        """
        return self._app_provider

    @app_provider.setter
    def app_provider(self, app_provider: str):
        """Sets the app_provider of this ApplicationLocationAvailabilityAppInfo.

        Provider of the MEC application. The length of the value shall not exceed 32 characters.  # noqa: E501

        :param app_provider: The app_provider of this ApplicationLocationAvailabilityAppInfo.
        :type app_provider: str
        """
        if app_provider is None:
            raise ValueError("Invalid value for `app_provider`, must not be `None`")  # noqa: E501

        self._app_provider = app_provider

    @property
    def app_soft_version(self) -> str:
        """Gets the app_soft_version of this ApplicationLocationAvailabilityAppInfo.

        Software version of the MEC application. The length of the value shall not exceed 32 characters.  # noqa: E501

        :return: The app_soft_version of this ApplicationLocationAvailabilityAppInfo.
        :rtype: str
        """
        return self._app_soft_version

    @app_soft_version.setter
    def app_soft_version(self, app_soft_version: str):
        """Sets the app_soft_version of this ApplicationLocationAvailabilityAppInfo.

        Software version of the MEC application. The length of the value shall not exceed 32 characters.  # noqa: E501

        :param app_soft_version: The app_soft_version of this ApplicationLocationAvailabilityAppInfo.
        :type app_soft_version: str
        """

        self._app_soft_version = app_soft_version

    @property
    def available_locations(self) -> List[ApplicationLocationAvailabilityAppInfoAvailableLocations]:
        """Gets the available_locations of this ApplicationLocationAvailabilityAppInfo.

        MEC application location constraints.   # noqa: E501

        :return: The available_locations of this ApplicationLocationAvailabilityAppInfo.
        :rtype: List[ApplicationLocationAvailabilityAppInfoAvailableLocations]
        """
        return self._available_locations

    @available_locations.setter
    def available_locations(self, available_locations: List[ApplicationLocationAvailabilityAppInfoAvailableLocations]):
        """Sets the available_locations of this ApplicationLocationAvailabilityAppInfo.

        MEC application location constraints.   # noqa: E501

        :param available_locations: The available_locations of this ApplicationLocationAvailabilityAppInfo.
        :type available_locations: List[ApplicationLocationAvailabilityAppInfoAvailableLocations]
        """

        self._available_locations = available_locations
