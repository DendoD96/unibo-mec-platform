# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class RabEstNotificationTempUeId(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, mmec: str=None, mtmsi: str=None):  # noqa: E501
        """RabEstNotificationTempUeId - a model defined in Swagger

        :param mmec: The mmec of this RabEstNotificationTempUeId.  # noqa: E501
        :type mmec: str
        :param mtmsi: The mtmsi of this RabEstNotificationTempUeId.  # noqa: E501
        :type mtmsi: str
        """
        self.swagger_types = {
            'mmec': str,
            'mtmsi': str
        }

        self.attribute_map = {
            'mmec': 'mmec',
            'mtmsi': 'mtmsi'
        }
        self._mmec = mmec
        self._mtmsi = mtmsi

    @classmethod
    def from_dict(cls, dikt) -> 'RabEstNotificationTempUeId':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The RabEstNotification_tempUeId of this RabEstNotificationTempUeId.  # noqa: E501
        :rtype: RabEstNotificationTempUeId
        """
        return util.deserialize_model(dikt, cls)

    @property
    def mmec(self) -> str:
        """Gets the mmec of this RabEstNotificationTempUeId.

        MMEC as defined in ETSI TS 136 413 [i.3].  # noqa: E501

        :return: The mmec of this RabEstNotificationTempUeId.
        :rtype: str
        """
        return self._mmec

    @mmec.setter
    def mmec(self, mmec: str):
        """Sets the mmec of this RabEstNotificationTempUeId.

        MMEC as defined in ETSI TS 136 413 [i.3].  # noqa: E501

        :param mmec: The mmec of this RabEstNotificationTempUeId.
        :type mmec: str
        """
        if mmec is None:
            raise ValueError("Invalid value for `mmec`, must not be `None`")  # noqa: E501

        self._mmec = mmec

    @property
    def mtmsi(self) -> str:
        """Gets the mtmsi of this RabEstNotificationTempUeId.

        M-TMSI as defined in ETSI TS 136 413 [i.3].  # noqa: E501

        :return: The mtmsi of this RabEstNotificationTempUeId.
        :rtype: str
        """
        return self._mtmsi

    @mtmsi.setter
    def mtmsi(self, mtmsi: str):
        """Sets the mtmsi of this RabEstNotificationTempUeId.

        M-TMSI as defined in ETSI TS 136 413 [i.3].  # noqa: E501

        :param mtmsi: The mtmsi of this RabEstNotificationTempUeId.
        :type mtmsi: str
        """
        if mtmsi is None:
            raise ValueError("Invalid value for `mtmsi`, must not be `None`")  # noqa: E501

        self._mtmsi = mtmsi