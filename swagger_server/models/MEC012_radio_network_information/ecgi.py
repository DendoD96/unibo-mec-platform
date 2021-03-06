# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.MEC012_radio_network_information.cell_id import CellId  # noqa: F401,E501
from swagger_server.models.MEC012_radio_network_information.plmn import Plmn  # noqa: F401,E501
from swagger_server import util


class Ecgi(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, cell_id: CellId=None, plmn: Plmn=None):  # noqa: E501
        """Ecgi - a model defined in Swagger

        :param cell_id: The cell_id of this Ecgi.  # noqa: E501
        :type cell_id: CellId
        :param plmn: The plmn of this Ecgi.  # noqa: E501
        :type plmn: Plmn
        """
        self.swagger_types = {
            'cell_id': CellId,
            'plmn': Plmn
        }

        self.attribute_map = {
            'cell_id': 'cellId',
            'plmn': 'plmn'
        }
        self._cell_id = cell_id
        self._plmn = plmn

    @classmethod
    def from_dict(cls, dikt) -> 'Ecgi':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Ecgi of this Ecgi.  # noqa: E501
        :rtype: Ecgi
        """
        return util.deserialize_model(dikt, cls)

    @property
    def cell_id(self) -> CellId:
        """Gets the cell_id of this Ecgi.


        :return: The cell_id of this Ecgi.
        :rtype: CellId
        """
        return self._cell_id

    @cell_id.setter
    def cell_id(self, cell_id: CellId):
        """Sets the cell_id of this Ecgi.


        :param cell_id: The cell_id of this Ecgi.
        :type cell_id: CellId
        """
        if cell_id is None:
            raise ValueError("Invalid value for `cell_id`, must not be `None`")  # noqa: E501

        self._cell_id = cell_id

    @property
    def plmn(self) -> Plmn:
        """Gets the plmn of this Ecgi.


        :return: The plmn of this Ecgi.
        :rtype: Plmn
        """
        return self._plmn

    @plmn.setter
    def plmn(self, plmn: Plmn):
        """Sets the plmn of this Ecgi.


        :param plmn: The plmn of this Ecgi.
        :type plmn: Plmn
        """
        if plmn is None:
            raise ValueError("Invalid value for `plmn`, must not be `None`")  # noqa: E501

        self._plmn = plmn
