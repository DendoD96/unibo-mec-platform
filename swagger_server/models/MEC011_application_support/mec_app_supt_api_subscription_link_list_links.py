# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.MEC011_application_support.link_type import LinkType  # noqa: F401,E501
from swagger_server.models.MEC011_application_support.mec_app_supt_api_subscription_link_list_subscription import MecAppSuptApiSubscriptionLinkListSubscription  # noqa: F401,E501
from swagger_server import util


class MecAppSuptApiSubscriptionLinkListLinks(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, _self: LinkType=None, subscriptions: List[MecAppSuptApiSubscriptionLinkListSubscription]=None):  # noqa: E501
        """MecAppSuptApiSubscriptionLinkListLinks - a model defined in Swagger

        :param _self: The _self of this MecAppSuptApiSubscriptionLinkListLinks.  # noqa: E501
        :type _self: LinkType
        :param subscriptions: The subscriptions of this MecAppSuptApiSubscriptionLinkListLinks.  # noqa: E501
        :type subscriptions: List[MecAppSuptApiSubscriptionLinkListSubscription]
        """
        self.swagger_types = {
            '_self': LinkType,
            'subscriptions': List[MecAppSuptApiSubscriptionLinkListSubscription]
        }

        self.attribute_map = {
            '_self': 'self',
            'subscriptions': 'subscriptions'
        }
        self.__self = _self
        self._subscriptions = subscriptions

    @classmethod
    def from_dict(cls, dikt) -> 'MecAppSuptApiSubscriptionLinkListLinks':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The MecAppSuptApiSubscriptionLinkList.Links of this MecAppSuptApiSubscriptionLinkListLinks.  # noqa: E501
        :rtype: MecAppSuptApiSubscriptionLinkListLinks
        """
        return util.deserialize_model(dikt, cls)

    @property
    def _self(self) -> LinkType:
        """Gets the _self of this MecAppSuptApiSubscriptionLinkListLinks.


        :return: The _self of this MecAppSuptApiSubscriptionLinkListLinks.
        :rtype: LinkType
        """
        return self.__self

    @_self.setter
    def _self(self, _self: LinkType):
        """Sets the _self of this MecAppSuptApiSubscriptionLinkListLinks.


        :param _self: The _self of this MecAppSuptApiSubscriptionLinkListLinks.
        :type _self: LinkType
        """
        if _self is None:
            raise ValueError("Invalid value for `_self`, must not be `None`")  # noqa: E501

        self.__self = _self

    @property
    def subscriptions(self) -> List[MecAppSuptApiSubscriptionLinkListSubscription]:
        """Gets the subscriptions of this MecAppSuptApiSubscriptionLinkListLinks.

        The MEC application instance's subscriptions  # noqa: E501

        :return: The subscriptions of this MecAppSuptApiSubscriptionLinkListLinks.
        :rtype: List[MecAppSuptApiSubscriptionLinkListSubscription]
        """
        return self._subscriptions

    @subscriptions.setter
    def subscriptions(self, subscriptions: List[MecAppSuptApiSubscriptionLinkListSubscription]):
        """Sets the subscriptions of this MecAppSuptApiSubscriptionLinkListLinks.

        The MEC application instance's subscriptions  # noqa: E501

        :param subscriptions: The subscriptions of this MecAppSuptApiSubscriptionLinkListLinks.
        :type subscriptions: List[MecAppSuptApiSubscriptionLinkListSubscription]
        """

        self._subscriptions = subscriptions
