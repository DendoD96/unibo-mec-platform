# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401 # pylint: disable=unused-import

from typing import List, Dict  # noqa: F401 # pylint: disable=unused-import

from swagger_server.models.base_model_ import Model
from swagger_server.models.MEC011_application_support.timing_caps_ntp_servers_authentication_key_num import \
	TimingCapsNtpServersAuthenticationKeyNum  # noqa: F401 # pylint: disable=unused-import,E501
from swagger_server.models.MEC011_application_support.timing_caps_ntp_servers_authentication_option import \
	TimingCapsNtpServersAuthenticationOption  # noqa: F401 # pylint: disable=unused-import,E501
from swagger_server.models.MEC011_application_support.timing_caps_ntp_servers_local_priority import \
	TimingCapsNtpServersLocalPriority  # noqa: F401 # pylint: disable=unused-import,E501
from swagger_server.models.MEC011_application_support.timing_caps_ntp_servers_max_polling_interval import \
	TimingCapsNtpServersMaxPollingInterval  # noqa: F401 # pylint: disable=unused-import,E501
from swagger_server.models.MEC011_application_support.timing_caps_ntp_servers_min_polling_interval import \
	TimingCapsNtpServersMinPollingInterval  # noqa: F401 # pylint: disable=unused-import,E501
from swagger_server.models.MEC011_application_support.timing_caps_ntp_servers_ntp_server_addr import \
	TimingCapsNtpServersNtpServerAddr  # noqa: F401 # pylint: disable=unused-import,E501
from swagger_server.models.MEC011_application_support.timing_caps_ntp_servers_ntp_server_addr_type import \
	TimingCapsNtpServersNtpServerAddrType  # noqa: F401 # pylint: disable=unused-import,E501
from swagger_server import util


