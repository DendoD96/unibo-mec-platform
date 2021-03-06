# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.MEC011_application_support.destination_interface_interface_type import DestinationInterfaceInterfaceType  # noqa: F401,E501
from swagger_server.models.MEC011_application_support.destination_interface_ip_address import DestinationInterfaceIpAddress  # noqa: F401,E501
from swagger_server.models.MEC011_application_support.destination_interface_mac_address import DestinationInterfaceMacAddress  # noqa: F401,E501
from swagger_server.models.MEC011_application_support.tunnel_info import TunnelInfo  # noqa: F401,E501
from swagger_server import util


class DestinationInterface(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, interface_type: DestinationInterfaceInterfaceType=None, tunnel_info: TunnelInfo=None, src_mac_address: DestinationInterfaceMacAddress=None, dst_mac_address: DestinationInterfaceMacAddress=None, dst_ip_address: DestinationInterfaceIpAddress=None):  # noqa: E501
        """DestinationInterface - a model defined in Swagger

        :param interface_type: The interface_type of this DestinationInterface.  # noqa: E501
        :type interface_type: DestinationInterfaceInterfaceType
        :param tunnel_info: The tunnel_info of this DestinationInterface.  # noqa: E501
        :type tunnel_info: TunnelInfo
        :param src_mac_address: The src_mac_address of this DestinationInterface.  # noqa: E501
        :type src_mac_address: DestinationInterfaceMacAddress
        :param dst_mac_address: The dst_mac_address of this DestinationInterface.  # noqa: E501
        :type dst_mac_address: DestinationInterfaceMacAddress
        :param dst_ip_address: The dst_ip_address of this DestinationInterface.  # noqa: E501
        :type dst_ip_address: DestinationInterfaceIpAddress
        """
        self.swagger_types = {
            'interface_type': DestinationInterfaceInterfaceType,
            'tunnel_info': TunnelInfo,
            'src_mac_address': DestinationInterfaceMacAddress,
            'dst_mac_address': DestinationInterfaceMacAddress,
            'dst_ip_address': DestinationInterfaceIpAddress
        }

        self.attribute_map = {
            'interface_type': 'interfaceType',
            'tunnel_info': 'tunnelInfo',
            'src_mac_address': 'srcMacAddress',
            'dst_mac_address': 'dstMacAddress',
            'dst_ip_address': 'dstIpAddress'
        }
        self._interface_type = interface_type
        self._tunnel_info = tunnel_info
        self._src_mac_address = src_mac_address
        self._dst_mac_address = dst_mac_address
        self._dst_ip_address = dst_ip_address

    @classmethod
    def from_dict(cls, dikt) -> 'DestinationInterface':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The DestinationInterface of this DestinationInterface.  # noqa: E501
        :rtype: DestinationInterface
        """
        return util.deserialize_model(dikt, cls)

    @property
    def interface_type(self) -> DestinationInterfaceInterfaceType:
        """Gets the interface_type of this DestinationInterface.


        :return: The interface_type of this DestinationInterface.
        :rtype: DestinationInterfaceInterfaceType
        """
        return self._interface_type

    @interface_type.setter
    def interface_type(self, interface_type: DestinationInterfaceInterfaceType):
        """Sets the interface_type of this DestinationInterface.


        :param interface_type: The interface_type of this DestinationInterface.
        :type interface_type: DestinationInterfaceInterfaceType
        """
        if interface_type is None:
            raise ValueError("Invalid value for `interface_type`, must not be `None`")  # noqa: E501

        self._interface_type = interface_type

    @property
    def tunnel_info(self) -> TunnelInfo:
        """Gets the tunnel_info of this DestinationInterface.


        :return: The tunnel_info of this DestinationInterface.
        :rtype: TunnelInfo
        """
        return self._tunnel_info

    @tunnel_info.setter
    def tunnel_info(self, tunnel_info: TunnelInfo):
        """Sets the tunnel_info of this DestinationInterface.


        :param tunnel_info: The tunnel_info of this DestinationInterface.
        :type tunnel_info: TunnelInfo
        """

        self._tunnel_info = tunnel_info

    @property
    def src_mac_address(self) -> DestinationInterfaceMacAddress:
        """Gets the src_mac_address of this DestinationInterface.


        :return: The src_mac_address of this DestinationInterface.
        :rtype: DestinationInterfaceMacAddress
        """
        return self._src_mac_address

    @src_mac_address.setter
    def src_mac_address(self, src_mac_address: DestinationInterfaceMacAddress):
        """Sets the src_mac_address of this DestinationInterface.


        :param src_mac_address: The src_mac_address of this DestinationInterface.
        :type src_mac_address: DestinationInterfaceMacAddress
        """

        self._src_mac_address = src_mac_address

    @property
    def dst_mac_address(self) -> DestinationInterfaceMacAddress:
        """Gets the dst_mac_address of this DestinationInterface.


        :return: The dst_mac_address of this DestinationInterface.
        :rtype: DestinationInterfaceMacAddress
        """
        return self._dst_mac_address

    @dst_mac_address.setter
    def dst_mac_address(self, dst_mac_address: DestinationInterfaceMacAddress):
        """Sets the dst_mac_address of this DestinationInterface.


        :param dst_mac_address: The dst_mac_address of this DestinationInterface.
        :type dst_mac_address: DestinationInterfaceMacAddress
        """

        self._dst_mac_address = dst_mac_address

    @property
    def dst_ip_address(self) -> DestinationInterfaceIpAddress:
        """Gets the dst_ip_address of this DestinationInterface.


        :return: The dst_ip_address of this DestinationInterface.
        :rtype: DestinationInterfaceIpAddress
        """
        return self._dst_ip_address

    @dst_ip_address.setter
    def dst_ip_address(self, dst_ip_address: DestinationInterfaceIpAddress):
        """Sets the dst_ip_address of this DestinationInterface.


        :param dst_ip_address: The dst_ip_address of this DestinationInterface.
        :type dst_ip_address: DestinationInterfaceIpAddress
        """

        self._dst_ip_address = dst_ip_address
