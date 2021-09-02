# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.MEC011_service_management.end_point_info_address_host import EndPointInfoAddressHost  # noqa: F401,E501
from swagger_server.models.MEC011_service_management.end_point_info_address_port import EndPointInfoAddressPort  # noqa: F401,E501
from swagger_server import util


class EndPointInfoAddress(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, host: EndPointInfoAddressHost=None, port: EndPointInfoAddressPort=None):  # noqa: E501
        """EndPointInfoAddress - a model defined in Swagger

        :param host: The host of this EndPointInfoAddress.  # noqa: E501
        :type host: EndPointInfoAddressHost
        :param port: The port of this EndPointInfoAddress.  # noqa: E501
        :type port: EndPointInfoAddressPort
        """
        self.swagger_types = {
            'host': EndPointInfoAddressHost,
            'port': EndPointInfoAddressPort
        }

        self.attribute_map = {
            'host': 'host',
            'port': 'port'
        }
        self._host = host
        self._port = port

    @classmethod
    def from_dict(cls, dikt) -> 'EndPointInfoAddress':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The EndPointInfo.Address of this EndPointInfoAddress.  # noqa: E501
        :rtype: EndPointInfoAddress
        """
        return util.deserialize_model(dikt, cls)

    @property
    def host(self) -> EndPointInfoAddressHost:
        """Gets the host of this EndPointInfoAddress.


        :return: The host of this EndPointInfoAddress.
        :rtype: EndPointInfoAddressHost
        """
        return self._host

    @host.setter
    def host(self, host: EndPointInfoAddressHost):
        """Sets the host of this EndPointInfoAddress.


        :param host: The host of this EndPointInfoAddress.
        :type host: EndPointInfoAddressHost
        """
        if host is None:
            raise ValueError("Invalid value for `host`, must not be `None`")  # noqa: E501

        self._host = host

    @property
    def port(self) -> EndPointInfoAddressPort:
        """Gets the port of this EndPointInfoAddress.


        :return: The port of this EndPointInfoAddress.
        :rtype: EndPointInfoAddressPort
        """
        return self._port

    @port.setter
    def port(self, port: EndPointInfoAddressPort):
        """Sets the port of this EndPointInfoAddress.


        :param port: The port of this EndPointInfoAddress.
        :type port: EndPointInfoAddressPort
        """
        if port is None:
            raise ValueError("Invalid value for `port`, must not be `None`")  # noqa: E501

        self._port = port
