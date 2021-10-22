# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401 # pylint: disable=unused-import

from typing import List, Dict  # noqa: F401 # pylint: disable=unused-import

from swagger_server.models.base_model_ import Model
from swagger_server import util


class InlineSubscription(Model):
	"""NOTE: This class is auto generated by the swagger code generator program.

	Do not edit the class manually.
	"""

	def __init__(self):  # noqa: E501
		"""InlineSubscription - a model defined in Swagger

		"""
		self.swagger_types = {
		}

		self.attribute_map = {
		}

	@classmethod
	def from_dict(cls, dikt) -> 'InlineSubscription':
		"""Returns the dict as a model

		:param dikt: A dict.
		:type: dict
		:return: The InlineSubscription of this InlineSubscription.  # noqa: E501
		:rtype: InlineSubscription
		"""
		return util.deserialize_model(dikt, cls)
