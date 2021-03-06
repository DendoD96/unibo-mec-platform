# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.MEC029_fixed_access_information.onu_alarm_subscription_filter_criteria_onu_alarm import OnuAlarmSubscriptionFilterCriteriaOnuAlarm  # noqa: F401,E501
from swagger_server.models.MEC029_fixed_access_information.onu_alarm_subscription_links import OnuAlarmSubscriptionLinks  # noqa: F401,E501
from swagger_server.models.MEC029_fixed_access_information.time_stamp import TimeStamp  # noqa: F401,E501
from swagger_server import util


class OnuAlarmSubscription(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, links: OnuAlarmSubscriptionLinks=None, callback_reference: str=None, expiry_deadline: TimeStamp=None, filter_criteria_onu_alarm: OnuAlarmSubscriptionFilterCriteriaOnuAlarm=None, subscription_type: str=None):  # noqa: E501
        """OnuAlarmSubscription - a model defined in Swagger

        :param links: The links of this OnuAlarmSubscription.  # noqa: E501
        :type links: OnuAlarmSubscriptionLinks
        :param callback_reference: The callback_reference of this OnuAlarmSubscription.  # noqa: E501
        :type callback_reference: str
        :param expiry_deadline: The expiry_deadline of this OnuAlarmSubscription.  # noqa: E501
        :type expiry_deadline: TimeStamp
        :param filter_criteria_onu_alarm: The filter_criteria_onu_alarm of this OnuAlarmSubscription.  # noqa: E501
        :type filter_criteria_onu_alarm: OnuAlarmSubscriptionFilterCriteriaOnuAlarm
        :param subscription_type: The subscription_type of this OnuAlarmSubscription.  # noqa: E501
        :type subscription_type: str
        """
        self.swagger_types = {
            'links': OnuAlarmSubscriptionLinks,
            'callback_reference': str,
            'expiry_deadline': TimeStamp,
            'filter_criteria_onu_alarm': OnuAlarmSubscriptionFilterCriteriaOnuAlarm,
            'subscription_type': str
        }

        self.attribute_map = {
            'links': '_links',
            'callback_reference': 'callbackReference',
            'expiry_deadline': 'expiryDeadline',
            'filter_criteria_onu_alarm': 'filterCriteriaOnuAlarm',
            'subscription_type': 'subscriptionType'
        }
        self._links = links
        self._callback_reference = callback_reference
        self._expiry_deadline = expiry_deadline
        self._filter_criteria_onu_alarm = filter_criteria_onu_alarm
        self._subscription_type = subscription_type

    @classmethod
    def from_dict(cls, dikt) -> 'OnuAlarmSubscription':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The OnuAlarmSubscription of this OnuAlarmSubscription.  # noqa: E501
        :rtype: OnuAlarmSubscription
        """
        return util.deserialize_model(dikt, cls)

    @property
    def links(self) -> OnuAlarmSubscriptionLinks:
        """Gets the links of this OnuAlarmSubscription.


        :return: The links of this OnuAlarmSubscription.
        :rtype: OnuAlarmSubscriptionLinks
        """
        return self._links

    @links.setter
    def links(self, links: OnuAlarmSubscriptionLinks):
        """Sets the links of this OnuAlarmSubscription.


        :param links: The links of this OnuAlarmSubscription.
        :type links: OnuAlarmSubscriptionLinks
        """

        self._links = links

    @property
    def callback_reference(self) -> str:
        """Gets the callback_reference of this OnuAlarmSubscription.

        URI selected by the service consumer to receive notifications on the subscribed FAIS information. This shall be included both in the request and in response.  # noqa: E501

        :return: The callback_reference of this OnuAlarmSubscription.
        :rtype: str
        """
        return self._callback_reference

    @callback_reference.setter
    def callback_reference(self, callback_reference: str):
        """Sets the callback_reference of this OnuAlarmSubscription.

        URI selected by the service consumer to receive notifications on the subscribed FAIS information. This shall be included both in the request and in response.  # noqa: E501

        :param callback_reference: The callback_reference of this OnuAlarmSubscription.
        :type callback_reference: str
        """
        if callback_reference is None:
            raise ValueError("Invalid value for `callback_reference`, must not be `None`")  # noqa: E501

        self._callback_reference = callback_reference

    @property
    def expiry_deadline(self) -> TimeStamp:
        """Gets the expiry_deadline of this OnuAlarmSubscription.


        :return: The expiry_deadline of this OnuAlarmSubscription.
        :rtype: TimeStamp
        """
        return self._expiry_deadline

    @expiry_deadline.setter
    def expiry_deadline(self, expiry_deadline: TimeStamp):
        """Sets the expiry_deadline of this OnuAlarmSubscription.


        :param expiry_deadline: The expiry_deadline of this OnuAlarmSubscription.
        :type expiry_deadline: TimeStamp
        """

        self._expiry_deadline = expiry_deadline

    @property
    def filter_criteria_onu_alarm(self) -> OnuAlarmSubscriptionFilterCriteriaOnuAlarm:
        """Gets the filter_criteria_onu_alarm of this OnuAlarmSubscription.


        :return: The filter_criteria_onu_alarm of this OnuAlarmSubscription.
        :rtype: OnuAlarmSubscriptionFilterCriteriaOnuAlarm
        """
        return self._filter_criteria_onu_alarm

    @filter_criteria_onu_alarm.setter
    def filter_criteria_onu_alarm(self, filter_criteria_onu_alarm: OnuAlarmSubscriptionFilterCriteriaOnuAlarm):
        """Sets the filter_criteria_onu_alarm of this OnuAlarmSubscription.


        :param filter_criteria_onu_alarm: The filter_criteria_onu_alarm of this OnuAlarmSubscription.
        :type filter_criteria_onu_alarm: OnuAlarmSubscriptionFilterCriteriaOnuAlarm
        """
        if filter_criteria_onu_alarm is None:
            raise ValueError("Invalid value for `filter_criteria_onu_alarm`, must not be `None`")  # noqa: E501

        self._filter_criteria_onu_alarm = filter_criteria_onu_alarm

    @property
    def subscription_type(self) -> str:
        """Gets the subscription_type of this OnuAlarmSubscription.

        Shall be set to \\\"OnuAlarmSubscription\\\".  # noqa: E501

        :return: The subscription_type of this OnuAlarmSubscription.
        :rtype: str
        """
        return self._subscription_type

    @subscription_type.setter
    def subscription_type(self, subscription_type: str):
        """Sets the subscription_type of this OnuAlarmSubscription.

        Shall be set to \\\"OnuAlarmSubscription\\\".  # noqa: E501

        :param subscription_type: The subscription_type of this OnuAlarmSubscription.
        :type subscription_type: str
        """
        if subscription_type is None:
            raise ValueError("Invalid value for `subscription_type`, must not be `None`")  # noqa: E501

        self._subscription_type = subscription_type
