# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class ReportedBeaconFrameInfo(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, frame_type: int=None, phy_type: int=None):  # noqa: E501
        """ReportedBeaconFrameInfo - a model defined in Swagger

        :param frame_type: The frame_type of this ReportedBeaconFrameInfo.  # noqa: E501
        :type frame_type: int
        :param phy_type: The phy_type of this ReportedBeaconFrameInfo.  # noqa: E501
        :type phy_type: int
        """
        self.swagger_types = {
            'frame_type': int,
            'phy_type': int
        }

        self.attribute_map = {
            'frame_type': 'frameType',
            'phy_type': 'phyType'
        }
        self._frame_type = frame_type
        self._phy_type = phy_type

    @classmethod
    def from_dict(cls, dikt) -> 'ReportedBeaconFrameInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ReportedBeaconFrameInfo of this ReportedBeaconFrameInfo.  # noqa: E501
        :rtype: ReportedBeaconFrameInfo
        """
        return util.deserialize_model(dikt, cls)

    @property
    def frame_type(self) -> int:
        """Gets the frame_type of this ReportedBeaconFrameInfo.

        A value of 0 indicates a Beacon or Probe Response. A value of 1 indicates a Measurement Pilot frame.  # noqa: E501

        :return: The frame_type of this ReportedBeaconFrameInfo.
        :rtype: int
        """
        return self._frame_type

    @frame_type.setter
    def frame_type(self, frame_type: int):
        """Sets the frame_type of this ReportedBeaconFrameInfo.

        A value of 0 indicates a Beacon or Probe Response. A value of 1 indicates a Measurement Pilot frame.  # noqa: E501

        :param frame_type: The frame_type of this ReportedBeaconFrameInfo.
        :type frame_type: int
        """
        if frame_type is None:
            raise ValueError("Invalid value for `frame_type`, must not be `None`")  # noqa: E501

        self._frame_type = frame_type

    @property
    def phy_type(self) -> int:
        """Gets the phy_type of this ReportedBeaconFrameInfo.

        Value between 0 and 127 coded according to dot11PHYType.  # noqa: E501

        :return: The phy_type of this ReportedBeaconFrameInfo.
        :rtype: int
        """
        return self._phy_type

    @phy_type.setter
    def phy_type(self, phy_type: int):
        """Sets the phy_type of this ReportedBeaconFrameInfo.

        Value between 0 and 127 coded according to dot11PHYType.  # noqa: E501

        :param phy_type: The phy_type of this ReportedBeaconFrameInfo.
        :type phy_type: int
        """
        if phy_type is None:
            raise ValueError("Invalid value for `phy_type`, must not be `None`")  # noqa: E501

        self._phy_type = phy_type
