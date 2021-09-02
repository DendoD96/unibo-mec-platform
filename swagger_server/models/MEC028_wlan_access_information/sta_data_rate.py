# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.MEC028_wlan_access_information.sta_identity import StaIdentity  # noqa: F401,E501
from swagger_server import util


class StaDataRate(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, sta_id: StaIdentity=None, sta_last_data_downlink_rate: int=None, sta_last_data_uplink_rate: int=None):  # noqa: E501
        """StaDataRate - a model defined in Swagger

        :param sta_id: The sta_id of this StaDataRate.  # noqa: E501
        :type sta_id: StaIdentity
        :param sta_last_data_downlink_rate: The sta_last_data_downlink_rate of this StaDataRate.  # noqa: E501
        :type sta_last_data_downlink_rate: int
        :param sta_last_data_uplink_rate: The sta_last_data_uplink_rate of this StaDataRate.  # noqa: E501
        :type sta_last_data_uplink_rate: int
        """
        self.swagger_types = {
            'sta_id': StaIdentity,
            'sta_last_data_downlink_rate': int,
            'sta_last_data_uplink_rate': int
        }

        self.attribute_map = {
            'sta_id': 'staId',
            'sta_last_data_downlink_rate': 'staLastDataDownlinkRate',
            'sta_last_data_uplink_rate': 'staLastDataUplinkRate'
        }
        self._sta_id = sta_id
        self._sta_last_data_downlink_rate = sta_last_data_downlink_rate
        self._sta_last_data_uplink_rate = sta_last_data_uplink_rate

    @classmethod
    def from_dict(cls, dikt) -> 'StaDataRate':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The StaDataRate of this StaDataRate.  # noqa: E501
        :rtype: StaDataRate
        """
        return util.deserialize_model(dikt, cls)

    @property
    def sta_id(self) -> StaIdentity:
        """Gets the sta_id of this StaDataRate.


        :return: The sta_id of this StaDataRate.
        :rtype: StaIdentity
        """
        return self._sta_id

    @sta_id.setter
    def sta_id(self, sta_id: StaIdentity):
        """Sets the sta_id of this StaDataRate.


        :param sta_id: The sta_id of this StaDataRate.
        :type sta_id: StaIdentity
        """

        self._sta_id = sta_id

    @property
    def sta_last_data_downlink_rate(self) -> int:
        """Gets the sta_last_data_downlink_rate of this StaDataRate.

        The data transmit rate in kbps that was most recently used for transmission of data PPDUs from the access point to the station.  # noqa: E501

        :return: The sta_last_data_downlink_rate of this StaDataRate.
        :rtype: int
        """
        return self._sta_last_data_downlink_rate

    @sta_last_data_downlink_rate.setter
    def sta_last_data_downlink_rate(self, sta_last_data_downlink_rate: int):
        """Sets the sta_last_data_downlink_rate of this StaDataRate.

        The data transmit rate in kbps that was most recently used for transmission of data PPDUs from the access point to the station.  # noqa: E501

        :param sta_last_data_downlink_rate: The sta_last_data_downlink_rate of this StaDataRate.
        :type sta_last_data_downlink_rate: int
        """

        self._sta_last_data_downlink_rate = sta_last_data_downlink_rate

    @property
    def sta_last_data_uplink_rate(self) -> int:
        """Gets the sta_last_data_uplink_rate of this StaDataRate.

        The data transmit rate in Kbps that was most recently used for transmission of data PPDUs from the associated station to the access point.  # noqa: E501

        :return: The sta_last_data_uplink_rate of this StaDataRate.
        :rtype: int
        """
        return self._sta_last_data_uplink_rate

    @sta_last_data_uplink_rate.setter
    def sta_last_data_uplink_rate(self, sta_last_data_uplink_rate: int):
        """Sets the sta_last_data_uplink_rate of this StaDataRate.

        The data transmit rate in Kbps that was most recently used for transmission of data PPDUs from the associated station to the access point.  # noqa: E501

        :param sta_last_data_uplink_rate: The sta_last_data_uplink_rate of this StaDataRate.
        :type sta_last_data_uplink_rate: int
        """

        self._sta_last_data_uplink_rate = sta_last_data_uplink_rate