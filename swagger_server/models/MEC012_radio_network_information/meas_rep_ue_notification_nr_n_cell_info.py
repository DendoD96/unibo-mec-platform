# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.MEC012_radio_network_information.nr_cell_id import NrCellId  # noqa: F401,E501
from swagger_server.models.MEC012_radio_network_information.plmn import Plmn  # noqa: F401,E501
from swagger_server import util


class MeasRepUeNotificationNrNCellInfo(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, nr_n_cell_g_id: NrCellId=None, nr_n_cell_plmn: List[Plmn]=None):  # noqa: E501
        """MeasRepUeNotificationNrNCellInfo - a model defined in Swagger

        :param nr_n_cell_g_id: The nr_n_cell_g_id of this MeasRepUeNotificationNrNCellInfo.  # noqa: E501
        :type nr_n_cell_g_id: NrCellId
        :param nr_n_cell_plmn: The nr_n_cell_plmn of this MeasRepUeNotificationNrNCellInfo.  # noqa: E501
        :type nr_n_cell_plmn: List[Plmn]
        """
        self.swagger_types = {
            'nr_n_cell_g_id': NrCellId,
            'nr_n_cell_plmn': List[Plmn]
        }

        self.attribute_map = {
            'nr_n_cell_g_id': 'nrNCellGId',
            'nr_n_cell_plmn': 'nrNCellPlmn'
        }
        self._nr_n_cell_g_id = nr_n_cell_g_id
        self._nr_n_cell_plmn = nr_n_cell_plmn

    @classmethod
    def from_dict(cls, dikt) -> 'MeasRepUeNotificationNrNCellInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The MeasRepUeNotification_nrNCellInfo of this MeasRepUeNotificationNrNCellInfo.  # noqa: E501
        :rtype: MeasRepUeNotificationNrNCellInfo
        """
        return util.deserialize_model(dikt, cls)

    @property
    def nr_n_cell_g_id(self) -> NrCellId:
        """Gets the nr_n_cell_g_id of this MeasRepUeNotificationNrNCellInfo.


        :return: The nr_n_cell_g_id of this MeasRepUeNotificationNrNCellInfo.
        :rtype: NrCellId
        """
        return self._nr_n_cell_g_id

    @nr_n_cell_g_id.setter
    def nr_n_cell_g_id(self, nr_n_cell_g_id: NrCellId):
        """Sets the nr_n_cell_g_id of this MeasRepUeNotificationNrNCellInfo.


        :param nr_n_cell_g_id: The nr_n_cell_g_id of this MeasRepUeNotificationNrNCellInfo.
        :type nr_n_cell_g_id: NrCellId
        """

        self._nr_n_cell_g_id = nr_n_cell_g_id

    @property
    def nr_n_cell_plmn(self) -> List[Plmn]:
        """Gets the nr_n_cell_plmn of this MeasRepUeNotificationNrNCellInfo.

        Public land mobile network identities.  # noqa: E501

        :return: The nr_n_cell_plmn of this MeasRepUeNotificationNrNCellInfo.
        :rtype: List[Plmn]
        """
        return self._nr_n_cell_plmn

    @nr_n_cell_plmn.setter
    def nr_n_cell_plmn(self, nr_n_cell_plmn: List[Plmn]):
        """Sets the nr_n_cell_plmn of this MeasRepUeNotificationNrNCellInfo.

        Public land mobile network identities.  # noqa: E501

        :param nr_n_cell_plmn: The nr_n_cell_plmn of this MeasRepUeNotificationNrNCellInfo.
        :type nr_n_cell_plmn: List[Plmn]
        """

        self._nr_n_cell_plmn = nr_n_cell_plmn
