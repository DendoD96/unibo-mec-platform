# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Polygon(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, coordinates: List[List[List[float]]]=None):  # noqa: E501
        """Polygon - a model defined in Swagger

        :param coordinates: The coordinates of this Polygon.  # noqa: E501
        :type coordinates: List[List[List[float]]]
        """
        self.swagger_types = {
            'coordinates': List[List[List[float]]]
        }

        self.attribute_map = {
            'coordinates': 'coordinates'
        }
        self._coordinates = coordinates

    @classmethod
    def from_dict(cls, dikt) -> 'Polygon':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Polygon of this Polygon.  # noqa: E501
        :rtype: Polygon
        """
        return util.deserialize_model(dikt, cls)

    @property
    def coordinates(self) -> List[List[List[float]]]:
        """Gets the coordinates of this Polygon.


        :return: The coordinates of this Polygon.
        :rtype: List[List[List[float]]]
        """
        return self._coordinates

    @coordinates.setter
    def coordinates(self, coordinates: List[List[List[float]]]):
        """Sets the coordinates of this Polygon.


        :param coordinates: The coordinates of this Polygon.
        :type coordinates: List[List[List[float]]]
        """

        self._coordinates = coordinates
