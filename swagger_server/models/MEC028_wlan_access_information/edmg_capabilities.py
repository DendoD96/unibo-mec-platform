# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class EdmgCapabilities(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, ampdu_parameters: int=None, supported_mcs: int=None, trn_parameters: int=None):  # noqa: E501
        """EdmgCapabilities - a model defined in Swagger

        :param ampdu_parameters: The ampdu_parameters of this EdmgCapabilities.  # noqa: E501
        :type ampdu_parameters: int
        :param supported_mcs: The supported_mcs of this EdmgCapabilities.  # noqa: E501
        :type supported_mcs: int
        :param trn_parameters: The trn_parameters of this EdmgCapabilities.  # noqa: E501
        :type trn_parameters: int
        """
        self.swagger_types = {
            'ampdu_parameters': int,
            'supported_mcs': int,
            'trn_parameters': int
        }

        self.attribute_map = {
            'ampdu_parameters': 'ampduParameters',
            'supported_mcs': 'supportedMcs',
            'trn_parameters': 'trnParameters'
        }
        self._ampdu_parameters = ampdu_parameters
        self._supported_mcs = supported_mcs
        self._trn_parameters = trn_parameters

    @classmethod
    def from_dict(cls, dikt) -> 'EdmgCapabilities':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The EdmgCapabilities of this EdmgCapabilities.  # noqa: E501
        :rtype: EdmgCapabilities
        """
        return util.deserialize_model(dikt, cls)

    @property
    def ampdu_parameters(self) -> int:
        """Gets the ampdu_parameters of this EdmgCapabilities.

        A-MPDU parameters as defined in draft IEEE P802.11ay [i.11]  # noqa: E501

        :return: The ampdu_parameters of this EdmgCapabilities.
        :rtype: int
        """
        return self._ampdu_parameters

    @ampdu_parameters.setter
    def ampdu_parameters(self, ampdu_parameters: int):
        """Sets the ampdu_parameters of this EdmgCapabilities.

        A-MPDU parameters as defined in draft IEEE P802.11ay [i.11]  # noqa: E501

        :param ampdu_parameters: The ampdu_parameters of this EdmgCapabilities.
        :type ampdu_parameters: int
        """
        if ampdu_parameters is None:
            raise ValueError("Invalid value for `ampdu_parameters`, must not be `None`")  # noqa: E501

        self._ampdu_parameters = ampdu_parameters

    @property
    def supported_mcs(self) -> int:
        """Gets the supported_mcs of this EdmgCapabilities.

        Supported MCS as defined in draft IEEE P802.11ay [i.11]  # noqa: E501

        :return: The supported_mcs of this EdmgCapabilities.
        :rtype: int
        """
        return self._supported_mcs

    @supported_mcs.setter
    def supported_mcs(self, supported_mcs: int):
        """Sets the supported_mcs of this EdmgCapabilities.

        Supported MCS as defined in draft IEEE P802.11ay [i.11]  # noqa: E501

        :param supported_mcs: The supported_mcs of this EdmgCapabilities.
        :type supported_mcs: int
        """
        if supported_mcs is None:
            raise ValueError("Invalid value for `supported_mcs`, must not be `None`")  # noqa: E501

        self._supported_mcs = supported_mcs

    @property
    def trn_parameters(self) -> int:
        """Gets the trn_parameters of this EdmgCapabilities.

        Training parameters as defined in draft IEEE P802.11ay [i.11]  # noqa: E501

        :return: The trn_parameters of this EdmgCapabilities.
        :rtype: int
        """
        return self._trn_parameters

    @trn_parameters.setter
    def trn_parameters(self, trn_parameters: int):
        """Sets the trn_parameters of this EdmgCapabilities.

        Training parameters as defined in draft IEEE P802.11ay [i.11]  # noqa: E501

        :param trn_parameters: The trn_parameters of this EdmgCapabilities.
        :type trn_parameters: int
        """
        if trn_parameters is None:
            raise ValueError("Invalid value for `trn_parameters`, must not be `None`")  # noqa: E501

        self._trn_parameters = trn_parameters
