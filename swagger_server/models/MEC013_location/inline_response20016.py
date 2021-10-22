# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401 # pylint: disable=unused-import

from typing import List, Dict  # noqa: F401 # pylint: disable=unused-import

from swagger_server.models.base_model_ import Model
from swagger_server.models.MEC013_location.zonal_traffic_subscription import \
	ZonalTrafficSubscription  # noqa: F401 # pylint: disable=unused-import,E501
from swagger_server import util


class InlineResponse20016(Model):
	"""NOTE: This class is auto generated by the swagger code generator program.

	Do not edit the class manually.
	"""

	def __init__(self, zonal_traffic_subscription: ZonalTrafficSubscription = None):  # noqa: E501
		"""InlineResponse20016 - a model defined in Swagger

		:param zonal_traffic_subscription: The zonal_traffic_subscription of this InlineResponse20016.  # noqa: E501
		:type zonal_traffic_subscription: ZonalTrafficSubscription
		"""
		self.swagger_types = {
			'zonal_traffic_subscription': ZonalTrafficSubscription
		}

		self.attribute_map = {
			'zonal_traffic_subscription': 'zonalTrafficSubscription'
		}
		self._zonal_traffic_subscription = zonal_traffic_subscription

	@classmethod
	def from_dict(cls, dikt) -> 'InlineResponse20016':
		"""Returns the dict as a model

		:param dikt: A dict.
		:type: dict
		:return: The inline_response_200_16 of this InlineResponse20016.  # noqa: E501
		:rtype: InlineResponse20016
		"""
		return util.deserialize_model(dikt, cls)

	@property
	def zonal_traffic_subscription(self) -> ZonalTrafficSubscription:
		"""Gets the zonal_traffic_subscription of this InlineResponse20016.


		:return: The zonal_traffic_subscription of this InlineResponse20016.
		:rtype: ZonalTrafficSubscription
		"""
		return self._zonal_traffic_subscription

	@zonal_traffic_subscription.setter
	def zonal_traffic_subscription(self, zonal_traffic_subscription: ZonalTrafficSubscription):
		"""Sets the zonal_traffic_subscription of this InlineResponse20016.


		:param zonal_traffic_subscription: The zonal_traffic_subscription of this InlineResponse20016.
		:type zonal_traffic_subscription: ZonalTrafficSubscription
		"""
		if zonal_traffic_subscription is None:
			raise ValueError("Invalid value for `zonal_traffic_subscription`, must not be `None`")  # noqa: E501

		self._zonal_traffic_subscription = zonal_traffic_subscription
