# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401 # pylint: disable=unused-import

from typing import List, Dict  # noqa: F401 # pylint: disable=unused-import

from swagger_server.models.base_model_ import Model
from swagger_server.models.MEC012_radio_network_information.rab_mod_notification_erab_qos_parameters_qos_information import \
	RabModNotificationErabQosParametersQosInformation  # noqa: F401 # pylint: disable=unused-import,E501
from swagger_server import util


class RabModNotificationErabQosParameters(Model):
	"""NOTE: This class is auto generated by the swagger code generator program.

	Do not edit the class manually.
	"""

	def __init__(self, qci: int = None,
	             qos_information: RabModNotificationErabQosParametersQosInformation = None):  # noqa: E501
		"""RabModNotificationErabQosParameters - a model defined in Swagger

		:param qci: The qci of this RabModNotificationErabQosParameters.  # noqa: E501
		:type qci: int
		:param qos_information: The qos_information of this RabModNotificationErabQosParameters.  # noqa: E501
		:type qos_information: RabModNotificationErabQosParametersQosInformation
		"""
		self.swagger_types = {
			'qci': int,
			'qos_information': RabModNotificationErabQosParametersQosInformation
		}

		self.attribute_map = {
			'qci': 'qci',
			'qos_information': 'qosInformation'
		}
		self._qci = qci
		self._qos_information = qos_information

	@classmethod
	def from_dict(cls, dikt) -> 'RabModNotificationErabQosParameters':
		"""Returns the dict as a model

		:param dikt: A dict.
		:type: dict
		:return: The RabModNotification_erabQosParameters of this RabModNotificationErabQosParameters.  # noqa: E501
		:rtype: RabModNotificationErabQosParameters
		"""
		return util.deserialize_model(dikt, cls)

	@property
	def qci(self) -> int:
		"""Gets the qci of this RabModNotificationErabQosParameters.

		QoS Class Identifier as defined in ETSI TS 123 401 [i.4].  # noqa: E501

		:return: The qci of this RabModNotificationErabQosParameters.
		:rtype: int
		"""
		return self._qci

	@qci.setter
	def qci(self, qci: int):
		"""Sets the qci of this RabModNotificationErabQosParameters.

		QoS Class Identifier as defined in ETSI TS 123 401 [i.4].  # noqa: E501

		:param qci: The qci of this RabModNotificationErabQosParameters.
		:type qci: int
		"""
		if qci is None:
			raise ValueError("Invalid value for `qci`, must not be `None`")  # noqa: E501

		self._qci = qci

	@property
	def qos_information(self) -> RabModNotificationErabQosParametersQosInformation:
		"""Gets the qos_information of this RabModNotificationErabQosParameters.


		:return: The qos_information of this RabModNotificationErabQosParameters.
		:rtype: RabModNotificationErabQosParametersQosInformation
		"""
		return self._qos_information

	@qos_information.setter
	def qos_information(self, qos_information: RabModNotificationErabQosParametersQosInformation):
		"""Sets the qos_information of this RabModNotificationErabQosParameters.


		:param qos_information: The qos_information of this RabModNotificationErabQosParameters.
		:type qos_information: RabModNotificationErabQosParametersQosInformation
		"""

		self._qos_information = qos_information
