# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.MEC011_service_management.href import Href  # noqa: F401,E501
from swagger_server import util


class LinkType(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, href: Href=None):  # noqa: E501
        """LinkType - a model defined in Swagger

        :param href: The href of this LinkType.  # noqa: E501
        :type href: Href
        """
        self.swagger_types = {
            'href': Href
        }

        self.attribute_map = {
            'href': 'href'
        }
        self._href = href

    @classmethod
    def from_dict(cls, dikt) -> 'LinkType':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The LinkType of this LinkType.  # noqa: E501
        :rtype: LinkType
        """
        return util.deserialize_model(dikt, cls)

    @property
    def href(self) -> Href:
        """Gets the href of this LinkType.


        :return: The href of this LinkType.
        :rtype: Href
        """
        return self._href

    @href.setter
    def href(self, href: Href):
        """Sets the href of this LinkType.


        :param href: The href of this LinkType.
        :type href: Href
        """

        self._href = href
