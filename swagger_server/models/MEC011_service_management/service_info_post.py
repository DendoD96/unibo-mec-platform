# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.MEC011_service_management.category_ref import CategoryRef  # noqa: F401,E501
from swagger_server.models.MEC011_service_management.locality_type import LocalityType  # noqa: F401,E501
from swagger_server.models.MEC011_service_management.serializer_type import SerializerType  # noqa: F401,E501
from swagger_server.models.MEC011_service_management.service_info_consumed_local_only import ServiceInfoConsumedLocalOnly  # noqa: F401,E501
from swagger_server.models.MEC011_service_management.service_info_is_local import ServiceInfoIsLocal  # noqa: F401,E501
from swagger_server.models.MEC011_service_management.service_info_ser_instance_id import ServiceInfoSerInstanceId  # noqa: F401,E501
from swagger_server.models.MEC011_service_management.service_info_ser_name import ServiceInfoSerName  # noqa: F401,E501
from swagger_server.models.MEC011_service_management.service_info_transport_id import ServiceInfoTransportId  # noqa: F401,E501
from swagger_server.models.MEC011_service_management.service_info_version import ServiceInfoVersion  # noqa: F401,E501
from swagger_server.models.MEC011_service_management.service_state import ServiceState  # noqa: F401,E501
from swagger_server.models.MEC011_service_management.transport_info import TransportInfo  # noqa: F401,E501
from swagger_server import util


