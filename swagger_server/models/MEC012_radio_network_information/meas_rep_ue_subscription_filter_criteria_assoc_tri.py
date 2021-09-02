# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.MEC012_radio_network_information.associate_id import AssociateId  # noqa: F401,E501
from swagger_server.models.MEC012_radio_network_information.ecgi import Ecgi  # noqa: F401,E501
from swagger_server.models.MEC012_radio_network_information.trigger import Trigger  # noqa: F401,E501
from swagger_server import util


class MeasRepUeSubscriptionFilterCriteriaAssocTri(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, app_instance_id: str=None, associate_id: List[AssociateId]=None, ecgi: List[Ecgi]=None, trigger: List[Trigger]=None):  # noqa: E501
        """MeasRepUeSubscriptionFilterCriteriaAssocTri - a model defined in Swagger

        :param app_instance_id: The app_instance_id of this MeasRepUeSubscriptionFilterCriteriaAssocTri.  # noqa: E501
        :type app_instance_id: str
        :param associate_id: The associate_id of this MeasRepUeSubscriptionFilterCriteriaAssocTri.  # noqa: E501
        :type associate_id: List[AssociateId]
        :param ecgi: The ecgi of this MeasRepUeSubscriptionFilterCriteriaAssocTri.  # noqa: E501
        :type ecgi: List[Ecgi]
        :param trigger: The trigger of this MeasRepUeSubscriptionFilterCriteriaAssocTri.  # noqa: E501
        :type trigger: List[Trigger]
        """
        self.swagger_types = {
            'app_instance_id': str,
            'associate_id': List[AssociateId],
            'ecgi': List[Ecgi],
            'trigger': List[Trigger]
        }

        self.attribute_map = {
            'app_instance_id': 'appInstanceId',
            'associate_id': 'associateId',
            'ecgi': 'ecgi',
            'trigger': 'trigger'
        }
        self._app_instance_id = app_instance_id
        self._associate_id = associate_id
        self._ecgi = ecgi
        self._trigger = trigger

    @classmethod
    def from_dict(cls, dikt) -> 'MeasRepUeSubscriptionFilterCriteriaAssocTri':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The MeasRepUeSubscription_filterCriteriaAssocTri of this MeasRepUeSubscriptionFilterCriteriaAssocTri.  # noqa: E501
        :rtype: MeasRepUeSubscriptionFilterCriteriaAssocTri
        """
        return util.deserialize_model(dikt, cls)

    @property
    def app_instance_id(self) -> str:
        """Gets the app_instance_id of this MeasRepUeSubscriptionFilterCriteriaAssocTri.

        Unique identifier for the MEC application instance.  # noqa: E501

        :return: The app_instance_id of this MeasRepUeSubscriptionFilterCriteriaAssocTri.
        :rtype: str
        """
        return self._app_instance_id

    @app_instance_id.setter
    def app_instance_id(self, app_instance_id: str):
        """Sets the app_instance_id of this MeasRepUeSubscriptionFilterCriteriaAssocTri.

        Unique identifier for the MEC application instance.  # noqa: E501

        :param app_instance_id: The app_instance_id of this MeasRepUeSubscriptionFilterCriteriaAssocTri.
        :type app_instance_id: str
        """

        self._app_instance_id = app_instance_id

    @property
    def associate_id(self) -> List[AssociateId]:
        """Gets the associate_id of this MeasRepUeSubscriptionFilterCriteriaAssocTri.

        0 to N identifiers to associate the information for a specific UE or flow.  # noqa: E501

        :return: The associate_id of this MeasRepUeSubscriptionFilterCriteriaAssocTri.
        :rtype: List[AssociateId]
        """
        return self._associate_id

    @associate_id.setter
    def associate_id(self, associate_id: List[AssociateId]):
        """Sets the associate_id of this MeasRepUeSubscriptionFilterCriteriaAssocTri.

        0 to N identifiers to associate the information for a specific UE or flow.  # noqa: E501

        :param associate_id: The associate_id of this MeasRepUeSubscriptionFilterCriteriaAssocTri.
        :type associate_id: List[AssociateId]
        """

        self._associate_id = associate_id

    @property
    def ecgi(self) -> List[Ecgi]:
        """Gets the ecgi of this MeasRepUeSubscriptionFilterCriteriaAssocTri.

        E-UTRAN Cell Global Identifier.  # noqa: E501

        :return: The ecgi of this MeasRepUeSubscriptionFilterCriteriaAssocTri.
        :rtype: List[Ecgi]
        """
        return self._ecgi

    @ecgi.setter
    def ecgi(self, ecgi: List[Ecgi]):
        """Sets the ecgi of this MeasRepUeSubscriptionFilterCriteriaAssocTri.

        E-UTRAN Cell Global Identifier.  # noqa: E501

        :param ecgi: The ecgi of this MeasRepUeSubscriptionFilterCriteriaAssocTri.
        :type ecgi: List[Ecgi]
        """

        self._ecgi = ecgi

    @property
    def trigger(self) -> List[Trigger]:
        """Gets the trigger of this MeasRepUeSubscriptionFilterCriteriaAssocTri.

        Corresponds to a specific E-UTRAN UE Measurement Report trigger.  # noqa: E501

        :return: The trigger of this MeasRepUeSubscriptionFilterCriteriaAssocTri.
        :rtype: List[Trigger]
        """
        return self._trigger

    @trigger.setter
    def trigger(self, trigger: List[Trigger]):
        """Sets the trigger of this MeasRepUeSubscriptionFilterCriteriaAssocTri.

        Corresponds to a specific E-UTRAN UE Measurement Report trigger.  # noqa: E501

        :param trigger: The trigger of this MeasRepUeSubscriptionFilterCriteriaAssocTri.
        :type trigger: List[Trigger]
        """

        self._trigger = trigger