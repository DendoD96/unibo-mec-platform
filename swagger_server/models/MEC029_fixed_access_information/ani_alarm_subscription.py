# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.MEC029_fixed_access_information.ani_alarm_subscription_filter_criteria_ani_alarm import AniAlarmSubscriptionFilterCriteriaAniAlarm  # noqa: F401,E501
from swagger_server.models.MEC029_fixed_access_information.ani_alarm_subscription_links import AniAlarmSubscriptionLinks  # noqa: F401,E501
from swagger_server.models.MEC029_fixed_access_information.time_stamp import TimeStamp  # noqa: F401,E501
from swagger_server import util


class AniAlarmSubscription(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, subscription_type: str=None, links: AniAlarmSubscriptionLinks=None, ani_index: str=None, callback_reference: str=None, expiry_deadline: TimeStamp=None, filter_criteria_ani_alarm: AniAlarmSubscriptionFilterCriteriaAniAlarm=None):  # noqa: E501
        """AniAlarmSubscription - a model defined in Swagger

        :param subscription_type: The subscription_type of this AniAlarmSubscription.  # noqa: E501
        :type subscription_type: str
        :param links: The links of this AniAlarmSubscription.  # noqa: E501
        :type links: AniAlarmSubscriptionLinks
        :param ani_index: The ani_index of this AniAlarmSubscription.  # noqa: E501
        :type ani_index: str
        :param callback_reference: The callback_reference of this AniAlarmSubscription.  # noqa: E501
        :type callback_reference: str
        :param expiry_deadline: The expiry_deadline of this AniAlarmSubscription.  # noqa: E501
        :type expiry_deadline: TimeStamp
        :param filter_criteria_ani_alarm: The filter_criteria_ani_alarm of this AniAlarmSubscription.  # noqa: E501
        :type filter_criteria_ani_alarm: AniAlarmSubscriptionFilterCriteriaAniAlarm
        """
        self.swagger_types = {
            'subscription_type': str,
            'links': AniAlarmSubscriptionLinks,
            'ani_index': str,
            'callback_reference': str,
            'expiry_deadline': TimeStamp,
            'filter_criteria_ani_alarm': AniAlarmSubscriptionFilterCriteriaAniAlarm
        }

        self.attribute_map = {
            'subscription_type': 'subscriptionType',
            'links': '_links',
            'ani_index': 'aniIndex',
            'callback_reference': 'callbackReference',
            'expiry_deadline': 'expiryDeadline',
            'filter_criteria_ani_alarm': 'filterCriteriaAniAlarm'
        }
        self._subscription_type = subscription_type
        self._links = links
        self._ani_index = ani_index
        self._callback_reference = callback_reference
        self._expiry_deadline = expiry_deadline
        self._filter_criteria_ani_alarm = filter_criteria_ani_alarm

    @classmethod
    def from_dict(cls, dikt) -> 'AniAlarmSubscription':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AniAlarmSubscription of this AniAlarmSubscription.  # noqa: E501
        :rtype: AniAlarmSubscription
        """
        return util.deserialize_model(dikt, cls)

    @property
    def subscription_type(self) -> str:
        """Gets the subscription_type of this AniAlarmSubscription.

        Shall be set to \\\"AniAlarmSubscription\\\"  # noqa: E501

        :return: The subscription_type of this AniAlarmSubscription.
        :rtype: str
        """
        return self._subscription_type

    @subscription_type.setter
    def subscription_type(self, subscription_type: str):
        """Sets the subscription_type of this AniAlarmSubscription.

        Shall be set to \\\"AniAlarmSubscription\\\"  # noqa: E501

        :param subscription_type: The subscription_type of this AniAlarmSubscription.
        :type subscription_type: str
        """
        if subscription_type is None:
            raise ValueError("Invalid value for `subscription_type`, must not be `None`")  # noqa: E501

        self._subscription_type = subscription_type

    @property
    def links(self) -> AniAlarmSubscriptionLinks:
        """Gets the links of this AniAlarmSubscription.


        :return: The links of this AniAlarmSubscription.
        :rtype: AniAlarmSubscriptionLinks
        """
        return self._links

    @links.setter
    def links(self, links: AniAlarmSubscriptionLinks):
        """Sets the links of this AniAlarmSubscription.


        :param links: The links of this AniAlarmSubscription.
        :type links: AniAlarmSubscriptionLinks
        """

        self._links = links

    @property
    def ani_index(self) -> str:
        """Gets the ani_index of this AniAlarmSubscription.

        The index of an access network interface supported by the optical network unit.  # noqa: E501

        :return: The ani_index of this AniAlarmSubscription.
        :rtype: str
        """
        return self._ani_index

    @ani_index.setter
    def ani_index(self, ani_index: str):
        """Sets the ani_index of this AniAlarmSubscription.

        The index of an access network interface supported by the optical network unit.  # noqa: E501

        :param ani_index: The ani_index of this AniAlarmSubscription.
        :type ani_index: str
        """
        if ani_index is None:
            raise ValueError("Invalid value for `ani_index`, must not be `None`")  # noqa: E501

        self._ani_index = ani_index

    @property
    def callback_reference(self) -> str:
        """Gets the callback_reference of this AniAlarmSubscription.

        URI selected by the service consumer to receive notifications on the subscribed FAIS information. This shall be included both in the request and in response.  # noqa: E501

        :return: The callback_reference of this AniAlarmSubscription.
        :rtype: str
        """
        return self._callback_reference

    @callback_reference.setter
    def callback_reference(self, callback_reference: str):
        """Sets the callback_reference of this AniAlarmSubscription.

        URI selected by the service consumer to receive notifications on the subscribed FAIS information. This shall be included both in the request and in response.  # noqa: E501

        :param callback_reference: The callback_reference of this AniAlarmSubscription.
        :type callback_reference: str
        """
        if callback_reference is None:
            raise ValueError("Invalid value for `callback_reference`, must not be `None`")  # noqa: E501

        self._callback_reference = callback_reference

    @property
    def expiry_deadline(self) -> TimeStamp:
        """Gets the expiry_deadline of this AniAlarmSubscription.


        :return: The expiry_deadline of this AniAlarmSubscription.
        :rtype: TimeStamp
        """
        return self._expiry_deadline

    @expiry_deadline.setter
    def expiry_deadline(self, expiry_deadline: TimeStamp):
        """Sets the expiry_deadline of this AniAlarmSubscription.


        :param expiry_deadline: The expiry_deadline of this AniAlarmSubscription.
        :type expiry_deadline: TimeStamp
        """

        self._expiry_deadline = expiry_deadline

    @property
    def filter_criteria_ani_alarm(self) -> AniAlarmSubscriptionFilterCriteriaAniAlarm:
        """Gets the filter_criteria_ani_alarm of this AniAlarmSubscription.


        :return: The filter_criteria_ani_alarm of this AniAlarmSubscription.
        :rtype: AniAlarmSubscriptionFilterCriteriaAniAlarm
        """
        return self._filter_criteria_ani_alarm

    @filter_criteria_ani_alarm.setter
    def filter_criteria_ani_alarm(self, filter_criteria_ani_alarm: AniAlarmSubscriptionFilterCriteriaAniAlarm):
        """Sets the filter_criteria_ani_alarm of this AniAlarmSubscription.


        :param filter_criteria_ani_alarm: The filter_criteria_ani_alarm of this AniAlarmSubscription.
        :type filter_criteria_ani_alarm: AniAlarmSubscriptionFilterCriteriaAniAlarm
        """
        if filter_criteria_ani_alarm is None:
            raise ValueError("Invalid value for `filter_criteria_ani_alarm`, must not be `None`")  # noqa: E501

        self._filter_criteria_ani_alarm = filter_criteria_ani_alarm
