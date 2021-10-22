# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401 # pylint: disable=unused-import

from typing import List, Dict  # noqa: F401 # pylint: disable=unused-import

from swagger_server.models.base_model_ import Model
from swagger_server.models.MEC013_location.user_tracking_subscription import \
	UserTrackingSubscription  # noqa: F401 # pylint: disable=unused-import,E501
from swagger_server import util


class InlineResponse20013(Model):
	"""NOTE: This class is auto generated by the swagger code generator program.

	Do not edit the class manually.
	"""

	def __init__(self, user_tracking_subscription: UserTrackingSubscription = None):  # noqa: E501
		"""InlineResponse20013 - a model defined in Swagger

		:param user_tracking_subscription: The user_tracking_subscription of this InlineResponse20013.  # noqa: E501
		:type user_tracking_subscription: UserTrackingSubscription
		"""
		self.swagger_types = {
			'user_tracking_subscription': UserTrackingSubscription
		}

		self.attribute_map = {
			'user_tracking_subscription': 'userTrackingSubscription'
		}
		self._user_tracking_subscription = user_tracking_subscription

	@classmethod
	def from_dict(cls, dikt) -> 'InlineResponse20013':
		"""Returns the dict as a model

		:param dikt: A dict.
		:type: dict
		:return: The inline_response_200_13 of this InlineResponse20013.  # noqa: E501
		:rtype: InlineResponse20013
		"""
		return util.deserialize_model(dikt, cls)

	@property
	def user_tracking_subscription(self) -> UserTrackingSubscription:
		"""Gets the user_tracking_subscription of this InlineResponse20013.


		:return: The user_tracking_subscription of this InlineResponse20013.
		:rtype: UserTrackingSubscription
		"""
		return self._user_tracking_subscription

	@user_tracking_subscription.setter
	def user_tracking_subscription(self, user_tracking_subscription: UserTrackingSubscription):
		"""Sets the user_tracking_subscription of this InlineResponse20013.


		:param user_tracking_subscription: The user_tracking_subscription of this InlineResponse20013.
		:type user_tracking_subscription: UserTrackingSubscription
		"""
		if user_tracking_subscription is None:
			raise ValueError("Invalid value for `user_tracking_subscription`, must not be `None`")  # noqa: E501

		self._user_tracking_subscription = user_tracking_subscription
