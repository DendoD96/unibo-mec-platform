# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401 # pylint: disable=unused-import

from typing import List, Dict  # noqa: F401 # pylint: disable=unused-import

from swagger_server.models.base_model_ import Model
from swagger_server.models.MEC012_radio_network_information.associate_id import \
	AssociateId  # noqa: F401 # pylint: disable=unused-import,E501
from swagger_server.models.MEC012_radio_network_information.ecgi import \
	Ecgi  # noqa: F401 # pylint: disable=unused-import,E501
from swagger_server.models.MEC012_radio_network_information.rab_est_notification_erab_qos_parameters import \
	RabEstNotificationErabQosParameters  # noqa: F401 # pylint: disable=unused-import,E501
from swagger_server.models.MEC012_radio_network_information.rab_est_notification_temp_ue_id import \
	RabEstNotificationTempUeId  # noqa: F401 # pylint: disable=unused-import,E501
from swagger_server.models.MEC012_radio_network_information.time_stamp import \
	TimeStamp  # noqa: F401 # pylint: disable=unused-import,E501
from swagger_server import util


class RabEstNotification(Model):
	"""NOTE: This class is auto generated by the swagger code generator program.

	Do not edit the class manually.
	"""

	def __init__(self, associate_id: List[AssociateId] = None, ecgi: Ecgi = None, erab_id: int = None,
	             erab_qos_parameters: RabEstNotificationErabQosParameters = None, notification_type: str = None,
	             temp_ue_id: RabEstNotificationTempUeId = None, time_stamp: TimeStamp = None):  # noqa: E501
		"""RabEstNotification - a model defined in Swagger

		:param associate_id: The associate_id of this RabEstNotification.  # noqa: E501
		:type associate_id: List[AssociateId]
		:param ecgi: The ecgi of this RabEstNotification.  # noqa: E501
		:type ecgi: Ecgi
		:param erab_id: The erab_id of this RabEstNotification.  # noqa: E501
		:type erab_id: int
		:param erab_qos_parameters: The erab_qos_parameters of this RabEstNotification.  # noqa: E501
		:type erab_qos_parameters: RabEstNotificationErabQosParameters
		:param notification_type: The notification_type of this RabEstNotification.  # noqa: E501
		:type notification_type: str
		:param temp_ue_id: The temp_ue_id of this RabEstNotification.  # noqa: E501
		:type temp_ue_id: RabEstNotificationTempUeId
		:param time_stamp: The time_stamp of this RabEstNotification.  # noqa: E501
		:type time_stamp: TimeStamp
		"""
		self.swagger_types = {
			'associate_id': List[AssociateId],
			'ecgi': Ecgi,
			'erab_id': int,
			'erab_qos_parameters': RabEstNotificationErabQosParameters,
			'notification_type': str,
			'temp_ue_id': RabEstNotificationTempUeId,
			'time_stamp': TimeStamp
		}

		self.attribute_map = {
			'associate_id': 'associateId',
			'ecgi': 'ecgi',
			'erab_id': 'erabId',
			'erab_qos_parameters': 'erabQosParameters',
			'notification_type': 'notificationType',
			'temp_ue_id': 'tempUeId',
			'time_stamp': 'timeStamp'
		}
		self._associate_id = associate_id
		self._ecgi = ecgi
		self._erab_id = erab_id
		self._erab_qos_parameters = erab_qos_parameters
		self._notification_type = notification_type
		self._temp_ue_id = temp_ue_id
		self._time_stamp = time_stamp

	@classmethod
	def from_dict(cls, dikt) -> 'RabEstNotification':
		"""Returns the dict as a model

		:param dikt: A dict.
		:type: dict
		:return: The RabEstNotification of this RabEstNotification.  # noqa: E501
		:rtype: RabEstNotification
		"""
		return util.deserialize_model(dikt, cls)

	@property
	def associate_id(self) -> List[AssociateId]:
		"""Gets the associate_id of this RabEstNotification.

		0 to N identifiers to bind the event for a specific UE or flow.   # noqa: E501

		:return: The associate_id of this RabEstNotification.
		:rtype: List[AssociateId]
		"""
		return self._associate_id

	@associate_id.setter
	def associate_id(self, associate_id: List[AssociateId]):
		"""Sets the associate_id of this RabEstNotification.

		0 to N identifiers to bind the event for a specific UE or flow.   # noqa: E501

		:param associate_id: The associate_id of this RabEstNotification.
		:type associate_id: List[AssociateId]
		"""

		self._associate_id = associate_id

	@property
	def ecgi(self) -> Ecgi:
		"""Gets the ecgi of this RabEstNotification.


		:return: The ecgi of this RabEstNotification.
		:rtype: Ecgi
		"""
		return self._ecgi

	@ecgi.setter
	def ecgi(self, ecgi: Ecgi):
		"""Sets the ecgi of this RabEstNotification.


		:param ecgi: The ecgi of this RabEstNotification.
		:type ecgi: Ecgi
		"""
		if ecgi is None:
			raise ValueError("Invalid value for `ecgi`, must not be `None`")  # noqa: E501

		self._ecgi = ecgi

	@property
	def erab_id(self) -> int:
		"""Gets the erab_id of this RabEstNotification.

		The attribute that uniquely identifies a Radio Access bearer for specific UE as defined in ETSI TS 136 413 [i.3].  # noqa: E501

		:return: The erab_id of this RabEstNotification.
		:rtype: int
		"""
		return self._erab_id

	@erab_id.setter
	def erab_id(self, erab_id: int):
		"""Sets the erab_id of this RabEstNotification.

		The attribute that uniquely identifies a Radio Access bearer for specific UE as defined in ETSI TS 136 413 [i.3].  # noqa: E501

		:param erab_id: The erab_id of this RabEstNotification.
		:type erab_id: int
		"""
		if erab_id is None:
			raise ValueError("Invalid value for `erab_id`, must not be `None`")  # noqa: E501

		self._erab_id = erab_id

	@property
	def erab_qos_parameters(self) -> RabEstNotificationErabQosParameters:
		"""Gets the erab_qos_parameters of this RabEstNotification.


		:return: The erab_qos_parameters of this RabEstNotification.
		:rtype: RabEstNotificationErabQosParameters
		"""
		return self._erab_qos_parameters

	@erab_qos_parameters.setter
	def erab_qos_parameters(self, erab_qos_parameters: RabEstNotificationErabQosParameters):
		"""Sets the erab_qos_parameters of this RabEstNotification.


		:param erab_qos_parameters: The erab_qos_parameters of this RabEstNotification.
		:type erab_qos_parameters: RabEstNotificationErabQosParameters
		"""

		self._erab_qos_parameters = erab_qos_parameters

	@property
	def notification_type(self) -> str:
		"""Gets the notification_type of this RabEstNotification.

		Shall be set to \"RabEstNotification\".  # noqa: E501

		:return: The notification_type of this RabEstNotification.
		:rtype: str
		"""
		return self._notification_type

	@notification_type.setter
	def notification_type(self, notification_type: str):
		"""Sets the notification_type of this RabEstNotification.

		Shall be set to \"RabEstNotification\".  # noqa: E501

		:param notification_type: The notification_type of this RabEstNotification.
		:type notification_type: str
		"""
		if notification_type is None:
			raise ValueError("Invalid value for `notification_type`, must not be `None`")  # noqa: E501

		self._notification_type = notification_type

	@property
	def temp_ue_id(self) -> RabEstNotificationTempUeId:
		"""Gets the temp_ue_id of this RabEstNotification.


		:return: The temp_ue_id of this RabEstNotification.
		:rtype: RabEstNotificationTempUeId
		"""
		return self._temp_ue_id

	@temp_ue_id.setter
	def temp_ue_id(self, temp_ue_id: RabEstNotificationTempUeId):
		"""Sets the temp_ue_id of this RabEstNotification.


		:param temp_ue_id: The temp_ue_id of this RabEstNotification.
		:type temp_ue_id: RabEstNotificationTempUeId
		"""

		self._temp_ue_id = temp_ue_id

	@property
	def time_stamp(self) -> TimeStamp:
		"""Gets the time_stamp of this RabEstNotification.


		:return: The time_stamp of this RabEstNotification.
		:rtype: TimeStamp
		"""
		return self._time_stamp

	@time_stamp.setter
	def time_stamp(self, time_stamp: TimeStamp):
		"""Sets the time_stamp of this RabEstNotification.


		:param time_stamp: The time_stamp of this RabEstNotification.
		:type time_stamp: TimeStamp
		"""

		self._time_stamp = time_stamp
