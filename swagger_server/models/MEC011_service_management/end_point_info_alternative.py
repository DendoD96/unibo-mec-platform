# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class EndPointInfoAlternative(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, alternative: object=None):  # noqa: E501
        """EndPointInfoAlternative - a model defined in Swagger

        :param alternative: The alternative of this EndPointInfoAlternative.  # noqa: E501
        :type alternative: object
        """
        self.swagger_types = {
            'alternative': object
        }

        self.attribute_map = {
            'alternative': 'alternative'
        }
        self._alternative = alternative

    @classmethod
    def from_dict(cls, dikt) -> 'EndPointInfoAlternative':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The EndPointInfo.Alternative of this EndPointInfoAlternative.  # noqa: E501
        :rtype: EndPointInfoAlternative
        """
        return util.deserialize_model(dikt, cls)

    @property
    def alternative(self) -> object:
        """Gets the alternative of this EndPointInfoAlternative.


        :return: The alternative of this EndPointInfoAlternative.
        :rtype: object
        """
        return self._alternative

    @alternative.setter
    def alternative(self, alternative: object):
        """Sets the alternative of this EndPointInfoAlternative.


        :param alternative: The alternative of this EndPointInfoAlternative.
        :type alternative: object
        """
        if alternative is None:
            raise ValueError("Invalid value for `alternative`, must not be `None`")  # noqa: E501

        self._alternative = alternative
