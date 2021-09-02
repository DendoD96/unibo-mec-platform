# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.MEC011_application_support.destination_interface import \
	DestinationInterface  # noqa: F401,E501
from swagger_server.models.MEC011_application_support.traffic_filter import TrafficFilter  # noqa: F401,E501
from swagger_server.models.MEC011_application_support.traffic_rule_action import TrafficRuleAction  # noqa: F401,E501
from swagger_server.models.MEC011_application_support.traffic_rule_filter_type import \
	TrafficRuleFilterType  # noqa: F401,E501
from swagger_server.models.MEC011_application_support.traffic_rule_id import TrafficRuleId  # noqa: F401,E501
from swagger_server.models.MEC011_application_support.traffic_rule_priority import \
	TrafficRulePriority  # noqa: F401,E501
from swagger_server.models.MEC011_application_support.traffic_rule_state import TrafficRuleState  # noqa: F401,E501
from swagger_server import util


class TrafficRule(Model):
	"""NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

	def __init__(self, traffic_rule_id: TrafficRuleId = None, filter_type: TrafficRuleFilterType = None,
	             priority: TrafficRulePriority = None, traffic_filter: List[TrafficFilter] = None,
	             action: TrafficRuleAction = None, dst_interface: DestinationInterface = None,
	             state: TrafficRuleState = None):  # noqa: E501
		"""TrafficRule - a model defined in Swagger

        :param traffic_rule_id: The traffic_rule_id of this TrafficRule.  # noqa: E501
        :type traffic_rule_id: TrafficRuleId
        :param filter_type: The filter_type of this TrafficRule.  # noqa: E501
        :type filter_type: TrafficRuleFilterType
        :param priority: The priority of this TrafficRule.  # noqa: E501
        :type priority: TrafficRulePriority
        :param traffic_filter: The traffic_filter of this TrafficRule.  # noqa: E501
        :type traffic_filter: List[TrafficFilter]
        :param action: The action of this TrafficRule.  # noqa: E501
        :type action: TrafficRuleAction
        :param dst_interface: The dst_interface of this TrafficRule.  # noqa: E501
        :type dst_interface: DestinationInterface
        :param state: The state of this TrafficRule.  # noqa: E501
        :type state: TrafficRuleState
        """
		self.swagger_types = {
			'traffic_rule_id': TrafficRuleId,
			'filter_type': TrafficRuleFilterType,
			'priority': TrafficRulePriority,
			'traffic_filter': List[TrafficFilter],
			'action': TrafficRuleAction,
			'dst_interface': DestinationInterface,
			'state': TrafficRuleState
		}

		self.attribute_map = {
			'traffic_rule_id': 'trafficRuleId',
			'filter_type': 'filterType',
			'priority': 'priority',
			'traffic_filter': 'trafficFilter',
			'action': 'action',
			'dst_interface': 'dstInterface',
			'state': 'state'
		}
		self._traffic_rule_id = traffic_rule_id
		self._filter_type = filter_type
		self._priority = priority
		self._traffic_filter = traffic_filter
		self._action = action
		self._dst_interface = dst_interface
		self._state = state

	@classmethod
	def from_dict(cls, dikt) -> 'TrafficRule':
		"""Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The TrafficRule of this TrafficRule.  # noqa: E501
        :rtype: TrafficRule
        """
		return util.deserialize_model(dikt, cls)

	@property
	def traffic_rule_id(self) -> TrafficRuleId:
		"""Gets the traffic_rule_id of this TrafficRule.


        :return: The traffic_rule_id of this TrafficRule.
        :rtype: TrafficRuleId
        """
		return self._traffic_rule_id

	@traffic_rule_id.setter
	def traffic_rule_id(self, traffic_rule_id: TrafficRuleId):
		"""Sets the traffic_rule_id of this TrafficRule.


        :param traffic_rule_id: The traffic_rule_id of this TrafficRule.
        :type traffic_rule_id: TrafficRuleId
        """
		if traffic_rule_id is None:
			raise ValueError("Invalid value for `traffic_rule_id`, must not be `None`")  # noqa: E501

		self._traffic_rule_id = traffic_rule_id

	@property
	def filter_type(self) -> TrafficRuleFilterType:
		"""Gets the filter_type of this TrafficRule.


        :return: The filter_type of this TrafficRule.
        :rtype: TrafficRuleFilterType
        """
		return self._filter_type

	@filter_type.setter
	def filter_type(self, filter_type: TrafficRuleFilterType):
		"""Sets the filter_type of this TrafficRule.


        :param filter_type: The filter_type of this TrafficRule.
        :type filter_type: TrafficRuleFilterType
        """
		if filter_type is None:
			raise ValueError("Invalid value for `filter_type`, must not be `None`")  # noqa: E501

		self._filter_type = filter_type

	@property
	def priority(self) -> TrafficRulePriority:
		"""Gets the priority of this TrafficRule.


        :return: The priority of this TrafficRule.
        :rtype: TrafficRulePriority
        """
		return self._priority

	@priority.setter
	def priority(self, priority: TrafficRulePriority):
		"""Sets the priority of this TrafficRule.


        :param priority: The priority of this TrafficRule.
        :type priority: TrafficRulePriority
        """
		if priority is None:
			raise ValueError("Invalid value for `priority`, must not be `None`")  # noqa: E501

		self._priority = priority

	@property
	def traffic_filter(self) -> List[TrafficFilter]:
		"""Gets the traffic_filter of this TrafficRule.


        :return: The traffic_filter of this TrafficRule.
        :rtype: List[TrafficFilter]
        """
		return self._traffic_filter

	@traffic_filter.setter
	def traffic_filter(self, traffic_filter: List[TrafficFilter]):
		"""Sets the traffic_filter of this TrafficRule.


        :param traffic_filter: The traffic_filter of this TrafficRule.
        :type traffic_filter: List[TrafficFilter]
        """
		if traffic_filter is None:
			raise ValueError("Invalid value for `traffic_filter`, must not be `None`")  # noqa: E501

		self._traffic_filter = traffic_filter

	@property
	def action(self) -> TrafficRuleAction:
		"""Gets the action of this TrafficRule.


        :return: The action of this TrafficRule.
        :rtype: TrafficRuleAction
        """
		return self._action

	@action.setter
	def action(self, action: TrafficRuleAction):
		"""Sets the action of this TrafficRule.


        :param action: The action of this TrafficRule.
        :type action: TrafficRuleAction
        """
		if action is None:
			raise ValueError("Invalid value for `action`, must not be `None`")  # noqa: E501

		self._action = action

	@property
	def dst_interface(self) -> DestinationInterface:
		"""Gets the dst_interface of this TrafficRule.


        :return: The dst_interface of this TrafficRule.
        :rtype: DestinationInterface
        """
		return self._dst_interface

	@dst_interface.setter
	def dst_interface(self, dst_interface: DestinationInterface):
		"""Sets the dst_interface of this TrafficRule.


        :param dst_interface: The dst_interface of this TrafficRule.
        :type dst_interface: DestinationInterface
        """

		self._dst_interface = dst_interface

	@property
	def state(self) -> TrafficRuleState:
		"""Gets the state of this TrafficRule.


        :return: The state of this TrafficRule.
        :rtype: TrafficRuleState
        """
		return self._state

	@state.setter
	def state(self, state: TrafficRuleState):
		"""Sets the state of this TrafficRule.


        :param state: The state of this TrafficRule.
        :type state: TrafficRuleState
        """
		if state is None:
			raise ValueError("Invalid value for `state`, must not be `None`")  # noqa: E501

		self._state = state