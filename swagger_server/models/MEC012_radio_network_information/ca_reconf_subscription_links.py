# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401 # pylint: disable=unused-import

from typing import List, Dict  # noqa: F401 # pylint: disable=unused-import

from swagger_server.models.base_model_ import Model
from swagger_server.models.MEC012_radio_network_information.link_type import \
	LinkType  # noqa: F401 # pylint: disable=unused-import,E501
from swagger_server import util


class CaReconfSubscriptionLinks(Model):
	"""NOTE: This class is auto generated by the swagger code generator program.

	Do not edit the class manually.
	"""

	def __init__(self, _self: LinkType = None):  # noqa: E501
		"""CaReconfSubscriptionLinks - a model defined in Swagger

		:param _self: The _self of this CaReconfSubscriptionLinks.  # noqa: E501
		:type _self: LinkType
		"""
		self.swagger_types = {
			'_self': LinkType
		}

		self.attribute_map = {
			'_self': 'self'
		}
		self.__self = _self

	@classmethod
	def from_dict(cls, dikt) -> 'CaReconfSubscriptionLinks':
		"""Returns the dict as a model

		:param dikt: A dict.
		:type: dict
		:return: The CaReconfSubscription__links of this CaReconfSubscriptionLinks.  # noqa: E501
		:rtype: CaReconfSubscriptionLinks
		"""
		return util.deserialize_model(dikt, cls)

	@property
	def _self(self) -> LinkType:
		"""Gets the _self of this CaReconfSubscriptionLinks.


		:return: The _self of this CaReconfSubscriptionLinks.
		:rtype: LinkType
		"""
		return self.__self

	@_self.setter
	def _self(self, _self: LinkType):
		"""Sets the _self of this CaReconfSubscriptionLinks.


		:param _self: The _self of this CaReconfSubscriptionLinks.
		:type _self: LinkType
		"""
		if _self is None:
			raise ValueError("Invalid value for `_self`, must not be `None`")  # noqa: E501

		self.__self = _self
