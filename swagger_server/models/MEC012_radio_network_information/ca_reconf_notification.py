# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.MEC012_radio_network_information.associate_id import AssociateId  # noqa: F401,E501
from swagger_server.models.MEC012_radio_network_information.ca_reconf_notification_carrier_aggregation_meas_info import CaReconfNotificationCarrierAggregationMeasInfo  # noqa: F401,E501
from swagger_server.models.MEC012_radio_network_information.ca_reconf_notification_secondary_cell_add import CaReconfNotificationSecondaryCellAdd  # noqa: F401,E501
from swagger_server.models.MEC012_radio_network_information.ecgi import Ecgi  # noqa: F401,E501
from swagger_server.models.MEC012_radio_network_information.time_stamp import TimeStamp  # noqa: F401,E501
from swagger_server import util


class CaReconfNotification(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, associate_id: List[AssociateId]=None, carrier_aggregation_meas_info: List[CaReconfNotificationCarrierAggregationMeasInfo]=None, ecgi: Ecgi=None, notification_type: str=None, secondary_cell_add: List[CaReconfNotificationSecondaryCellAdd]=None, secondary_cell_remove: List[CaReconfNotificationSecondaryCellAdd]=None, time_stamp: TimeStamp=None):  # noqa: E501
        """CaReconfNotification - a model defined in Swagger

        :param associate_id: The associate_id of this CaReconfNotification.  # noqa: E501
        :type associate_id: List[AssociateId]
        :param carrier_aggregation_meas_info: The carrier_aggregation_meas_info of this CaReconfNotification.  # noqa: E501
        :type carrier_aggregation_meas_info: List[CaReconfNotificationCarrierAggregationMeasInfo]
        :param ecgi: The ecgi of this CaReconfNotification.  # noqa: E501
        :type ecgi: Ecgi
        :param notification_type: The notification_type of this CaReconfNotification.  # noqa: E501
        :type notification_type: str
        :param secondary_cell_add: The secondary_cell_add of this CaReconfNotification.  # noqa: E501
        :type secondary_cell_add: List[CaReconfNotificationSecondaryCellAdd]
        :param secondary_cell_remove: The secondary_cell_remove of this CaReconfNotification.  # noqa: E501
        :type secondary_cell_remove: List[CaReconfNotificationSecondaryCellAdd]
        :param time_stamp: The time_stamp of this CaReconfNotification.  # noqa: E501
        :type time_stamp: TimeStamp
        """
        self.swagger_types = {
            'associate_id': List[AssociateId],
            'carrier_aggregation_meas_info': List[CaReconfNotificationCarrierAggregationMeasInfo],
            'ecgi': Ecgi,
            'notification_type': str,
            'secondary_cell_add': List[CaReconfNotificationSecondaryCellAdd],
            'secondary_cell_remove': List[CaReconfNotificationSecondaryCellAdd],
            'time_stamp': TimeStamp
        }

        self.attribute_map = {
            'associate_id': 'associateId',
            'carrier_aggregation_meas_info': 'carrierAggregationMeasInfo',
            'ecgi': 'ecgi',
            'notification_type': 'notificationType',
            'secondary_cell_add': 'secondaryCellAdd',
            'secondary_cell_remove': 'secondaryCellRemove',
            'time_stamp': 'timeStamp'
        }
        self._associate_id = associate_id
        self._carrier_aggregation_meas_info = carrier_aggregation_meas_info
        self._ecgi = ecgi
        self._notification_type = notification_type
        self._secondary_cell_add = secondary_cell_add
        self._secondary_cell_remove = secondary_cell_remove
        self._time_stamp = time_stamp

    @classmethod
    def from_dict(cls, dikt) -> 'CaReconfNotification':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The CaReconfNotification of this CaReconfNotification.  # noqa: E501
        :rtype: CaReconfNotification
        """
        return util.deserialize_model(dikt, cls)

    @property
    def associate_id(self) -> List[AssociateId]:
        """Gets the associate_id of this CaReconfNotification.

        0 to N identifiers to associate the event for a specific UE or flow.  # noqa: E501

        :return: The associate_id of this CaReconfNotification.
        :rtype: List[AssociateId]
        """
        return self._associate_id

    @associate_id.setter
    def associate_id(self, associate_id: List[AssociateId]):
        """Sets the associate_id of this CaReconfNotification.

        0 to N identifiers to associate the event for a specific UE or flow.  # noqa: E501

        :param associate_id: The associate_id of this CaReconfNotification.
        :type associate_id: List[AssociateId]
        """

        self._associate_id = associate_id

    @property
    def carrier_aggregation_meas_info(self) -> List[CaReconfNotificationCarrierAggregationMeasInfo]:
        """Gets the carrier_aggregation_meas_info of this CaReconfNotification.

        This parameter can be repeated to contain information of all the carriers assign for Carrier Aggregation up to M.  # noqa: E501

        :return: The carrier_aggregation_meas_info of this CaReconfNotification.
        :rtype: List[CaReconfNotificationCarrierAggregationMeasInfo]
        """
        return self._carrier_aggregation_meas_info

    @carrier_aggregation_meas_info.setter
    def carrier_aggregation_meas_info(self, carrier_aggregation_meas_info: List[CaReconfNotificationCarrierAggregationMeasInfo]):
        """Sets the carrier_aggregation_meas_info of this CaReconfNotification.

        This parameter can be repeated to contain information of all the carriers assign for Carrier Aggregation up to M.  # noqa: E501

        :param carrier_aggregation_meas_info: The carrier_aggregation_meas_info of this CaReconfNotification.
        :type carrier_aggregation_meas_info: List[CaReconfNotificationCarrierAggregationMeasInfo]
        """

        self._carrier_aggregation_meas_info = carrier_aggregation_meas_info

    @property
    def ecgi(self) -> Ecgi:
        """Gets the ecgi of this CaReconfNotification.


        :return: The ecgi of this CaReconfNotification.
        :rtype: Ecgi
        """
        return self._ecgi

    @ecgi.setter
    def ecgi(self, ecgi: Ecgi):
        """Sets the ecgi of this CaReconfNotification.


        :param ecgi: The ecgi of this CaReconfNotification.
        :type ecgi: Ecgi
        """
        if ecgi is None:
            raise ValueError("Invalid value for `ecgi`, must not be `None`")  # noqa: E501

        self._ecgi = ecgi

    @property
    def notification_type(self) -> str:
        """Gets the notification_type of this CaReconfNotification.

        Shall be set to \"CaReConfNotification\".  # noqa: E501

        :return: The notification_type of this CaReconfNotification.
        :rtype: str
        """
        return self._notification_type

    @notification_type.setter
    def notification_type(self, notification_type: str):
        """Sets the notification_type of this CaReconfNotification.

        Shall be set to \"CaReConfNotification\".  # noqa: E501

        :param notification_type: The notification_type of this CaReconfNotification.
        :type notification_type: str
        """
        if notification_type is None:
            raise ValueError("Invalid value for `notification_type`, must not be `None`")  # noqa: E501

        self._notification_type = notification_type

    @property
    def secondary_cell_add(self) -> List[CaReconfNotificationSecondaryCellAdd]:
        """Gets the secondary_cell_add of this CaReconfNotification.


        :return: The secondary_cell_add of this CaReconfNotification.
        :rtype: List[CaReconfNotificationSecondaryCellAdd]
        """
        return self._secondary_cell_add

    @secondary_cell_add.setter
    def secondary_cell_add(self, secondary_cell_add: List[CaReconfNotificationSecondaryCellAdd]):
        """Sets the secondary_cell_add of this CaReconfNotification.


        :param secondary_cell_add: The secondary_cell_add of this CaReconfNotification.
        :type secondary_cell_add: List[CaReconfNotificationSecondaryCellAdd]
        """

        self._secondary_cell_add = secondary_cell_add

    @property
    def secondary_cell_remove(self) -> List[CaReconfNotificationSecondaryCellAdd]:
        """Gets the secondary_cell_remove of this CaReconfNotification.


        :return: The secondary_cell_remove of this CaReconfNotification.
        :rtype: List[CaReconfNotificationSecondaryCellAdd]
        """
        return self._secondary_cell_remove

    @secondary_cell_remove.setter
    def secondary_cell_remove(self, secondary_cell_remove: List[CaReconfNotificationSecondaryCellAdd]):
        """Sets the secondary_cell_remove of this CaReconfNotification.


        :param secondary_cell_remove: The secondary_cell_remove of this CaReconfNotification.
        :type secondary_cell_remove: List[CaReconfNotificationSecondaryCellAdd]
        """

        self._secondary_cell_remove = secondary_cell_remove

    @property
    def time_stamp(self) -> TimeStamp:
        """Gets the time_stamp of this CaReconfNotification.


        :return: The time_stamp of this CaReconfNotification.
        :rtype: TimeStamp
        """
        return self._time_stamp

    @time_stamp.setter
    def time_stamp(self, time_stamp: TimeStamp):
        """Sets the time_stamp of this CaReconfNotification.


        :param time_stamp: The time_stamp of this CaReconfNotification.
        :type time_stamp: TimeStamp
        """

        self._time_stamp = time_stamp