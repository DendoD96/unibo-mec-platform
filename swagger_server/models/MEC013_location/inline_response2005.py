# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401 # pylint: disable=unused-import

from typing import List, Dict  # noqa: F401 # pylint: disable=unused-import

from swagger_server.models.base_model_ import Model
from swagger_server.models.MEC013_location.access_point_info import \
	AccessPointInfo  # noqa: F401 # pylint: disable=unused-import,E501
from swagger_server import util


class InlineResponse2005(Model):
	"""NOTE: This class is auto generated by the swagger code generator program.

	Do not edit the class manually.
	"""

	def __init__(self, access_point_info: AccessPointInfo = None):  # noqa: E501
		"""InlineResponse2005 - a model defined in Swagger

		:param access_point_info: The access_point_info of this InlineResponse2005.  # noqa: E501
		:type access_point_info: AccessPointInfo
		"""
		self.swagger_types = {
			'access_point_info': AccessPointInfo
		}

		self.attribute_map = {
			'access_point_info': 'accessPointInfo'
		}
		self._access_point_info = access_point_info

	@classmethod
	def from_dict(cls, dikt) -> 'InlineResponse2005':
		"""Returns the dict as a model

		:param dikt: A dict.
		:type: dict
		:return: The inline_response_200_5 of this InlineResponse2005.  # noqa: E501
		:rtype: InlineResponse2005
		"""
		return util.deserialize_model(dikt, cls)

	@property
	def access_point_info(self) -> AccessPointInfo:
		"""Gets the access_point_info of this InlineResponse2005.


		:return: The access_point_info of this InlineResponse2005.
		:rtype: AccessPointInfo
		"""
		return self._access_point_info

	@access_point_info.setter
	def access_point_info(self, access_point_info: AccessPointInfo):
		"""Sets the access_point_info of this InlineResponse2005.


		:param access_point_info: The access_point_info of this InlineResponse2005.
		:type access_point_info: AccessPointInfo
		"""

		self._access_point_info = access_point_info
