# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401 # pylint: disable=unused-import

from typing import List, Dict  # noqa: F401 # pylint: disable=unused-import

from swagger_server.models.base_model_ import Model
from swagger_server import util


class AniAlarmNotificationAniId(Model):
	"""NOTE: This class is auto generated by the swagger code generator program.

	Do not edit the class manually.
	"""

	def __init__(self, onu_id: str = None, ani_index: str = None):  # noqa: E501
		"""AniAlarmNotificationAniId - a model defined in Swagger

		:param onu_id: The onu_id of this AniAlarmNotificationAniId.  # noqa: E501
		:type onu_id: str
		:param ani_index: The ani_index of this AniAlarmNotificationAniId.  # noqa: E501
		:type ani_index: str
		"""
		self.swagger_types = {
			'onu_id': str,
			'ani_index': str
		}

		self.attribute_map = {
			'onu_id': 'onuId',
			'ani_index': 'aniIndex'
		}
		self._onu_id = onu_id
		self._ani_index = ani_index

	@classmethod
	def from_dict(cls, dikt) -> 'AniAlarmNotificationAniId':
		"""Returns the dict as a model

		:param dikt: A dict.
		:type: dict
		:return: The AniAlarmNotification.aniId of this AniAlarmNotificationAniId.  # noqa: E501
		:rtype: AniAlarmNotificationAniId
		"""
		return util.deserialize_model(dikt, cls)

	@property
	def onu_id(self) -> str:
		"""Gets the onu_id of this AniAlarmNotificationAniId.

		The unique identifiers for the optical network unit.  # noqa: E501

		:return: The onu_id of this AniAlarmNotificationAniId.
		:rtype: str
		"""
		return self._onu_id

	@onu_id.setter
	def onu_id(self, onu_id: str):
		"""Sets the onu_id of this AniAlarmNotificationAniId.

		The unique identifiers for the optical network unit.  # noqa: E501

		:param onu_id: The onu_id of this AniAlarmNotificationAniId.
		:type onu_id: str
		"""
		if onu_id is None:
			raise ValueError("Invalid value for `onu_id`, must not be `None`")  # noqa: E501

		self._onu_id = onu_id

	@property
	def ani_index(self) -> str:
		"""Gets the ani_index of this AniAlarmNotificationAniId.

		The index of an access network interface supported by the optical network unit.  # noqa: E501

		:return: The ani_index of this AniAlarmNotificationAniId.
		:rtype: str
		"""
		return self._ani_index

	@ani_index.setter
	def ani_index(self, ani_index: str):
		"""Sets the ani_index of this AniAlarmNotificationAniId.

		The index of an access network interface supported by the optical network unit.  # noqa: E501

		:param ani_index: The ani_index of this AniAlarmNotificationAniId.
		:type ani_index: str
		"""
		if ani_index is None:
			raise ValueError("Invalid value for `ani_index`, must not be `None`")  # noqa: E501

		self._ani_index = ani_index
