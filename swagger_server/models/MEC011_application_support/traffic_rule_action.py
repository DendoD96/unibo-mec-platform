# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class TrafficRuleAction(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    DROP = "DROP"
    FORWARD_DECAPSULATED = "FORWARD_DECAPSULATED"
    FORWARD_ENCAPSULATED = "FORWARD_ENCAPSULATED"
    PASSTHROUGH = "PASSTHROUGH"
    DUPLICATE_DECAPSULATED = "DUPLICATE_DECAPSULATED"
    DUPLICATE_ENCAPSULATED = "DUPLICATE_ENCAPSULATED"
    def __init__(self):  # noqa: E501
        """TrafficRuleAction - a model defined in Swagger

        """
        self.swagger_types = {
        }

        self.attribute_map = {
        }

    @classmethod
    def from_dict(cls, dikt) -> 'TrafficRuleAction':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The TrafficRule.Action of this TrafficRuleAction.  # noqa: E501
        :rtype: TrafficRuleAction
        """
        return util.deserialize_model(dikt, cls)
