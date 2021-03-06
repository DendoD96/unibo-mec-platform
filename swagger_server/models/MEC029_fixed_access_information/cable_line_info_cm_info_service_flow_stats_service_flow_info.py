# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.MEC029_fixed_access_information.time_stamp import TimeStamp  # noqa: F401,E501
from swagger_server import util


class CableLineInfoCmInfoServiceFlowStatsServiceFlowInfo(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, aqm_dropped_pkts: int=None, pkts: int=None, policed_delay_pkts: int=None, policed_drop_pkts: int=None, service_flow_id: int=None, time_active: int=None, time_created: TimeStamp=None):  # noqa: E501
        """CableLineInfoCmInfoServiceFlowStatsServiceFlowInfo - a model defined in Swagger

        :param aqm_dropped_pkts: The aqm_dropped_pkts of this CableLineInfoCmInfoServiceFlowStatsServiceFlowInfo.  # noqa: E501
        :type aqm_dropped_pkts: int
        :param pkts: The pkts of this CableLineInfoCmInfoServiceFlowStatsServiceFlowInfo.  # noqa: E501
        :type pkts: int
        :param policed_delay_pkts: The policed_delay_pkts of this CableLineInfoCmInfoServiceFlowStatsServiceFlowInfo.  # noqa: E501
        :type policed_delay_pkts: int
        :param policed_drop_pkts: The policed_drop_pkts of this CableLineInfoCmInfoServiceFlowStatsServiceFlowInfo.  # noqa: E501
        :type policed_drop_pkts: int
        :param service_flow_id: The service_flow_id of this CableLineInfoCmInfoServiceFlowStatsServiceFlowInfo.  # noqa: E501
        :type service_flow_id: int
        :param time_active: The time_active of this CableLineInfoCmInfoServiceFlowStatsServiceFlowInfo.  # noqa: E501
        :type time_active: int
        :param time_created: The time_created of this CableLineInfoCmInfoServiceFlowStatsServiceFlowInfo.  # noqa: E501
        :type time_created: TimeStamp
        """
        self.swagger_types = {
            'aqm_dropped_pkts': int,
            'pkts': int,
            'policed_delay_pkts': int,
            'policed_drop_pkts': int,
            'service_flow_id': int,
            'time_active': int,
            'time_created': TimeStamp
        }

        self.attribute_map = {
            'aqm_dropped_pkts': 'aqmDroppedPkts',
            'pkts': 'pkts',
            'policed_delay_pkts': 'policedDelayPkts',
            'policed_drop_pkts': 'policedDropPkts',
            'service_flow_id': 'serviceFlowId',
            'time_active': 'timeActive',
            'time_created': 'timeCreated'
        }
        self._aqm_dropped_pkts = aqm_dropped_pkts
        self._pkts = pkts
        self._policed_delay_pkts = policed_delay_pkts
        self._policed_drop_pkts = policed_drop_pkts
        self._service_flow_id = service_flow_id
        self._time_active = time_active
        self._time_created = time_created

    @classmethod
    def from_dict(cls, dikt) -> 'CableLineInfoCmInfoServiceFlowStatsServiceFlowInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The CableLineInfo.cmInfo.serviceFlowStats.serviceFlowInfo of this CableLineInfoCmInfoServiceFlowStatsServiceFlowInfo.  # noqa: E501
        :rtype: CableLineInfoCmInfoServiceFlowStatsServiceFlowInfo
        """
        return util.deserialize_model(dikt, cls)

    @property
    def aqm_dropped_pkts(self) -> int:
        """Gets the aqm_dropped_pkts of this CableLineInfoCmInfoServiceFlowStatsServiceFlowInfo.

        For upstream service flows on which AQM is enabled, this attribute counts the number of Packet Data PDUs classified to this service flow dropped due to Active Queue Management drop decisions.  # noqa: E501

        :return: The aqm_dropped_pkts of this CableLineInfoCmInfoServiceFlowStatsServiceFlowInfo.
        :rtype: int
        """
        return self._aqm_dropped_pkts

    @aqm_dropped_pkts.setter
    def aqm_dropped_pkts(self, aqm_dropped_pkts: int):
        """Sets the aqm_dropped_pkts of this CableLineInfoCmInfoServiceFlowStatsServiceFlowInfo.

        For upstream service flows on which AQM is enabled, this attribute counts the number of Packet Data PDUs classified to this service flow dropped due to Active Queue Management drop decisions.  # noqa: E501

        :param aqm_dropped_pkts: The aqm_dropped_pkts of this CableLineInfoCmInfoServiceFlowStatsServiceFlowInfo.
        :type aqm_dropped_pkts: int
        """
        if aqm_dropped_pkts is None:
            raise ValueError("Invalid value for `aqm_dropped_pkts`, must not be `None`")  # noqa: E501

        self._aqm_dropped_pkts = aqm_dropped_pkts

    @property
    def pkts(self) -> int:
        """Gets the pkts of this CableLineInfoCmInfoServiceFlowStatsServiceFlowInfo.

        For outgoing Service Flows, this attribute counts the number of Packet Data PDUs forwarded to this Service Flow. For incoming upstream CMTS service flows, this attribute counts the number of Packet Data PDUs actually received on the Service Flow identified by the SID for which the packet was scheduled.  # noqa: E501

        :return: The pkts of this CableLineInfoCmInfoServiceFlowStatsServiceFlowInfo.
        :rtype: int
        """
        return self._pkts

    @pkts.setter
    def pkts(self, pkts: int):
        """Sets the pkts of this CableLineInfoCmInfoServiceFlowStatsServiceFlowInfo.

        For outgoing Service Flows, this attribute counts the number of Packet Data PDUs forwarded to this Service Flow. For incoming upstream CMTS service flows, this attribute counts the number of Packet Data PDUs actually received on the Service Flow identified by the SID for which the packet was scheduled.  # noqa: E501

        :param pkts: The pkts of this CableLineInfoCmInfoServiceFlowStatsServiceFlowInfo.
        :type pkts: int
        """
        if pkts is None:
            raise ValueError("Invalid value for `pkts`, must not be `None`")  # noqa: E501

        self._pkts = pkts

    @property
    def policed_delay_pkts(self) -> int:
        """Gets the policed_delay_pkts of this CableLineInfoCmInfoServiceFlowStatsServiceFlowInfo.

        It counts only outgoing packets delayed in order to maintain the Maximum Sustained Traffic Rate.  # noqa: E501

        :return: The policed_delay_pkts of this CableLineInfoCmInfoServiceFlowStatsServiceFlowInfo.
        :rtype: int
        """
        return self._policed_delay_pkts

    @policed_delay_pkts.setter
    def policed_delay_pkts(self, policed_delay_pkts: int):
        """Sets the policed_delay_pkts of this CableLineInfoCmInfoServiceFlowStatsServiceFlowInfo.

        It counts only outgoing packets delayed in order to maintain the Maximum Sustained Traffic Rate.  # noqa: E501

        :param policed_delay_pkts: The policed_delay_pkts of this CableLineInfoCmInfoServiceFlowStatsServiceFlowInfo.
        :type policed_delay_pkts: int
        """
        if policed_delay_pkts is None:
            raise ValueError("Invalid value for `policed_delay_pkts`, must not be `None`")  # noqa: E501

        self._policed_delay_pkts = policed_delay_pkts

    @property
    def policed_drop_pkts(self) -> int:
        """Gets the policed_drop_pkts of this CableLineInfoCmInfoServiceFlowStatsServiceFlowInfo.

        For upstream service flows, this attribute counts the number of Packet Data PDUs classified to this service flow dropped due to: 1) exceeding the selected Buffer Size for the service flow; or 2) UGS packets dropped due to exceeding the Unsolicited Grant Size with a Request/Transmission policy that requires such packets to be dropped.  # noqa: E501

        :return: The policed_drop_pkts of this CableLineInfoCmInfoServiceFlowStatsServiceFlowInfo.
        :rtype: int
        """
        return self._policed_drop_pkts

    @policed_drop_pkts.setter
    def policed_drop_pkts(self, policed_drop_pkts: int):
        """Sets the policed_drop_pkts of this CableLineInfoCmInfoServiceFlowStatsServiceFlowInfo.

        For upstream service flows, this attribute counts the number of Packet Data PDUs classified to this service flow dropped due to: 1) exceeding the selected Buffer Size for the service flow; or 2) UGS packets dropped due to exceeding the Unsolicited Grant Size with a Request/Transmission policy that requires such packets to be dropped.  # noqa: E501

        :param policed_drop_pkts: The policed_drop_pkts of this CableLineInfoCmInfoServiceFlowStatsServiceFlowInfo.
        :type policed_drop_pkts: int
        """
        if policed_drop_pkts is None:
            raise ValueError("Invalid value for `policed_drop_pkts`, must not be `None`")  # noqa: E501

        self._policed_drop_pkts = policed_drop_pkts

    @property
    def service_flow_id(self) -> int:
        """Gets the service_flow_id of this CableLineInfoCmInfoServiceFlowStatsServiceFlowInfo.

        It represents an identifier assigned to a Service Flow by CMTS within a MAC Domain.  # noqa: E501

        :return: The service_flow_id of this CableLineInfoCmInfoServiceFlowStatsServiceFlowInfo.
        :rtype: int
        """
        return self._service_flow_id

    @service_flow_id.setter
    def service_flow_id(self, service_flow_id: int):
        """Sets the service_flow_id of this CableLineInfoCmInfoServiceFlowStatsServiceFlowInfo.

        It represents an identifier assigned to a Service Flow by CMTS within a MAC Domain.  # noqa: E501

        :param service_flow_id: The service_flow_id of this CableLineInfoCmInfoServiceFlowStatsServiceFlowInfo.
        :type service_flow_id: int
        """
        if service_flow_id is None:
            raise ValueError("Invalid value for `service_flow_id`, must not be `None`")  # noqa: E501

        self._service_flow_id = service_flow_id

    @property
    def time_active(self) -> int:
        """Gets the time_active of this CableLineInfoCmInfoServiceFlowStatsServiceFlowInfo.

        It indicates the number of seconds that the service flow has been active.  # noqa: E501

        :return: The time_active of this CableLineInfoCmInfoServiceFlowStatsServiceFlowInfo.
        :rtype: int
        """
        return self._time_active

    @time_active.setter
    def time_active(self, time_active: int):
        """Sets the time_active of this CableLineInfoCmInfoServiceFlowStatsServiceFlowInfo.

        It indicates the number of seconds that the service flow has been active.  # noqa: E501

        :param time_active: The time_active of this CableLineInfoCmInfoServiceFlowStatsServiceFlowInfo.
        :type time_active: int
        """
        if time_active is None:
            raise ValueError("Invalid value for `time_active`, must not be `None`")  # noqa: E501

        self._time_active = time_active

    @property
    def time_created(self) -> TimeStamp:
        """Gets the time_created of this CableLineInfoCmInfoServiceFlowStatsServiceFlowInfo.


        :return: The time_created of this CableLineInfoCmInfoServiceFlowStatsServiceFlowInfo.
        :rtype: TimeStamp
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created: TimeStamp):
        """Sets the time_created of this CableLineInfoCmInfoServiceFlowStatsServiceFlowInfo.


        :param time_created: The time_created of this CableLineInfoCmInfoServiceFlowStatsServiceFlowInfo.
        :type time_created: TimeStamp
        """
        if time_created is None:
            raise ValueError("Invalid value for `time_created`, must not be `None`")  # noqa: E501

        self._time_created = time_created
