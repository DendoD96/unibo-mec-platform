# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.MEC011_service_management.category_ref_href import CategoryRefHref  # noqa: F401,E501
from swagger_server.models.MEC011_service_management.category_ref_id import CategoryRefId  # noqa: F401,E501
from swagger_server.models.MEC011_service_management.category_ref_name import CategoryRefName  # noqa: F401,E501
from swagger_server.models.MEC011_service_management.category_ref_version import CategoryRefVersion  # noqa: F401,E501
from swagger_server import util


class CategoryRef(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, href: CategoryRefHref=None, id: CategoryRefId=None, name: CategoryRefName=None, version: CategoryRefVersion=None):  # noqa: E501
        """CategoryRef - a model defined in Swagger

        :param href: The href of this CategoryRef.  # noqa: E501
        :type href: CategoryRefHref
        :param id: The id of this CategoryRef.  # noqa: E501
        :type id: CategoryRefId
        :param name: The name of this CategoryRef.  # noqa: E501
        :type name: CategoryRefName
        :param version: The version of this CategoryRef.  # noqa: E501
        :type version: CategoryRefVersion
        """
        self.swagger_types = {
            'href': CategoryRefHref,
            'id': CategoryRefId,
            'name': CategoryRefName,
            'version': CategoryRefVersion
        }

        self.attribute_map = {
            'href': 'href',
            'id': 'id',
            'name': 'name',
            'version': 'version'
        }
        self._href = href
        self._id = id
        self._name = name
        self._version = version

    @classmethod
    def from_dict(cls, dikt) -> 'CategoryRef':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The CategoryRef of this CategoryRef.  # noqa: E501
        :rtype: CategoryRef
        """
        return util.deserialize_model(dikt, cls)

    @property
    def href(self) -> CategoryRefHref:
        """Gets the href of this CategoryRef.


        :return: The href of this CategoryRef.
        :rtype: CategoryRefHref
        """
        return self._href

    @href.setter
    def href(self, href: CategoryRefHref):
        """Sets the href of this CategoryRef.


        :param href: The href of this CategoryRef.
        :type href: CategoryRefHref
        """
        if href is None:
            raise ValueError("Invalid value for `href`, must not be `None`")  # noqa: E501

        self._href = href

    @property
    def id(self) -> CategoryRefId:
        """Gets the id of this CategoryRef.


        :return: The id of this CategoryRef.
        :rtype: CategoryRefId
        """
        return self._id

    @id.setter
    def id(self, id: CategoryRefId):
        """Sets the id of this CategoryRef.


        :param id: The id of this CategoryRef.
        :type id: CategoryRefId
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self) -> CategoryRefName:
        """Gets the name of this CategoryRef.


        :return: The name of this CategoryRef.
        :rtype: CategoryRefName
        """
        return self._name

    @name.setter
    def name(self, name: CategoryRefName):
        """Sets the name of this CategoryRef.


        :param name: The name of this CategoryRef.
        :type name: CategoryRefName
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def version(self) -> CategoryRefVersion:
        """Gets the version of this CategoryRef.


        :return: The version of this CategoryRef.
        :rtype: CategoryRefVersion
        """
        return self._version

    @version.setter
    def version(self, version: CategoryRefVersion):
        """Sets the version of this CategoryRef.


        :param version: The version of this CategoryRef.
        :type version: CategoryRefVersion
        """
        if version is None:
            raise ValueError("Invalid value for `version`, must not be `None`")  # noqa: E501

        self._version = version