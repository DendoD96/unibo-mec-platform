# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.MEC012_radio_network_information.ecgi import Ecgi  # noqa: F401,E501
from swagger_server.models.MEC012_radio_network_information.rab_info_ue_info import RabInfoUeInfo  # noqa: F401,E501
from swagger_server import util


class RabInfoCellUserInfo(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, ecgi: Ecgi=None, ue_info: List[RabInfoUeInfo]=None):  # noqa: E501
        """RabInfoCellUserInfo - a model defined in Swagger

        :param ecgi: The ecgi of this RabInfoCellUserInfo.  # noqa: E501
        :type ecgi: Ecgi
        :param ue_info: The ue_info of this RabInfoCellUserInfo.  # noqa: E501
        :type ue_info: List[RabInfoUeInfo]
        """
        self.swagger_types = {
            'ecgi': Ecgi,
            'ue_info': List[RabInfoUeInfo]
        }

        self.attribute_map = {
            'ecgi': 'ecgi',
            'ue_info': 'ueInfo'
        }
        self._ecgi = ecgi
        self._ue_info = ue_info

    @classmethod
    def from_dict(cls, dikt) -> 'RabInfoCellUserInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The RabInfo_cellUserInfo of this RabInfoCellUserInfo.  # noqa: E501
        :rtype: RabInfoCellUserInfo
        """
        return util.deserialize_model(dikt, cls)

    @property
    def ecgi(self) -> Ecgi:
        """Gets the ecgi of this RabInfoCellUserInfo.


        :return: The ecgi of this RabInfoCellUserInfo.
        :rtype: Ecgi
        """
        return self._ecgi

    @ecgi.setter
    def ecgi(self, ecgi: Ecgi):
        """Sets the ecgi of this RabInfoCellUserInfo.


        :param ecgi: The ecgi of this RabInfoCellUserInfo.
        :type ecgi: Ecgi
        """

        self._ecgi = ecgi

    @property
    def ue_info(self) -> List[RabInfoUeInfo]:
        """Gets the ue_info of this RabInfoCellUserInfo.

        Information on UEs in the specific cell as defined below.  # noqa: E501

        :return: The ue_info of this RabInfoCellUserInfo.
        :rtype: List[RabInfoUeInfo]
        """
        return self._ue_info

    @ue_info.setter
    def ue_info(self, ue_info: List[RabInfoUeInfo]):
        """Sets the ue_info of this RabInfoCellUserInfo.

        Information on UEs in the specific cell as defined below.  # noqa: E501

        :param ue_info: The ue_info of this RabInfoCellUserInfo.
        :type ue_info: List[RabInfoUeInfo]
        """

        self._ue_info = ue_info
