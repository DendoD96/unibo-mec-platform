# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.MEC013_location.circle_notification_subscription import CircleNotificationSubscription  # noqa: F401,E501
from swagger_server import util


class AreaCircleBody(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, circle_notification_subscription: CircleNotificationSubscription=None):  # noqa: E501
        """AreaCircleBody - a model defined in Swagger

        :param circle_notification_subscription: The circle_notification_subscription of this AreaCircleBody.  # noqa: E501
        :type circle_notification_subscription: CircleNotificationSubscription
        """
        self.swagger_types = {
            'circle_notification_subscription': CircleNotificationSubscription
        }

        self.attribute_map = {
            'circle_notification_subscription': 'circleNotificationSubscription'
        }
        self._circle_notification_subscription = circle_notification_subscription

    @classmethod
    def from_dict(cls, dikt) -> 'AreaCircleBody':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The area_circle_body of this AreaCircleBody.  # noqa: E501
        :rtype: AreaCircleBody
        """
        return util.deserialize_model(dikt, cls)

    @property
    def circle_notification_subscription(self) -> CircleNotificationSubscription:
        """Gets the circle_notification_subscription of this AreaCircleBody.


        :return: The circle_notification_subscription of this AreaCircleBody.
        :rtype: CircleNotificationSubscription
        """
        return self._circle_notification_subscription

    @circle_notification_subscription.setter
    def circle_notification_subscription(self, circle_notification_subscription: CircleNotificationSubscription):
        """Sets the circle_notification_subscription of this AreaCircleBody.


        :param circle_notification_subscription: The circle_notification_subscription of this AreaCircleBody.
        :type circle_notification_subscription: CircleNotificationSubscription
        """

        self._circle_notification_subscription = circle_notification_subscription
