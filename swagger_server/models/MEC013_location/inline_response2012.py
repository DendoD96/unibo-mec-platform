# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.MEC013_location.periodic_notification_subscription import PeriodicNotificationSubscription  # noqa: F401,E501
from swagger_server import util


class InlineResponse2012(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, periodic_notification_subscription: PeriodicNotificationSubscription=None):  # noqa: E501
        """InlineResponse2012 - a model defined in Swagger

        :param periodic_notification_subscription: The periodic_notification_subscription of this InlineResponse2012.  # noqa: E501
        :type periodic_notification_subscription: PeriodicNotificationSubscription
        """
        self.swagger_types = {
            'periodic_notification_subscription': PeriodicNotificationSubscription
        }

        self.attribute_map = {
            'periodic_notification_subscription': 'periodicNotificationSubscription'
        }
        self._periodic_notification_subscription = periodic_notification_subscription

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponse2012':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_201_2 of this InlineResponse2012.  # noqa: E501
        :rtype: InlineResponse2012
        """
        return util.deserialize_model(dikt, cls)

    @property
    def periodic_notification_subscription(self) -> PeriodicNotificationSubscription:
        """Gets the periodic_notification_subscription of this InlineResponse2012.


        :return: The periodic_notification_subscription of this InlineResponse2012.
        :rtype: PeriodicNotificationSubscription
        """
        return self._periodic_notification_subscription

    @periodic_notification_subscription.setter
    def periodic_notification_subscription(self, periodic_notification_subscription: PeriodicNotificationSubscription):
        """Sets the periodic_notification_subscription of this InlineResponse2012.


        :param periodic_notification_subscription: The periodic_notification_subscription of this InlineResponse2012.
        :type periodic_notification_subscription: PeriodicNotificationSubscription
        """

        self._periodic_notification_subscription = periodic_notification_subscription
