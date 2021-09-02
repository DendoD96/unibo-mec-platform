# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.MEC028_wlan_access_information.test_notification_links import TestNotificationLinks  # noqa: F401,E501
from swagger_server import util


class TestNotification(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, links: TestNotificationLinks=None, notification_type: str=None):  # noqa: E501
        """TestNotification - a model defined in Swagger

        :param links: The links of this TestNotification.  # noqa: E501
        :type links: TestNotificationLinks
        :param notification_type: The notification_type of this TestNotification.  # noqa: E501
        :type notification_type: str
        """
        self.swagger_types = {
            'links': TestNotificationLinks,
            'notification_type': str
        }

        self.attribute_map = {
            'links': '_links',
            'notification_type': 'notificationType'
        }
        self._links = links
        self._notification_type = notification_type

    @classmethod
    def from_dict(cls, dikt) -> 'TestNotification':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The TestNotification of this TestNotification.  # noqa: E501
        :rtype: TestNotification
        """
        return util.deserialize_model(dikt, cls)

    @property
    def links(self) -> TestNotificationLinks:
        """Gets the links of this TestNotification.


        :return: The links of this TestNotification.
        :rtype: TestNotificationLinks
        """
        return self._links

    @links.setter
    def links(self, links: TestNotificationLinks):
        """Sets the links of this TestNotification.


        :param links: The links of this TestNotification.
        :type links: TestNotificationLinks
        """
        if links is None:
            raise ValueError("Invalid value for `links`, must not be `None`")  # noqa: E501

        self._links = links

    @property
    def notification_type(self) -> str:
        """Gets the notification_type of this TestNotification.

        Shall be set to \"TestNotification\".  # noqa: E501

        :return: The notification_type of this TestNotification.
        :rtype: str
        """
        return self._notification_type

    @notification_type.setter
    def notification_type(self, notification_type: str):
        """Sets the notification_type of this TestNotification.

        Shall be set to \"TestNotification\".  # noqa: E501

        :param notification_type: The notification_type of this TestNotification.
        :type notification_type: str
        """
        if notification_type is None:
            raise ValueError("Invalid value for `notification_type`, must not be `None`")  # noqa: E501

        self._notification_type = notification_type
