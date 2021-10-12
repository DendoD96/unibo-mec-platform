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


class MeasRepUeNotificationNrBNCsNrBNCellInfo(Model):
	"""NOTE: This class is auto generated by the swagger code generator program.

	Do not edit the class manually.
	"""

	def __init__(self, nr_bn_cell_g_id: NrCellId = None, nr_bn_cell_plmn: List[Plmn] = None):  # noqa: E501
		"""MeasRepUeNotificationNrBNCsNrBNCellInfo - a model defined in Swagger

		:param nr_bn_cell_g_id: The nr_bn_cell_g_id of this MeasRepUeNotificationNrBNCsNrBNCellInfo.  # noqa: E501
		:type nr_bn_cell_g_id: NrCellId
		:param nr_bn_cell_plmn: The nr_bn_cell_plmn of this MeasRepUeNotificationNrBNCsNrBNCellInfo.  # noqa: E501
		:type nr_bn_cell_plmn: List[Plmn]
		"""
		self.swagger_types = {
			'nr_bn_cell_g_id': NrCellId,
			'nr_bn_cell_plmn': List[Plmn]
		}

		self.attribute_map = {
			'nr_bn_cell_g_id': 'nrBNCellGId',
			'nr_bn_cell_plmn': 'nrBNCellPlmn'
		}
		self._nr_bn_cell_g_id = nr_bn_cell_g_id
		self._nr_bn_cell_plmn = nr_bn_cell_plmn

	@classmethod
	def from_dict(cls, dikt) -> 'MeasRepUeNotificationNrBNCsNrBNCellInfo':
		"""Returns the dict as a model

		:param dikt: A dict.
		:type: dict
		:return: The MeasRepUeNotification_nrBNCs_nrBNCellInfo of this MeasRepUeNotificationNrBNCsNrBNCellInfo.  # noqa: E501
		:rtype: MeasRepUeNotificationNrBNCsNrBNCellInfo
		"""
		return util.deserialize_model(dikt, cls)

	@property
	def nr_bn_cell_g_id(self) -> NrCellId:
		"""Gets the nr_bn_cell_g_id of this MeasRepUeNotificationNrBNCsNrBNCellInfo.


		:return: The nr_bn_cell_g_id of this MeasRepUeNotificationNrBNCsNrBNCellInfo.
		:rtype: NrCellId
		"""
		return self._nr_bn_cell_g_id

	@nr_bn_cell_g_id.setter
	def nr_bn_cell_g_id(self, nr_bn_cell_g_id: NrCellId):
		"""Sets the nr_bn_cell_g_id of this MeasRepUeNotificationNrBNCsNrBNCellInfo.


		:param nr_bn_cell_g_id: The nr_bn_cell_g_id of this MeasRepUeNotificationNrBNCsNrBNCellInfo.
		:type nr_bn_cell_g_id: NrCellId
		"""

		self._nr_bn_cell_g_id = nr_bn_cell_g_id

	@property
	def nr_bn_cell_plmn(self) -> List[Plmn]:
		"""Gets the nr_bn_cell_plmn of this MeasRepUeNotificationNrBNCsNrBNCellInfo.

		Public land mobile network identities  # noqa: E501

		:return: The nr_bn_cell_plmn of this MeasRepUeNotificationNrBNCsNrBNCellInfo.
		:rtype: List[Plmn]
		"""
		return self._nr_bn_cell_plmn

	@nr_bn_cell_plmn.setter
	def nr_bn_cell_plmn(self, nr_bn_cell_plmn: List[Plmn]):
		"""Sets the nr_bn_cell_plmn of this MeasRepUeNotificationNrBNCsNrBNCellInfo.

		Public land mobile network identities  # noqa: E501

		:param nr_bn_cell_plmn: The nr_bn_cell_plmn of this MeasRepUeNotificationNrBNCsNrBNCellInfo.
		:type nr_bn_cell_plmn: List[Plmn]
		"""

		self._nr_bn_cell_plmn = nr_bn_cell_plmn
