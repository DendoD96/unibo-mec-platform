# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class CurrentTime(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, seconds: int=None, nano_seconds: int=None, time_source_status: str=None):  # noqa: E501
        """CurrentTime - a model defined in Swagger

        :param seconds: The seconds of this CurrentTime.  # noqa: E501
        :type seconds: int
        :param nano_seconds: The nano_seconds of this CurrentTime.  # noqa: E501
        :type nano_seconds: int
        :param time_source_status: The time_source_status of this CurrentTime.  # noqa: E501
        :type time_source_status: str
        """
        self.swagger_types = {
            'seconds': int,
            'nano_seconds': int,
            'time_source_status': str
        }

        self.attribute_map = {
            'seconds': 'seconds',
            'nano_seconds': 'nanoSeconds',
            'time_source_status': 'timeSourceStatus'
        }
        self._seconds = seconds
        self._nano_seconds = nano_seconds
        self._time_source_status = time_source_status

    @classmethod
    def from_dict(cls, dikt) -> 'CurrentTime':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The CurrentTime of this CurrentTime.  # noqa: E501
        :rtype: CurrentTime
        """
        return util.deserialize_model(dikt, cls)

    @property
    def seconds(self) -> int:
        """Gets the seconds of this CurrentTime.

        The seconds part of the time. Time is defined as Unix-time since January 1, 1970, 00:00:00 UTC  # noqa: E501

        :return: The seconds of this CurrentTime.
        :rtype: int
        """
        return self._seconds

    @seconds.setter
    def seconds(self, seconds: int):
        """Sets the seconds of this CurrentTime.

        The seconds part of the time. Time is defined as Unix-time since January 1, 1970, 00:00:00 UTC  # noqa: E501

        :param seconds: The seconds of this CurrentTime.
        :type seconds: int
        """
        if seconds is None:
            raise ValueError("Invalid value for `seconds`, must not be `None`")  # noqa: E501

        self._seconds = seconds

    @property
    def nano_seconds(self) -> int:
        """Gets the nano_seconds of this CurrentTime.

        The nanoseconds part of the time. Time is defined as Unix-time since January 1, 1970, 00:00:00 UTC  # noqa: E501

        :return: The nano_seconds of this CurrentTime.
        :rtype: int
        """
        return self._nano_seconds

    @nano_seconds.setter
    def nano_seconds(self, nano_seconds: int):
        """Sets the nano_seconds of this CurrentTime.

        The nanoseconds part of the time. Time is defined as Unix-time since January 1, 1970, 00:00:00 UTC  # noqa: E501

        :param nano_seconds: The nano_seconds of this CurrentTime.
        :type nano_seconds: int
        """
        if nano_seconds is None:
            raise ValueError("Invalid value for `nano_seconds`, must not be `None`")  # noqa: E501

        self._nano_seconds = nano_seconds

    @property
    def time_source_status(self) -> str:
        """Gets the time_source_status of this CurrentTime.

        Platform Time Source status. 1 = TRACEABLE - time source is locked to the UTC time source. 2 = NONTRACEABLE - time source is not locked to the UTC time source  # noqa: E501

        :return: The time_source_status of this CurrentTime.
        :rtype: str
        """
        return self._time_source_status

    @time_source_status.setter
    def time_source_status(self, time_source_status: str):
        """Sets the time_source_status of this CurrentTime.

        Platform Time Source status. 1 = TRACEABLE - time source is locked to the UTC time source. 2 = NONTRACEABLE - time source is not locked to the UTC time source  # noqa: E501

        :param time_source_status: The time_source_status of this CurrentTime.
        :type time_source_status: str
        """
        allowed_values = ["TRACEABLE", "NONTRACEABLE"]  # noqa: E501
        if time_source_status not in allowed_values:
            raise ValueError(
                "Invalid value for `time_source_status` ({0}), must be one of {1}"
                .format(time_source_status, allowed_values)
            )

        self._time_source_status = time_source_status
