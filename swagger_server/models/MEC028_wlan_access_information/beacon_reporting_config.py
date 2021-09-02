# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class BeaconReportingConfig(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, reporting_condition: int=None, threshold: int=None):  # noqa: E501
        """BeaconReportingConfig - a model defined in Swagger

        :param reporting_condition: The reporting_condition of this BeaconReportingConfig.  # noqa: E501
        :type reporting_condition: int
        :param threshold: The threshold of this BeaconReportingConfig.  # noqa: E501
        :type threshold: int
        """
        self.swagger_types = {
            'reporting_condition': int,
            'threshold': int
        }

        self.attribute_map = {
            'reporting_condition': 'reportingCondition',
            'threshold': 'threshold'
        }
        self._reporting_condition = reporting_condition
        self._threshold = threshold

    @classmethod
    def from_dict(cls, dikt) -> 'BeaconReportingConfig':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The BeaconReportingConfig of this BeaconReportingConfig.  # noqa: E501
        :rtype: BeaconReportingConfig
        """
        return util.deserialize_model(dikt, cls)

    @property
    def reporting_condition(self) -> int:
        """Gets the reporting_condition of this BeaconReportingConfig.

        Reporting condition for the Beacon Report as per Table 9-89 of IEEE 802.11-2016 [8]: 0 = Report to be issued after each measurement. 1 = measured RCPI level is greater than the threshold. 2 = measured RCPI level is less than the threshold. 3 = measured RSNI level is greater than the threshold. 4 = measured RSNI level is less than the threshold. 5 = measured RCPI level is greater than a threshold defined by an offset from the serving AP's reference RCPI. 6 = measured RCPI level is less than a threshold defined by an offset from the serving AP's reference RCPI. 7 = measured RSNI level is greater than a threshold defined by an offset from the serving AP's reference RSNI. 8 = measured RSNI level is less than a threshold defined by an offset from the serving AP's reference RSNI. 9 = measured RCPI level is in a range bound by the serving AP's reference RCPI and an offset from the serving AP's reference RCPI. 10 = measured RSNI level is in a range bound by the serving AP's reference RSNI and an offset from the serving AP's reference RSNI.  # noqa: E501

        :return: The reporting_condition of this BeaconReportingConfig.
        :rtype: int
        """
        return self._reporting_condition

    @reporting_condition.setter
    def reporting_condition(self, reporting_condition: int):
        """Sets the reporting_condition of this BeaconReportingConfig.

        Reporting condition for the Beacon Report as per Table 9-89 of IEEE 802.11-2016 [8]: 0 = Report to be issued after each measurement. 1 = measured RCPI level is greater than the threshold. 2 = measured RCPI level is less than the threshold. 3 = measured RSNI level is greater than the threshold. 4 = measured RSNI level is less than the threshold. 5 = measured RCPI level is greater than a threshold defined by an offset from the serving AP's reference RCPI. 6 = measured RCPI level is less than a threshold defined by an offset from the serving AP's reference RCPI. 7 = measured RSNI level is greater than a threshold defined by an offset from the serving AP's reference RSNI. 8 = measured RSNI level is less than a threshold defined by an offset from the serving AP's reference RSNI. 9 = measured RCPI level is in a range bound by the serving AP's reference RCPI and an offset from the serving AP's reference RCPI. 10 = measured RSNI level is in a range bound by the serving AP's reference RSNI and an offset from the serving AP's reference RSNI.  # noqa: E501

        :param reporting_condition: The reporting_condition of this BeaconReportingConfig.
        :type reporting_condition: int
        """
        if reporting_condition is None:
            raise ValueError("Invalid value for `reporting_condition`, must not be `None`")  # noqa: E501

        self._reporting_condition = reporting_condition

    @property
    def threshold(self) -> int:
        """Gets the threshold of this BeaconReportingConfig.

        The threshold subfield contains either the threshold value or the offset value to be used for conditional reporting.  For reportingCondition subfield with values 1 and 2, the threshold value is a logarithmic function of the received signal power, as defined in section 9.4.2.38 of IEEE 802.11-2016 [8].  For reportingCondition subfield values 3 and 4, the threshold value is a logarithmic function of the signal-to-noise ratio, as described in section 9.4.2.41 of IEEE 802.11-2016 [8].  For reportingCondition subfield values 5 to 10, the offset value is an 8-bit 2s complement integer in units of 0,5 dBm. The indicated reporting condition applies individually to each measured Beacon, Measurement Pilot, or Probe Response frame.  # noqa: E501

        :return: The threshold of this BeaconReportingConfig.
        :rtype: int
        """
        return self._threshold

    @threshold.setter
    def threshold(self, threshold: int):
        """Sets the threshold of this BeaconReportingConfig.

        The threshold subfield contains either the threshold value or the offset value to be used for conditional reporting.  For reportingCondition subfield with values 1 and 2, the threshold value is a logarithmic function of the received signal power, as defined in section 9.4.2.38 of IEEE 802.11-2016 [8].  For reportingCondition subfield values 3 and 4, the threshold value is a logarithmic function of the signal-to-noise ratio, as described in section 9.4.2.41 of IEEE 802.11-2016 [8].  For reportingCondition subfield values 5 to 10, the offset value is an 8-bit 2s complement integer in units of 0,5 dBm. The indicated reporting condition applies individually to each measured Beacon, Measurement Pilot, or Probe Response frame.  # noqa: E501

        :param threshold: The threshold of this BeaconReportingConfig.
        :type threshold: int
        """
        if threshold is None:
            raise ValueError("Invalid value for `threshold`, must not be `None`")  # noqa: E501

        self._threshold = threshold
