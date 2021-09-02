# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class CmConnNotificationCmIfCmRegState(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    _1 = "1"
    _2 = "2"
    _3 = "3"
    _4 = "4"
    _5 = "5"
    _6 = "6"
    _7 = "7"
    _8 = "8"
    _9 = "9"
    _10 = "10"
    _11 = "11"
    _12 = "12"
    _13 = "13"
    _14 = "14"
    _15 = "15"
    _16 = "16"
    _17 = "17"
    _18 = "18"
    _19 = "19"
    _20 = "20"
    _21 = "21"
    def __init__(self):  # noqa: E501
        """CmConnNotificationCmIfCmRegState - a model defined in Swagger

        """
        self.swagger_types = {
        }

        self.attribute_map = {
        }

    @classmethod
    def from_dict(cls, dikt) -> 'CmConnNotificationCmIfCmRegState':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The CmConnNotification.cmIf.cmRegState of this CmConnNotificationCmIfCmRegState.  # noqa: E501
        :rtype: CmConnNotificationCmIfCmRegState
        """
        return util.deserialize_model(dikt, cls)