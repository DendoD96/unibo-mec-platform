# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.MEC012_radio_network_information.ca_reconf_subscription_links import CaReconfSubscriptionLinks  # noqa: F401,E501
from swagger_server.models.MEC012_radio_network_information.enum import Enum  # noqa: F401,E501
from swagger_server.models.MEC012_radio_network_information.s1_bearer_subscription_s1_bearer_subscription_criteria import S1BearerSubscriptionS1BearerSubscriptionCriteria  # noqa: F401,E501
from swagger_server.models.MEC012_radio_network_information.time_stamp import TimeStamp  # noqa: F401,E501
from swagger_server import util


class S1BearerSubscription(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, s1_bearer_subscription_criteria: S1BearerSubscriptionS1BearerSubscriptionCriteria=None, links: CaReconfSubscriptionLinks=None, callback_reference: str=None, event_type: List[Enum]=None, expiry_deadline: TimeStamp=None, subscription_type: str=None):  # noqa: E501
        """S1BearerSubscription - a model defined in Swagger

        :param s1_bearer_subscription_criteria: The s1_bearer_subscription_criteria of this S1BearerSubscription.  # noqa: E501
        :type s1_bearer_subscription_criteria: S1BearerSubscriptionS1BearerSubscriptionCriteria
        :param links: The links of this S1BearerSubscription.  # noqa: E501
        :type links: CaReconfSubscriptionLinks
        :param callback_reference: The callback_reference of this S1BearerSubscription.  # noqa: E501
        :type callback_reference: str
        :param event_type: The event_type of this S1BearerSubscription.  # noqa: E501
        :type event_type: List[Enum]
        :param expiry_deadline: The expiry_deadline of this S1BearerSubscription.  # noqa: E501
        :type expiry_deadline: TimeStamp
        :param subscription_type: The subscription_type of this S1BearerSubscription.  # noqa: E501
        :type subscription_type: str
        """
        self.swagger_types = {
            's1_bearer_subscription_criteria': S1BearerSubscriptionS1BearerSubscriptionCriteria,
            'links': CaReconfSubscriptionLinks,
            'callback_reference': str,
            'event_type': List[Enum],
            'expiry_deadline': TimeStamp,
            'subscription_type': str
        }

        self.attribute_map = {
            's1_bearer_subscription_criteria': 'S1BearerSubscriptionCriteria',
            'links': '_links',
            'callback_reference': 'callbackReference',
            'event_type': 'eventType',
            'expiry_deadline': 'expiryDeadline',
            'subscription_type': 'subscriptionType'
        }
        self._s1_bearer_subscription_criteria = s1_bearer_subscription_criteria
        self._links = links
        self._callback_reference = callback_reference
        self._event_type = event_type
        self._expiry_deadline = expiry_deadline
        self._subscription_type = subscription_type

    @classmethod
    def from_dict(cls, dikt) -> 'S1BearerSubscription':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The S1BearerSubscription of this S1BearerSubscription.  # noqa: E501
        :rtype: S1BearerSubscription
        """
        return util.deserialize_model(dikt, cls)

    @property
    def s1_bearer_subscription_criteria(self) -> S1BearerSubscriptionS1BearerSubscriptionCriteria:
        """Gets the s1_bearer_subscription_criteria of this S1BearerSubscription.


        :return: The s1_bearer_subscription_criteria of this S1BearerSubscription.
        :rtype: S1BearerSubscriptionS1BearerSubscriptionCriteria
        """
        return self._s1_bearer_subscription_criteria

    @s1_bearer_subscription_criteria.setter
    def s1_bearer_subscription_criteria(self, s1_bearer_subscription_criteria: S1BearerSubscriptionS1BearerSubscriptionCriteria):
        """Sets the s1_bearer_subscription_criteria of this S1BearerSubscription.


        :param s1_bearer_subscription_criteria: The s1_bearer_subscription_criteria of this S1BearerSubscription.
        :type s1_bearer_subscription_criteria: S1BearerSubscriptionS1BearerSubscriptionCriteria
        """
        if s1_bearer_subscription_criteria is None:
            raise ValueError("Invalid value for `s1_bearer_subscription_criteria`, must not be `None`")  # noqa: E501

        self._s1_bearer_subscription_criteria = s1_bearer_subscription_criteria

    @property
    def links(self) -> CaReconfSubscriptionLinks:
        """Gets the links of this S1BearerSubscription.


        :return: The links of this S1BearerSubscription.
        :rtype: CaReconfSubscriptionLinks
        """
        return self._links

    @links.setter
    def links(self, links: CaReconfSubscriptionLinks):
        """Sets the links of this S1BearerSubscription.


        :param links: The links of this S1BearerSubscription.
        :type links: CaReconfSubscriptionLinks
        """

        self._links = links

    @property
    def callback_reference(self) -> str:
        """Gets the callback_reference of this S1BearerSubscription.

        URI selected by the service consumer, to receive notifications on the subscribed RNIS information. This shall be included in the request and response.  # noqa: E501

        :return: The callback_reference of this S1BearerSubscription.
        :rtype: str
        """
        return self._callback_reference

    @callback_reference.setter
    def callback_reference(self, callback_reference: str):
        """Sets the callback_reference of this S1BearerSubscription.

        URI selected by the service consumer, to receive notifications on the subscribed RNIS information. This shall be included in the request and response.  # noqa: E501

        :param callback_reference: The callback_reference of this S1BearerSubscription.
        :type callback_reference: str
        """
        if callback_reference is None:
            raise ValueError("Invalid value for `callback_reference`, must not be `None`")  # noqa: E501

        self._callback_reference = callback_reference

    @property
    def event_type(self) -> List[Enum]:
        """Gets the event_type of this S1BearerSubscription.

        Description of the subscribed event. The event is included both in the request and in the response. \\nFor the eventType, the following values are currently defined: <p>0 = RESERVED. <p>1 = S1_BEARER_ESTABLISH. <p>2 = S1_BEARER_MODIFY. <p>3 = S1_BEARER_RELEASE.  # noqa: E501

        :return: The event_type of this S1BearerSubscription.
        :rtype: List[Enum]
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type: List[Enum]):
        """Sets the event_type of this S1BearerSubscription.

        Description of the subscribed event. The event is included both in the request and in the response. \\nFor the eventType, the following values are currently defined: <p>0 = RESERVED. <p>1 = S1_BEARER_ESTABLISH. <p>2 = S1_BEARER_MODIFY. <p>3 = S1_BEARER_RELEASE.  # noqa: E501

        :param event_type: The event_type of this S1BearerSubscription.
        :type event_type: List[Enum]
        """
        if event_type is None:
            raise ValueError("Invalid value for `event_type`, must not be `None`")  # noqa: E501

        self._event_type = event_type

    @property
    def expiry_deadline(self) -> TimeStamp:
        """Gets the expiry_deadline of this S1BearerSubscription.


        :return: The expiry_deadline of this S1BearerSubscription.
        :rtype: TimeStamp
        """
        return self._expiry_deadline

    @expiry_deadline.setter
    def expiry_deadline(self, expiry_deadline: TimeStamp):
        """Sets the expiry_deadline of this S1BearerSubscription.


        :param expiry_deadline: The expiry_deadline of this S1BearerSubscription.
        :type expiry_deadline: TimeStamp
        """

        self._expiry_deadline = expiry_deadline

    @property
    def subscription_type(self) -> str:
        """Gets the subscription_type of this S1BearerSubscription.

        Shall be set to \"S1BearerSubscription\".  # noqa: E501

        :return: The subscription_type of this S1BearerSubscription.
        :rtype: str
        """
        return self._subscription_type

    @subscription_type.setter
    def subscription_type(self, subscription_type: str):
        """Sets the subscription_type of this S1BearerSubscription.

        Shall be set to \"S1BearerSubscription\".  # noqa: E501

        :param subscription_type: The subscription_type of this S1BearerSubscription.
        :type subscription_type: str
        """
        if subscription_type is None:
            raise ValueError("Invalid value for `subscription_type`, must not be `None`")  # noqa: E501

        self._subscription_type = subscription_type
