# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401 # pylint: disable=unused-import

from typing import List, Dict  # noqa: F401 # pylint: disable=unused-import

from swagger_server.models.base_model_ import Model
from swagger_server.models.MEC029_fixed_access_information.ip_ping_diagnostics_diagnostics_state import \
	IPPingDiagnosticsDiagnosticsState  # noqa: F401 # pylint: disable=unused-import,E501
from swagger_server import util


class IPPingDiagnostics(Model):
	"""NOTE: This class is auto generated by the swagger code generator program.

	Do not edit the class manually.
	"""

	def __init__(self, average_response_time: int = None, data_block_size: int = None,
	             diagnostics_state: IPPingDiagnosticsDiagnosticsState = None, failure_count: int = None,
	             host: str = None, maximum_response_time: int = None, minimum_response_time: int = None,
	             number_of_repetitions: int = None, success_count: int = None, timeout: int = None):  # noqa: E501
		"""IPPingDiagnostics - a model defined in Swagger

		:param average_response_time: The average_response_time of this IPPingDiagnostics.  # noqa: E501
		:type average_response_time: int
		:param data_block_size: The data_block_size of this IPPingDiagnostics.  # noqa: E501
		:type data_block_size: int
		:param diagnostics_state: The diagnostics_state of this IPPingDiagnostics.  # noqa: E501
		:type diagnostics_state: IPPingDiagnosticsDiagnosticsState
		:param failure_count: The failure_count of this IPPingDiagnostics.  # noqa: E501
		:type failure_count: int
		:param host: The host of this IPPingDiagnostics.  # noqa: E501
		:type host: str
		:param maximum_response_time: The maximum_response_time of this IPPingDiagnostics.  # noqa: E501
		:type maximum_response_time: int
		:param minimum_response_time: The minimum_response_time of this IPPingDiagnostics.  # noqa: E501
		:type minimum_response_time: int
		:param number_of_repetitions: The number_of_repetitions of this IPPingDiagnostics.  # noqa: E501
		:type number_of_repetitions: int
		:param success_count: The success_count of this IPPingDiagnostics.  # noqa: E501
		:type success_count: int
		:param timeout: The timeout of this IPPingDiagnostics.  # noqa: E501
		:type timeout: int
		"""
		self.swagger_types = {
			'average_response_time': int,
			'data_block_size': int,
			'diagnostics_state': IPPingDiagnosticsDiagnosticsState,
			'failure_count': int,
			'host': str,
			'maximum_response_time': int,
			'minimum_response_time': int,
			'number_of_repetitions': int,
			'success_count': int,
			'timeout': int
		}

		self.attribute_map = {
			'average_response_time': 'averageResponseTime',
			'data_block_size': 'dataBlockSize',
			'diagnostics_state': 'diagnosticsState',
			'failure_count': 'failureCount',
			'host': 'host',
			'maximum_response_time': 'maximumResponseTime',
			'minimum_response_time': 'minimumResponseTime',
			'number_of_repetitions': 'numberOfRepetitions',
			'success_count': 'successCount',
			'timeout': 'timeout'
		}
		self._average_response_time = average_response_time
		self._data_block_size = data_block_size
		self._diagnostics_state = diagnostics_state
		self._failure_count = failure_count
		self._host = host
		self._maximum_response_time = maximum_response_time
		self._minimum_response_time = minimum_response_time
		self._number_of_repetitions = number_of_repetitions
		self._success_count = success_count
		self._timeout = timeout

	@classmethod
	def from_dict(cls, dikt) -> 'IPPingDiagnostics':
		"""Returns the dict as a model

		:param dikt: A dict.
		:type: dict
		:return: The IPPingDiagnostics of this IPPingDiagnostics.  # noqa: E501
		:rtype: IPPingDiagnostics
		"""
		return util.deserialize_model(dikt, cls)

	@property
	def average_response_time(self) -> int:
		"""Gets the average_response_time of this IPPingDiagnostics.

		Result parameter indicating the average response time in milliseconds over all repetitions with successful responses of the most recent ping test.  If there were no successful responses, this value shall be zero.  # noqa: E501

		:return: The average_response_time of this IPPingDiagnostics.
		:rtype: int
		"""
		return self._average_response_time

	@average_response_time.setter
	def average_response_time(self, average_response_time: int):
		"""Sets the average_response_time of this IPPingDiagnostics.

		Result parameter indicating the average response time in milliseconds over all repetitions with successful responses of the most recent ping test.  If there were no successful responses, this value shall be zero.  # noqa: E501

		:param average_response_time: The average_response_time of this IPPingDiagnostics.
		:type average_response_time: int
		"""

		self._average_response_time = average_response_time

	@property
	def data_block_size(self) -> int:
		"""Gets the data_block_size of this IPPingDiagnostics.

		Size of the data block in bytes to be sent for each ping.  # noqa: E501

		:return: The data_block_size of this IPPingDiagnostics.
		:rtype: int
		"""
		return self._data_block_size

	@data_block_size.setter
	def data_block_size(self, data_block_size: int):
		"""Sets the data_block_size of this IPPingDiagnostics.

		Size of the data block in bytes to be sent for each ping.  # noqa: E501

		:param data_block_size: The data_block_size of this IPPingDiagnostics.
		:type data_block_size: int
		"""

		self._data_block_size = data_block_size

	@property
	def diagnostics_state(self) -> IPPingDiagnosticsDiagnosticsState:
		"""Gets the diagnostics_state of this IPPingDiagnostics.


		:return: The diagnostics_state of this IPPingDiagnostics.
		:rtype: IPPingDiagnosticsDiagnosticsState
		"""
		return self._diagnostics_state

	@diagnostics_state.setter
	def diagnostics_state(self, diagnostics_state: IPPingDiagnosticsDiagnosticsState):
		"""Sets the diagnostics_state of this IPPingDiagnostics.


		:param diagnostics_state: The diagnostics_state of this IPPingDiagnostics.
		:type diagnostics_state: IPPingDiagnosticsDiagnosticsState
		"""
		if diagnostics_state is None:
			raise ValueError("Invalid value for `diagnostics_state`, must not be `None`")  # noqa: E501

		self._diagnostics_state = diagnostics_state

	@property
	def failure_count(self) -> int:
		"""Gets the failure_count of this IPPingDiagnostics.

		Result parameter indicating the number of failed pings in the most recent ping test.  # noqa: E501

		:return: The failure_count of this IPPingDiagnostics.
		:rtype: int
		"""
		return self._failure_count

	@failure_count.setter
	def failure_count(self, failure_count: int):
		"""Sets the failure_count of this IPPingDiagnostics.

		Result parameter indicating the number of failed pings in the most recent ping test.  # noqa: E501

		:param failure_count: The failure_count of this IPPingDiagnostics.
		:type failure_count: int
		"""

		self._failure_count = failure_count

	@property
	def host(self) -> str:
		"""Gets the host of this IPPingDiagnostics.

		Host name or address of the host to ping.  # noqa: E501

		:return: The host of this IPPingDiagnostics.
		:rtype: str
		"""
		return self._host

	@host.setter
	def host(self, host: str):
		"""Sets the host of this IPPingDiagnostics.

		Host name or address of the host to ping.  # noqa: E501

		:param host: The host of this IPPingDiagnostics.
		:type host: str
		"""

		self._host = host

	@property
	def maximum_response_time(self) -> int:
		"""Gets the maximum_response_time of this IPPingDiagnostics.

		Result parameter indicating the maximum response time in milliseconds over all repetitions with successful responses of the most recent ping test.  If there were no successful responses, this value shall be zero.  # noqa: E501

		:return: The maximum_response_time of this IPPingDiagnostics.
		:rtype: int
		"""
		return self._maximum_response_time

	@maximum_response_time.setter
	def maximum_response_time(self, maximum_response_time: int):
		"""Sets the maximum_response_time of this IPPingDiagnostics.

		Result parameter indicating the maximum response time in milliseconds over all repetitions with successful responses of the most recent ping test.  If there were no successful responses, this value shall be zero.  # noqa: E501

		:param maximum_response_time: The maximum_response_time of this IPPingDiagnostics.
		:type maximum_response_time: int
		"""

		self._maximum_response_time = maximum_response_time

	@property
	def minimum_response_time(self) -> int:
		"""Gets the minimum_response_time of this IPPingDiagnostics.

		Result parameter indicating the minimum response time in milliseconds over all repetitions with successful responses of the most recent ping test.  If there were no successful responses, this value shall be zero.  # noqa: E501

		:return: The minimum_response_time of this IPPingDiagnostics.
		:rtype: int
		"""
		return self._minimum_response_time

	@minimum_response_time.setter
	def minimum_response_time(self, minimum_response_time: int):
		"""Sets the minimum_response_time of this IPPingDiagnostics.

		Result parameter indicating the minimum response time in milliseconds over all repetitions with successful responses of the most recent ping test.  If there were no successful responses, this value shall be zero.  # noqa: E501

		:param minimum_response_time: The minimum_response_time of this IPPingDiagnostics.
		:type minimum_response_time: int
		"""

		self._minimum_response_time = minimum_response_time

	@property
	def number_of_repetitions(self) -> int:
		"""Gets the number_of_repetitions of this IPPingDiagnostics.

		Number of repetitions of the ping test to perform before reporting the results.  # noqa: E501

		:return: The number_of_repetitions of this IPPingDiagnostics.
		:rtype: int
		"""
		return self._number_of_repetitions

	@number_of_repetitions.setter
	def number_of_repetitions(self, number_of_repetitions: int):
		"""Sets the number_of_repetitions of this IPPingDiagnostics.

		Number of repetitions of the ping test to perform before reporting the results.  # noqa: E501

		:param number_of_repetitions: The number_of_repetitions of this IPPingDiagnostics.
		:type number_of_repetitions: int
		"""

		self._number_of_repetitions = number_of_repetitions

	@property
	def success_count(self) -> int:
		"""Gets the success_count of this IPPingDiagnostics.

		Result parameter indicating the number of successful pings (those in which a successful response was received prior to the timeout) in the most recent ping test.  # noqa: E501

		:return: The success_count of this IPPingDiagnostics.
		:rtype: int
		"""
		return self._success_count

	@success_count.setter
	def success_count(self, success_count: int):
		"""Sets the success_count of this IPPingDiagnostics.

		Result parameter indicating the number of successful pings (those in which a successful response was received prior to the timeout) in the most recent ping test.  # noqa: E501

		:param success_count: The success_count of this IPPingDiagnostics.
		:type success_count: int
		"""

		self._success_count = success_count

	@property
	def timeout(self) -> int:
		"""Gets the timeout of this IPPingDiagnostics.

		Timeout in milliseconds for the ping test.  # noqa: E501

		:return: The timeout of this IPPingDiagnostics.
		:rtype: int
		"""
		return self._timeout

	@timeout.setter
	def timeout(self, timeout: int):
		"""Sets the timeout of this IPPingDiagnostics.

		Timeout in milliseconds for the ping test.  # noqa: E501

		:param timeout: The timeout of this IPPingDiagnostics.
		:type timeout: int
		"""

		self._timeout = timeout
