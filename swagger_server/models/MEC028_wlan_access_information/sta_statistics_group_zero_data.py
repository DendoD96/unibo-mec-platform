# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401 # pylint: disable=unused-import

from typing import List, Dict  # noqa: F401 # pylint: disable=unused-import

from swagger_server.models.base_model_ import Model
from swagger_server.models.MEC028_wlan_access_information.reporting_reason_sta_counters import \
	ReportingReasonStaCounters  # noqa: F401 # pylint: disable=unused-import,E501
from swagger_server import util


class StaStatisticsGroupZeroData(Model):
	"""NOTE: This class is auto generated by the swagger code generator program.

	Do not edit the class manually.
	"""

	def __init__(self, failed_count: int = None, fcs_error_count: int = None, group_received_frame_count: int = None,
	             group_transmitted_frame_count: int = None, received_fragment_count: int = None,
	             reporting_reason_sta_counters: ReportingReasonStaCounters = None,
	             transmitted_fragment_count: int = None, transmitted_frame_count: int = None):  # noqa: E501
		"""StaStatisticsGroupZeroData - a model defined in Swagger

		:param failed_count: The failed_count of this StaStatisticsGroupZeroData.  # noqa: E501
		:type failed_count: int
		:param fcs_error_count: The fcs_error_count of this StaStatisticsGroupZeroData.  # noqa: E501
		:type fcs_error_count: int
		:param group_received_frame_count: The group_received_frame_count of this StaStatisticsGroupZeroData.  # noqa: E501
		:type group_received_frame_count: int
		:param group_transmitted_frame_count: The group_transmitted_frame_count of this StaStatisticsGroupZeroData.  # noqa: E501
		:type group_transmitted_frame_count: int
		:param received_fragment_count: The received_fragment_count of this StaStatisticsGroupZeroData.  # noqa: E501
		:type received_fragment_count: int
		:param reporting_reason_sta_counters: The reporting_reason_sta_counters of this StaStatisticsGroupZeroData.  # noqa: E501
		:type reporting_reason_sta_counters: ReportingReasonStaCounters
		:param transmitted_fragment_count: The transmitted_fragment_count of this StaStatisticsGroupZeroData.  # noqa: E501
		:type transmitted_fragment_count: int
		:param transmitted_frame_count: The transmitted_frame_count of this StaStatisticsGroupZeroData.  # noqa: E501
		:type transmitted_frame_count: int
		"""
		self.swagger_types = {
			'failed_count': int,
			'fcs_error_count': int,
			'group_received_frame_count': int,
			'group_transmitted_frame_count': int,
			'received_fragment_count': int,
			'reporting_reason_sta_counters': ReportingReasonStaCounters,
			'transmitted_fragment_count': int,
			'transmitted_frame_count': int
		}

		self.attribute_map = {
			'failed_count': 'failedCount',
			'fcs_error_count': 'fcsErrorCount',
			'group_received_frame_count': 'groupReceivedFrameCount',
			'group_transmitted_frame_count': 'groupTransmittedFrameCount',
			'received_fragment_count': 'receivedFragmentCount',
			'reporting_reason_sta_counters': 'reportingReasonStaCounters',
			'transmitted_fragment_count': 'transmittedFragmentCount',
			'transmitted_frame_count': 'transmittedFrameCount'
		}
		self._failed_count = failed_count
		self._fcs_error_count = fcs_error_count
		self._group_received_frame_count = group_received_frame_count
		self._group_transmitted_frame_count = group_transmitted_frame_count
		self._received_fragment_count = received_fragment_count
		self._reporting_reason_sta_counters = reporting_reason_sta_counters
		self._transmitted_fragment_count = transmitted_fragment_count
		self._transmitted_frame_count = transmitted_frame_count

	@classmethod
	def from_dict(cls, dikt) -> 'StaStatisticsGroupZeroData':
		"""Returns the dict as a model

		:param dikt: A dict.
		:type: dict
		:return: The StaStatisticsGroupZeroData of this StaStatisticsGroupZeroData.  # noqa: E501
		:rtype: StaStatisticsGroupZeroData
		"""
		return util.deserialize_model(dikt, cls)

	@property
	def failed_count(self) -> int:
		"""Gets the failed_count of this StaStatisticsGroupZeroData.

		dot11FailedCount counter  # noqa: E501

		:return: The failed_count of this StaStatisticsGroupZeroData.
		:rtype: int
		"""
		return self._failed_count

	@failed_count.setter
	def failed_count(self, failed_count: int):
		"""Sets the failed_count of this StaStatisticsGroupZeroData.

		dot11FailedCount counter  # noqa: E501

		:param failed_count: The failed_count of this StaStatisticsGroupZeroData.
		:type failed_count: int
		"""
		if failed_count is None:
			raise ValueError("Invalid value for `failed_count`, must not be `None`")  # noqa: E501

		self._failed_count = failed_count

	@property
	def fcs_error_count(self) -> int:
		"""Gets the fcs_error_count of this StaStatisticsGroupZeroData.

		dot11FCSErrorCount counter  # noqa: E501

		:return: The fcs_error_count of this StaStatisticsGroupZeroData.
		:rtype: int
		"""
		return self._fcs_error_count

	@fcs_error_count.setter
	def fcs_error_count(self, fcs_error_count: int):
		"""Sets the fcs_error_count of this StaStatisticsGroupZeroData.

		dot11FCSErrorCount counter  # noqa: E501

		:param fcs_error_count: The fcs_error_count of this StaStatisticsGroupZeroData.
		:type fcs_error_count: int
		"""
		if fcs_error_count is None:
			raise ValueError("Invalid value for `fcs_error_count`, must not be `None`")  # noqa: E501

		self._fcs_error_count = fcs_error_count

	@property
	def group_received_frame_count(self) -> int:
		"""Gets the group_received_frame_count of this StaStatisticsGroupZeroData.

		dot11GroupReceivedFrameCount counter  # noqa: E501

		:return: The group_received_frame_count of this StaStatisticsGroupZeroData.
		:rtype: int
		"""
		return self._group_received_frame_count

	@group_received_frame_count.setter
	def group_received_frame_count(self, group_received_frame_count: int):
		"""Sets the group_received_frame_count of this StaStatisticsGroupZeroData.

		dot11GroupReceivedFrameCount counter  # noqa: E501

		:param group_received_frame_count: The group_received_frame_count of this StaStatisticsGroupZeroData.
		:type group_received_frame_count: int
		"""
		if group_received_frame_count is None:
			raise ValueError("Invalid value for `group_received_frame_count`, must not be `None`")  # noqa: E501

		self._group_received_frame_count = group_received_frame_count

	@property
	def group_transmitted_frame_count(self) -> int:
		"""Gets the group_transmitted_frame_count of this StaStatisticsGroupZeroData.

		dot11GroupTransmittedFrameCount counter  # noqa: E501

		:return: The group_transmitted_frame_count of this StaStatisticsGroupZeroData.
		:rtype: int
		"""
		return self._group_transmitted_frame_count

	@group_transmitted_frame_count.setter
	def group_transmitted_frame_count(self, group_transmitted_frame_count: int):
		"""Sets the group_transmitted_frame_count of this StaStatisticsGroupZeroData.

		dot11GroupTransmittedFrameCount counter  # noqa: E501

		:param group_transmitted_frame_count: The group_transmitted_frame_count of this StaStatisticsGroupZeroData.
		:type group_transmitted_frame_count: int
		"""
		if group_transmitted_frame_count is None:
			raise ValueError("Invalid value for `group_transmitted_frame_count`, must not be `None`")  # noqa: E501

		self._group_transmitted_frame_count = group_transmitted_frame_count

	@property
	def received_fragment_count(self) -> int:
		"""Gets the received_fragment_count of this StaStatisticsGroupZeroData.

		dot11ReceivedFragmentCount counter  # noqa: E501

		:return: The received_fragment_count of this StaStatisticsGroupZeroData.
		:rtype: int
		"""
		return self._received_fragment_count

	@received_fragment_count.setter
	def received_fragment_count(self, received_fragment_count: int):
		"""Sets the received_fragment_count of this StaStatisticsGroupZeroData.

		dot11ReceivedFragmentCount counter  # noqa: E501

		:param received_fragment_count: The received_fragment_count of this StaStatisticsGroupZeroData.
		:type received_fragment_count: int
		"""
		if received_fragment_count is None:
			raise ValueError("Invalid value for `received_fragment_count`, must not be `None`")  # noqa: E501

		self._received_fragment_count = received_fragment_count

	@property
	def reporting_reason_sta_counters(self) -> ReportingReasonStaCounters:
		"""Gets the reporting_reason_sta_counters of this StaStatisticsGroupZeroData.


		:return: The reporting_reason_sta_counters of this StaStatisticsGroupZeroData.
		:rtype: ReportingReasonStaCounters
		"""
		return self._reporting_reason_sta_counters

	@reporting_reason_sta_counters.setter
	def reporting_reason_sta_counters(self, reporting_reason_sta_counters: ReportingReasonStaCounters):
		"""Sets the reporting_reason_sta_counters of this StaStatisticsGroupZeroData.


		:param reporting_reason_sta_counters: The reporting_reason_sta_counters of this StaStatisticsGroupZeroData.
		:type reporting_reason_sta_counters: ReportingReasonStaCounters
		"""

		self._reporting_reason_sta_counters = reporting_reason_sta_counters

	@property
	def transmitted_fragment_count(self) -> int:
		"""Gets the transmitted_fragment_count of this StaStatisticsGroupZeroData.

		dot11TransmittedFragmentCount counter  # noqa: E501

		:return: The transmitted_fragment_count of this StaStatisticsGroupZeroData.
		:rtype: int
		"""
		return self._transmitted_fragment_count

	@transmitted_fragment_count.setter
	def transmitted_fragment_count(self, transmitted_fragment_count: int):
		"""Sets the transmitted_fragment_count of this StaStatisticsGroupZeroData.

		dot11TransmittedFragmentCount counter  # noqa: E501

		:param transmitted_fragment_count: The transmitted_fragment_count of this StaStatisticsGroupZeroData.
		:type transmitted_fragment_count: int
		"""
		if transmitted_fragment_count is None:
			raise ValueError("Invalid value for `transmitted_fragment_count`, must not be `None`")  # noqa: E501

		self._transmitted_fragment_count = transmitted_fragment_count

	@property
	def transmitted_frame_count(self) -> int:
		"""Gets the transmitted_frame_count of this StaStatisticsGroupZeroData.

		dot11TransmittedFrameCount counter  # noqa: E501

		:return: The transmitted_frame_count of this StaStatisticsGroupZeroData.
		:rtype: int
		"""
		return self._transmitted_frame_count

	@transmitted_frame_count.setter
	def transmitted_frame_count(self, transmitted_frame_count: int):
		"""Sets the transmitted_frame_count of this StaStatisticsGroupZeroData.

		dot11TransmittedFrameCount counter  # noqa: E501

		:param transmitted_frame_count: The transmitted_frame_count of this StaStatisticsGroupZeroData.
		:type transmitted_frame_count: int
		"""
		if transmitted_frame_count is None:
			raise ValueError("Invalid value for `transmitted_frame_count`, must not be `None`")  # noqa: E501

		self._transmitted_frame_count = transmitted_frame_count
