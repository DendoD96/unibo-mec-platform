# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401 # pylint: disable=unused-import

from typing import List, Dict  # noqa: F401 # pylint: disable=unused-import

from swagger_server.models.base_model_ import Model
from swagger_server.models.MEC012_radio_network_information.rab_est_notification_erab_qos_parameters import \
	RabEstNotificationErabQosParameters  # noqa: F401 # pylint: disable=unused-import,E501
from swagger_server import util


class RabInfoErabInfo(Model):
	"""NOTE: This class is auto generated by the swagger code generator program.

	Do not edit the class manually.
	"""

	def __init__(self, erab_id: int = None,
	             erab_qos_parameters: RabEstNotificationErabQosParameters = None):  # noqa: E501
		"""RabInfoErabInfo - a model defined in Swagger

		:param erab_id: The erab_id of this RabInfoErabInfo.  # noqa: E501
		:type erab_id: int
		:param erab_qos_parameters: The erab_qos_parameters of this RabInfoErabInfo.  # noqa: E501
		:type erab_qos_parameters: RabEstNotificationErabQosParameters
		"""
		self.swagger_types = {
			'erab_id': int,
			'erab_qos_parameters': RabEstNotificationErabQosParameters
		}

		self.attribute_map = {
			'erab_id': 'erabId',
			'erab_qos_parameters': 'erabQosParameters'
		}
		self._erab_id = erab_id
		self._erab_qos_parameters = erab_qos_parameters

	@classmethod
	def from_dict(cls, dikt) -> 'RabInfoErabInfo':
		"""Returns the dict as a model

		:param dikt: A dict.
		:type: dict
		:return: The RabInfo_erabInfo of this RabInfoErabInfo.  # noqa: E501
		:rtype: RabInfoErabInfo
		"""
		return util.deserialize_model(dikt, cls)

	@property
	def erab_id(self) -> int:
		"""Gets the erab_id of this RabInfoErabInfo.

		The attribute that uniquely identifies a Radio Access bearer for specific UE as defined in ETSI TS 136 413 [i.3].  # noqa: E501

		:return: The erab_id of this RabInfoErabInfo.
		:rtype: int
		"""
		return self._erab_id

	@erab_id.setter
	def erab_id(self, erab_id: int):
		"""Sets the erab_id of this RabInfoErabInfo.

		The attribute that uniquely identifies a Radio Access bearer for specific UE as defined in ETSI TS 136 413 [i.3].  # noqa: E501

		:param erab_id: The erab_id of this RabInfoErabInfo.
		:type erab_id: int
		"""

		self._erab_id = erab_id

	@property
	def erab_qos_parameters(self) -> RabEstNotificationErabQosParameters:
		"""Gets the erab_qos_parameters of this RabInfoErabInfo.


		:return: The erab_qos_parameters of this RabInfoErabInfo.
		:rtype: RabEstNotificationErabQosParameters
		"""
		return self._erab_qos_parameters

	@erab_qos_parameters.setter
	def erab_qos_parameters(self, erab_qos_parameters: RabEstNotificationErabQosParameters):
		"""Sets the erab_qos_parameters of this RabInfoErabInfo.


		:param erab_qos_parameters: The erab_qos_parameters of this RabInfoErabInfo.
		:type erab_qos_parameters: RabEstNotificationErabQosParameters
		"""

		self._erab_qos_parameters = erab_qos_parameters
