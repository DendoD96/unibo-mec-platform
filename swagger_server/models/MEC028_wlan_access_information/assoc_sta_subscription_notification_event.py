# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class AssocStaSubscriptionNotificationEvent(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, threshold: int=None, trigger: int=None):  # noqa: E501
        """AssocStaSubscriptionNotificationEvent - a model defined in Swagger

        :param threshold: The threshold of this AssocStaSubscriptionNotificationEvent.  # noqa: E501
        :type threshold: int
        :param trigger: The trigger of this AssocStaSubscriptionNotificationEvent.  # noqa: E501
        :type trigger: int
        """
        self.swagger_types = {
            'threshold': int,
            'trigger': int
        }

        self.attribute_map = {
            'threshold': 'threshold',
            'trigger': 'trigger'
        }
        self._threshold = threshold
        self._trigger = trigger

    @classmethod
    def from_dict(cls, dikt) -> 'AssocStaSubscriptionNotificationEvent':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AssocStaSubscription_notificationEvent of this AssocStaSubscriptionNotificationEvent.  # noqa: E501
        :rtype: AssocStaSubscriptionNotificationEvent
        """
        return util.deserialize_model(dikt, cls)

    @property
    def threshold(self) -> int:
        """Gets the threshold of this AssocStaSubscriptionNotificationEvent.

        Number of connected stations threshold for trigger-based event reporting.  # noqa: E501

        :return: The threshold of this AssocStaSubscriptionNotificationEvent.
        :rtype: int
        """
        return self._threshold

    @threshold.setter
    def threshold(self, threshold: int):
        """Sets the threshold of this AssocStaSubscriptionNotificationEvent.

        Number of connected stations threshold for trigger-based event reporting.  # noqa: E501

        :param threshold: The threshold of this AssocStaSubscriptionNotificationEvent.
        :type threshold: int
        """
        if threshold is None:
            raise ValueError("Invalid value for `threshold`, must not be `None`")  # noqa: E501

        self._threshold = threshold

    @property
    def trigger(self) -> int:
        """Gets the trigger of this AssocStaSubscriptionNotificationEvent.

        Trigger for the notification: 1 = Notification issued when the number of connected stations is greater than or equal to the threshold. 2 = Notification issued when the number of connected stations is less than or equal to the threshold.  # noqa: E501

        :return: The trigger of this AssocStaSubscriptionNotificationEvent.
        :rtype: int
        """
        return self._trigger

    @trigger.setter
    def trigger(self, trigger: int):
        """Sets the trigger of this AssocStaSubscriptionNotificationEvent.

        Trigger for the notification: 1 = Notification issued when the number of connected stations is greater than or equal to the threshold. 2 = Notification issued when the number of connected stations is less than or equal to the threshold.  # noqa: E501

        :param trigger: The trigger of this AssocStaSubscriptionNotificationEvent.
        :type trigger: int
        """
        allowed_values = ["1", "2"]  # noqa: E501
        if trigger not in allowed_values:
            raise ValueError(
                "Invalid value for `trigger` ({0}), must be one of {1}"
                .format(trigger, allowed_values)
            )

        self._trigger = trigger
