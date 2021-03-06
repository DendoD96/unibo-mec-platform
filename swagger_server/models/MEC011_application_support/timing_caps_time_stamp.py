# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class TimingCapsTimeStamp(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, seconds: int=None, nano_seconds: int=None):  # noqa: E501
        """TimingCapsTimeStamp - a model defined in Swagger

        :param seconds: The seconds of this TimingCapsTimeStamp.  # noqa: E501
        :type seconds: int
        :param nano_seconds: The nano_seconds of this TimingCapsTimeStamp.  # noqa: E501
        :type nano_seconds: int
        """
        self.swagger_types = {
            'seconds': int,
            'nano_seconds': int
        }

        self.attribute_map = {
            'seconds': 'seconds',
            'nano_seconds': 'nanoSeconds'
        }
        self._seconds = seconds
        self._nano_seconds = nano_seconds

    @classmethod
    def from_dict(cls, dikt) -> 'TimingCapsTimeStamp':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The TimingCaps.TimeStamp of this TimingCapsTimeStamp.  # noqa: E501
        :rtype: TimingCapsTimeStamp
        """
        return util.deserialize_model(dikt, cls)

    @property
    def seconds(self) -> int:
        """Gets the seconds of this TimingCapsTimeStamp.

        The seconds part of the time. Time is defined as Unix-time since January 1, 1970, 00:00:00 UTC  # noqa: E501

        :return: The seconds of this TimingCapsTimeStamp.
        :rtype: int
        """
        return self._seconds

    @seconds.setter
    def seconds(self, seconds: int):
        """Sets the seconds of this TimingCapsTimeStamp.

        The seconds part of the time. Time is defined as Unix-time since January 1, 1970, 00:00:00 UTC  # noqa: E501

        :param seconds: The seconds of this TimingCapsTimeStamp.
        :type seconds: int
        """
        if seconds is None:
            raise ValueError("Invalid value for `seconds`, must not be `None`")  # noqa: E501

        self._seconds = seconds

    @property
    def nano_seconds(self) -> int:
        """Gets the nano_seconds of this TimingCapsTimeStamp.

        The nanoseconds part of the time. Time is defined as Unix-time since January 1, 1970, 00:00:00 UTC  # noqa: E501

        :return: The nano_seconds of this TimingCapsTimeStamp.
        :rtype: int
        """
        return self._nano_seconds

    @nano_seconds.setter
    def nano_seconds(self, nano_seconds: int):
        """Sets the nano_seconds of this TimingCapsTimeStamp.

        The nanoseconds part of the time. Time is defined as Unix-time since January 1, 1970, 00:00:00 UTC  # noqa: E501

        :param nano_seconds: The nano_seconds of this TimingCapsTimeStamp.
        :type nano_seconds: int
        """
        if nano_seconds is None:
            raise ValueError("Invalid value for `nano_seconds`, must not be `None`")  # noqa: E501

        self._nano_seconds = nano_seconds
