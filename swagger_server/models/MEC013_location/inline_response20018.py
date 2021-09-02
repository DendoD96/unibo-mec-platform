# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.MEC013_location.notification_subscription_list import NotificationSubscriptionList  # noqa: F401,E501
from swagger_server import util


class InlineResponse20018(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, notification_subscription_list: NotificationSubscriptionList=None):  # noqa: E501
        """InlineResponse20018 - a model defined in Swagger

        :param notification_subscription_list: The notification_subscription_list of this InlineResponse20018.  # noqa: E501
        :type notification_subscription_list: NotificationSubscriptionList
        """
        self.swagger_types = {
            'notification_subscription_list': NotificationSubscriptionList
        }

        self.attribute_map = {
            'notification_subscription_list': 'notificationSubscriptionList'
        }
        self._notification_subscription_list = notification_subscription_list

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponse20018':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_200_18 of this InlineResponse20018.  # noqa: E501
        :rtype: InlineResponse20018
        """
        return util.deserialize_model(dikt, cls)

    @property
    def notification_subscription_list(self) -> NotificationSubscriptionList:
        """Gets the notification_subscription_list of this InlineResponse20018.


        :return: The notification_subscription_list of this InlineResponse20018.
        :rtype: NotificationSubscriptionList
        """
        return self._notification_subscription_list

    @notification_subscription_list.setter
    def notification_subscription_list(self, notification_subscription_list: NotificationSubscriptionList):
        """Sets the notification_subscription_list of this InlineResponse20018.


        :param notification_subscription_list: The notification_subscription_list of this InlineResponse20018.
        :type notification_subscription_list: NotificationSubscriptionList
        """
        if notification_subscription_list is None:
            raise ValueError("Invalid value for `notification_subscription_list`, must not be `None`")  # noqa: E501

        self._notification_subscription_list = notification_subscription_list
