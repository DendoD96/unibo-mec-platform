# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.MEC016_device_application_interface.application_location_availability_app_info import ApplicationLocationAvailabilityAppInfo  # noqa: F401,E501
from swagger_server import util


class ApplicationLocationAvailability(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, app_info: ApplicationLocationAvailabilityAppInfo=None, associate_dev_app_id: str=None):  # noqa: E501
        """ApplicationLocationAvailability - a model defined in Swagger

        :param app_info: The app_info of this ApplicationLocationAvailability.  # noqa: E501
        :type app_info: ApplicationLocationAvailabilityAppInfo
        :param associate_dev_app_id: The associate_dev_app_id of this ApplicationLocationAvailability.  # noqa: E501
        :type associate_dev_app_id: str
        """
        self.swagger_types = {
            'app_info': ApplicationLocationAvailabilityAppInfo,
            'associate_dev_app_id': str
        }

        self.attribute_map = {
            'app_info': 'appInfo',
            'associate_dev_app_id': 'associateDevAppId'
        }
        self._app_info = app_info
        self._associate_dev_app_id = associate_dev_app_id

    @classmethod
    def from_dict(cls, dikt) -> 'ApplicationLocationAvailability':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ApplicationLocationAvailability of this ApplicationLocationAvailability.  # noqa: E501
        :rtype: ApplicationLocationAvailability
        """
        return util.deserialize_model(dikt, cls)

    @property
    def app_info(self) -> ApplicationLocationAvailabilityAppInfo:
        """Gets the app_info of this ApplicationLocationAvailability.


        :return: The app_info of this ApplicationLocationAvailability.
        :rtype: ApplicationLocationAvailabilityAppInfo
        """
        return self._app_info

    @app_info.setter
    def app_info(self, app_info: ApplicationLocationAvailabilityAppInfo):
        """Sets the app_info of this ApplicationLocationAvailability.


        :param app_info: The app_info of this ApplicationLocationAvailability.
        :type app_info: ApplicationLocationAvailabilityAppInfo
        """
        if app_info is None:
            raise ValueError("Invalid value for `app_info`, must not be `None`")  # noqa: E501

        self._app_info = app_info

    @property
    def associate_dev_app_id(self) -> str:
        """Gets the associate_dev_app_id of this ApplicationLocationAvailability.

        Uniquely identifies the device application. The length of the value shall not exceed 32 characters.  # noqa: E501

        :return: The associate_dev_app_id of this ApplicationLocationAvailability.
        :rtype: str
        """
        return self._associate_dev_app_id

    @associate_dev_app_id.setter
    def associate_dev_app_id(self, associate_dev_app_id: str):
        """Sets the associate_dev_app_id of this ApplicationLocationAvailability.

        Uniquely identifies the device application. The length of the value shall not exceed 32 characters.  # noqa: E501

        :param associate_dev_app_id: The associate_dev_app_id of this ApplicationLocationAvailability.
        :type associate_dev_app_id: str
        """
        if associate_dev_app_id is None:
            raise ValueError("Invalid value for `associate_dev_app_id`, must not be `None`")  # noqa: E501

        self._associate_dev_app_id = associate_dev_app_id
