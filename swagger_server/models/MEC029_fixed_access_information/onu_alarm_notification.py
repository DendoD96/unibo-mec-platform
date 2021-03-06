# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.MEC029_fixed_access_information.cp_info import CpInfo  # noqa: F401,E501
from swagger_server.models.MEC029_fixed_access_information.onu_alarm_notification_alarm import OnuAlarmNotificationAlarm  # noqa: F401,E501
from swagger_server.models.MEC029_fixed_access_information.time_stamp import TimeStamp  # noqa: F401,E501
from swagger_server import util


class OnuAlarmNotification(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, alarm: OnuAlarmNotificationAlarm=None, customer_premises_info: List[CpInfo]=None, notification_type: str=None, onu_id: str=None, time_stamp: TimeStamp=None):  # noqa: E501
        """OnuAlarmNotification - a model defined in Swagger

        :param alarm: The alarm of this OnuAlarmNotification.  # noqa: E501
        :type alarm: OnuAlarmNotificationAlarm
        :param customer_premises_info: The customer_premises_info of this OnuAlarmNotification.  # noqa: E501
        :type customer_premises_info: List[CpInfo]
        :param notification_type: The notification_type of this OnuAlarmNotification.  # noqa: E501
        :type notification_type: str
        :param onu_id: The onu_id of this OnuAlarmNotification.  # noqa: E501
        :type onu_id: str
        :param time_stamp: The time_stamp of this OnuAlarmNotification.  # noqa: E501
        :type time_stamp: TimeStamp
        """
        self.swagger_types = {
            'alarm': OnuAlarmNotificationAlarm,
            'customer_premises_info': List[CpInfo],
            'notification_type': str,
            'onu_id': str,
            'time_stamp': TimeStamp
        }

        self.attribute_map = {
            'alarm': 'alarm',
            'customer_premises_info': 'customerPremisesInfo',
            'notification_type': 'notificationType',
            'onu_id': 'onuId',
            'time_stamp': 'timeStamp'
        }
        self._alarm = alarm
        self._customer_premises_info = customer_premises_info
        self._notification_type = notification_type
        self._onu_id = onu_id
        self._time_stamp = time_stamp

    @classmethod
    def from_dict(cls, dikt) -> 'OnuAlarmNotification':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The OnuAlarmNotification of this OnuAlarmNotification.  # noqa: E501
        :rtype: OnuAlarmNotification
        """
        return util.deserialize_model(dikt, cls)

    @property
    def alarm(self) -> OnuAlarmNotificationAlarm:
        """Gets the alarm of this OnuAlarmNotification.


        :return: The alarm of this OnuAlarmNotification.
        :rtype: OnuAlarmNotificationAlarm
        """
        return self._alarm

    @alarm.setter
    def alarm(self, alarm: OnuAlarmNotificationAlarm):
        """Sets the alarm of this OnuAlarmNotification.


        :param alarm: The alarm of this OnuAlarmNotification.
        :type alarm: OnuAlarmNotificationAlarm
        """
        if alarm is None:
            raise ValueError("Invalid value for `alarm`, must not be `None`")  # noqa: E501

        self._alarm = alarm

    @property
    def customer_premises_info(self) -> List[CpInfo]:
        """Gets the customer_premises_info of this OnuAlarmNotification.

        The physical location of the related customer sites.  # noqa: E501

        :return: The customer_premises_info of this OnuAlarmNotification.
        :rtype: List[CpInfo]
        """
        return self._customer_premises_info

    @customer_premises_info.setter
    def customer_premises_info(self, customer_premises_info: List[CpInfo]):
        """Sets the customer_premises_info of this OnuAlarmNotification.

        The physical location of the related customer sites.  # noqa: E501

        :param customer_premises_info: The customer_premises_info of this OnuAlarmNotification.
        :type customer_premises_info: List[CpInfo]
        """

        self._customer_premises_info = customer_premises_info

    @property
    def notification_type(self) -> str:
        """Gets the notification_type of this OnuAlarmNotification.

        Shall be set to \"OnuAlarmNotification\".  # noqa: E501

        :return: The notification_type of this OnuAlarmNotification.
        :rtype: str
        """
        return self._notification_type

    @notification_type.setter
    def notification_type(self, notification_type: str):
        """Sets the notification_type of this OnuAlarmNotification.

        Shall be set to \"OnuAlarmNotification\".  # noqa: E501

        :param notification_type: The notification_type of this OnuAlarmNotification.
        :type notification_type: str
        """
        if notification_type is None:
            raise ValueError("Invalid value for `notification_type`, must not be `None`")  # noqa: E501

        self._notification_type = notification_type

    @property
    def onu_id(self) -> str:
        """Gets the onu_id of this OnuAlarmNotification.

        The unique identifier for an optical network unit.  # noqa: E501

        :return: The onu_id of this OnuAlarmNotification.
        :rtype: str
        """
        return self._onu_id

    @onu_id.setter
    def onu_id(self, onu_id: str):
        """Sets the onu_id of this OnuAlarmNotification.

        The unique identifier for an optical network unit.  # noqa: E501

        :param onu_id: The onu_id of this OnuAlarmNotification.
        :type onu_id: str
        """
        if onu_id is None:
            raise ValueError("Invalid value for `onu_id`, must not be `None`")  # noqa: E501

        self._onu_id = onu_id

    @property
    def time_stamp(self) -> TimeStamp:
        """Gets the time_stamp of this OnuAlarmNotification.


        :return: The time_stamp of this OnuAlarmNotification.
        :rtype: TimeStamp
        """
        return self._time_stamp

    @time_stamp.setter
    def time_stamp(self, time_stamp: TimeStamp):
        """Sets the time_stamp of this OnuAlarmNotification.


        :param time_stamp: The time_stamp of this OnuAlarmNotification.
        :type time_stamp: TimeStamp
        """

        self._time_stamp = time_stamp