class TimingCapsNtpServers(Model):
	"""NOTE: This class is auto generated by the swagger code generator program.

	Do not edit the class manually.
	"""

	def __init__(self, ntp_server_addr_type: TimingCapsNtpServersNtpServerAddrType = None,
	             ntp_server_addr: TimingCapsNtpServersNtpServerAddr = None,
	             min_polling_interval: TimingCapsNtpServersMinPollingInterval = None,
	             max_polling_interval: TimingCapsNtpServersMaxPollingInterval = None,
	             local_priority: TimingCapsNtpServersLocalPriority = None,
	             authentication_option: TimingCapsNtpServersAuthenticationOption = None,
	             authentication_key_num: TimingCapsNtpServersAuthenticationKeyNum = None):  # noqa: E501
		"""TimingCapsNtpServers - a model defined in Swagger

		:param ntp_server_addr_type: The ntp_server_addr_type of this TimingCapsNtpServers.  # noqa: E501
		:type ntp_server_addr_type: TimingCapsNtpServersNtpServerAddrType
		:param ntp_server_addr: The ntp_server_addr of this TimingCapsNtpServers.  # noqa: E501
		:type ntp_server_addr: TimingCapsNtpServersNtpServerAddr
		:param min_polling_interval: The min_polling_interval of this TimingCapsNtpServers.  # noqa: E501
		:type min_polling_interval: TimingCapsNtpServersMinPollingInterval
		:param max_polling_interval: The max_polling_interval of this TimingCapsNtpServers.  # noqa: E501
		:type max_polling_interval: TimingCapsNtpServersMaxPollingInterval
		:param local_priority: The local_priority of this TimingCapsNtpServers.  # noqa: E501
		:type local_priority: TimingCapsNtpServersLocalPriority
		:param authentication_option: The authentication_option of this TimingCapsNtpServers.  # noqa: E501
		:type authentication_option: TimingCapsNtpServersAuthenticationOption
		:param authentication_key_num: The authentication_key_num of this TimingCapsNtpServers.  # noqa: E501
		:type authentication_key_num: TimingCapsNtpServersAuthenticationKeyNum
		"""
		self.swagger_types = {
			'ntp_server_addr_type': TimingCapsNtpServersNtpServerAddrType,
			'ntp_server_addr': TimingCapsNtpServersNtpServerAddr,
			'min_polling_interval': TimingCapsNtpServersMinPollingInterval,
			'max_polling_interval': TimingCapsNtpServersMaxPollingInterval,
			'local_priority': TimingCapsNtpServersLocalPriority,
			'authentication_option': TimingCapsNtpServersAuthenticationOption,
			'authentication_key_num': TimingCapsNtpServersAuthenticationKeyNum
		}

		self.attribute_map = {
			'ntp_server_addr_type': 'ntpServerAddrType',
			'ntp_server_addr': 'ntpServerAddr',
			'min_polling_interval': 'minPollingInterval',
			'max_polling_interval': 'maxPollingInterval',
			'local_priority': 'localPriority',
			'authentication_option': 'authenticationOption',
			'authentication_key_num': 'authenticationKeyNum'
		}
		self._ntp_server_addr_type = ntp_server_addr_type
		self._ntp_server_addr = ntp_server_addr
		self._min_polling_interval = min_polling_interval
		self._max_polling_interval = max_polling_interval
		self._local_priority = local_priority
		self._authentication_option = authentication_option
		self._authentication_key_num = authentication_key_num

	@classmethod
	def from_dict(cls, dikt) -> 'TimingCapsNtpServers':
		"""Returns the dict as a model

		:param dikt: A dict.
		:type: dict
		:return: The TimingCaps.NtpServers of this TimingCapsNtpServers.  # noqa: E501
		:rtype: TimingCapsNtpServers
		"""
		return util.deserialize_model(dikt, cls)

	@property
	def ntp_server_addr_type(self) -> TimingCapsNtpServersNtpServerAddrType:
		"""Gets the ntp_server_addr_type of this TimingCapsNtpServers.


		:return: The ntp_server_addr_type of this TimingCapsNtpServers.
		:rtype: TimingCapsNtpServersNtpServerAddrType
		"""
		return self._ntp_server_addr_type

	@ntp_server_addr_type.setter
	def ntp_server_addr_type(self, ntp_server_addr_type: TimingCapsNtpServersNtpServerAddrType):
		"""Sets the ntp_server_addr_type of this TimingCapsNtpServers.


		:param ntp_server_addr_type: The ntp_server_addr_type of this TimingCapsNtpServers.
		:type ntp_server_addr_type: TimingCapsNtpServersNtpServerAddrType
		"""
		if ntp_server_addr_type is None:
			raise ValueError("Invalid value for `ntp_server_addr_type`, must not be `None`")  # noqa: E501

		self._ntp_server_addr_type = ntp_server_addr_type

	@property
	def ntp_server_addr(self) -> TimingCapsNtpServersNtpServerAddr:
		"""Gets the ntp_server_addr of this TimingCapsNtpServers.


		:return: The ntp_server_addr of this TimingCapsNtpServers.
		:rtype: TimingCapsNtpServersNtpServerAddr
		"""
		return self._ntp_server_addr

	@ntp_server_addr.setter
	def ntp_server_addr(self, ntp_server_addr: TimingCapsNtpServersNtpServerAddr):
		"""Sets the ntp_server_addr of this TimingCapsNtpServers.


		:param ntp_server_addr: The ntp_server_addr of this TimingCapsNtpServers.
		:type ntp_server_addr: TimingCapsNtpServersNtpServerAddr
		"""
		if ntp_server_addr is None:
			raise ValueError("Invalid value for `ntp_server_addr`, must not be `None`")  # noqa: E501

		self._ntp_server_addr = ntp_server_addr

	@property
	def min_polling_interval(self) -> TimingCapsNtpServersMinPollingInterval:
		"""Gets the min_polling_interval of this TimingCapsNtpServers.


		:return: The min_polling_interval of this TimingCapsNtpServers.
		:rtype: TimingCapsNtpServersMinPollingInterval
		"""
		return self._min_polling_interval

	@min_polling_interval.setter
	def min_polling_interval(self, min_polling_interval: TimingCapsNtpServersMinPollingInterval):
		"""Sets the min_polling_interval of this TimingCapsNtpServers.


		:param min_polling_interval: The min_polling_interval of this TimingCapsNtpServers.
		:type min_polling_interval: TimingCapsNtpServersMinPollingInterval
		"""
		if min_polling_interval is None:
			raise ValueError("Invalid value for `min_polling_interval`, must not be `None`")  # noqa: E501

		self._min_polling_interval = min_polling_interval

	@property
	def max_polling_interval(self) -> TimingCapsNtpServersMaxPollingInterval:
		"""Gets the max_polling_interval of this TimingCapsNtpServers.


		:return: The max_polling_interval of this TimingCapsNtpServers.
		:rtype: TimingCapsNtpServersMaxPollingInterval
		"""
		return self._max_polling_interval

	@max_polling_interval.setter
	def max_polling_interval(self, max_polling_interval: TimingCapsNtpServersMaxPollingInterval):
		"""Sets the max_polling_interval of this TimingCapsNtpServers.


		:param max_polling_interval: The max_polling_interval of this TimingCapsNtpServers.
		:type max_polling_interval: TimingCapsNtpServersMaxPollingInterval
		"""
		if max_polling_interval is None:
			raise ValueError("Invalid value for `max_polling_interval`, must not be `None`")  # noqa: E501

		self._max_polling_interval = max_polling_interval

	@property
	def local_priority(self) -> TimingCapsNtpServersLocalPriority:
		"""Gets the local_priority of this TimingCapsNtpServers.


		:return: The local_priority of this TimingCapsNtpServers.
		:rtype: TimingCapsNtpServersLocalPriority
		"""
		return self._local_priority

	@local_priority.setter
	def local_priority(self, local_priority: TimingCapsNtpServersLocalPriority):
		"""Sets the local_priority of this TimingCapsNtpServers.


		:param local_priority: The local_priority of this TimingCapsNtpServers.
		:type local_priority: TimingCapsNtpServersLocalPriority
		"""
		if local_priority is None:
			raise ValueError("Invalid value for `local_priority`, must not be `None`")  # noqa: E501

		self._local_priority = local_priority

	@property
	def authentication_option(self) -> TimingCapsNtpServersAuthenticationOption:
		"""Gets the authentication_option of this TimingCapsNtpServers.


		:return: The authentication_option of this TimingCapsNtpServers.
		:rtype: TimingCapsNtpServersAuthenticationOption
		"""
		return self._authentication_option

	@authentication_option.setter
	def authentication_option(self, authentication_option: TimingCapsNtpServersAuthenticationOption):
		"""Sets the authentication_option of this TimingCapsNtpServers.


		:param authentication_option: The authentication_option of this TimingCapsNtpServers.
		:type authentication_option: TimingCapsNtpServersAuthenticationOption
		"""
		if authentication_option is None:
			raise ValueError("Invalid value for `authentication_option`, must not be `None`")  # noqa: E501

		self._authentication_option = authentication_option

	@property
	def authentication_key_num(self) -> TimingCapsNtpServersAuthenticationKeyNum:
		"""Gets the authentication_key_num of this TimingCapsNtpServers.


		:return: The authentication_key_num of this TimingCapsNtpServers.
		:rtype: TimingCapsNtpServersAuthenticationKeyNum
		"""
		return self._authentication_key_num

	@authentication_key_num.setter
	def authentication_key_num(self, authentication_key_num: TimingCapsNtpServersAuthenticationKeyNum):
		"""Sets the authentication_key_num of this TimingCapsNtpServers.


		:param authentication_key_num: The authentication_key_num of this TimingCapsNtpServers.
		:type authentication_key_num: TimingCapsNtpServersAuthenticationKeyNum
		"""
		if authentication_key_num is None:
			raise ValueError("Invalid value for `authentication_key_num`, must not be `None`")  # noqa: E501

		self._authentication_key_num = authentication_key_num
