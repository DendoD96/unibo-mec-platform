# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401 # pylint: disable=unused-import

from typing import List, Dict  # noqa: F401 # pylint: disable=unused-import

from swagger_server.models.base_model_ import Model
from swagger_server.models.MEC012_radio_network_information.ca_reconf_subscription_filter_criteria_assoc import \
	CaReconfSubscriptionFilterCriteriaAssoc  # noqa: F401 # pylint: disable=unused-import,E501
from swagger_server.models.MEC012_radio_network_information.ca_reconf_subscription_links import \
	CaReconfSubscriptionLinks  # noqa: F401 # pylint: disable=unused-import,E501
from swagger_server.models.MEC012_radio_network_information.time_stamp import \
	TimeStamp  # noqa: F401 # pylint: disable=unused-import,E501
from swagger_server import util


class MeasTaSubscription(Model):
	"""NOTE: This class is auto generated by the swagger code generator program.

	Do not edit the class manually.
	"""

	def __init__(self, links: CaReconfSubscriptionLinks = None, callback_reference: str = None,
	             expiry_deadline: TimeStamp = None,
	             filter_criteria_assoc: CaReconfSubscriptionFilterCriteriaAssoc = None,
	             subscription_type: str = None):  # noqa: E501
		"""MeasTaSubscription - a model defined in Swagger

		:param links: The links of this MeasTaSubscription.  # noqa: E501
		:type links: CaReconfSubscriptionLinks
		:param callback_reference: The callback_reference of this MeasTaSubscription.  # noqa: E501
		:type callback_reference: str
		:param expiry_deadline: The expiry_deadline of this MeasTaSubscription.  # noqa: E501
		:type expiry_deadline: TimeStamp
		:param filter_criteria_assoc: The filter_criteria_assoc of this MeasTaSubscription.  # noqa: E501
		:type filter_criteria_assoc: CaReconfSubscriptionFilterCriteriaAssoc
		:param subscription_type: The subscription_type of this MeasTaSubscription.  # noqa: E501
		:type subscription_type: str
		"""
		self.swagger_types = {
			'links': CaReconfSubscriptionLinks,
			'callback_reference': str,
			'expiry_deadline': TimeStamp,
			'filter_criteria_assoc': CaReconfSubscriptionFilterCriteriaAssoc,
			'subscription_type': str
		}

		self.attribute_map = {
			'links': '_links',
			'callback_reference': 'callbackReference',
			'expiry_deadline': 'expiryDeadline',
			'filter_criteria_assoc': 'filterCriteriaAssoc',
			'subscription_type': 'subscriptionType'
		}
		self._links = links
		self._callback_reference = callback_reference
		self._expiry_deadline = expiry_deadline
		self._filter_criteria_assoc = filter_criteria_assoc
		self._subscription_type = subscription_type

	@classmethod
	def from_dict(cls, dikt) -> 'MeasTaSubscription':
		"""Returns the dict as a model

		:param dikt: A dict.
		:type: dict
		:return: The MeasTaSubscription of this MeasTaSubscription.  # noqa: E501
		:rtype: MeasTaSubscription
		"""
		return util.deserialize_model(dikt, cls)

	@property
	def links(self) -> CaReconfSubscriptionLinks:
		"""Gets the links of this MeasTaSubscription.


		:return: The links of this MeasTaSubscription.
		:rtype: CaReconfSubscriptionLinks
		"""
		return self._links

	@links.setter
	def links(self, links: CaReconfSubscriptionLinks):
		"""Sets the links of this MeasTaSubscription.


		:param links: The links of this MeasTaSubscription.
		:type links: CaReconfSubscriptionLinks
		"""

		self._links = links

	@property
	def callback_reference(self) -> str:
		"""Gets the callback_reference of this MeasTaSubscription.

		URI selected by the service consumer to receive notifications on the subscribed RNIS information. This shall be included both in the request and in response.  # noqa: E501

		:return: The callback_reference of this MeasTaSubscription.
		:rtype: str
		"""
		return self._callback_reference

	@callback_reference.setter
	def callback_reference(self, callback_reference: str):
		"""Sets the callback_reference of this MeasTaSubscription.

		URI selected by the service consumer to receive notifications on the subscribed RNIS information. This shall be included both in the request and in response.  # noqa: E501

		:param callback_reference: The callback_reference of this MeasTaSubscription.
		:type callback_reference: str
		"""
		if callback_reference is None:
			raise ValueError("Invalid value for `callback_reference`, must not be `None`")  # noqa: E501

		self._callback_reference = callback_reference

	@property
	def expiry_deadline(self) -> TimeStamp:
		"""Gets the expiry_deadline of this MeasTaSubscription.


		:return: The expiry_deadline of this MeasTaSubscription.
		:rtype: TimeStamp
		"""
		return self._expiry_deadline

	@expiry_deadline.setter
	def expiry_deadline(self, expiry_deadline: TimeStamp):
		"""Sets the expiry_deadline of this MeasTaSubscription.


		:param expiry_deadline: The expiry_deadline of this MeasTaSubscription.
		:type expiry_deadline: TimeStamp
		"""

		self._expiry_deadline = expiry_deadline

	@property
	def filter_criteria_assoc(self) -> CaReconfSubscriptionFilterCriteriaAssoc:
		"""Gets the filter_criteria_assoc of this MeasTaSubscription.


		:return: The filter_criteria_assoc of this MeasTaSubscription.
		:rtype: CaReconfSubscriptionFilterCriteriaAssoc
		"""
		return self._filter_criteria_assoc

	@filter_criteria_assoc.setter
	def filter_criteria_assoc(self, filter_criteria_assoc: CaReconfSubscriptionFilterCriteriaAssoc):
		"""Sets the filter_criteria_assoc of this MeasTaSubscription.


		:param filter_criteria_assoc: The filter_criteria_assoc of this MeasTaSubscription.
		:type filter_criteria_assoc: CaReconfSubscriptionFilterCriteriaAssoc
		"""
		if filter_criteria_assoc is None:
			raise ValueError("Invalid value for `filter_criteria_assoc`, must not be `None`")  # noqa: E501

		self._filter_criteria_assoc = filter_criteria_assoc

	@property
	def subscription_type(self) -> str:
		"""Gets the subscription_type of this MeasTaSubscription.

		Shall be set to \"MeasTaSubscription\".  # noqa: E501

		:return: The subscription_type of this MeasTaSubscription.
		:rtype: str
		"""
		return self._subscription_type

	@subscription_type.setter
	def subscription_type(self, subscription_type: str):
		"""Sets the subscription_type of this MeasTaSubscription.

		Shall be set to \"MeasTaSubscription\".  # noqa: E501

		:param subscription_type: The subscription_type of this MeasTaSubscription.
		:type subscription_type: str
		"""
		if subscription_type is None:
			raise ValueError("Invalid value for `subscription_type`, must not be `None`")  # noqa: E501

		self._subscription_type = subscription_type
