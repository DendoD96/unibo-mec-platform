# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.MEC011_service_management.end_point_info_address import EndPointInfoAddress  # noqa: F401,E501
from swagger_server import util


class EndPointInfoAddresses(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, addresses: List[EndPointInfoAddress]=None):  # noqa: E501
        """EndPointInfoAddresses - a model defined in Swagger

        :param addresses: The addresses of this EndPointInfoAddresses.  # noqa: E501
        :type addresses: List[EndPointInfoAddress]
        """
        self.swagger_types = {
            'addresses': List[EndPointInfoAddress]
        }

        self.attribute_map = {
            'addresses': 'addresses'
        }
        self._addresses = addresses

    @classmethod
    def from_dict(cls, dikt) -> 'EndPointInfoAddresses':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The EndPointInfo.Addresses of this EndPointInfoAddresses.  # noqa: E501
        :rtype: EndPointInfoAddresses
        """
        return util.deserialize_model(dikt, cls)

    @property
    def addresses(self) -> List[EndPointInfoAddress]:
        """Gets the addresses of this EndPointInfoAddresses.


        :return: The addresses of this EndPointInfoAddresses.
        :rtype: List[EndPointInfoAddress]
        """
        return self._addresses

    @addresses.setter
    def addresses(self, addresses: List[EndPointInfoAddress]):
        """Sets the addresses of this EndPointInfoAddresses.


        :param addresses: The addresses of this EndPointInfoAddresses.
        :type addresses: List[EndPointInfoAddress]
        """
        if addresses is None:
            raise ValueError("Invalid value for `addresses`, must not be `None`")  # noqa: E501

        self._addresses = addresses
