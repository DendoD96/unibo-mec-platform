# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.MEC012_radio_network_information.expiry_notification_links import ExpiryNotificationLinks  # noqa: F401,E501
from swagger_server.models.MEC012_radio_network_information.time_stamp import TimeStamp  # noqa: F401,E501
from swagger_server import util


class ExpiryNotification(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, links: ExpiryNotificationLinks=None, expiry_deadline: TimeStamp=None, time_stamp: TimeStamp=None):  # noqa: E501
        """ExpiryNotification - a model defined in Swagger

        :param links: The links of this ExpiryNotification.  # noqa: E501
        :type links: ExpiryNotificationLinks
        :param expiry_deadline: The expiry_deadline of this ExpiryNotification.  # noqa: E501
        :type expiry_deadline: TimeStamp
        :param time_stamp: The time_stamp of this ExpiryNotification.  # noqa: E501
        :type time_stamp: TimeStamp
        """
        self.swagger_types = {
            'links': ExpiryNotificationLinks,
            'expiry_deadline': TimeStamp,
            'time_stamp': TimeStamp
        }

        self.attribute_map = {
            'links': '_links',
            'expiry_deadline': 'expiryDeadline',
            'time_stamp': 'timeStamp'
        }
        self._links = links
        self._expiry_deadline = expiry_deadline
        self._time_stamp = time_stamp

    @classmethod
    def from_dict(cls, dikt) -> 'ExpiryNotification':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ExpiryNotification of this ExpiryNotification.  # noqa: E501
        :rtype: ExpiryNotification
        """
        return util.deserialize_model(dikt, cls)

    @property
    def links(self) -> ExpiryNotificationLinks:
        """Gets the links of this ExpiryNotification.


        :return: The links of this ExpiryNotification.
        :rtype: ExpiryNotificationLinks
        """
        return self._links

    @links.setter
    def links(self, links: ExpiryNotificationLinks):
        """Sets the links of this ExpiryNotification.


        :param links: The links of this ExpiryNotification.
        :type links: ExpiryNotificationLinks
        """
        if links is None:
            raise ValueError("Invalid value for `links`, must not be `None`")  # noqa: E501

        self._links = links

    @property
    def expiry_deadline(self) -> TimeStamp:
        """Gets the expiry_deadline of this ExpiryNotification.


        :return: The expiry_deadline of this ExpiryNotification.
        :rtype: TimeStamp
        """
        return self._expiry_deadline

    @expiry_deadline.setter
    def expiry_deadline(self, expiry_deadline: TimeStamp):
        """Sets the expiry_deadline of this ExpiryNotification.


        :param expiry_deadline: The expiry_deadline of this ExpiryNotification.
        :type expiry_deadline: TimeStamp
        """
        if expiry_deadline is None:
            raise ValueError("Invalid value for `expiry_deadline`, must not be `None`")  # noqa: E501

        self._expiry_deadline = expiry_deadline

    @property
    def time_stamp(self) -> TimeStamp:
        """Gets the time_stamp of this ExpiryNotification.


        :return: The time_stamp of this ExpiryNotification.
        :rtype: TimeStamp
        """
        return self._time_stamp

    @time_stamp.setter
    def time_stamp(self, time_stamp: TimeStamp):
        """Sets the time_stamp of this ExpiryNotification.


        :param time_stamp: The time_stamp of this ExpiryNotification.
        :type time_stamp: TimeStamp
        """

        self._time_stamp = time_stamp