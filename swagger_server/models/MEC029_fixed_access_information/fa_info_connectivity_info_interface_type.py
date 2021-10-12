# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401 # pylint: disable=unused-import

from typing import List, Dict  # noqa: F401 # pylint: disable=unused-import

from swagger_server.models.base_model_ import Model
from swagger_server import util


class FaInfoConnectivityInfoInterfaceType(Model):
	"""NOTE: This class is auto generated by the swagger code generator program.

	Do not edit the class manually.
	"""

	_1 = "1"
	_2 = "2"
	_3 = "3"
	_4 = "4"
	_5 = "5"
	_6 = "6"
	_7 = "7"
	_8 = "8"
	_9 = "9"
	_10 = "10"

	def __init__(self):  # noqa: E501
		"""FaInfoConnectivityInfoInterfaceType - a model defined in Swagger

		"""
		self.swagger_types = {
		}

		self.attribute_map = {
		}

	@classmethod
	def from_dict(cls, dikt) -> 'FaInfoConnectivityInfoInterfaceType':
		"""Returns the dict as a model

		:param dikt: A dict.
		:type: dict
		:return: The FaInfo.connectivityInfo.interfaceType of this FaInfoConnectivityInfoInterfaceType.  # noqa: E501
		:rtype: FaInfoConnectivityInfoInterfaceType
		"""
		return util.deserialize_model(dikt, cls)
