# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.MEC012_radio_network_information.associate_id import AssociateId  # noqa: F401,E501
from swagger_server.models.MEC012_radio_network_information.ecgi import Ecgi  # noqa: F401,E501
from swagger_server.models.MEC012_radio_network_information.enum import Enum  # noqa: F401,E501
from swagger_server import util


class CellChangeSubscriptionFilterCriteriaAssocHo(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, app_instance_id: str=None, associate_id: List[AssociateId]=None, ecgi: List[Ecgi]=None, ho_status: List[Enum]=None):  # noqa: E501
        """CellChangeSubscriptionFilterCriteriaAssocHo - a model defined in Swagger

        :param app_instance_id: The app_instance_id of this CellChangeSubscriptionFilterCriteriaAssocHo.  # noqa: E501
        :type app_instance_id: str
        :param associate_id: The associate_id of this CellChangeSubscriptionFilterCriteriaAssocHo.  # noqa: E501
        :type associate_id: List[AssociateId]
        :param ecgi: The ecgi of this CellChangeSubscriptionFilterCriteriaAssocHo.  # noqa: E501
        :type ecgi: List[Ecgi]
        :param ho_status: The ho_status of this CellChangeSubscriptionFilterCriteriaAssocHo.  # noqa: E501
        :type ho_status: List[Enum]
        """
        self.swagger_types = {
            'app_instance_id': str,
            'associate_id': List[AssociateId],
            'ecgi': List[Ecgi],
            'ho_status': List[Enum]
        }

        self.attribute_map = {
            'app_instance_id': 'appInstanceId',
            'associate_id': 'associateId',
            'ecgi': 'ecgi',
            'ho_status': 'hoStatus'
        }
        self._app_instance_id = app_instance_id
        self._associate_id = associate_id
        self._ecgi = ecgi
        self._ho_status = ho_status

    @classmethod
    def from_dict(cls, dikt) -> 'CellChangeSubscriptionFilterCriteriaAssocHo':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The CellChangeSubscription_filterCriteriaAssocHo of this CellChangeSubscriptionFilterCriteriaAssocHo.  # noqa: E501
        :rtype: CellChangeSubscriptionFilterCriteriaAssocHo
        """
        return util.deserialize_model(dikt, cls)

    @property
    def app_instance_id(self) -> str:
        """Gets the app_instance_id of this CellChangeSubscriptionFilterCriteriaAssocHo.

        Unique identifier for the MEC application instance.  # noqa: E501

        :return: The app_instance_id of this CellChangeSubscriptionFilterCriteriaAssocHo.
        :rtype: str
        """
        return self._app_instance_id

    @app_instance_id.setter
    def app_instance_id(self, app_instance_id: str):
        """Sets the app_instance_id of this CellChangeSubscriptionFilterCriteriaAssocHo.

        Unique identifier for the MEC application instance.  # noqa: E501

        :param app_instance_id: The app_instance_id of this CellChangeSubscriptionFilterCriteriaAssocHo.
        :type app_instance_id: str
        """

        self._app_instance_id = app_instance_id

    @property
    def associate_id(self) -> List[AssociateId]:
        """Gets the associate_id of this CellChangeSubscriptionFilterCriteriaAssocHo.

        0 to N identifiers to associate the information for a specific UE or flow.  # noqa: E501

        :return: The associate_id of this CellChangeSubscriptionFilterCriteriaAssocHo.
        :rtype: List[AssociateId]
        """
        return self._associate_id

    @associate_id.setter
    def associate_id(self, associate_id: List[AssociateId]):
        """Sets the associate_id of this CellChangeSubscriptionFilterCriteriaAssocHo.

        0 to N identifiers to associate the information for a specific UE or flow.  # noqa: E501

        :param associate_id: The associate_id of this CellChangeSubscriptionFilterCriteriaAssocHo.
        :type associate_id: List[AssociateId]
        """

        self._associate_id = associate_id

    @property
    def ecgi(self) -> List[Ecgi]:
        """Gets the ecgi of this CellChangeSubscriptionFilterCriteriaAssocHo.

        E-UTRAN Cell Global Identifier.  # noqa: E501

        :return: The ecgi of this CellChangeSubscriptionFilterCriteriaAssocHo.
        :rtype: List[Ecgi]
        """
        return self._ecgi

    @ecgi.setter
    def ecgi(self, ecgi: List[Ecgi]):
        """Sets the ecgi of this CellChangeSubscriptionFilterCriteriaAssocHo.

        E-UTRAN Cell Global Identifier.  # noqa: E501

        :param ecgi: The ecgi of this CellChangeSubscriptionFilterCriteriaAssocHo.
        :type ecgi: List[Ecgi]
        """

        self._ecgi = ecgi

    @property
    def ho_status(self) -> List[Enum]:
        """Gets the ho_status of this CellChangeSubscriptionFilterCriteriaAssocHo.

        In case hoStatus is not included in the subscription request, the default value 3 = COMPLETED shall be used and included in the response: <p>1 = IN_PREPARATION. <p>2 = IN_EXECUTION. <p>3 = COMPLETED. <p>4 = REJECTED. <p>5 = CANCELLED.  # noqa: E501

        :return: The ho_status of this CellChangeSubscriptionFilterCriteriaAssocHo.
        :rtype: List[Enum]
        """
        return self._ho_status

    @ho_status.setter
    def ho_status(self, ho_status: List[Enum]):
        """Sets the ho_status of this CellChangeSubscriptionFilterCriteriaAssocHo.

        In case hoStatus is not included in the subscription request, the default value 3 = COMPLETED shall be used and included in the response: <p>1 = IN_PREPARATION. <p>2 = IN_EXECUTION. <p>3 = COMPLETED. <p>4 = REJECTED. <p>5 = CANCELLED.  # noqa: E501

        :param ho_status: The ho_status of this CellChangeSubscriptionFilterCriteriaAssocHo.
        :type ho_status: List[Enum]
        """

        self._ho_status = ho_status
