# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.MEC028_wlan_access_information.beacon_request_config import BeaconRequestConfig  # noqa: F401,E501
from swagger_server.models.MEC028_wlan_access_information.channel_load_config import ChannelLoadConfig  # noqa: F401,E501
from swagger_server.models.MEC028_wlan_access_information.neighbor_report_config import NeighborReportConfig  # noqa: F401,E501
from swagger_server.models.MEC028_wlan_access_information.sta_statistics_config import StaStatisticsConfig  # noqa: F401,E501
from swagger_server import util


class MeasurementInfo(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, beacon_request_conf: BeaconRequestConfig=None, channel_load_conf: ChannelLoadConfig=None, measurement_duration: int=None, neighbor_report_conf: NeighborReportConfig=None, random_interval: int=None, sta_statistics_conf: StaStatisticsConfig=None):  # noqa: E501
        """MeasurementInfo - a model defined in Swagger

        :param beacon_request_conf: The beacon_request_conf of this MeasurementInfo.  # noqa: E501
        :type beacon_request_conf: BeaconRequestConfig
        :param channel_load_conf: The channel_load_conf of this MeasurementInfo.  # noqa: E501
        :type channel_load_conf: ChannelLoadConfig
        :param measurement_duration: The measurement_duration of this MeasurementInfo.  # noqa: E501
        :type measurement_duration: int
        :param neighbor_report_conf: The neighbor_report_conf of this MeasurementInfo.  # noqa: E501
        :type neighbor_report_conf: NeighborReportConfig
        :param random_interval: The random_interval of this MeasurementInfo.  # noqa: E501
        :type random_interval: int
        :param sta_statistics_conf: The sta_statistics_conf of this MeasurementInfo.  # noqa: E501
        :type sta_statistics_conf: StaStatisticsConfig
        """
        self.swagger_types = {
            'beacon_request_conf': BeaconRequestConfig,
            'channel_load_conf': ChannelLoadConfig,
            'measurement_duration': int,
            'neighbor_report_conf': NeighborReportConfig,
            'random_interval': int,
            'sta_statistics_conf': StaStatisticsConfig
        }

        self.attribute_map = {
            'beacon_request_conf': 'beaconRequestConf',
            'channel_load_conf': 'channelLoadConf',
            'measurement_duration': 'measurementDuration',
            'neighbor_report_conf': 'neighborReportConf',
            'random_interval': 'randomInterval',
            'sta_statistics_conf': 'staStatisticsConf'
        }
        self._beacon_request_conf = beacon_request_conf
        self._channel_load_conf = channel_load_conf
        self._measurement_duration = measurement_duration
        self._neighbor_report_conf = neighbor_report_conf
        self._random_interval = random_interval
        self._sta_statistics_conf = sta_statistics_conf

    @classmethod
    def from_dict(cls, dikt) -> 'MeasurementInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The MeasurementInfo of this MeasurementInfo.  # noqa: E501
        :rtype: MeasurementInfo
        """
        return util.deserialize_model(dikt, cls)

    @property
    def beacon_request_conf(self) -> BeaconRequestConfig:
        """Gets the beacon_request_conf of this MeasurementInfo.


        :return: The beacon_request_conf of this MeasurementInfo.
        :rtype: BeaconRequestConfig
        """
        return self._beacon_request_conf

    @beacon_request_conf.setter
    def beacon_request_conf(self, beacon_request_conf: BeaconRequestConfig):
        """Sets the beacon_request_conf of this MeasurementInfo.


        :param beacon_request_conf: The beacon_request_conf of this MeasurementInfo.
        :type beacon_request_conf: BeaconRequestConfig
        """

        self._beacon_request_conf = beacon_request_conf

    @property
    def channel_load_conf(self) -> ChannelLoadConfig:
        """Gets the channel_load_conf of this MeasurementInfo.


        :return: The channel_load_conf of this MeasurementInfo.
        :rtype: ChannelLoadConfig
        """
        return self._channel_load_conf

    @channel_load_conf.setter
    def channel_load_conf(self, channel_load_conf: ChannelLoadConfig):
        """Sets the channel_load_conf of this MeasurementInfo.


        :param channel_load_conf: The channel_load_conf of this MeasurementInfo.
        :type channel_load_conf: ChannelLoadConfig
        """

        self._channel_load_conf = channel_load_conf

    @property
    def measurement_duration(self) -> int:
        """Gets the measurement_duration of this MeasurementInfo.

        Duration of the measurement in Time Units (TUs) of 1??024 ??s, as defined in section 11.11.4 of IEEE??802.11-2016 [8]. If not provided, the underlying system may utilize a default configuration that will be indicated in resulting measurement reports.  # noqa: E501

        :return: The measurement_duration of this MeasurementInfo.
        :rtype: int
        """
        return self._measurement_duration

    @measurement_duration.setter
    def measurement_duration(self, measurement_duration: int):
        """Sets the measurement_duration of this MeasurementInfo.

        Duration of the measurement in Time Units (TUs) of 1??024 ??s, as defined in section 11.11.4 of IEEE??802.11-2016 [8]. If not provided, the underlying system may utilize a default configuration that will be indicated in resulting measurement reports.  # noqa: E501

        :param measurement_duration: The measurement_duration of this MeasurementInfo.
        :type measurement_duration: int
        """

        self._measurement_duration = measurement_duration

    @property
    def neighbor_report_conf(self) -> NeighborReportConfig:
        """Gets the neighbor_report_conf of this MeasurementInfo.


        :return: The neighbor_report_conf of this MeasurementInfo.
        :rtype: NeighborReportConfig
        """
        return self._neighbor_report_conf

    @neighbor_report_conf.setter
    def neighbor_report_conf(self, neighbor_report_conf: NeighborReportConfig):
        """Sets the neighbor_report_conf of this MeasurementInfo.


        :param neighbor_report_conf: The neighbor_report_conf of this MeasurementInfo.
        :type neighbor_report_conf: NeighborReportConfig
        """

        self._neighbor_report_conf = neighbor_report_conf

    @property
    def random_interval(self) -> int:
        """Gets the random_interval of this MeasurementInfo.

        Random interval to be used for starting the measurement in TUs of 1??024 ??s, as specified in section??11.11.3 of IEEE 802.11-2016 [8]. If not provided, the underlying system may utilize a default configuration that will be indicated in resulting measurement reports.  # noqa: E501

        :return: The random_interval of this MeasurementInfo.
        :rtype: int
        """
        return self._random_interval

    @random_interval.setter
    def random_interval(self, random_interval: int):
        """Sets the random_interval of this MeasurementInfo.

        Random interval to be used for starting the measurement in TUs of 1??024 ??s, as specified in section??11.11.3 of IEEE 802.11-2016 [8]. If not provided, the underlying system may utilize a default configuration that will be indicated in resulting measurement reports.  # noqa: E501

        :param random_interval: The random_interval of this MeasurementInfo.
        :type random_interval: int
        """

        self._random_interval = random_interval

    @property
    def sta_statistics_conf(self) -> StaStatisticsConfig:
        """Gets the sta_statistics_conf of this MeasurementInfo.


        :return: The sta_statistics_conf of this MeasurementInfo.
        :rtype: StaStatisticsConfig
        """
        return self._sta_statistics_conf

    @sta_statistics_conf.setter
    def sta_statistics_conf(self, sta_statistics_conf: StaStatisticsConfig):
        """Sets the sta_statistics_conf of this MeasurementInfo.


        :param sta_statistics_conf: The sta_statistics_conf of this MeasurementInfo.
        :type sta_statistics_conf: StaStatisticsConfig
        """

        self._sta_statistics_conf = sta_statistics_conf
