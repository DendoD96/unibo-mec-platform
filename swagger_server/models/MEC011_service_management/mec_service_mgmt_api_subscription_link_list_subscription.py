# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.MEC011_service_management.href import Href  # noqa: F401,E501
from swagger_server import util


class MecServiceMgmtApiSubscriptionLinkListSubscription(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, href: Href=None, rel: str=None):  # noqa: E501
        """MecServiceMgmtApiSubscriptionLinkListSubscription - a model defined in Swagger

        :param href: The href of this MecServiceMgmtApiSubscriptionLinkListSubscription.  # noqa: E501
        :type href: Href
        :param rel: The rel of this MecServiceMgmtApiSubscriptionLinkListSubscription.  # noqa: E501
        :type rel: str
        """
        self.swagger_types = {
            'href': Href,
            'rel': str
        }

        self.attribute_map = {
            'href': 'href',
            'rel': 'rel'
        }
        self._href = href
        self._rel = rel

    @classmethod
    def from_dict(cls, dikt) -> 'MecServiceMgmtApiSubscriptionLinkListSubscription':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The MecServiceMgmtApiSubscriptionLinkList.Subscription of this MecServiceMgmtApiSubscriptionLinkListSubscription.  # noqa: E501
        :rtype: MecServiceMgmtApiSubscriptionLinkListSubscription
        """
        return util.deserialize_model(dikt, cls)

    @property
    def href(self) -> Href:
        """Gets the href of this MecServiceMgmtApiSubscriptionLinkListSubscription.


        :return: The href of this MecServiceMgmtApiSubscriptionLinkListSubscription.
        :rtype: Href
        """
        return self._href

    @href.setter
    def href(self, href: Href):
        """Sets the href of this MecServiceMgmtApiSubscriptionLinkListSubscription.


        :param href: The href of this MecServiceMgmtApiSubscriptionLinkListSubscription.
        :type href: Href
        """
        if href is None:
            raise ValueError("Invalid value for `href`, must not be `None`")  # noqa: E501

        self._href = href

    @property
    def rel(self) -> str:
        """Gets the rel of this MecServiceMgmtApiSubscriptionLinkListSubscription.

        The value shall be se to SerAvailabilityNotificationSubscription.  # noqa: E501

        :return: The rel of this MecServiceMgmtApiSubscriptionLinkListSubscription.
        :rtype: str
        """
        return self._rel

    @rel.setter
    def rel(self, rel: str):
        """Sets the rel of this MecServiceMgmtApiSubscriptionLinkListSubscription.

        The value shall be se to SerAvailabilityNotificationSubscription.  # noqa: E501

        :param rel: The rel of this MecServiceMgmtApiSubscriptionLinkListSubscription.
        :type rel: str
        """
        if rel is None:
            raise ValueError("Invalid value for `rel`, must not be `None`")  # noqa: E501

        self._rel = rel
