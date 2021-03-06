# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.MEC013_location.zone_status_subscription import ZoneStatusSubscription  # noqa: F401,E501
from swagger_server import util


class InlineResponse2015(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, zone_status_subscription: ZoneStatusSubscription=None):  # noqa: E501
        """InlineResponse2015 - a model defined in Swagger

        :param zone_status_subscription: The zone_status_subscription of this InlineResponse2015.  # noqa: E501
        :type zone_status_subscription: ZoneStatusSubscription
        """
        self.swagger_types = {
            'zone_status_subscription': ZoneStatusSubscription
        }

        self.attribute_map = {
            'zone_status_subscription': 'zoneStatusSubscription'
        }
        self._zone_status_subscription = zone_status_subscription

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponse2015':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_201_5 of this InlineResponse2015.  # noqa: E501
        :rtype: InlineResponse2015
        """
        return util.deserialize_model(dikt, cls)

    @property
    def zone_status_subscription(self) -> ZoneStatusSubscription:
        """Gets the zone_status_subscription of this InlineResponse2015.


        :return: The zone_status_subscription of this InlineResponse2015.
        :rtype: ZoneStatusSubscription
        """
        return self._zone_status_subscription

    @zone_status_subscription.setter
    def zone_status_subscription(self, zone_status_subscription: ZoneStatusSubscription):
        """Sets the zone_status_subscription of this InlineResponse2015.


        :param zone_status_subscription: The zone_status_subscription of this InlineResponse2015.
        :type zone_status_subscription: ZoneStatusSubscription
        """

        self._zone_status_subscription = zone_status_subscription
