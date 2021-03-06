# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.MEC011_service_management.model_self import ModelSelf  # noqa: F401,E501
from swagger_server.models.MEC011_service_management.ser_availability_notification_subscription_callback_reference import SerAvailabilityNotificationSubscriptionCallbackReference  # noqa: F401,E501
from swagger_server.models.MEC011_service_management.ser_availability_notification_subscription_filtering_criteria import SerAvailabilityNotificationSubscriptionFilteringCriteria  # noqa: F401,E501
from swagger_server.models.MEC011_service_management.ser_availability_notification_subscription_subscription_type import SerAvailabilityNotificationSubscriptionSubscriptionType  # noqa: F401,E501
from swagger_server import util


class SerAvailabilityNotificationSubscription(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, subscription_type: SerAvailabilityNotificationSubscriptionSubscriptionType=None, callback_reference: SerAvailabilityNotificationSubscriptionCallbackReference=None, links: ModelSelf=None, filtering_criteria: SerAvailabilityNotificationSubscriptionFilteringCriteria=None):  # noqa: E501
        """SerAvailabilityNotificationSubscription - a model defined in Swagger

        :param subscription_type: The subscription_type of this SerAvailabilityNotificationSubscription.  # noqa: E501
        :type subscription_type: SerAvailabilityNotificationSubscriptionSubscriptionType
        :param callback_reference: The callback_reference of this SerAvailabilityNotificationSubscription.  # noqa: E501
        :type callback_reference: SerAvailabilityNotificationSubscriptionCallbackReference
        :param links: The links of this SerAvailabilityNotificationSubscription.  # noqa: E501
        :type links: ModelSelf
        :param filtering_criteria: The filtering_criteria of this SerAvailabilityNotificationSubscription.  # noqa: E501
        :type filtering_criteria: SerAvailabilityNotificationSubscriptionFilteringCriteria
        """
        self.swagger_types = {
            'subscription_type': SerAvailabilityNotificationSubscriptionSubscriptionType,
            'callback_reference': SerAvailabilityNotificationSubscriptionCallbackReference,
            'links': ModelSelf,
            'filtering_criteria': SerAvailabilityNotificationSubscriptionFilteringCriteria
        }

        self.attribute_map = {
            'subscription_type': 'subscriptionType',
            'callback_reference': 'callbackReference',
            'links': '_links',
            'filtering_criteria': 'filteringCriteria'
        }
        self._subscription_type = subscription_type
        self._callback_reference = callback_reference
        self._links = links
        self._filtering_criteria = filtering_criteria

    @classmethod
    def from_dict(cls, dikt) -> 'SerAvailabilityNotificationSubscription':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SerAvailabilityNotificationSubscription of this SerAvailabilityNotificationSubscription.  # noqa: E501
        :rtype: SerAvailabilityNotificationSubscription
        """
        return util.deserialize_model(dikt, cls)

    @property
    def subscription_type(self) -> SerAvailabilityNotificationSubscriptionSubscriptionType:
        """Gets the subscription_type of this SerAvailabilityNotificationSubscription.


        :return: The subscription_type of this SerAvailabilityNotificationSubscription.
        :rtype: SerAvailabilityNotificationSubscriptionSubscriptionType
        """
        return self._subscription_type

    @subscription_type.setter
    def subscription_type(self, subscription_type: SerAvailabilityNotificationSubscriptionSubscriptionType):
        """Sets the subscription_type of this SerAvailabilityNotificationSubscription.


        :param subscription_type: The subscription_type of this SerAvailabilityNotificationSubscription.
        :type subscription_type: SerAvailabilityNotificationSubscriptionSubscriptionType
        """
        if subscription_type is None:
            raise ValueError("Invalid value for `subscription_type`, must not be `None`")  # noqa: E501

        self._subscription_type = subscription_type

    @property
    def callback_reference(self) -> SerAvailabilityNotificationSubscriptionCallbackReference:
        """Gets the callback_reference of this SerAvailabilityNotificationSubscription.


        :return: The callback_reference of this SerAvailabilityNotificationSubscription.
        :rtype: SerAvailabilityNotificationSubscriptionCallbackReference
        """
        return self._callback_reference

    @callback_reference.setter
    def callback_reference(self, callback_reference: SerAvailabilityNotificationSubscriptionCallbackReference):
        """Sets the callback_reference of this SerAvailabilityNotificationSubscription.


        :param callback_reference: The callback_reference of this SerAvailabilityNotificationSubscription.
        :type callback_reference: SerAvailabilityNotificationSubscriptionCallbackReference
        """
        if callback_reference is None:
            raise ValueError("Invalid value for `callback_reference`, must not be `None`")  # noqa: E501

        self._callback_reference = callback_reference

    @property
    def links(self) -> ModelSelf:
        """Gets the links of this SerAvailabilityNotificationSubscription.


        :return: The links of this SerAvailabilityNotificationSubscription.
        :rtype: ModelSelf
        """
        return self._links

    @links.setter
    def links(self, links: ModelSelf):
        """Sets the links of this SerAvailabilityNotificationSubscription.


        :param links: The links of this SerAvailabilityNotificationSubscription.
        :type links: ModelSelf
        """
        if links is None:
            raise ValueError("Invalid value for `links`, must not be `None`")  # noqa: E501

        self._links = links

    @property
    def filtering_criteria(self) -> SerAvailabilityNotificationSubscriptionFilteringCriteria:
        """Gets the filtering_criteria of this SerAvailabilityNotificationSubscription.


        :return: The filtering_criteria of this SerAvailabilityNotificationSubscription.
        :rtype: SerAvailabilityNotificationSubscriptionFilteringCriteria
        """
        return self._filtering_criteria

    @filtering_criteria.setter
    def filtering_criteria(self, filtering_criteria: SerAvailabilityNotificationSubscriptionFilteringCriteria):
        """Sets the filtering_criteria of this SerAvailabilityNotificationSubscription.


        :param filtering_criteria: The filtering_criteria of this SerAvailabilityNotificationSubscription.
        :type filtering_criteria: SerAvailabilityNotificationSubscriptionFilteringCriteria
        """

        self._filtering_criteria = filtering_criteria
