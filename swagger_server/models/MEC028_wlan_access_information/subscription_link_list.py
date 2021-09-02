# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.MEC028_wlan_access_information.subscription_link_list_links import SubscriptionLinkListLinks  # noqa: F401,E501
from swagger_server.models.MEC028_wlan_access_information.subscription_link_list_subscription import SubscriptionLinkListSubscription  # noqa: F401,E501
from swagger_server import util


class SubscriptionLinkList(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, links: SubscriptionLinkListLinks=None, subscription: List[SubscriptionLinkListSubscription]=None):  # noqa: E501
        """SubscriptionLinkList - a model defined in Swagger

        :param links: The links of this SubscriptionLinkList.  # noqa: E501
        :type links: SubscriptionLinkListLinks
        :param subscription: The subscription of this SubscriptionLinkList.  # noqa: E501
        :type subscription: List[SubscriptionLinkListSubscription]
        """
        self.swagger_types = {
            'links': SubscriptionLinkListLinks,
            'subscription': List[SubscriptionLinkListSubscription]
        }

        self.attribute_map = {
            'links': '_links',
            'subscription': 'subscription'
        }
        self._links = links
        self._subscription = subscription

    @classmethod
    def from_dict(cls, dikt) -> 'SubscriptionLinkList':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SubscriptionLinkList of this SubscriptionLinkList.  # noqa: E501
        :rtype: SubscriptionLinkList
        """
        return util.deserialize_model(dikt, cls)

    @property
    def links(self) -> SubscriptionLinkListLinks:
        """Gets the links of this SubscriptionLinkList.


        :return: The links of this SubscriptionLinkList.
        :rtype: SubscriptionLinkListLinks
        """
        return self._links

    @links.setter
    def links(self, links: SubscriptionLinkListLinks):
        """Sets the links of this SubscriptionLinkList.


        :param links: The links of this SubscriptionLinkList.
        :type links: SubscriptionLinkListLinks
        """
        if links is None:
            raise ValueError("Invalid value for `links`, must not be `None`")  # noqa: E501

        self._links = links

    @property
    def subscription(self) -> List[SubscriptionLinkListSubscription]:
        """Gets the subscription of this SubscriptionLinkList.


        :return: The subscription of this SubscriptionLinkList.
        :rtype: List[SubscriptionLinkListSubscription]
        """
        return self._subscription

    @subscription.setter
    def subscription(self, subscription: List[SubscriptionLinkListSubscription]):
        """Sets the subscription of this SubscriptionLinkList.


        :param subscription: The subscription of this SubscriptionLinkList.
        :type subscription: List[SubscriptionLinkListSubscription]
        """

        self._subscription = subscription