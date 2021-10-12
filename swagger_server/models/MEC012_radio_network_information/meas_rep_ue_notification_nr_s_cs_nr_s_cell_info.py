# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401 # pylint: disable=unused-import

from typing import List, Dict  # noqa: F401 # pylint: disable=unused-import

from swagger_server.models.base_model_ import Model
from swagger_server.models.MEC012_radio_network_information.nr_cell_id import \
	NrCellId  # noqa: F401 # pylint: disable=unused-import,E501
from swagger_server.models.MEC012_radio_network_information.plmn import \
	Plmn  # noqa: F401 # pylint: disable=unused-import,E501
from swagger_server import util


class MeasRepUeNotificationNrSCsNrSCellInfo(Model):
	"""NOTE: This class is auto generated by the swagger code generator program.

	Do not edit the class manually.
	"""

	def __init__(self, nr_s_cell_g_id: NrCellId = None, nr_s_cell_plmn: List[Plmn] = None):  # noqa: E501
		"""MeasRepUeNotificationNrSCsNrSCellInfo - a model defined in Swagger

		:param nr_s_cell_g_id: The nr_s_cell_g_id of this MeasRepUeNotificationNrSCsNrSCellInfo.  # noqa: E501
		:type nr_s_cell_g_id: NrCellId
		:param nr_s_cell_plmn: The nr_s_cell_plmn of this MeasRepUeNotificationNrSCsNrSCellInfo.  # noqa: E501
		:type nr_s_cell_plmn: List[Plmn]
		"""
		self.swagger_types = {
			'nr_s_cell_g_id': NrCellId,
			'nr_s_cell_plmn': List[Plmn]
		}

		self.attribute_map = {
			'nr_s_cell_g_id': 'nrSCellGId',
			'nr_s_cell_plmn': 'nrSCellPlmn'
		}
		self._nr_s_cell_g_id = nr_s_cell_g_id
		self._nr_s_cell_plmn = nr_s_cell_plmn

	@classmethod
	def from_dict(cls, dikt) -> 'MeasRepUeNotificationNrSCsNrSCellInfo':
		"""Returns the dict as a model

		:param dikt: A dict.
		:type: dict
		:return: The MeasRepUeNotification_nrSCs_nrSCellInfo of this MeasRepUeNotificationNrSCsNrSCellInfo.  # noqa: E501
		:rtype: MeasRepUeNotificationNrSCsNrSCellInfo
		"""
		return util.deserialize_model(dikt, cls)

	@property
	def nr_s_cell_g_id(self) -> NrCellId:
		"""Gets the nr_s_cell_g_id of this MeasRepUeNotificationNrSCsNrSCellInfo.


		:return: The nr_s_cell_g_id of this MeasRepUeNotificationNrSCsNrSCellInfo.
		:rtype: NrCellId
		"""
		return self._nr_s_cell_g_id

	@nr_s_cell_g_id.setter
	def nr_s_cell_g_id(self, nr_s_cell_g_id: NrCellId):
		"""Sets the nr_s_cell_g_id of this MeasRepUeNotificationNrSCsNrSCellInfo.


		:param nr_s_cell_g_id: The nr_s_cell_g_id of this MeasRepUeNotificationNrSCsNrSCellInfo.
		:type nr_s_cell_g_id: NrCellId
		"""

		self._nr_s_cell_g_id = nr_s_cell_g_id

	@property
	def nr_s_cell_plmn(self) -> List[Plmn]:
		"""Gets the nr_s_cell_plmn of this MeasRepUeNotificationNrSCsNrSCellInfo.

		Public land mobile network identities.  # noqa: E501

		:return: The nr_s_cell_plmn of this MeasRepUeNotificationNrSCsNrSCellInfo.
		:rtype: List[Plmn]
		"""
		return self._nr_s_cell_plmn

	@nr_s_cell_plmn.setter
	def nr_s_cell_plmn(self, nr_s_cell_plmn: List[Plmn]):
		"""Sets the nr_s_cell_plmn of this MeasRepUeNotificationNrSCsNrSCellInfo.

		Public land mobile network identities.  # noqa: E501

		:param nr_s_cell_plmn: The nr_s_cell_plmn of this MeasRepUeNotificationNrSCsNrSCellInfo.
		:type nr_s_cell_plmn: List[Plmn]
		"""

		self._nr_s_cell_plmn = nr_s_cell_plmn
