# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401 # pylint: disable=unused-import

from typing import List, Dict  # noqa: F401 # pylint: disable=unused-import

from swagger_server.models.base_model_ import Model
from swagger_server import util


class DmgCapabilities(Model):
	"""NOTE: This class is auto generated by the swagger code generator program.

	Do not edit the class manually.
	"""

	def __init__(self, ext_sc_mcs_cap: int = None, dmg_ap_or_pcp_cap_info: int = None,
	             dmg_sta_beam_track_time_limit: int = None, dmg_sta_cap_info: int = None,
	             max_nr_basic_amsdu_subframes: int = None, max_nr_short_amsdu_subframes: int = None):  # noqa: E501
		"""DmgCapabilities - a model defined in Swagger

		:param ext_sc_mcs_cap: The ext_sc_mcs_cap of this DmgCapabilities.  # noqa: E501
		:type ext_sc_mcs_cap: int
		:param dmg_ap_or_pcp_cap_info: The dmg_ap_or_pcp_cap_info of this DmgCapabilities.  # noqa: E501
		:type dmg_ap_or_pcp_cap_info: int
		:param dmg_sta_beam_track_time_limit: The dmg_sta_beam_track_time_limit of this DmgCapabilities.  # noqa: E501
		:type dmg_sta_beam_track_time_limit: int
		:param dmg_sta_cap_info: The dmg_sta_cap_info of this DmgCapabilities.  # noqa: E501
		:type dmg_sta_cap_info: int
		:param max_nr_basic_amsdu_subframes: The max_nr_basic_amsdu_subframes of this DmgCapabilities.  # noqa: E501
		:type max_nr_basic_amsdu_subframes: int
		:param max_nr_short_amsdu_subframes: The max_nr_short_amsdu_subframes of this DmgCapabilities.  # noqa: E501
		:type max_nr_short_amsdu_subframes: int
		"""
		self.swagger_types = {
			'ext_sc_mcs_cap': int,
			'dmg_ap_or_pcp_cap_info': int,
			'dmg_sta_beam_track_time_limit': int,
			'dmg_sta_cap_info': int,
			'max_nr_basic_amsdu_subframes': int,
			'max_nr_short_amsdu_subframes': int
		}

		self.attribute_map = {
			'ext_sc_mcs_cap': 'ExtScMcsCap',
			'dmg_ap_or_pcp_cap_info': 'dmgApOrPcpCapInfo',
			'dmg_sta_beam_track_time_limit': 'dmgStaBeamTrackTimeLimit',
			'dmg_sta_cap_info': 'dmgStaCapInfo',
			'max_nr_basic_amsdu_subframes': 'maxNrBasicAmsduSubframes',
			'max_nr_short_amsdu_subframes': 'maxNrShortAmsduSubframes'
		}
		self._ext_sc_mcs_cap = ext_sc_mcs_cap
		self._dmg_ap_or_pcp_cap_info = dmg_ap_or_pcp_cap_info
		self._dmg_sta_beam_track_time_limit = dmg_sta_beam_track_time_limit
		self._dmg_sta_cap_info = dmg_sta_cap_info
		self._max_nr_basic_amsdu_subframes = max_nr_basic_amsdu_subframes
		self._max_nr_short_amsdu_subframes = max_nr_short_amsdu_subframes

	@classmethod
	def from_dict(cls, dikt) -> 'DmgCapabilities':
		"""Returns the dict as a model

		:param dikt: A dict.
		:type: dict
		:return: The DmgCapabilities of this DmgCapabilities.  # noqa: E501
		:rtype: DmgCapabilities
		"""
		return util.deserialize_model(dikt, cls)

	@property
	def ext_sc_mcs_cap(self) -> int:
		"""Gets the ext_sc_mcs_cap of this DmgCapabilities.

		Extended SC MCS capabilities as defined in IEEE 802.11-2016 [8].  # noqa: E501

		:return: The ext_sc_mcs_cap of this DmgCapabilities.
		:rtype: int
		"""
		return self._ext_sc_mcs_cap

	@ext_sc_mcs_cap.setter
	def ext_sc_mcs_cap(self, ext_sc_mcs_cap: int):
		"""Sets the ext_sc_mcs_cap of this DmgCapabilities.

		Extended SC MCS capabilities as defined in IEEE 802.11-2016 [8].  # noqa: E501

		:param ext_sc_mcs_cap: The ext_sc_mcs_cap of this DmgCapabilities.
		:type ext_sc_mcs_cap: int
		"""
		if ext_sc_mcs_cap is None:
			raise ValueError("Invalid value for `ext_sc_mcs_cap`, must not be `None`")  # noqa: E501

		self._ext_sc_mcs_cap = ext_sc_mcs_cap

	@property
	def dmg_ap_or_pcp_cap_info(self) -> int:
		"""Gets the dmg_ap_or_pcp_cap_info of this DmgCapabilities.

		DMG AP or PCP capabilities information as defined in IEEE 802.11-2016 [8].  # noqa: E501

		:return: The dmg_ap_or_pcp_cap_info of this DmgCapabilities.
		:rtype: int
		"""
		return self._dmg_ap_or_pcp_cap_info

	@dmg_ap_or_pcp_cap_info.setter
	def dmg_ap_or_pcp_cap_info(self, dmg_ap_or_pcp_cap_info: int):
		"""Sets the dmg_ap_or_pcp_cap_info of this DmgCapabilities.

		DMG AP or PCP capabilities information as defined in IEEE 802.11-2016 [8].  # noqa: E501

		:param dmg_ap_or_pcp_cap_info: The dmg_ap_or_pcp_cap_info of this DmgCapabilities.
		:type dmg_ap_or_pcp_cap_info: int
		"""
		if dmg_ap_or_pcp_cap_info is None:
			raise ValueError("Invalid value for `dmg_ap_or_pcp_cap_info`, must not be `None`")  # noqa: E501

		self._dmg_ap_or_pcp_cap_info = dmg_ap_or_pcp_cap_info

	@property
	def dmg_sta_beam_track_time_limit(self) -> int:
		"""Gets the dmg_sta_beam_track_time_limit of this DmgCapabilities.

		DMG station beam tracking time limit as defined in IEEE 802.11-2016 [8].   # noqa: E501

		:return: The dmg_sta_beam_track_time_limit of this DmgCapabilities.
		:rtype: int
		"""
		return self._dmg_sta_beam_track_time_limit

	@dmg_sta_beam_track_time_limit.setter
	def dmg_sta_beam_track_time_limit(self, dmg_sta_beam_track_time_limit: int):
		"""Sets the dmg_sta_beam_track_time_limit of this DmgCapabilities.

		DMG station beam tracking time limit as defined in IEEE 802.11-2016 [8].   # noqa: E501

		:param dmg_sta_beam_track_time_limit: The dmg_sta_beam_track_time_limit of this DmgCapabilities.
		:type dmg_sta_beam_track_time_limit: int
		"""
		if dmg_sta_beam_track_time_limit is None:
			raise ValueError("Invalid value for `dmg_sta_beam_track_time_limit`, must not be `None`")  # noqa: E501

		self._dmg_sta_beam_track_time_limit = dmg_sta_beam_track_time_limit

	@property
	def dmg_sta_cap_info(self) -> int:
		"""Gets the dmg_sta_cap_info of this DmgCapabilities.

		DMG station capabilities information as defined in IEEE 802.11-2016 [8].   # noqa: E501

		:return: The dmg_sta_cap_info of this DmgCapabilities.
		:rtype: int
		"""
		return self._dmg_sta_cap_info

	@dmg_sta_cap_info.setter
	def dmg_sta_cap_info(self, dmg_sta_cap_info: int):
		"""Sets the dmg_sta_cap_info of this DmgCapabilities.

		DMG station capabilities information as defined in IEEE 802.11-2016 [8].   # noqa: E501

		:param dmg_sta_cap_info: The dmg_sta_cap_info of this DmgCapabilities.
		:type dmg_sta_cap_info: int
		"""
		if dmg_sta_cap_info is None:
			raise ValueError("Invalid value for `dmg_sta_cap_info`, must not be `None`")  # noqa: E501

		self._dmg_sta_cap_info = dmg_sta_cap_info

	@property
	def max_nr_basic_amsdu_subframes(self) -> int:
		"""Gets the max_nr_basic_amsdu_subframes of this DmgCapabilities.

		Number of basic A-MSDU subframes in A-MSDU as defined in IEEE 802.11-2016 [8].  # noqa: E501

		:return: The max_nr_basic_amsdu_subframes of this DmgCapabilities.
		:rtype: int
		"""
		return self._max_nr_basic_amsdu_subframes

	@max_nr_basic_amsdu_subframes.setter
	def max_nr_basic_amsdu_subframes(self, max_nr_basic_amsdu_subframes: int):
		"""Sets the max_nr_basic_amsdu_subframes of this DmgCapabilities.

		Number of basic A-MSDU subframes in A-MSDU as defined in IEEE 802.11-2016 [8].  # noqa: E501

		:param max_nr_basic_amsdu_subframes: The max_nr_basic_amsdu_subframes of this DmgCapabilities.
		:type max_nr_basic_amsdu_subframes: int
		"""
		if max_nr_basic_amsdu_subframes is None:
			raise ValueError("Invalid value for `max_nr_basic_amsdu_subframes`, must not be `None`")  # noqa: E501

		self._max_nr_basic_amsdu_subframes = max_nr_basic_amsdu_subframes

	@property
	def max_nr_short_amsdu_subframes(self) -> int:
		"""Gets the max_nr_short_amsdu_subframes of this DmgCapabilities.

		Number of short A-MSDU subframes in A-MSDU as defined in IEEE 802.11-2016 [8].  # noqa: E501

		:return: The max_nr_short_amsdu_subframes of this DmgCapabilities.
		:rtype: int
		"""
		return self._max_nr_short_amsdu_subframes

	@max_nr_short_amsdu_subframes.setter
	def max_nr_short_amsdu_subframes(self, max_nr_short_amsdu_subframes: int):
		"""Sets the max_nr_short_amsdu_subframes of this DmgCapabilities.

		Number of short A-MSDU subframes in A-MSDU as defined in IEEE 802.11-2016 [8].  # noqa: E501

		:param max_nr_short_amsdu_subframes: The max_nr_short_amsdu_subframes of this DmgCapabilities.
		:type max_nr_short_amsdu_subframes: int
		"""
		if max_nr_short_amsdu_subframes is None:
			raise ValueError("Invalid value for `max_nr_short_amsdu_subframes`, must not be `None`")  # noqa: E501

		self._max_nr_short_amsdu_subframes = max_nr_short_amsdu_subframes
