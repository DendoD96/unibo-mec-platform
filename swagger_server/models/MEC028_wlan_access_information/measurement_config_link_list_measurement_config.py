# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class MeasurementConfigLinkListMeasurementConfig(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, href: str=None, measurement_id: str=None):  # noqa: E501
        """MeasurementConfigLinkListMeasurementConfig - a model defined in Swagger

        :param href: The href of this MeasurementConfigLinkListMeasurementConfig.  # noqa: E501
        :type href: str
        :param measurement_id: The measurement_id of this MeasurementConfigLinkListMeasurementConfig.  # noqa: E501
        :type measurement_id: str
        """
        self.swagger_types = {
            'href': str,
            'measurement_id': str
        }

        self.attribute_map = {
            'href': 'href',
            'measurement_id': 'measurementId'
        }
        self._href = href
        self._measurement_id = measurement_id

    @classmethod
    def from_dict(cls, dikt) -> 'MeasurementConfigLinkListMeasurementConfig':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The MeasurementConfigLinkList_measurementConfig of this MeasurementConfigLinkListMeasurementConfig.  # noqa: E501
        :rtype: MeasurementConfigLinkListMeasurementConfig
        """
        return util.deserialize_model(dikt, cls)

    @property
    def href(self) -> str:
        """Gets the href of this MeasurementConfigLinkListMeasurementConfig.

        The URI referring to a measurement configuration.  # noqa: E501

        :return: The href of this MeasurementConfigLinkListMeasurementConfig.
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href: str):
        """Sets the href of this MeasurementConfigLinkListMeasurementConfig.

        The URI referring to a measurement configuration.  # noqa: E501

        :param href: The href of this MeasurementConfigLinkListMeasurementConfig.
        :type href: str
        """
        if href is None:
            raise ValueError("Invalid value for `href`, must not be `None`")  # noqa: E501

        self._href = href

    @property
    def measurement_id(self) -> str:
        """Gets the measurement_id of this MeasurementConfigLinkListMeasurementConfig.

        Unique identifier allocated by the service consumer to identify measurement reports associated with this measurement configuration.  # noqa: E501

        :return: The measurement_id of this MeasurementConfigLinkListMeasurementConfig.
        :rtype: str
        """
        return self._measurement_id

    @measurement_id.setter
    def measurement_id(self, measurement_id: str):
        """Sets the measurement_id of this MeasurementConfigLinkListMeasurementConfig.

        Unique identifier allocated by the service consumer to identify measurement reports associated with this measurement configuration.  # noqa: E501

        :param measurement_id: The measurement_id of this MeasurementConfigLinkListMeasurementConfig.
        :type measurement_id: str
        """
        if measurement_id is None:
            raise ValueError("Invalid value for `measurement_id`, must not be `None`")  # noqa: E501

        self._measurement_id = measurement_id
