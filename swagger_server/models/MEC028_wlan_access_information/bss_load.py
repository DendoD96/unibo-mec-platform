# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401 # pylint: disable=unused-import

from typing import List, Dict  # noqa: F401 # pylint: disable=unused-import

from swagger_server.models.base_model_ import Model
from swagger_server import util


class BssLoad(Model):
	"""NOTE: This class is auto generated by the swagger code generator program.

	Do not edit the class manually.
	"""

	def __init__(self, avail_adm_cap: int = None, channel_utilization: int = None, sta_count: int = None):  # noqa: E501
		"""BssLoad - a model defined in Swagger

		:param avail_adm_cap: The avail_adm_cap of this BssLoad.  # noqa: E501
		:type avail_adm_cap: int
		:param channel_utilization: The channel_utilization of this BssLoad.  # noqa: E501
		:type channel_utilization: int
		:param sta_count: The sta_count of this BssLoad.  # noqa: E501
		:type sta_count: int
		"""
		self.swagger_types = {
			'avail_adm_cap': int,
			'channel_utilization': int,
			'sta_count': int
		}

		self.attribute_map = {
			'avail_adm_cap': 'availAdmCap',
			'channel_utilization': 'channelUtilization',
			'sta_count': 'staCount'
		}
		self._avail_adm_cap = avail_adm_cap
		self._channel_utilization = channel_utilization
		self._sta_count = sta_count

	@classmethod
	def from_dict(cls, dikt) -> 'BssLoad':
		"""Returns the dict as a model

		:param dikt: A dict.
		:type: dict
		:return: The BssLoad of this BssLoad.  # noqa: E501
		:rtype: BssLoad
		"""
		return util.deserialize_model(dikt, cls)

	@property
	def avail_adm_cap(self) -> int:
		"""Gets the avail_adm_cap of this BssLoad.

		Available Admission Capacity that specifies the remaining amount of medium time available via explicit admission control, in units of 32 s/s.  # noqa: E501

		:return: The avail_adm_cap of this BssLoad.
		:rtype: int
		"""
		return self._avail_adm_cap

	@avail_adm_cap.setter
	def avail_adm_cap(self, avail_adm_cap: int):
		"""Sets the avail_adm_cap of this BssLoad.

		Available Admission Capacity that specifies the remaining amount of medium time available via explicit admission control, in units of 32 s/s.  # noqa: E501

		:param avail_adm_cap: The avail_adm_cap of this BssLoad.
		:type avail_adm_cap: int
		"""
		if avail_adm_cap is None:
			raise ValueError("Invalid value for `avail_adm_cap`, must not be `None`")  # noqa: E501

		self._avail_adm_cap = avail_adm_cap

	@property
	def channel_utilization(self) -> int:
		"""Gets the channel_utilization of this BssLoad.

		The percentage of time, linearly scaled with 255 representing 100 %, that the AP sensed the medium was busy, as indicated by either the physical or virtual Carrier Sense (CS) mechanism.  # noqa: E501

		:return: The channel_utilization of this BssLoad.
		:rtype: int
		"""
		return self._channel_utilization

	@channel_utilization.setter
	def channel_utilization(self, channel_utilization: int):
		"""Sets the channel_utilization of this BssLoad.

		The percentage of time, linearly scaled with 255 representing 100 %, that the AP sensed the medium was busy, as indicated by either the physical or virtual Carrier Sense (CS) mechanism.  # noqa: E501

		:param channel_utilization: The channel_utilization of this BssLoad.
		:type channel_utilization: int
		"""
		if channel_utilization is None:
			raise ValueError("Invalid value for `channel_utilization`, must not be `None`")  # noqa: E501

		self._channel_utilization = channel_utilization

	@property
	def sta_count(self) -> int:
		"""Gets the sta_count of this BssLoad.

		An unsigned integer that indicates the total number of STAs currently associated with this BSS.  # noqa: E501

		:return: The sta_count of this BssLoad.
		:rtype: int
		"""
		return self._sta_count

	@sta_count.setter
	def sta_count(self, sta_count: int):
		"""Sets the sta_count of this BssLoad.

		An unsigned integer that indicates the total number of STAs currently associated with this BSS.  # noqa: E501

		:param sta_count: The sta_count of this BssLoad.
		:type sta_count: int
		"""
		if sta_count is None:
			raise ValueError("Invalid value for `sta_count`, must not be `None`")  # noqa: E501

		self._sta_count = sta_count
