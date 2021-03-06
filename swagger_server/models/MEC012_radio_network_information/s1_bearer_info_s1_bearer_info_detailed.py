# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.MEC012_radio_network_information.s1_bearer_info_enb_info import S1BearerInfoEnbInfo  # noqa: F401,E501
from swagger_server.models.MEC012_radio_network_information.s1_bearer_info_s_gw_info import S1BearerInfoSGwInfo  # noqa: F401,E501
from swagger_server import util


class S1BearerInfoS1BearerInfoDetailed(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, enb_info: S1BearerInfoEnbInfo=None, erab_id: int=None, s_gw_info: S1BearerInfoSGwInfo=None):  # noqa: E501
        """S1BearerInfoS1BearerInfoDetailed - a model defined in Swagger

        :param enb_info: The enb_info of this S1BearerInfoS1BearerInfoDetailed.  # noqa: E501
        :type enb_info: S1BearerInfoEnbInfo
        :param erab_id: The erab_id of this S1BearerInfoS1BearerInfoDetailed.  # noqa: E501
        :type erab_id: int
        :param s_gw_info: The s_gw_info of this S1BearerInfoS1BearerInfoDetailed.  # noqa: E501
        :type s_gw_info: S1BearerInfoSGwInfo
        """
        self.swagger_types = {
            'enb_info': S1BearerInfoEnbInfo,
            'erab_id': int,
            's_gw_info': S1BearerInfoSGwInfo
        }

        self.attribute_map = {
            'enb_info': 'enbInfo',
            'erab_id': 'erabId',
            's_gw_info': 'sGwInfo'
        }
        self._enb_info = enb_info
        self._erab_id = erab_id
        self._s_gw_info = s_gw_info

    @classmethod
    def from_dict(cls, dikt) -> 'S1BearerInfoS1BearerInfoDetailed':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The S1BearerInfo_s1BearerInfoDetailed of this S1BearerInfoS1BearerInfoDetailed.  # noqa: E501
        :rtype: S1BearerInfoS1BearerInfoDetailed
        """
        return util.deserialize_model(dikt, cls)

    @property
    def enb_info(self) -> S1BearerInfoEnbInfo:
        """Gets the enb_info of this S1BearerInfoS1BearerInfoDetailed.


        :return: The enb_info of this S1BearerInfoS1BearerInfoDetailed.
        :rtype: S1BearerInfoEnbInfo
        """
        return self._enb_info

    @enb_info.setter
    def enb_info(self, enb_info: S1BearerInfoEnbInfo):
        """Sets the enb_info of this S1BearerInfoS1BearerInfoDetailed.


        :param enb_info: The enb_info of this S1BearerInfoS1BearerInfoDetailed.
        :type enb_info: S1BearerInfoEnbInfo
        """

        self._enb_info = enb_info

    @property
    def erab_id(self) -> int:
        """Gets the erab_id of this S1BearerInfoS1BearerInfoDetailed.

        The attribute that uniquely identifies a S1 bearer for a specific UE, as defined in ETSI TS 136 413 [i.3].  # noqa: E501

        :return: The erab_id of this S1BearerInfoS1BearerInfoDetailed.
        :rtype: int
        """
        return self._erab_id

    @erab_id.setter
    def erab_id(self, erab_id: int):
        """Sets the erab_id of this S1BearerInfoS1BearerInfoDetailed.

        The attribute that uniquely identifies a S1 bearer for a specific UE, as defined in ETSI TS 136 413 [i.3].  # noqa: E501

        :param erab_id: The erab_id of this S1BearerInfoS1BearerInfoDetailed.
        :type erab_id: int
        """

        self._erab_id = erab_id

    @property
    def s_gw_info(self) -> S1BearerInfoSGwInfo:
        """Gets the s_gw_info of this S1BearerInfoS1BearerInfoDetailed.


        :return: The s_gw_info of this S1BearerInfoS1BearerInfoDetailed.
        :rtype: S1BearerInfoSGwInfo
        """
        return self._s_gw_info

    @s_gw_info.setter
    def s_gw_info(self, s_gw_info: S1BearerInfoSGwInfo):
        """Sets the s_gw_info of this S1BearerInfoS1BearerInfoDetailed.


        :param s_gw_info: The s_gw_info of this S1BearerInfoS1BearerInfoDetailed.
        :type s_gw_info: S1BearerInfoSGwInfo
        """

        self._s_gw_info = s_gw_info
