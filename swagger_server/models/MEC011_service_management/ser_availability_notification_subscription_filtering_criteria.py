# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.MEC011_service_management.category_refs import CategoryRefs  # noqa: F401,E501
from swagger_server.models.MEC011_service_management.ser_instance_ids import SerInstanceIds  # noqa: F401,E501
from swagger_server.models.MEC011_service_management.ser_names import SerNames  # noqa: F401,E501
from swagger_server.models.MEC011_service_management.service_info_is_local import ServiceInfoIsLocal  # noqa: F401,E501
from swagger_server.models.MEC011_service_management.service_states import ServiceStates  # noqa: F401,E501
from swagger_server import util


class SerAvailabilityNotificationSubscriptionFilteringCriteria(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, ser_instance_ids: SerInstanceIds=None, ser_names: SerNames=None, ser_categories: CategoryRefs=None, states: ServiceStates=None, is_local: ServiceInfoIsLocal=None):  # noqa: E501
        """SerAvailabilityNotificationSubscriptionFilteringCriteria - a model defined in Swagger

        :param ser_instance_ids: The ser_instance_ids of this SerAvailabilityNotificationSubscriptionFilteringCriteria.  # noqa: E501
        :type ser_instance_ids: SerInstanceIds
        :param ser_names: The ser_names of this SerAvailabilityNotificationSubscriptionFilteringCriteria.  # noqa: E501
        :type ser_names: SerNames
        :param ser_categories: The ser_categories of this SerAvailabilityNotificationSubscriptionFilteringCriteria.  # noqa: E501
        :type ser_categories: CategoryRefs
        :param states: The states of this SerAvailabilityNotificationSubscriptionFilteringCriteria.  # noqa: E501
        :type states: ServiceStates
        :param is_local: The is_local of this SerAvailabilityNotificationSubscriptionFilteringCriteria.  # noqa: E501
        :type is_local: ServiceInfoIsLocal
        """
        self.swagger_types = {
            'ser_instance_ids': SerInstanceIds,
            'ser_names': SerNames,
            'ser_categories': CategoryRefs,
            'states': ServiceStates,
            'is_local': ServiceInfoIsLocal
        }

        self.attribute_map = {
            'ser_instance_ids': 'serInstanceIds',
            'ser_names': 'serNames',
            'ser_categories': 'serCategories',
            'states': 'states',
            'is_local': 'isLocal'
        }
        self._ser_instance_ids = ser_instance_ids
        self._ser_names = ser_names
        self._ser_categories = ser_categories
        self._states = states
        self._is_local = is_local

    @classmethod
    def from_dict(cls, dikt) -> 'SerAvailabilityNotificationSubscriptionFilteringCriteria':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SerAvailabilityNotificationSubscription.FilteringCriteria of this SerAvailabilityNotificationSubscriptionFilteringCriteria.  # noqa: E501
        :rtype: SerAvailabilityNotificationSubscriptionFilteringCriteria
        """
        return util.deserialize_model(dikt, cls)

    @property
    def ser_instance_ids(self) -> SerInstanceIds:
        """Gets the ser_instance_ids of this SerAvailabilityNotificationSubscriptionFilteringCriteria.


        :return: The ser_instance_ids of this SerAvailabilityNotificationSubscriptionFilteringCriteria.
        :rtype: SerInstanceIds
        """
        return self._ser_instance_ids

    @ser_instance_ids.setter
    def ser_instance_ids(self, ser_instance_ids: SerInstanceIds):
        """Sets the ser_instance_ids of this SerAvailabilityNotificationSubscriptionFilteringCriteria.


        :param ser_instance_ids: The ser_instance_ids of this SerAvailabilityNotificationSubscriptionFilteringCriteria.
        :type ser_instance_ids: SerInstanceIds
        """

        self._ser_instance_ids = ser_instance_ids

    @property
    def ser_names(self) -> SerNames:
        """Gets the ser_names of this SerAvailabilityNotificationSubscriptionFilteringCriteria.


        :return: The ser_names of this SerAvailabilityNotificationSubscriptionFilteringCriteria.
        :rtype: SerNames
        """
        return self._ser_names

    @ser_names.setter
    def ser_names(self, ser_names: SerNames):
        """Sets the ser_names of this SerAvailabilityNotificationSubscriptionFilteringCriteria.


        :param ser_names: The ser_names of this SerAvailabilityNotificationSubscriptionFilteringCriteria.
        :type ser_names: SerNames
        """

        self._ser_names = ser_names

    @property
    def ser_categories(self) -> CategoryRefs:
        """Gets the ser_categories of this SerAvailabilityNotificationSubscriptionFilteringCriteria.


        :return: The ser_categories of this SerAvailabilityNotificationSubscriptionFilteringCriteria.
        :rtype: CategoryRefs
        """
        return self._ser_categories

    @ser_categories.setter
    def ser_categories(self, ser_categories: CategoryRefs):
        """Sets the ser_categories of this SerAvailabilityNotificationSubscriptionFilteringCriteria.


        :param ser_categories: The ser_categories of this SerAvailabilityNotificationSubscriptionFilteringCriteria.
        :type ser_categories: CategoryRefs
        """

        self._ser_categories = ser_categories

    @property
    def states(self) -> ServiceStates:
        """Gets the states of this SerAvailabilityNotificationSubscriptionFilteringCriteria.


        :return: The states of this SerAvailabilityNotificationSubscriptionFilteringCriteria.
        :rtype: ServiceStates
        """
        return self._states

    @states.setter
    def states(self, states: ServiceStates):
        """Sets the states of this SerAvailabilityNotificationSubscriptionFilteringCriteria.


        :param states: The states of this SerAvailabilityNotificationSubscriptionFilteringCriteria.
        :type states: ServiceStates
        """

        self._states = states

    @property
    def is_local(self) -> ServiceInfoIsLocal:
        """Gets the is_local of this SerAvailabilityNotificationSubscriptionFilteringCriteria.


        :return: The is_local of this SerAvailabilityNotificationSubscriptionFilteringCriteria.
        :rtype: ServiceInfoIsLocal
        """
        return self._is_local

    @is_local.setter
    def is_local(self, is_local: ServiceInfoIsLocal):
        """Sets the is_local of this SerAvailabilityNotificationSubscriptionFilteringCriteria.


        :param is_local: The is_local of this SerAvailabilityNotificationSubscriptionFilteringCriteria.
        :type is_local: ServiceInfoIsLocal
        """

        self._is_local = is_local
