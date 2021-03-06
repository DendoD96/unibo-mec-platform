# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.MEC029_fixed_access_information.link_type import LinkType  # noqa: F401,E501
from swagger_server import util


class CmConnSubscriptionLinks(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, _self: LinkType=None):  # noqa: E501
        """CmConnSubscriptionLinks - a model defined in Swagger

        :param _self: The _self of this CmConnSubscriptionLinks.  # noqa: E501
        :type _self: LinkType
        """
        self.swagger_types = {
            '_self': LinkType
        }

        self.attribute_map = {
            '_self': 'self'
        }
        self.__self = _self

    @classmethod
    def from_dict(cls, dikt) -> 'CmConnSubscriptionLinks':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The CmConnSubscription.links of this CmConnSubscriptionLinks.  # noqa: E501
        :rtype: CmConnSubscriptionLinks
        """
        return util.deserialize_model(dikt, cls)

    @property
    def _self(self) -> LinkType:
        """Gets the _self of this CmConnSubscriptionLinks.


        :return: The _self of this CmConnSubscriptionLinks.
        :rtype: LinkType
        """
        return self.__self

    @_self.setter
    def _self(self, _self: LinkType):
        """Sets the _self of this CmConnSubscriptionLinks.


        :param _self: The _self of this CmConnSubscriptionLinks.
        :type _self: LinkType
        """
        if _self is None:
            raise ValueError("Invalid value for `_self`, must not be `None`")  # noqa: E501

        self.__self = _self