class ServiceInfoPost(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, ser_instance_id: ServiceInfoSerInstanceId=None, ser_name: ServiceInfoSerName=None, ser_category: CategoryRef=None, version: ServiceInfoVersion=None, state: ServiceState=None, transport_id: ServiceInfoTransportId=None, transport_info: TransportInfo=None, serializer: SerializerType=None, scope_of_locality: LocalityType=None, consumed_local_only: ServiceInfoConsumedLocalOnly=None, is_local: ServiceInfoIsLocal=None):  # noqa: E501
        """ServiceInfoPost - a model defined in Swagger

        :param ser_instance_id: The ser_instance_id of this ServiceInfoPost.  # noqa: E501
        :type ser_instance_id: ServiceInfoSerInstanceId
        :param ser_name: The ser_name of this ServiceInfoPost.  # noqa: E501
        :type ser_name: ServiceInfoSerName
        :param ser_category: The ser_category of this ServiceInfoPost.  # noqa: E501
        :type ser_category: CategoryRef
        :param version: The version of this ServiceInfoPost.  # noqa: E501
        :type version: ServiceInfoVersion
        :param state: The state of this ServiceInfoPost.  # noqa: E501
        :type state: ServiceState
        :param transport_id: The transport_id of this ServiceInfoPost.  # noqa: E501
        :type transport_id: ServiceInfoTransportId
        :param transport_info: The transport_info of this ServiceInfoPost.  # noqa: E501
        :type transport_info: TransportInfo
        :param serializer: The serializer of this ServiceInfoPost.  # noqa: E501
        :type serializer: SerializerType
        :param scope_of_locality: The scope_of_locality of this ServiceInfoPost.  # noqa: E501
        :type scope_of_locality: LocalityType
        :param consumed_local_only: The consumed_local_only of this ServiceInfoPost.  # noqa: E501
        :type consumed_local_only: ServiceInfoConsumedLocalOnly
        :param is_local: The is_local of this ServiceInfoPost.  # noqa: E501
        :type is_local: ServiceInfoIsLocal
        """
        self.swagger_types = {
            'ser_instance_id': ServiceInfoSerInstanceId,
            'ser_name': ServiceInfoSerName,
            'ser_category': CategoryRef,
            'version': ServiceInfoVersion,
            'state': ServiceState,
            'transport_id': ServiceInfoTransportId,
            'transport_info': TransportInfo,
            'serializer': SerializerType,
            'scope_of_locality': LocalityType,
            'consumed_local_only': ServiceInfoConsumedLocalOnly,
            'is_local': ServiceInfoIsLocal
        }

        self.attribute_map = {
            'ser_instance_id': 'serInstanceId',
            'ser_name': 'serName',
            'ser_category': 'serCategory',
            'version': 'version',
            'state': 'state',
            'transport_id': 'transportId',
            'transport_info': 'transportInfo',
            'serializer': 'serializer',
            'scope_of_locality': 'scopeOfLocality',
            'consumed_local_only': 'consumedLocalOnly',
            'is_local': 'isLocal'
        }
        self._ser_instance_id = ser_instance_id
        self._ser_name = ser_name
        self._ser_category = ser_category
        self._version = version
        self._state = state
        self._transport_id = transport_id
        self._transport_info = transport_info
        self._serializer = serializer
        self._scope_of_locality = scope_of_locality
        self._consumed_local_only = consumed_local_only
        self._is_local = is_local

    @classmethod
    def from_dict(cls, dikt) -> 'ServiceInfoPost':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ServiceInfo.Post of this ServiceInfoPost.  # noqa: E501
        :rtype: ServiceInfoPost
        """
        return util.deserialize_model(dikt, cls)

    @property
    def ser_instance_id(self) -> ServiceInfoSerInstanceId:
        """Gets the ser_instance_id of this ServiceInfoPost.


        :return: The ser_instance_id of this ServiceInfoPost.
        :rtype: ServiceInfoSerInstanceId
        """
        return self._ser_instance_id

    @ser_instance_id.setter
    def ser_instance_id(self, ser_instance_id: ServiceInfoSerInstanceId):
        """Sets the ser_instance_id of this ServiceInfoPost.


        :param ser_instance_id: The ser_instance_id of this ServiceInfoPost.
        :type ser_instance_id: ServiceInfoSerInstanceId
        """

        self._ser_instance_id = ser_instance_id

    @property
    def ser_name(self) -> ServiceInfoSerName:
        """Gets the ser_name of this ServiceInfoPost.


        :return: The ser_name of this ServiceInfoPost.
        :rtype: ServiceInfoSerName
        """
        return self._ser_name

    @ser_name.setter
    def ser_name(self, ser_name: ServiceInfoSerName):
        """Sets the ser_name of this ServiceInfoPost.


        :param ser_name: The ser_name of this ServiceInfoPost.
        :type ser_name: ServiceInfoSerName
        """
        if ser_name is None:
            raise ValueError("Invalid value for `ser_name`, must not be `None`")  # noqa: E501

        self._ser_name = ser_name

    @property
    def ser_category(self) -> CategoryRef:
        """Gets the ser_category of this ServiceInfoPost.


        :return: The ser_category of this ServiceInfoPost.
        :rtype: CategoryRef
        """
        return self._ser_category

    @ser_category.setter
    def ser_category(self, ser_category: CategoryRef):
        """Sets the ser_category of this ServiceInfoPost.


        :param ser_category: The ser_category of this ServiceInfoPost.
        :type ser_category: CategoryRef
        """

        self._ser_category = ser_category

    @property
    def version(self) -> ServiceInfoVersion:
        """Gets the version of this ServiceInfoPost.


        :return: The version of this ServiceInfoPost.
        :rtype: ServiceInfoVersion
        """
        return self._version

    @version.setter
    def version(self, version: ServiceInfoVersion):
        """Sets the version of this ServiceInfoPost.


        :param version: The version of this ServiceInfoPost.
        :type version: ServiceInfoVersion
        """
        if version is None:
            raise ValueError("Invalid value for `version`, must not be `None`")  # noqa: E501

        self._version = version

    @property
    def state(self) -> ServiceState:
        """Gets the state of this ServiceInfoPost.


        :return: The state of this ServiceInfoPost.
        :rtype: ServiceState
        """
        return self._state

    @state.setter
    def state(self, state: ServiceState):
        """Sets the state of this ServiceInfoPost.


        :param state: The state of this ServiceInfoPost.
        :type state: ServiceState
        """
        if state is None:
            raise ValueError("Invalid value for `state`, must not be `None`")  # noqa: E501

        self._state = state

    @property
    def transport_id(self) -> ServiceInfoTransportId:
        """Gets the transport_id of this ServiceInfoPost.


        :return: The transport_id of this ServiceInfoPost.
        :rtype: ServiceInfoTransportId
        """
        return self._transport_id

    @transport_id.setter
    def transport_id(self, transport_id: ServiceInfoTransportId):
        """Sets the transport_id of this ServiceInfoPost.


        :param transport_id: The transport_id of this ServiceInfoPost.
        :type transport_id: ServiceInfoTransportId
        """

        self._transport_id = transport_id

    @property
    def transport_info(self) -> TransportInfo:
        """Gets the transport_info of this ServiceInfoPost.


        :return: The transport_info of this ServiceInfoPost.
        :rtype: TransportInfo
        """
        return self._transport_info

    @transport_info.setter
    def transport_info(self, transport_info: TransportInfo):
        """Sets the transport_info of this ServiceInfoPost.


        :param transport_info: The transport_info of this ServiceInfoPost.
        :type transport_info: TransportInfo
        """

        self._transport_info = transport_info

    @property
    def serializer(self) -> SerializerType:
        """Gets the serializer of this ServiceInfoPost.


        :return: The serializer of this ServiceInfoPost.
        :rtype: SerializerType
        """
        return self._serializer

    @serializer.setter
    def serializer(self, serializer: SerializerType):
        """Sets the serializer of this ServiceInfoPost.


        :param serializer: The serializer of this ServiceInfoPost.
        :type serializer: SerializerType
        """
        if serializer is None:
            raise ValueError("Invalid value for `serializer`, must not be `None`")  # noqa: E501

        self._serializer = serializer

    @property
    def scope_of_locality(self) -> LocalityType:
        """Gets the scope_of_locality of this ServiceInfoPost.


        :return: The scope_of_locality of this ServiceInfoPost.
        :rtype: LocalityType
        """
        return self._scope_of_locality

    @scope_of_locality.setter
    def scope_of_locality(self, scope_of_locality: LocalityType):
        """Sets the scope_of_locality of this ServiceInfoPost.


        :param scope_of_locality: The scope_of_locality of this ServiceInfoPost.
        :type scope_of_locality: LocalityType
        """

        self._scope_of_locality = scope_of_locality

    @property
    def consumed_local_only(self) -> ServiceInfoConsumedLocalOnly:
        """Gets the consumed_local_only of this ServiceInfoPost.


        :return: The consumed_local_only of this ServiceInfoPost.
        :rtype: ServiceInfoConsumedLocalOnly
        """
        return self._consumed_local_only

    @consumed_local_only.setter
    def consumed_local_only(self, consumed_local_only: ServiceInfoConsumedLocalOnly):
        """Sets the consumed_local_only of this ServiceInfoPost.


        :param consumed_local_only: The consumed_local_only of this ServiceInfoPost.
        :type consumed_local_only: ServiceInfoConsumedLocalOnly
        """

        self._consumed_local_only = consumed_local_only

    @property
    def is_local(self) -> ServiceInfoIsLocal:
        """Gets the is_local of this ServiceInfoPost.


        :return: The is_local of this ServiceInfoPost.
        :rtype: ServiceInfoIsLocal
        """
        return self._is_local

    @is_local.setter
    def is_local(self, is_local: ServiceInfoIsLocal):
        """Sets the is_local of this ServiceInfoPost.


        :param is_local: The is_local of this ServiceInfoPost.
        :type is_local: ServiceInfoIsLocal
        """

        self._is_local = is_local
