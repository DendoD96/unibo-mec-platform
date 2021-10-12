# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401 # pylint: disable=unused-import

from typing import List, Dict  # noqa: F401 # pylint: disable=unused-import

from swagger_server.models.base_model_ import Model
from swagger_server import util


class ApIdentity(Model):
	"""NOTE: This class is auto generated by the swagger code generator program.

	Do not edit the class manually.
	"""

	def __init__(self, bssid: str = None, ip_address: List[str] = None, ssid: List[str] = None):  # noqa: E501
		"""ApIdentity - a model defined in Swagger

		:param bssid: The bssid of this ApIdentity.  # noqa: E501
		:type bssid: str
		:param ip_address: The ip_address of this ApIdentity.  # noqa: E501
		:type ip_address: List[str]
		:param ssid: The ssid of this ApIdentity.  # noqa: E501
		:type ssid: List[str]
		"""
		self.swagger_types = {
			'bssid': str,
			'ip_address': List[str],
			'ssid': List[str]
		}

		self.attribute_map = {
			'bssid': 'bssid',
			'ip_address': 'ipAddress',
			'ssid': 'ssid'
		}
		self._bssid = bssid
		self._ip_address = ip_address
		self._ssid = ssid

	@classmethod
	def from_dict(cls, dikt) -> 'ApIdentity':
		"""Returns the dict as a model

		:param dikt: A dict.
		:type: dict
		:return: The ApIdentity of this ApIdentity.  # noqa: E501
		:rtype: ApIdentity
		"""
		return util.deserialize_model(dikt, cls)

	@property
	def bssid(self) -> str:
		"""Gets the bssid of this ApIdentity.

		Basic Service Set Identifier (BSSID) is a unique Identifier assigned to an Access Point (as network interface controller) for communications at the data link layer of a network segment. BSSID is typically set to an access point's MAC address.  # noqa: E501

		:return: The bssid of this ApIdentity.
		:rtype: str
		"""
		return self._bssid

	@bssid.setter
	def bssid(self, bssid: str):
		"""Sets the bssid of this ApIdentity.

		Basic Service Set Identifier (BSSID) is a unique Identifier assigned to an Access Point (as network interface controller) for communications at the data link layer of a network segment. BSSID is typically set to an access point's MAC address.  # noqa: E501

		:param bssid: The bssid of this ApIdentity.
		:type bssid: str
		"""
		if bssid is None:
			raise ValueError("Invalid value for `bssid`, must not be `None`")  # noqa: E501

		self._bssid = bssid

	@property
	def ip_address(self) -> List[str]:
		"""Gets the ip_address of this ApIdentity.

		IPv4 or IPv6 address allocated for the Access Point.  # noqa: E501

		:return: The ip_address of this ApIdentity.
		:rtype: List[str]
		"""
		return self._ip_address

	@ip_address.setter
	def ip_address(self, ip_address: List[str]):
		"""Sets the ip_address of this ApIdentity.

		IPv4 or IPv6 address allocated for the Access Point.  # noqa: E501

		:param ip_address: The ip_address of this ApIdentity.
		:type ip_address: List[str]
		"""

		self._ip_address = ip_address

	@property
	def ssid(self) -> List[str]:
		"""Gets the ssid of this ApIdentity.

		Service Set Identifier (SSID) to identify logical WLAN networks available via the Access Point.  # noqa: E501

		:return: The ssid of this ApIdentity.
		:rtype: List[str]
		"""
		return self._ssid

	@ssid.setter
	def ssid(self, ssid: List[str]):
		"""Sets the ssid of this ApIdentity.

		Service Set Identifier (SSID) to identify logical WLAN networks available via the Access Point.  # noqa: E501

		:param ssid: The ssid of this ApIdentity.
		:type ssid: List[str]
		"""

		self._ssid = ssid
