# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.MEC012_radio_network_information.associate_id import AssociateId  # noqa: F401,E501
from swagger_server.models.MEC012_radio_network_information.ecgi import Ecgi  # noqa: F401,E501
from swagger_server.models.MEC012_radio_network_information.rab_mod_notification_erab_qos_parameters import RabModNotificationErabQosParameters  # noqa: F401,E501
from swagger_server.models.MEC012_radio_network_information.time_stamp import TimeStamp  # noqa: F401,E501
from swagger_server import util


class RabModNotification(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, associate_id: List[AssociateId]=None, ecgi: Ecgi=None, erab_id: int=None, erab_qos_parameters: RabModNotificationErabQosParameters=None, notification_type: str=None, time_stamp: TimeStamp=None):  # noqa: E501
        """RabModNotification - a model defined in Swagger

        :param associate_id: The associate_id of this RabModNotification.  # noqa: E501
        :type associate_id: List[AssociateId]
        :param ecgi: The ecgi of this RabModNotification.  # noqa: E501
        :type ecgi: Ecgi
        :param erab_id: The erab_id of this RabModNotification.  # noqa: E501
        :type erab_id: int
        :param erab_qos_parameters: The erab_qos_parameters of this RabModNotification.  # noqa: E501
        :type erab_qos_parameters: RabModNotificationErabQosParameters
        :param notification_type: The notification_type of this RabModNotification.  # noqa: E501
        :type notification_type: str
        :param time_stamp: The time_stamp of this RabModNotification.  # noqa: E501
        :type time_stamp: TimeStamp
        """
        self.swagger_types = {
            'associate_id': List[AssociateId],
            'ecgi': Ecgi,
            'erab_id': int,
            'erab_qos_parameters': RabModNotificationErabQosParameters,
            'notification_type': str,
            'time_stamp': TimeStamp
        }

        self.attribute_map = {
            'associate_id': 'associateId',
            'ecgi': 'ecgi',
            'erab_id': 'erabId',
            'erab_qos_parameters': 'erabQosParameters',
            'notification_type': 'notificationType',
            'time_stamp': 'timeStamp'
        }
        self._associate_id = associate_id
        self._ecgi = ecgi
        self._erab_id = erab_id
        self._erab_qos_parameters = erab_qos_parameters
        self._notification_type = notification_type
        self._time_stamp = time_stamp

    @classmethod
    def from_dict(cls, dikt) -> 'RabModNotification':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The RabModNotification of this RabModNotification.  # noqa: E501
        :rtype: RabModNotification
        """
        return util.deserialize_model(dikt, cls)

    @property
    def associate_id(self) -> List[AssociateId]:
        """Gets the associate_id of this RabModNotification.

        0 to N identifiers to bind the event for a specific UE or flow.   # noqa: E501

        :return: The associate_id of this RabModNotification.
        :rtype: List[AssociateId]
        """
        return self._associate_id

    @associate_id.setter
    def associate_id(self, associate_id: List[AssociateId]):
        """Sets the associate_id of this RabModNotification.

        0 to N identifiers to bind the event for a specific UE or flow.   # noqa: E501

        :param associate_id: The associate_id of this RabModNotification.
        :type associate_id: List[AssociateId]
        """

        self._associate_id = associate_id

    @property
    def ecgi(self) -> Ecgi:
        """Gets the ecgi of this RabModNotification.


        :return: The ecgi of this RabModNotification.
        :rtype: Ecgi
        """
        return self._ecgi

    @ecgi.setter
    def ecgi(self, ecgi: Ecgi):
        """Sets the ecgi of this RabModNotification.


        :param ecgi: The ecgi of this RabModNotification.
        :type ecgi: Ecgi
        """
        if ecgi is None:
            raise ValueError("Invalid value for `ecgi`, must not be `None`")  # noqa: E501

        self._ecgi = ecgi

    @property
    def erab_id(self) -> int:
        """Gets the erab_id of this RabModNotification.

        The attribute that uniquely identifies a Radio Access bearer for specific UE as defined in ETSI TS 136 413 [i.3].  # noqa: E501

        :return: The erab_id of this RabModNotification.
        :rtype: int
        """
        return self._erab_id

    @erab_id.setter
    def erab_id(self, erab_id: int):
        """Sets the erab_id of this RabModNotification.

        The attribute that uniquely identifies a Radio Access bearer for specific UE as defined in ETSI TS 136 413 [i.3].  # noqa: E501

        :param erab_id: The erab_id of this RabModNotification.
        :type erab_id: int
        """
        if erab_id is None:
            raise ValueError("Invalid value for `erab_id`, must not be `None`")  # noqa: E501

        self._erab_id = erab_id

    @property
    def erab_qos_parameters(self) -> RabModNotificationErabQosParameters:
        """Gets the erab_qos_parameters of this RabModNotification.


        :return: The erab_qos_parameters of this RabModNotification.
        :rtype: RabModNotificationErabQosParameters
        """
        return self._erab_qos_parameters

    @erab_qos_parameters.setter
    def erab_qos_parameters(self, erab_qos_parameters: RabModNotificationErabQosParameters):
        """Sets the erab_qos_parameters of this RabModNotification.


        :param erab_qos_parameters: The erab_qos_parameters of this RabModNotification.
        :type erab_qos_parameters: RabModNotificationErabQosParameters
        """

        self._erab_qos_parameters = erab_qos_parameters

    @property
    def notification_type(self) -> str:
        """Gets the notification_type of this RabModNotification.

        Shall be set to \"RabModNotification\".  # noqa: E501

        :return: The notification_type of this RabModNotification.
        :rtype: str
        """
        return self._notification_type

    @notification_type.setter
    def notification_type(self, notification_type: str):
        """Sets the notification_type of this RabModNotification.

        Shall be set to \"RabModNotification\".  # noqa: E501

        :param notification_type: The notification_type of this RabModNotification.
        :type notification_type: str
        """
        if notification_type is None:
            raise ValueError("Invalid value for `notification_type`, must not be `None`")  # noqa: E501

        self._notification_type = notification_type

    @property
    def time_stamp(self) -> TimeStamp:
        """Gets the time_stamp of this RabModNotification.


        :return: The time_stamp of this RabModNotification.
        :rtype: TimeStamp
        """
        return self._time_stamp

    @time_stamp.setter
    def time_stamp(self, time_stamp: TimeStamp):
        """Sets the time_stamp of this RabModNotification.


        :param time_stamp: The time_stamp of this RabModNotification.
        :type time_stamp: TimeStamp
        """

        self._time_stamp = time_stamp
