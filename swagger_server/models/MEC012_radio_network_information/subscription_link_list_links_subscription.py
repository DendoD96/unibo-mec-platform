# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401 # pylint: disable=unused-import

from typing import List, Dict  # noqa: F401 # pylint: disable=unused-import

from swagger_server.models.base_model_ import Model
from swagger_server import util


class SubscriptionLinkListLinksSubscription(Model):
	"""NOTE: This class is auto generated by the swagger code generator program.

	Do not edit the class manually.
	"""

	def __init__(self, href: str = None, subscription_type: str = None):  # noqa: E501
		"""SubscriptionLinkListLinksSubscription - a model defined in Swagger

		:param href: The href of this SubscriptionLinkListLinksSubscription.  # noqa: E501
		:type href: str
		:param subscription_type: The subscription_type of this SubscriptionLinkListLinksSubscription.  # noqa: E501
		:type subscription_type: str
		"""
		self.swagger_types = {
			'href': str,
			'subscription_type': str
		}

		self.attribute_map = {
			'href': 'href',
			'subscription_type': 'subscriptionType'
		}
		self._href = href
		self._subscription_type = subscription_type

	@classmethod
	def from_dict(cls, dikt) -> 'SubscriptionLinkListLinksSubscription':
		"""Returns the dict as a model

		:param dikt: A dict.
		:type: dict
		:return: The SubscriptionLinkList__links_subscription of this SubscriptionLinkListLinksSubscription.  # noqa: E501
		:rtype: SubscriptionLinkListLinksSubscription
		"""
		return util.deserialize_model(dikt, cls)

	@property
	def href(self) -> str:
		"""Gets the href of this SubscriptionLinkListLinksSubscription.

		The URI referring to the subscription.  # noqa: E501

		:return: The href of this SubscriptionLinkListLinksSubscription.
		:rtype: str
		"""
		return self._href

	@href.setter
	def href(self, href: str):
		"""Sets the href of this SubscriptionLinkListLinksSubscription.

		The URI referring to the subscription.  # noqa: E501

		:param href: The href of this SubscriptionLinkListLinksSubscription.
		:type href: str
		"""

		self._href = href

	@property
	def subscription_type(self) -> str:
		"""Gets the subscription_type of this SubscriptionLinkListLinksSubscription.

		Type of the subscription. The string shall be set according to the \"subscriptionType\" attribute of the associated subscription data type event defined in clause 6.3.  # noqa: E501

		:return: The subscription_type of this SubscriptionLinkListLinksSubscription.
		:rtype: str
		"""
		return self._subscription_type

	@subscription_type.setter
	def subscription_type(self, subscription_type: str):
		"""Sets the subscription_type of this SubscriptionLinkListLinksSubscription.

		Type of the subscription. The string shall be set according to the \"subscriptionType\" attribute of the associated subscription data type event defined in clause 6.3.  # noqa: E501

		:param subscription_type: The subscription_type of this SubscriptionLinkListLinksSubscription.
		:type subscription_type: str
		"""

		self._subscription_type = subscription_type
