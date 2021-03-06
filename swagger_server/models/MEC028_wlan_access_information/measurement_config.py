# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.MEC028_wlan_access_information.measurement_config_links import MeasurementConfigLinks  # noqa: F401,E501
from swagger_server.models.MEC028_wlan_access_information.measurement_info import MeasurementInfo  # noqa: F401,E501
from swagger_server.models.MEC028_wlan_access_information.sta_identity import StaIdentity  # noqa: F401,E501
from swagger_server import util


class MeasurementConfig(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, links: MeasurementConfigLinks=None, measurement_id: str=None, measurement_info: MeasurementInfo=None, sta_id: List[StaIdentity]=None):  # noqa: E501
        """MeasurementConfig - a model defined in Swagger

        :param links: The links of this MeasurementConfig.  # noqa: E501
        :type links: MeasurementConfigLinks
        :param measurement_id: The measurement_id of this MeasurementConfig.  # noqa: E501
        :type measurement_id: str
        :param measurement_info: The measurement_info of this MeasurementConfig.  # noqa: E501
        :type measurement_info: MeasurementInfo
        :param sta_id: The sta_id of this MeasurementConfig.  # noqa: E501
        :type sta_id: List[StaIdentity]
        """
        self.swagger_types = {
            'links': MeasurementConfigLinks,
            'measurement_id': str,
            'measurement_info': MeasurementInfo,
            'sta_id': List[StaIdentity]
        }

        self.attribute_map = {
            'links': '_links',
            'measurement_id': 'measurementId',
            'measurement_info': 'measurementInfo',
            'sta_id': 'staId'
        }
        self._links = links
        self._measurement_id = measurement_id
        self._measurement_info = measurement_info
        self._sta_id = sta_id

    @classmethod
    def from_dict(cls, dikt) -> 'MeasurementConfig':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The MeasurementConfig of this MeasurementConfig.  # noqa: E501
        :rtype: MeasurementConfig
        """
        return util.deserialize_model(dikt, cls)

    @property
    def links(self) -> MeasurementConfigLinks:
        """Gets the links of this MeasurementConfig.


        :return: The links of this MeasurementConfig.
        :rtype: MeasurementConfigLinks
        """
        return self._links

    @links.setter
    def links(self, links: MeasurementConfigLinks):
        """Sets the links of this MeasurementConfig.


        :param links: The links of this MeasurementConfig.
        :type links: MeasurementConfigLinks
        """

        self._links = links

    @property
    def measurement_id(self) -> str:
        """Gets the measurement_id of this MeasurementConfig.

        Unique identifier allocated by the service consumer to identify measurement reports (within sta_information query), associated with this measurement configuration.  # noqa: E501

        :return: The measurement_id of this MeasurementConfig.
        :rtype: str
        """
        return self._measurement_id

    @measurement_id.setter
    def measurement_id(self, measurement_id: str):
        """Sets the measurement_id of this MeasurementConfig.

        Unique identifier allocated by the service consumer to identify measurement reports (within sta_information query), associated with this measurement configuration.  # noqa: E501

        :param measurement_id: The measurement_id of this MeasurementConfig.
        :type measurement_id: str
        """
        if measurement_id is None:
            raise ValueError("Invalid value for `measurement_id`, must not be `None`")  # noqa: E501

        self._measurement_id = measurement_id

    @property
    def measurement_info(self) -> MeasurementInfo:
        """Gets the measurement_info of this MeasurementConfig.


        :return: The measurement_info of this MeasurementConfig.
        :rtype: MeasurementInfo
        """
        return self._measurement_info

    @measurement_info.setter
    def measurement_info(self, measurement_info: MeasurementInfo):
        """Sets the measurement_info of this MeasurementConfig.


        :param measurement_info: The measurement_info of this MeasurementConfig.
        :type measurement_info: MeasurementInfo
        """
        if measurement_info is None:
            raise ValueError("Invalid value for `measurement_info`, must not be `None`")  # noqa: E501

        self._measurement_info = measurement_info

    @property
    def sta_id(self) -> List[StaIdentity]:
        """Gets the sta_id of this MeasurementConfig.

        Identifier(s) to uniquely specify the target client station(s) for the measurement configuration.  # noqa: E501

        :return: The sta_id of this MeasurementConfig.
        :rtype: List[StaIdentity]
        """
        return self._sta_id

    @sta_id.setter
    def sta_id(self, sta_id: List[StaIdentity]):
        """Sets the sta_id of this MeasurementConfig.

        Identifier(s) to uniquely specify the target client station(s) for the measurement configuration.  # noqa: E501

        :param sta_id: The sta_id of this MeasurementConfig.
        :type sta_id: List[StaIdentity]
        """
        if sta_id is None:
            raise ValueError("Invalid value for `sta_id`, must not be `None`")  # noqa: E501

        self._sta_id = sta_id
