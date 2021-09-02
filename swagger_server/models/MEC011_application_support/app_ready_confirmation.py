# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.MEC011_application_support.ready_indication_type import ReadyIndicationType  # noqa: F401,E501
from swagger_server import util


class AppReadyConfirmation(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, indication: ReadyIndicationType=None):  # noqa: E501
        """AppReadyConfirmation - a model defined in Swagger

        :param indication: The indication of this AppReadyConfirmation.  # noqa: E501
        :type indication: ReadyIndicationType
        """
        self.swagger_types = {
            'indication': ReadyIndicationType
        }

        self.attribute_map = {
            'indication': 'indication'
        }
        self._indication = indication

    @classmethod
    def from_dict(cls, dikt) -> 'AppReadyConfirmation':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AppReadyConfirmation of this AppReadyConfirmation.  # noqa: E501
        :rtype: AppReadyConfirmation
        """
        return util.deserialize_model(dikt, cls)

    @property
    def indication(self) -> ReadyIndicationType:
        """Gets the indication of this AppReadyConfirmation.


        :return: The indication of this AppReadyConfirmation.
        :rtype: ReadyIndicationType
        """
        return self._indication

    @indication.setter
    def indication(self, indication: ReadyIndicationType):
        """Sets the indication of this AppReadyConfirmation.


        :param indication: The indication of this AppReadyConfirmation.
        :type indication: ReadyIndicationType
        """
        if indication is None:
            raise ValueError("Invalid value for `indication`, must not be `None`")  # noqa: E501

        self._indication = indication