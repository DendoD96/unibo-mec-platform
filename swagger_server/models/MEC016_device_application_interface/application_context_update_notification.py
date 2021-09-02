# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.MEC016_device_application_interface.application_context_update_notification_user_app_instance_info import ApplicationContextUpdateNotificationUserAppInstanceInfo  # noqa: F401,E501
from swagger_server import util


class ApplicationContextUpdateNotification(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, context_id: str=None, notification_type: str=None, user_app_instance_info: List[ApplicationContextUpdateNotificationUserAppInstanceInfo]=None):  # noqa: E501
        """ApplicationContextUpdateNotification - a model defined in Swagger

        :param context_id: The context_id of this ApplicationContextUpdateNotification.  # noqa: E501
        :type context_id: str
        :param notification_type: The notification_type of this ApplicationContextUpdateNotification.  # noqa: E501
        :type notification_type: str
        :param user_app_instance_info: The user_app_instance_info of this ApplicationContextUpdateNotification.  # noqa: E501
        :type user_app_instance_info: List[ApplicationContextUpdateNotificationUserAppInstanceInfo]
        """
        self.swagger_types = {
            'context_id': str,
            'notification_type': str,
            'user_app_instance_info': List[ApplicationContextUpdateNotificationUserAppInstanceInfo]
        }

        self.attribute_map = {
            'context_id': 'contextId',
            'notification_type': 'notificationType',
            'user_app_instance_info': 'userAppInstanceInfo'
        }
        self._context_id = context_id
        self._notification_type = notification_type
        self._user_app_instance_info = user_app_instance_info

    @classmethod
    def from_dict(cls, dikt) -> 'ApplicationContextUpdateNotification':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ApplicationContextUpdateNotification of this ApplicationContextUpdateNotification.  # noqa: E501
        :rtype: ApplicationContextUpdateNotification
        """
        return util.deserialize_model(dikt, cls)

    @property
    def context_id(self) -> str:
        """Gets the context_id of this ApplicationContextUpdateNotification.

        Uniquely identifies the application context in the MEC system.  # noqa: E501

        :return: The context_id of this ApplicationContextUpdateNotification.
        :rtype: str
        """
        return self._context_id

    @context_id.setter
    def context_id(self, context_id: str):
        """Sets the context_id of this ApplicationContextUpdateNotification.

        Uniquely identifies the application context in the MEC system.  # noqa: E501

        :param context_id: The context_id of this ApplicationContextUpdateNotification.
        :type context_id: str
        """
        if context_id is None:
            raise ValueError("Invalid value for `context_id`, must not be `None`")  # noqa: E501

        self._context_id = context_id

    @property
    def notification_type(self) -> str:
        """Gets the notification_type of this ApplicationContextUpdateNotification.

        Shall be set to \"ApplicationContextUpdateNotification\".  # noqa: E501

        :return: The notification_type of this ApplicationContextUpdateNotification.
        :rtype: str
        """
        return self._notification_type

    @notification_type.setter
    def notification_type(self, notification_type: str):
        """Sets the notification_type of this ApplicationContextUpdateNotification.

        Shall be set to \"ApplicationContextUpdateNotification\".  # noqa: E501

        :param notification_type: The notification_type of this ApplicationContextUpdateNotification.
        :type notification_type: str
        """
        if notification_type is None:
            raise ValueError("Invalid value for `notification_type`, must not be `None`")  # noqa: E501

        self._notification_type = notification_type

    @property
    def user_app_instance_info(self) -> List[ApplicationContextUpdateNotificationUserAppInstanceInfo]:
        """Gets the user_app_instance_info of this ApplicationContextUpdateNotification.

        List of user application instance information.  # noqa: E501

        :return: The user_app_instance_info of this ApplicationContextUpdateNotification.
        :rtype: List[ApplicationContextUpdateNotificationUserAppInstanceInfo]
        """
        return self._user_app_instance_info

    @user_app_instance_info.setter
    def user_app_instance_info(self, user_app_instance_info: List[ApplicationContextUpdateNotificationUserAppInstanceInfo]):
        """Sets the user_app_instance_info of this ApplicationContextUpdateNotification.

        List of user application instance information.  # noqa: E501

        :param user_app_instance_info: The user_app_instance_info of this ApplicationContextUpdateNotification.
        :type user_app_instance_info: List[ApplicationContextUpdateNotificationUserAppInstanceInfo]
        """
        if user_app_instance_info is None:
            raise ValueError("Invalid value for `user_app_instance_info`, must not be `None`")  # noqa: E501

        self._user_app_instance_info = user_app_instance_info