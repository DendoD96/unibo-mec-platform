# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.MEC012_radio_network_information.meas_rep_ue_notification_nr_bn_cs import MeasRepUeNotificationNrBNCs  # noqa: F401,E501
from swagger_server.models.MEC012_radio_network_information.meas_rep_ue_notification_nr_s_cs import MeasRepUeNotificationNrSCs  # noqa: F401,E501
from swagger_server import util


class MeasRepUeNotificationNewRadioMeasInfo(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, nr_bn_cs: MeasRepUeNotificationNrBNCs=None, nr_carrier_freq: int=None, nr_s_cs: MeasRepUeNotificationNrSCs=None):  # noqa: E501
        """MeasRepUeNotificationNewRadioMeasInfo - a model defined in Swagger

        :param nr_bn_cs: The nr_bn_cs of this MeasRepUeNotificationNewRadioMeasInfo.  # noqa: E501
        :type nr_bn_cs: MeasRepUeNotificationNrBNCs
        :param nr_carrier_freq: The nr_carrier_freq of this MeasRepUeNotificationNewRadioMeasInfo.  # noqa: E501
        :type nr_carrier_freq: int
        :param nr_s_cs: The nr_s_cs of this MeasRepUeNotificationNewRadioMeasInfo.  # noqa: E501
        :type nr_s_cs: MeasRepUeNotificationNrSCs
        """
        self.swagger_types = {
            'nr_bn_cs': MeasRepUeNotificationNrBNCs,
            'nr_carrier_freq': int,
            'nr_s_cs': MeasRepUeNotificationNrSCs
        }

        self.attribute_map = {
            'nr_bn_cs': 'nrBNCs',
            'nr_carrier_freq': 'nrCarrierFreq',
            'nr_s_cs': 'nrSCs'
        }
        self._nr_bn_cs = nr_bn_cs
        self._nr_carrier_freq = nr_carrier_freq
        self._nr_s_cs = nr_s_cs

    @classmethod
    def from_dict(cls, dikt) -> 'MeasRepUeNotificationNewRadioMeasInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The MeasRepUeNotification_newRadioMeasInfo of this MeasRepUeNotificationNewRadioMeasInfo.  # noqa: E501
        :rtype: MeasRepUeNotificationNewRadioMeasInfo
        """
        return util.deserialize_model(dikt, cls)

    @property
    def nr_bn_cs(self) -> MeasRepUeNotificationNrBNCs:
        """Gets the nr_bn_cs of this MeasRepUeNotificationNewRadioMeasInfo.


        :return: The nr_bn_cs of this MeasRepUeNotificationNewRadioMeasInfo.
        :rtype: MeasRepUeNotificationNrBNCs
        """
        return self._nr_bn_cs

    @nr_bn_cs.setter
    def nr_bn_cs(self, nr_bn_cs: MeasRepUeNotificationNrBNCs):
        """Sets the nr_bn_cs of this MeasRepUeNotificationNewRadioMeasInfo.


        :param nr_bn_cs: The nr_bn_cs of this MeasRepUeNotificationNewRadioMeasInfo.
        :type nr_bn_cs: MeasRepUeNotificationNrBNCs
        """

        self._nr_bn_cs = nr_bn_cs

    @property
    def nr_carrier_freq(self) -> int:
        """Gets the nr_carrier_freq of this MeasRepUeNotificationNewRadioMeasInfo.

        ARFCN applicable for a downlink, uplink or bi-directional (TDD) NR carrier frequency, as defined in ETSI TS 138.101 [i.15].  # noqa: E501

        :return: The nr_carrier_freq of this MeasRepUeNotificationNewRadioMeasInfo.
        :rtype: int
        """
        return self._nr_carrier_freq

    @nr_carrier_freq.setter
    def nr_carrier_freq(self, nr_carrier_freq: int):
        """Sets the nr_carrier_freq of this MeasRepUeNotificationNewRadioMeasInfo.

        ARFCN applicable for a downlink, uplink or bi-directional (TDD) NR carrier frequency, as defined in ETSI TS 138.101 [i.15].  # noqa: E501

        :param nr_carrier_freq: The nr_carrier_freq of this MeasRepUeNotificationNewRadioMeasInfo.
        :type nr_carrier_freq: int
        """

        self._nr_carrier_freq = nr_carrier_freq

    @property
    def nr_s_cs(self) -> MeasRepUeNotificationNrSCs:
        """Gets the nr_s_cs of this MeasRepUeNotificationNewRadioMeasInfo.


        :return: The nr_s_cs of this MeasRepUeNotificationNewRadioMeasInfo.
        :rtype: MeasRepUeNotificationNrSCs
        """
        return self._nr_s_cs

    @nr_s_cs.setter
    def nr_s_cs(self, nr_s_cs: MeasRepUeNotificationNrSCs):
        """Sets the nr_s_cs of this MeasRepUeNotificationNewRadioMeasInfo.


        :param nr_s_cs: The nr_s_cs of this MeasRepUeNotificationNewRadioMeasInfo.
        :type nr_s_cs: MeasRepUeNotificationNrSCs
        """

        self._nr_s_cs = nr_s_cs
