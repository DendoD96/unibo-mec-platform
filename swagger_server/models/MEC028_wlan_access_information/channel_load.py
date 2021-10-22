# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401 # pylint: disable=unused-import

from typing import List, Dict  # noqa: F401 # pylint: disable=unused-import

from swagger_server.models.base_model_ import Model
from swagger_server.models.MEC028_wlan_access_information.sta_identity import \
	StaIdentity  # noqa: F401 # pylint: disable=unused-import,E501
from swagger_server import util


class ChannelLoad(Model):
	"""NOTE: This class is auto generated by the swagger code generator program.

	Do not edit the class manually.
	"""

	def __init__(self, channel: int = None, channel_load: int = None, measurement_duration: int = None,
	             measurement_id: str = None, operating_class: int = None, sta_id: StaIdentity = None):  # noqa: E501
		"""ChannelLoad - a model defined in Swagger

		:param channel: The channel of this ChannelLoad.  # noqa: E501
		:type channel: int
		:param channel_load: The channel_load of this ChannelLoad.  # noqa: E501
		:type channel_load: int
		:param measurement_duration: The measurement_duration of this ChannelLoad.  # noqa: E501
		:type measurement_duration: int
		:param measurement_id: The measurement_id of this ChannelLoad.  # noqa: E501
		:type measurement_id: str
		:param operating_class: The operating_class of this ChannelLoad.  # noqa: E501
		:type operating_class: int
		:param sta_id: The sta_id of this ChannelLoad.  # noqa: E501
		:type sta_id: StaIdentity
		"""
		self.swagger_types = {
			'channel': int,
			'channel_load': int,
			'measurement_duration': int,
			'measurement_id': str,
			'operating_class': int,
			'sta_id': StaIdentity
		}

		self.attribute_map = {
			'channel': 'channel',
			'channel_load': 'channelLoad',
			'measurement_duration': 'measurementDuration',
			'measurement_id': 'measurementId',
			'operating_class': 'operatingClass',
			'sta_id': 'staId'
		}
		self._channel = channel
		self._channel_load = channel_load
		self._measurement_duration = measurement_duration
		self._measurement_id = measurement_id
		self._operating_class = operating_class
		self._sta_id = sta_id

	@classmethod
	def from_dict(cls, dikt) -> 'ChannelLoad':
		"""Returns the dict as a model

		:param dikt: A dict.
		:type: dict
		:return: The ChannelLoad of this ChannelLoad.  # noqa: E501
		:rtype: ChannelLoad
		"""
		return util.deserialize_model(dikt, cls)

	@property
	def channel(self) -> int:
		"""Gets the channel of this ChannelLoad.

		Channel number indicates the channel number for which the measurement report applies.  # noqa: E501

		:return: The channel of this ChannelLoad.
		:rtype: int
		"""
		return self._channel

	@channel.setter
	def channel(self, channel: int):
		"""Sets the channel of this ChannelLoad.

		Channel number indicates the channel number for which the measurement report applies.  # noqa: E501

		:param channel: The channel of this ChannelLoad.
		:type channel: int
		"""
		if channel is None:
			raise ValueError("Invalid value for `channel`, must not be `None`")  # noqa: E501

		self._channel = channel

	@property
	def channel_load(self) -> int:
		"""Gets the channel_load of this ChannelLoad.

		Proportion of measurement duration for which the measuring STA determined the channel to be busy, as a percentage of time, linearly scaled with 255 representing 100 %.  # noqa: E501

		:return: The channel_load of this ChannelLoad.
		:rtype: int
		"""
		return self._channel_load

	@channel_load.setter
	def channel_load(self, channel_load: int):
		"""Sets the channel_load of this ChannelLoad.

		Proportion of measurement duration for which the measuring STA determined the channel to be busy, as a percentage of time, linearly scaled with 255 representing 100 %.  # noqa: E501

		:param channel_load: The channel_load of this ChannelLoad.
		:type channel_load: int
		"""
		if channel_load is None:
			raise ValueError("Invalid value for `channel_load`, must not be `None`")  # noqa: E501

		self._channel_load = channel_load

	@property
	def measurement_duration(self) -> int:
		"""Gets the measurement_duration of this ChannelLoad.

		Duration over which the Channel Load report was measured, in units of TUs of 1 024 µs.  # noqa: E501

		:return: The measurement_duration of this ChannelLoad.
		:rtype: int
		"""
		return self._measurement_duration

	@measurement_duration.setter
	def measurement_duration(self, measurement_duration: int):
		"""Sets the measurement_duration of this ChannelLoad.

		Duration over which the Channel Load report was measured, in units of TUs of 1 024 µs.  # noqa: E501

		:param measurement_duration: The measurement_duration of this ChannelLoad.
		:type measurement_duration: int
		"""
		if measurement_duration is None:
			raise ValueError("Invalid value for `measurement_duration`, must not be `None`")  # noqa: E501

		self._measurement_duration = measurement_duration

	@property
	def measurement_id(self) -> str:
		"""Gets the measurement_id of this ChannelLoad.

		Measurement ID of the Measurement configuration applied to this Channel Load Report.  # noqa: E501

		:return: The measurement_id of this ChannelLoad.
		:rtype: str
		"""
		return self._measurement_id

	@measurement_id.setter
	def measurement_id(self, measurement_id: str):
		"""Sets the measurement_id of this ChannelLoad.

		Measurement ID of the Measurement configuration applied to this Channel Load Report.  # noqa: E501

		:param measurement_id: The measurement_id of this ChannelLoad.
		:type measurement_id: str
		"""
		if measurement_id is None:
			raise ValueError("Invalid value for `measurement_id`, must not be `None`")  # noqa: E501

		self._measurement_id = measurement_id

	@property
	def operating_class(self) -> int:
		"""Gets the operating_class of this ChannelLoad.

		Operating Class field indicates an operating class value as defined in Annex E within IEEE 802.11-2016 [8].  # noqa: E501

		:return: The operating_class of this ChannelLoad.
		:rtype: int
		"""
		return self._operating_class

	@operating_class.setter
	def operating_class(self, operating_class: int):
		"""Sets the operating_class of this ChannelLoad.

		Operating Class field indicates an operating class value as defined in Annex E within IEEE 802.11-2016 [8].  # noqa: E501

		:param operating_class: The operating_class of this ChannelLoad.
		:type operating_class: int
		"""
		if operating_class is None:
			raise ValueError("Invalid value for `operating_class`, must not be `None`")  # noqa: E501

		self._operating_class = operating_class

	@property
	def sta_id(self) -> StaIdentity:
		"""Gets the sta_id of this ChannelLoad.


		:return: The sta_id of this ChannelLoad.
		:rtype: StaIdentity
		"""
		return self._sta_id

	@sta_id.setter
	def sta_id(self, sta_id: StaIdentity):
		"""Sets the sta_id of this ChannelLoad.


		:param sta_id: The sta_id of this ChannelLoad.
		:type sta_id: StaIdentity
		"""

		self._sta_id = sta_id
