# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401 # pylint: disable=unused-import

from typing import List, Dict  # noqa: F401 # pylint: disable=unused-import

from swagger_server.models.base_model_ import Model
from swagger_server.models.MEC012_radio_network_information.ecgi import \
	Ecgi  # noqa: F401 # pylint: disable=unused-import,E501
from swagger_server import util


class MeasRepUeNotificationEutranNeighbourCellMeasInfo(Model):
	"""NOTE: This class is auto generated by the swagger code generator program.

	Do not edit the class manually.
	"""

	def __init__(self, ecgi: Ecgi = None, rsrp: int = None, rsrp_ex: int = None, rsrq: int = None, rsrq_ex: int = None,
	             sinr: int = None):  # noqa: E501
		"""MeasRepUeNotificationEutranNeighbourCellMeasInfo - a model defined in Swagger

		:param ecgi: The ecgi of this MeasRepUeNotificationEutranNeighbourCellMeasInfo.  # noqa: E501
		:type ecgi: Ecgi
		:param rsrp: The rsrp of this MeasRepUeNotificationEutranNeighbourCellMeasInfo.  # noqa: E501
		:type rsrp: int
		:param rsrp_ex: The rsrp_ex of this MeasRepUeNotificationEutranNeighbourCellMeasInfo.  # noqa: E501
		:type rsrp_ex: int
		:param rsrq: The rsrq of this MeasRepUeNotificationEutranNeighbourCellMeasInfo.  # noqa: E501
		:type rsrq: int
		:param rsrq_ex: The rsrq_ex of this MeasRepUeNotificationEutranNeighbourCellMeasInfo.  # noqa: E501
		:type rsrq_ex: int
		:param sinr: The sinr of this MeasRepUeNotificationEutranNeighbourCellMeasInfo.  # noqa: E501
		:type sinr: int
		"""
		self.swagger_types = {
			'ecgi': Ecgi,
			'rsrp': int,
			'rsrp_ex': int,
			'rsrq': int,
			'rsrq_ex': int,
			'sinr': int
		}

		self.attribute_map = {
			'ecgi': 'ecgi',
			'rsrp': 'rsrp',
			'rsrp_ex': 'rsrpEx',
			'rsrq': 'rsrq',
			'rsrq_ex': 'rsrqEx',
			'sinr': 'sinr'
		}
		self._ecgi = ecgi
		self._rsrp = rsrp
		self._rsrp_ex = rsrp_ex
		self._rsrq = rsrq
		self._rsrq_ex = rsrq_ex
		self._sinr = sinr

	@classmethod
	def from_dict(cls, dikt) -> 'MeasRepUeNotificationEutranNeighbourCellMeasInfo':
		"""Returns the dict as a model

		:param dikt: A dict.
		:type: dict
		:return: The MeasRepUeNotification_eutranNeighbourCellMeasInfo of this MeasRepUeNotificationEutranNeighbourCellMeasInfo.  # noqa: E501
		:rtype: MeasRepUeNotificationEutranNeighbourCellMeasInfo
		"""
		return util.deserialize_model(dikt, cls)

	@property
	def ecgi(self) -> Ecgi:
		"""Gets the ecgi of this MeasRepUeNotificationEutranNeighbourCellMeasInfo.


		:return: The ecgi of this MeasRepUeNotificationEutranNeighbourCellMeasInfo.
		:rtype: Ecgi
		"""
		return self._ecgi

	@ecgi.setter
	def ecgi(self, ecgi: Ecgi):
		"""Sets the ecgi of this MeasRepUeNotificationEutranNeighbourCellMeasInfo.


		:param ecgi: The ecgi of this MeasRepUeNotificationEutranNeighbourCellMeasInfo.
		:type ecgi: Ecgi
		"""

		self._ecgi = ecgi

	@property
	def rsrp(self) -> int:
		"""Gets the rsrp of this MeasRepUeNotificationEutranNeighbourCellMeasInfo.

		Reference Signal Received Power as defined in ETSI TS 136 214 [i.5].  # noqa: E501

		:return: The rsrp of this MeasRepUeNotificationEutranNeighbourCellMeasInfo.
		:rtype: int
		"""
		return self._rsrp

	@rsrp.setter
	def rsrp(self, rsrp: int):
		"""Sets the rsrp of this MeasRepUeNotificationEutranNeighbourCellMeasInfo.

		Reference Signal Received Power as defined in ETSI TS 136 214 [i.5].  # noqa: E501

		:param rsrp: The rsrp of this MeasRepUeNotificationEutranNeighbourCellMeasInfo.
		:type rsrp: int
		"""

		self._rsrp = rsrp

	@property
	def rsrp_ex(self) -> int:
		"""Gets the rsrp_ex of this MeasRepUeNotificationEutranNeighbourCellMeasInfo.

		Extended Reference Signal Received Power, with value mapping defined in ETSI TS 136 133 [i.16].  # noqa: E501

		:return: The rsrp_ex of this MeasRepUeNotificationEutranNeighbourCellMeasInfo.
		:rtype: int
		"""
		return self._rsrp_ex

	@rsrp_ex.setter
	def rsrp_ex(self, rsrp_ex: int):
		"""Sets the rsrp_ex of this MeasRepUeNotificationEutranNeighbourCellMeasInfo.

		Extended Reference Signal Received Power, with value mapping defined in ETSI TS 136 133 [i.16].  # noqa: E501

		:param rsrp_ex: The rsrp_ex of this MeasRepUeNotificationEutranNeighbourCellMeasInfo.
		:type rsrp_ex: int
		"""

		self._rsrp_ex = rsrp_ex

	@property
	def rsrq(self) -> int:
		"""Gets the rsrq of this MeasRepUeNotificationEutranNeighbourCellMeasInfo.

		Reference Signal Received Quality as defined in ETSI TS 136 214 [i.5].  # noqa: E501

		:return: The rsrq of this MeasRepUeNotificationEutranNeighbourCellMeasInfo.
		:rtype: int
		"""
		return self._rsrq

	@rsrq.setter
	def rsrq(self, rsrq: int):
		"""Sets the rsrq of this MeasRepUeNotificationEutranNeighbourCellMeasInfo.

		Reference Signal Received Quality as defined in ETSI TS 136 214 [i.5].  # noqa: E501

		:param rsrq: The rsrq of this MeasRepUeNotificationEutranNeighbourCellMeasInfo.
		:type rsrq: int
		"""

		self._rsrq = rsrq

	@property
	def rsrq_ex(self) -> int:
		"""Gets the rsrq_ex of this MeasRepUeNotificationEutranNeighbourCellMeasInfo.

		Extended Reference Signal Received Quality, with value mapping defined in ETSI TS 136 133 [i.16].  # noqa: E501

		:return: The rsrq_ex of this MeasRepUeNotificationEutranNeighbourCellMeasInfo.
		:rtype: int
		"""
		return self._rsrq_ex

	@rsrq_ex.setter
	def rsrq_ex(self, rsrq_ex: int):
		"""Sets the rsrq_ex of this MeasRepUeNotificationEutranNeighbourCellMeasInfo.

		Extended Reference Signal Received Quality, with value mapping defined in ETSI TS 136 133 [i.16].  # noqa: E501

		:param rsrq_ex: The rsrq_ex of this MeasRepUeNotificationEutranNeighbourCellMeasInfo.
		:type rsrq_ex: int
		"""

		self._rsrq_ex = rsrq_ex

	@property
	def sinr(self) -> int:
		"""Gets the sinr of this MeasRepUeNotificationEutranNeighbourCellMeasInfo.

		Reference Signal \"Signal to Interference plus Noise Ratio\", with value mapping defined in ETSI TS 136 133 [i.16].  # noqa: E501

		:return: The sinr of this MeasRepUeNotificationEutranNeighbourCellMeasInfo.
		:rtype: int
		"""
		return self._sinr

	@sinr.setter
	def sinr(self, sinr: int):
		"""Sets the sinr of this MeasRepUeNotificationEutranNeighbourCellMeasInfo.

		Reference Signal \"Signal to Interference plus Noise Ratio\", with value mapping defined in ETSI TS 136 133 [i.16].  # noqa: E501

		:param sinr: The sinr of this MeasRepUeNotificationEutranNeighbourCellMeasInfo.
		:type sinr: int
		"""

		self._sinr = sinr
