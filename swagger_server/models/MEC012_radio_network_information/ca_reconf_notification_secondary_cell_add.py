# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.MEC012_radio_network_information.ecgi import Ecgi  # noqa: F401,E501
from swagger_server import util


class CaReconfNotificationSecondaryCellAdd(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, ecgi: Ecgi=None):  # noqa: E501
        """CaReconfNotificationSecondaryCellAdd - a model defined in Swagger

        :param ecgi: The ecgi of this CaReconfNotificationSecondaryCellAdd.  # noqa: E501
        :type ecgi: Ecgi
        """
        self.swagger_types = {
            'ecgi': Ecgi
        }

        self.attribute_map = {
            'ecgi': 'ecgi'
        }
        self._ecgi = ecgi

    @classmethod
    def from_dict(cls, dikt) -> 'CaReconfNotificationSecondaryCellAdd':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The CaReconfNotification_secondaryCellAdd of this CaReconfNotificationSecondaryCellAdd.  # noqa: E501
        :rtype: CaReconfNotificationSecondaryCellAdd
        """
        return util.deserialize_model(dikt, cls)

    @property
    def ecgi(self) -> Ecgi:
        """Gets the ecgi of this CaReconfNotificationSecondaryCellAdd.


        :return: The ecgi of this CaReconfNotificationSecondaryCellAdd.
        :rtype: Ecgi
        """
        return self._ecgi

    @ecgi.setter
    def ecgi(self, ecgi: Ecgi):
        """Sets the ecgi of this CaReconfNotificationSecondaryCellAdd.


        :param ecgi: The ecgi of this CaReconfNotificationSecondaryCellAdd.
        :type ecgi: Ecgi
        """

        self._ecgi = ecgi