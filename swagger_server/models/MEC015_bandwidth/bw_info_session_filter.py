# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401 # pylint: disable=unused-import

from typing import List, Dict  # noqa: F401 # pylint: disable=unused-import

from swagger_server.models.base_model_ import Model
from swagger_server import util


class BwInfoSessionFilter(Model):
	"""NOTE: This class is auto generated by the swagger code generator program.

	Do not edit the class manually.
	"""

	def __init__(self, dst_address: str = None, dst_port: List[str] = None, protocol: str = None, source_ip: str = None,
	             source_port: List[str] = None):  # noqa: E501
		"""BwInfoSessionFilter - a model defined in Swagger

		:param dst_address: The dst_address of this BwInfoSessionFilter.  # noqa: E501
		:type dst_address: str
		:param dst_port: The dst_port of this BwInfoSessionFilter.  # noqa: E501
		:type dst_port: List[str]
		:param protocol: The protocol of this BwInfoSessionFilter.  # noqa: E501
		:type protocol: str
		:param source_ip: The source_ip of this BwInfoSessionFilter.  # noqa: E501
		:type source_ip: str
		:param source_port: The source_port of this BwInfoSessionFilter.  # noqa: E501
		:type source_port: List[str]
		"""
		self.swagger_types = {
			'dst_address': str,
			'dst_port': List[str],
			'protocol': str,
			'source_ip': str,
			'source_port': List[str]
		}

		self.attribute_map = {
			'dst_address': 'dstAddress',
			'dst_port': 'dstPort',
			'protocol': 'protocol',
			'source_ip': 'sourceIp',
			'source_port': 'sourcePort'
		}
		self._dst_address = dst_address
		self._dst_port = dst_port
		self._protocol = protocol
		self._source_ip = source_ip
		self._source_port = source_port

	@classmethod
	def from_dict(cls, dikt) -> 'BwInfoSessionFilter':
		"""Returns the dict as a model

		:param dikt: A dict.
		:type: dict
		:return: The BwInfo_sessionFilter of this BwInfoSessionFilter.  # noqa: E501
		:rtype: BwInfoSessionFilter
		"""
		return util.deserialize_model(dikt, cls)

	@property
	def dst_address(self) -> str:
		"""Gets the dst_address of this BwInfoSessionFilter.

		Destination address identity of session (including range)  # noqa: E501

		:return: The dst_address of this BwInfoSessionFilter.
		:rtype: str
		"""
		return self._dst_address

	@dst_address.setter
	def dst_address(self, dst_address: str):
		"""Sets the dst_address of this BwInfoSessionFilter.

		Destination address identity of session (including range)  # noqa: E501

		:param dst_address: The dst_address of this BwInfoSessionFilter.
		:type dst_address: str
		"""

		self._dst_address = dst_address

	@property
	def dst_port(self) -> List[str]:
		"""Gets the dst_port of this BwInfoSessionFilter.

		Destination port identity of session  # noqa: E501

		:return: The dst_port of this BwInfoSessionFilter.
		:rtype: List[str]
		"""
		return self._dst_port

	@dst_port.setter
	def dst_port(self, dst_port: List[str]):
		"""Sets the dst_port of this BwInfoSessionFilter.

		Destination port identity of session  # noqa: E501

		:param dst_port: The dst_port of this BwInfoSessionFilter.
		:type dst_port: List[str]
		"""

		self._dst_port = dst_port

	@property
	def protocol(self) -> str:
		"""Gets the protocol of this BwInfoSessionFilter.

		Protocol number  # noqa: E501

		:return: The protocol of this BwInfoSessionFilter.
		:rtype: str
		"""
		return self._protocol

	@protocol.setter
	def protocol(self, protocol: str):
		"""Sets the protocol of this BwInfoSessionFilter.

		Protocol number  # noqa: E501

		:param protocol: The protocol of this BwInfoSessionFilter.
		:type protocol: str
		"""

		self._protocol = protocol

	@property
	def source_ip(self) -> str:
		"""Gets the source_ip of this BwInfoSessionFilter.

		Source address identity of session (including range)  # noqa: E501

		:return: The source_ip of this BwInfoSessionFilter.
		:rtype: str
		"""
		return self._source_ip

	@source_ip.setter
	def source_ip(self, source_ip: str):
		"""Sets the source_ip of this BwInfoSessionFilter.

		Source address identity of session (including range)  # noqa: E501

		:param source_ip: The source_ip of this BwInfoSessionFilter.
		:type source_ip: str
		"""

		self._source_ip = source_ip

	@property
	def source_port(self) -> List[str]:
		"""Gets the source_port of this BwInfoSessionFilter.

		Source port identity of session  # noqa: E501

		:return: The source_port of this BwInfoSessionFilter.
		:rtype: List[str]
		"""
		return self._source_port

	@source_port.setter
	def source_port(self, source_port: List[str]):
		"""Sets the source_port of this BwInfoSessionFilter.

		Source port identity of session  # noqa: E501

		:param source_port: The source_port of this BwInfoSessionFilter.
		:type source_port: List[str]
		"""

		self._source_port = source_port
