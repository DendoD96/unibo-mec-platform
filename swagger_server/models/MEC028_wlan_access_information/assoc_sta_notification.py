# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.MEC028_wlan_access_information.ap_identity import ApIdentity  # noqa: F401,E501
from swagger_server.models.MEC028_wlan_access_information.sta_identity import StaIdentity  # noqa: F401,E501
from swagger_server.models.MEC028_wlan_access_information.time_stamp import TimeStamp  # noqa: F401,E501
from swagger_server import util


class AssocStaNotification(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, ap_id: ApIdentity=None, notification_type: str=None, sta_id: List[StaIdentity]=None, time_stamp: TimeStamp=None):  # noqa: E501
        """AssocStaNotification - a model defined in Swagger

        :param ap_id: The ap_id of this AssocStaNotification.  # noqa: E501
        :type ap_id: ApIdentity
        :param notification_type: The notification_type of this AssocStaNotification.  # noqa: E501
        :type notification_type: str
        :param sta_id: The sta_id of this AssocStaNotification.  # noqa: E501
        :type sta_id: List[StaIdentity]
        :param time_stamp: The time_stamp of this AssocStaNotification.  # noqa: E501
        :type time_stamp: TimeStamp
        """
        self.swagger_types = {
            'ap_id': ApIdentity,
            'notification_type': str,
            'sta_id': List[StaIdentity],
            'time_stamp': TimeStamp
        }

        self.attribute_map = {
            'ap_id': 'apId',
            'notification_type': 'notificationType',
            'sta_id': 'staId',
            'time_stamp': 'timeStamp'
        }
        self._ap_id = ap_id
        self._notification_type = notification_type
        self._sta_id = sta_id
        self._time_stamp = time_stamp

    @classmethod
    def from_dict(cls, dikt) -> 'AssocStaNotification':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AssocStaNotification of this AssocStaNotification.  # noqa: E501
        :rtype: AssocStaNotification
        """
        return util.deserialize_model(dikt, cls)

    @property
    def ap_id(self) -> ApIdentity:
        """Gets the ap_id of this AssocStaNotification.


        :return: The ap_id of this AssocStaNotification.
        :rtype: ApIdentity
        """
        return self._ap_id

    @ap_id.setter
    def ap_id(self, ap_id: ApIdentity):
        """Sets the ap_id of this AssocStaNotification.


        :param ap_id: The ap_id of this AssocStaNotification.
        :type ap_id: ApIdentity
        """
        if ap_id is None:
            raise ValueError("Invalid value for `ap_id`, must not be `None`")  # noqa: E501

        self._ap_id = ap_id

    @property
    def notification_type(self) -> str:
        """Gets the notification_type of this AssocStaNotification.

        Shall be set to \"AssocStaNotification\".  # noqa: E501

        :return: The notification_type of this AssocStaNotification.
        :rtype: str
        """
        return self._notification_type

    @notification_type.setter
    def notification_type(self, notification_type: str):
        """Sets the notification_type of this AssocStaNotification.

        Shall be set to \"AssocStaNotification\".  # noqa: E501

        :param notification_type: The notification_type of this AssocStaNotification.
        :type notification_type: str
        """
        if notification_type is None:
            raise ValueError("Invalid value for `notification_type`, must not be `None`")  # noqa: E501

        self._notification_type = notification_type

    @property
    def sta_id(self) -> List[StaIdentity]:
        """Gets the sta_id of this AssocStaNotification.

        Identifier(s) to uniquely specify the client station(s) associated.  # noqa: E501

        :return: The sta_id of this AssocStaNotification.
        :rtype: List[StaIdentity]
        """
        return self._sta_id

    @sta_id.setter
    def sta_id(self, sta_id: List[StaIdentity]):
        """Sets the sta_id of this AssocStaNotification.

        Identifier(s) to uniquely specify the client station(s) associated.  # noqa: E501

        :param sta_id: The sta_id of this AssocStaNotification.
        :type sta_id: List[StaIdentity]
        """

        self._sta_id = sta_id

    @property
    def time_stamp(self) -> TimeStamp:
        """Gets the time_stamp of this AssocStaNotification.


        :return: The time_stamp of this AssocStaNotification.
        :rtype: TimeStamp
        """
        return self._time_stamp

    @time_stamp.setter
    def time_stamp(self, time_stamp: TimeStamp):
        """Sets the time_stamp of this AssocStaNotification.


        :param time_stamp: The time_stamp of this AssocStaNotification.
        :type time_stamp: TimeStamp
        """

        self._time_stamp = time_stamp
