# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401 # pylint: disable=unused-import

from typing import List, Dict  # noqa: F401 # pylint: disable=unused-import

from swagger_server.models.base_model_ import Model
from swagger_server.models.MEC013_location.circle_notification_subscription import \
	CircleNotificationSubscription  # noqa: F401 # pylint: disable=unused-import,E501
from swagger_server import util


class InlineResponse2007(Model):
	"""NOTE: This class is auto generated by the swagger code generator program.

	Do not edit the class manually.
	"""

	def __init__(self, circle_notification_subscription: CircleNotificationSubscription = None):  # noqa: E501
		"""InlineResponse2007 - a model defined in Swagger

		:param circle_notification_subscription: The circle_notification_subscription of this InlineResponse2007.  # noqa: E501
		:type circle_notification_subscription: CircleNotificationSubscription
		"""
		self.swagger_types = {
			'circle_notification_subscription': CircleNotificationSubscription
		}

		self.attribute_map = {
			'circle_notification_subscription': 'circleNotificationSubscription'
		}
		self._circle_notification_subscription = circle_notification_subscription

	@classmethod
	def from_dict(cls, dikt) -> 'InlineResponse2007':
		"""Returns the dict as a model

		:param dikt: A dict.
		:type: dict
		:return: The inline_response_200_7 of this InlineResponse2007.  # noqa: E501
		:rtype: InlineResponse2007
		"""
		return util.deserialize_model(dikt, cls)

	@property
	def circle_notification_subscription(self) -> CircleNotificationSubscription:
		"""Gets the circle_notification_subscription of this InlineResponse2007.


		:return: The circle_notification_subscription of this InlineResponse2007.
		:rtype: CircleNotificationSubscription
		"""
		return self._circle_notification_subscription

	@circle_notification_subscription.setter
	def circle_notification_subscription(self, circle_notification_subscription: CircleNotificationSubscription):
		"""Sets the circle_notification_subscription of this InlineResponse2007.


		:param circle_notification_subscription: The circle_notification_subscription of this InlineResponse2007.
		:type circle_notification_subscription: CircleNotificationSubscription
		"""
		if circle_notification_subscription is None:
			raise ValueError("Invalid value for `circle_notification_subscription`, must not be `None`")  # noqa: E501

		self._circle_notification_subscription = circle_notification_subscription
