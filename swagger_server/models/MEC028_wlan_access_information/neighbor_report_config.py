# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401 # pylint: disable=unused-import

from typing import List, Dict  # noqa: F401 # pylint: disable=unused-import

from swagger_server.models.base_model_ import Model
from swagger_server import util


class NeighborReportConfig(Model):
	"""NOTE: This class is auto generated by the swagger code generator program.

	Do not edit the class manually.
	"""

	def __init__(self, bssid: str = None, ssid: str = None):  # noqa: E501
		"""NeighborReportConfig - a model defined in Swagger

		:param bssid: The bssid of this NeighborReportConfig.  # noqa: E501
		:type bssid: str
		:param ssid: The ssid of this NeighborReportConfig.  # noqa: E501
		:type ssid: str
		"""
		self.swagger_types = {
			'bssid': str,
			'ssid': str
		}

		self.attribute_map = {
			'bssid': 'bssid',
			'ssid': 'ssid'
		}
		self._bssid = bssid
		self._ssid = ssid

	@classmethod
	def from_dict(cls, dikt) -> 'NeighborReportConfig':
		"""Returns the dict as a model

		:param dikt: A dict.
		:type: dict
		:return: The NeighborReportConfig of this NeighborReportConfig.  # noqa: E501
		:rtype: NeighborReportConfig
		"""
		return util.deserialize_model(dikt, cls)

	@property
	def bssid(self) -> str:
		"""Gets the bssid of this NeighborReportConfig.

		BSSID of the neighbor AP which information is intended to obtain. If no specific BSSID is given, the information will be provided for all APs matching the ssid criteria.  # noqa: E501

		:return: The bssid of this NeighborReportConfig.
		:rtype: str
		"""
		return self._bssid

	@bssid.setter
	def bssid(self, bssid: str):
		"""Sets the bssid of this NeighborReportConfig.

		BSSID of the neighbor AP which information is intended to obtain. If no specific BSSID is given, the information will be provided for all APs matching the ssid criteria.  # noqa: E501

		:param bssid: The bssid of this NeighborReportConfig.
		:type bssid: str
		"""

		self._bssid = bssid

	@property
	def ssid(self) -> str:
		"""Gets the ssid of this NeighborReportConfig.

		The SSID field is optionally present. If present, it contains an SSID element. The presence of an SSID element in a Neighbor Report indicates a request for a neighbor list for the specified SSID in the SSID Element. The absence of an SSID element indicates neighbor report for the current ESS.  # noqa: E501

		:return: The ssid of this NeighborReportConfig.
		:rtype: str
		"""
		return self._ssid

	@ssid.setter
	def ssid(self, ssid: str):
		"""Sets the ssid of this NeighborReportConfig.

		The SSID field is optionally present. If present, it contains an SSID element. The presence of an SSID element in a Neighbor Report indicates a request for a neighbor list for the specified SSID in the SSID Element. The absence of an SSID element indicates neighbor report for the current ESS.  # noqa: E501

		:param ssid: The ssid of this NeighborReportConfig.
		:type ssid: str
		"""

		self._ssid = ssid
