# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.MEC011_application_support.timing_caps_ntp_servers import TimingCapsNtpServers  # noqa: F401,E501
from swagger_server.models.MEC011_application_support.timing_caps_ptp_masters import TimingCapsPtpMasters  # noqa: F401,E501
from swagger_server.models.MEC011_application_support.timing_caps_time_stamp import TimingCapsTimeStamp  # noqa: F401,E501
from swagger_server import util


class TimingCaps(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, time_stamp: TimingCapsTimeStamp=None, ntp_servers: List[TimingCapsNtpServers]=None, ptp_masters: List[TimingCapsPtpMasters]=None):  # noqa: E501
        """TimingCaps - a model defined in Swagger

        :param time_stamp: The time_stamp of this TimingCaps.  # noqa: E501
        :type time_stamp: TimingCapsTimeStamp
        :param ntp_servers: The ntp_servers of this TimingCaps.  # noqa: E501
        :type ntp_servers: List[TimingCapsNtpServers]
        :param ptp_masters: The ptp_masters of this TimingCaps.  # noqa: E501
        :type ptp_masters: List[TimingCapsPtpMasters]
        """
        self.swagger_types = {
            'time_stamp': TimingCapsTimeStamp,
            'ntp_servers': List[TimingCapsNtpServers],
            'ptp_masters': List[TimingCapsPtpMasters]
        }

        self.attribute_map = {
            'time_stamp': 'timeStamp',
            'ntp_servers': 'ntpServers',
            'ptp_masters': 'ptpMasters'
        }
        self._time_stamp = time_stamp
        self._ntp_servers = ntp_servers
        self._ptp_masters = ptp_masters

    @classmethod
    def from_dict(cls, dikt) -> 'TimingCaps':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The TimingCaps of this TimingCaps.  # noqa: E501
        :rtype: TimingCaps
        """
        return util.deserialize_model(dikt, cls)

    @property
    def time_stamp(self) -> TimingCapsTimeStamp:
        """Gets the time_stamp of this TimingCaps.


        :return: The time_stamp of this TimingCaps.
        :rtype: TimingCapsTimeStamp
        """
        return self._time_stamp

    @time_stamp.setter
    def time_stamp(self, time_stamp: TimingCapsTimeStamp):
        """Sets the time_stamp of this TimingCaps.


        :param time_stamp: The time_stamp of this TimingCaps.
        :type time_stamp: TimingCapsTimeStamp
        """

        self._time_stamp = time_stamp

    @property
    def ntp_servers(self) -> List[TimingCapsNtpServers]:
        """Gets the ntp_servers of this TimingCaps.

        Available NTP servers  # noqa: E501

        :return: The ntp_servers of this TimingCaps.
        :rtype: List[TimingCapsNtpServers]
        """
        return self._ntp_servers

    @ntp_servers.setter
    def ntp_servers(self, ntp_servers: List[TimingCapsNtpServers]):
        """Sets the ntp_servers of this TimingCaps.

        Available NTP servers  # noqa: E501

        :param ntp_servers: The ntp_servers of this TimingCaps.
        :type ntp_servers: List[TimingCapsNtpServers]
        """

        self._ntp_servers = ntp_servers

    @property
    def ptp_masters(self) -> List[TimingCapsPtpMasters]:
        """Gets the ptp_masters of this TimingCaps.

        Available PTP Masters  # noqa: E501

        :return: The ptp_masters of this TimingCaps.
        :rtype: List[TimingCapsPtpMasters]
        """
        return self._ptp_masters

    @ptp_masters.setter
    def ptp_masters(self, ptp_masters: List[TimingCapsPtpMasters]):
        """Sets the ptp_masters of this TimingCaps.

        Available PTP Masters  # noqa: E501

        :param ptp_masters: The ptp_masters of this TimingCaps.
        :type ptp_masters: List[TimingCapsPtpMasters]
        """

        self._ptp_masters = ptp_masters
