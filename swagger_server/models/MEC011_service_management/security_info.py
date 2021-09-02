# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.MEC011_service_management.security_info_o_auth2_info import SecurityInfoOAuth2Info  # noqa: F401,E501
from swagger_server import util


class SecurityInfo(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, o_auth2_info: SecurityInfoOAuth2Info=None):  # noqa: E501
        """SecurityInfo - a model defined in Swagger

        :param o_auth2_info: The o_auth2_info of this SecurityInfo.  # noqa: E501
        :type o_auth2_info: SecurityInfoOAuth2Info
        """
        self.swagger_types = {
            'o_auth2_info': SecurityInfoOAuth2Info
        }

        self.attribute_map = {
            'o_auth2_info': 'oAuth2Info'
        }
        self._o_auth2_info = o_auth2_info

    @classmethod
    def from_dict(cls, dikt) -> 'SecurityInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SecurityInfo of this SecurityInfo.  # noqa: E501
        :rtype: SecurityInfo
        """
        return util.deserialize_model(dikt, cls)

    @property
    def o_auth2_info(self) -> SecurityInfoOAuth2Info:
        """Gets the o_auth2_info of this SecurityInfo.


        :return: The o_auth2_info of this SecurityInfo.
        :rtype: SecurityInfoOAuth2Info
        """
        return self._o_auth2_info

    @o_auth2_info.setter
    def o_auth2_info(self, o_auth2_info: SecurityInfoOAuth2Info):
        """Sets the o_auth2_info of this SecurityInfo.


        :param o_auth2_info: The o_auth2_info of this SecurityInfo.
        :type o_auth2_info: SecurityInfoOAuth2Info
        """

        self._o_auth2_info = o_auth2_info
