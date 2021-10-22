# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401 # pylint: disable=unused-import

from typing import List, Dict  # noqa: F401 # pylint: disable=unused-import

from swagger_server.models.base_model_ import Model
from swagger_server.models.MEC012_radio_network_information.associate_id import \
	AssociateId  # noqa: F401 # pylint: disable=unused-import,E501
from swagger_server.models.MEC012_radio_network_information.ecgi import \
	Ecgi  # noqa: F401 # pylint: disable=unused-import,E501
from swagger_server.models.MEC012_radio_network_information.time_stamp import \
	TimeStamp  # noqa: F401 # pylint: disable=unused-import,E501
from swagger_server import util


class MeasTaNotification(Model):
	"""NOTE: This class is auto generated by the swagger code generator program.

	Do not edit the class manually.
	"""

	def __init__(self, associate_id: List[AssociateId] = None, ecgi: Ecgi = None, notification_type: str = None,
	             time_stamp: TimeStamp = None, timing_advance: int = None):  # noqa: E501
		"""MeasTaNotification - a model defined in Swagger

		:param associate_id: The associate_id of this MeasTaNotification.  # noqa: E501
		:type associate_id: List[AssociateId]
		:param ecgi: The ecgi of this MeasTaNotification.  # noqa: E501
		:type ecgi: Ecgi
		:param notification_type: The notification_type of this MeasTaNotification.  # noqa: E501
		:type notification_type: str
		:param time_stamp: The time_stamp of this MeasTaNotification.  # noqa: E501
		:type time_stamp: TimeStamp
		:param timing_advance: The timing_advance of this MeasTaNotification.  # noqa: E501
		:type timing_advance: int
		"""
		self.swagger_types = {
			'associate_id': List[AssociateId],
			'ecgi': Ecgi,
			'notification_type': str,
			'time_stamp': TimeStamp,
			'timing_advance': int
		}

		self.attribute_map = {
			'associate_id': 'associateId',
			'ecgi': 'ecgi',
			'notification_type': 'notificationType',
			'time_stamp': 'timeStamp',
			'timing_advance': 'timingAdvance'
		}
		self._associate_id = associate_id
		self._ecgi = ecgi
		self._notification_type = notification_type
		self._time_stamp = time_stamp
		self._timing_advance = timing_advance

	@classmethod
	def from_dict(cls, dikt) -> 'MeasTaNotification':
		"""Returns the dict as a model

		:param dikt: A dict.
		:type: dict
		:return: The MeasTaNotification of this MeasTaNotification.  # noqa: E501
		:rtype: MeasTaNotification
		"""
		return util.deserialize_model(dikt, cls)

	@property
	def associate_id(self) -> List[AssociateId]:
		"""Gets the associate_id of this MeasTaNotification.

		0 to N identifiers to associate the event for a specific UE or flow.  # noqa: E501

		:return: The associate_id of this MeasTaNotification.
		:rtype: List[AssociateId]
		"""
		return self._associate_id

	@associate_id.setter
	def associate_id(self, associate_id: List[AssociateId]):
		"""Sets the associate_id of this MeasTaNotification.

		0 to N identifiers to associate the event for a specific UE or flow.  # noqa: E501

		:param associate_id: The associate_id of this MeasTaNotification.
		:type associate_id: List[AssociateId]
		"""

		self._associate_id = associate_id

	@property
	def ecgi(self) -> Ecgi:
		"""Gets the ecgi of this MeasTaNotification.


		:return: The ecgi of this MeasTaNotification.
		:rtype: Ecgi
		"""
		return self._ecgi

	@ecgi.setter
	def ecgi(self, ecgi: Ecgi):
		"""Sets the ecgi of this MeasTaNotification.


		:param ecgi: The ecgi of this MeasTaNotification.
		:type ecgi: Ecgi
		"""
		if ecgi is None:
			raise ValueError("Invalid value for `ecgi`, must not be `None`")  # noqa: E501

		self._ecgi = ecgi

	@property
	def notification_type(self) -> str:
		"""Gets the notification_type of this MeasTaNotification.

		Shall be set to \"MeasTaNotification\".  # noqa: E501

		:return: The notification_type of this MeasTaNotification.
		:rtype: str
		"""
		return self._notification_type

	@notification_type.setter
	def notification_type(self, notification_type: str):
		"""Sets the notification_type of this MeasTaNotification.

		Shall be set to \"MeasTaNotification\".  # noqa: E501

		:param notification_type: The notification_type of this MeasTaNotification.
		:type notification_type: str
		"""
		if notification_type is None:
			raise ValueError("Invalid value for `notification_type`, must not be `None`")  # noqa: E501

		self._notification_type = notification_type

	@property
	def time_stamp(self) -> TimeStamp:
		"""Gets the time_stamp of this MeasTaNotification.


		:return: The time_stamp of this MeasTaNotification.
		:rtype: TimeStamp
		"""
		return self._time_stamp

	@time_stamp.setter
	def time_stamp(self, time_stamp: TimeStamp):
		"""Sets the time_stamp of this MeasTaNotification.


		:param time_stamp: The time_stamp of this MeasTaNotification.
		:type time_stamp: TimeStamp
		"""

		self._time_stamp = time_stamp

	@property
	def timing_advance(self) -> int:
		"""Gets the timing_advance of this MeasTaNotification.

		The timing advance as defined in ETSI TS 136 214 [i.5].  # noqa: E501

		:return: The timing_advance of this MeasTaNotification.
		:rtype: int
		"""
		return self._timing_advance

	@timing_advance.setter
	def timing_advance(self, timing_advance: int):
		"""Sets the timing_advance of this MeasTaNotification.

		The timing advance as defined in ETSI TS 136 214 [i.5].  # noqa: E501

		:param timing_advance: The timing_advance of this MeasTaNotification.
		:type timing_advance: int
		"""
		if timing_advance is None:
			raise ValueError("Invalid value for `timing_advance`, must not be `None`")  # noqa: E501

		self._timing_advance = timing_advance
