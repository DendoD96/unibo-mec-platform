# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class BwInfoTimeStamp(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, nano_seconds: int=None, seconds: int=None):  # noqa: E501
        """BwInfoTimeStamp - a model defined in Swagger

        :param nano_seconds: The nano_seconds of this BwInfoTimeStamp.  # noqa: E501
        :type nano_seconds: int
        :param seconds: The seconds of this BwInfoTimeStamp.  # noqa: E501
        :type seconds: int
        """
        self.swagger_types = {
            'nano_seconds': int,
            'seconds': int
        }

        self.attribute_map = {
            'nano_seconds': 'nanoSeconds',
            'seconds': 'seconds'
        }
        self._nano_seconds = nano_seconds
        self._seconds = seconds

    @classmethod
    def from_dict(cls, dikt) -> 'BwInfoTimeStamp':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The BwInfo_timeStamp of this BwInfoTimeStamp.  # noqa: E501
        :rtype: BwInfoTimeStamp
        """
        return util.deserialize_model(dikt, cls)

    @property
    def nano_seconds(self) -> int:
        """Gets the nano_seconds of this BwInfoTimeStamp.

        The nanoseconds part of the Time. Time is defined as Unix-time since January 1, 1970, 00:00:00 UTC  # noqa: E501

        :return: The nano_seconds of this BwInfoTimeStamp.
        :rtype: int
        """
        return self._nano_seconds

    @nano_seconds.setter
    def nano_seconds(self, nano_seconds: int):
        """Sets the nano_seconds of this BwInfoTimeStamp.

        The nanoseconds part of the Time. Time is defined as Unix-time since January 1, 1970, 00:00:00 UTC  # noqa: E501

        :param nano_seconds: The nano_seconds of this BwInfoTimeStamp.
        :type nano_seconds: int
        """
        if nano_seconds is None:
            raise ValueError("Invalid value for `nano_seconds`, must not be `None`")  # noqa: E501

        self._nano_seconds = nano_seconds

    @property
    def seconds(self) -> int:
        """Gets the seconds of this BwInfoTimeStamp.

        The seconds part of the Time. Time is defined as Unixtime since January 1, 1970, 00:00:00 UTC  # noqa: E501

        :return: The seconds of this BwInfoTimeStamp.
        :rtype: int
        """
        return self._seconds

    @seconds.setter
    def seconds(self, seconds: int):
        """Sets the seconds of this BwInfoTimeStamp.

        The seconds part of the Time. Time is defined as Unixtime since January 1, 1970, 00:00:00 UTC  # noqa: E501

        :param seconds: The seconds of this BwInfoTimeStamp.
        :type seconds: int
        """
        if seconds is None:
            raise ValueError("Invalid value for `seconds`, must not be `None`")  # noqa: E501

        self._seconds = seconds
