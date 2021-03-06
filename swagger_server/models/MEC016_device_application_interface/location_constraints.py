# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.MEC016_device_application_interface.location_constraints_civic_address_element import LocationConstraintsCivicAddressElement  # noqa: F401,E501
from swagger_server.models.MEC016_device_application_interface.polygon import Polygon  # noqa: F401,E501
from swagger_server import util


class LocationConstraints(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, area: Polygon=None, civic_address_element: List[LocationConstraintsCivicAddressElement]=None, country_code: str=None):  # noqa: E501
        """LocationConstraints - a model defined in Swagger

        :param area: The area of this LocationConstraints.  # noqa: E501
        :type area: Polygon
        :param civic_address_element: The civic_address_element of this LocationConstraints.  # noqa: E501
        :type civic_address_element: List[LocationConstraintsCivicAddressElement]
        :param country_code: The country_code of this LocationConstraints.  # noqa: E501
        :type country_code: str
        """
        self.swagger_types = {
            'area': Polygon,
            'civic_address_element': List[LocationConstraintsCivicAddressElement],
            'country_code': str
        }

        self.attribute_map = {
            'area': 'area',
            'civic_address_element': 'civicAddressElement',
            'country_code': 'countryCode'
        }
        self._area = area
        self._civic_address_element = civic_address_element
        self._country_code = country_code

    @classmethod
    def from_dict(cls, dikt) -> 'LocationConstraints':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The LocationConstraints of this LocationConstraints.  # noqa: E501
        :rtype: LocationConstraints
        """
        return util.deserialize_model(dikt, cls)

    @property
    def area(self) -> Polygon:
        """Gets the area of this LocationConstraints.


        :return: The area of this LocationConstraints.
        :rtype: Polygon
        """
        return self._area

    @area.setter
    def area(self, area: Polygon):
        """Sets the area of this LocationConstraints.


        :param area: The area of this LocationConstraints.
        :type area: Polygon
        """

        self._area = area

    @property
    def civic_address_element(self) -> List[LocationConstraintsCivicAddressElement]:
        """Gets the civic_address_element of this LocationConstraints.

        Zero or more elements comprising the civic address. Shall be absent if the \"area\" attribute is present.  # noqa: E501

        :return: The civic_address_element of this LocationConstraints.
        :rtype: List[LocationConstraintsCivicAddressElement]
        """
        return self._civic_address_element

    @civic_address_element.setter
    def civic_address_element(self, civic_address_element: List[LocationConstraintsCivicAddressElement]):
        """Sets the civic_address_element of this LocationConstraints.

        Zero or more elements comprising the civic address. Shall be absent if the \"area\" attribute is present.  # noqa: E501

        :param civic_address_element: The civic_address_element of this LocationConstraints.
        :type civic_address_element: List[LocationConstraintsCivicAddressElement]
        """

        self._civic_address_element = civic_address_element

    @property
    def country_code(self) -> str:
        """Gets the country_code of this LocationConstraints.

        The two-letter ISO 3166 [7] country code in capital letters. Shall be present in case the \"area\" attribute is absent. May be absent if the \"area\" attribute is present (see note).  # noqa: E501

        :return: The country_code of this LocationConstraints.
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code: str):
        """Sets the country_code of this LocationConstraints.

        The two-letter ISO 3166 [7] country code in capital letters. Shall be present in case the \"area\" attribute is absent. May be absent if the \"area\" attribute is present (see note).  # noqa: E501

        :param country_code: The country_code of this LocationConstraints.
        :type country_code: str
        """

        self._country_code = country_code
