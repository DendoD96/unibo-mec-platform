# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.MEC013_location.distance_notification_subscription import DistanceNotificationSubscription  # noqa: F401,E501
from swagger_server import util


class InlineResponse2011(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, distance_notification_subscription: DistanceNotificationSubscription=None):  # noqa: E501
        """InlineResponse2011 - a model defined in Swagger

        :param distance_notification_subscription: The distance_notification_subscription of this InlineResponse2011.  # noqa: E501
        :type distance_notification_subscription: DistanceNotificationSubscription
        """
        self.swagger_types = {
            'distance_notification_subscription': DistanceNotificationSubscription
        }

        self.attribute_map = {
            'distance_notification_subscription': 'distanceNotificationSubscription'
        }
        self._distance_notification_subscription = distance_notification_subscription

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponse2011':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_201_1 of this InlineResponse2011.  # noqa: E501
        :rtype: InlineResponse2011
        """
        return util.deserialize_model(dikt, cls)

    @property
    def distance_notification_subscription(self) -> DistanceNotificationSubscription:
        """Gets the distance_notification_subscription of this InlineResponse2011.


        :return: The distance_notification_subscription of this InlineResponse2011.
        :rtype: DistanceNotificationSubscription
        """
        return self._distance_notification_subscription

    @distance_notification_subscription.setter
    def distance_notification_subscription(self, distance_notification_subscription: DistanceNotificationSubscription):
        """Sets the distance_notification_subscription of this InlineResponse2011.


        :param distance_notification_subscription: The distance_notification_subscription of this InlineResponse2011.
        :type distance_notification_subscription: DistanceNotificationSubscription
        """

        self._distance_notification_subscription = distance_notification_subscription