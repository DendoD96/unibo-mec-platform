# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.MEC012_radio_network_information.rab_info_cell_user_info import RabInfoCellUserInfo  # noqa: F401,E501
from swagger_server.models.MEC012_radio_network_information.time_stamp import TimeStamp  # noqa: F401,E501
from swagger_server import util


class RabInfo(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, app_instance_id: str=None, cell_user_info: List[RabInfoCellUserInfo]=None, request_id: str=None, time_stamp: TimeStamp=None):  # noqa: E501
        """RabInfo - a model defined in Swagger

        :param app_instance_id: The app_instance_id of this RabInfo.  # noqa: E501
        :type app_instance_id: str
        :param cell_user_info: The cell_user_info of this RabInfo.  # noqa: E501
        :type cell_user_info: List[RabInfoCellUserInfo]
        :param request_id: The request_id of this RabInfo.  # noqa: E501
        :type request_id: str
        :param time_stamp: The time_stamp of this RabInfo.  # noqa: E501
        :type time_stamp: TimeStamp
        """
        self.swagger_types = {
            'app_instance_id': str,
            'cell_user_info': List[RabInfoCellUserInfo],
            'request_id': str,
            'time_stamp': TimeStamp
        }

        self.attribute_map = {
            'app_instance_id': 'appInstanceId',
            'cell_user_info': 'cellUserInfo',
            'request_id': 'requestId',
            'time_stamp': 'timeStamp'
        }
        self._app_instance_id = app_instance_id
        self._cell_user_info = cell_user_info
        self._request_id = request_id
        self._time_stamp = time_stamp

    @classmethod
    def from_dict(cls, dikt) -> 'RabInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The RabInfo of this RabInfo.  # noqa: E501
        :rtype: RabInfo
        """
        return util.deserialize_model(dikt, cls)

    @property
    def app_instance_id(self) -> str:
        """Gets the app_instance_id of this RabInfo.

        Unique identifier for the MEC application instance.  # noqa: E501

        :return: The app_instance_id of this RabInfo.
        :rtype: str
        """
        return self._app_instance_id

    @app_instance_id.setter
    def app_instance_id(self, app_instance_id: str):
        """Sets the app_instance_id of this RabInfo.

        Unique identifier for the MEC application instance.  # noqa: E501

        :param app_instance_id: The app_instance_id of this RabInfo.
        :type app_instance_id: str
        """
        if app_instance_id is None:
            raise ValueError("Invalid value for `app_instance_id`, must not be `None`")  # noqa: E501

        self._app_instance_id = app_instance_id

    @property
    def cell_user_info(self) -> List[RabInfoCellUserInfo]:
        """Gets the cell_user_info of this RabInfo.

        The information on users per cell as defined below.  # noqa: E501

        :return: The cell_user_info of this RabInfo.
        :rtype: List[RabInfoCellUserInfo]
        """
        return self._cell_user_info

    @cell_user_info.setter
    def cell_user_info(self, cell_user_info: List[RabInfoCellUserInfo]):
        """Sets the cell_user_info of this RabInfo.

        The information on users per cell as defined below.  # noqa: E501

        :param cell_user_info: The cell_user_info of this RabInfo.
        :type cell_user_info: List[RabInfoCellUserInfo]
        """

        self._cell_user_info = cell_user_info

    @property
    def request_id(self) -> str:
        """Gets the request_id of this RabInfo.

        Unique identifier allocated by the service consumer for the RAB Information request.  # noqa: E501

        :return: The request_id of this RabInfo.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id: str):
        """Sets the request_id of this RabInfo.

        Unique identifier allocated by the service consumer for the RAB Information request.  # noqa: E501

        :param request_id: The request_id of this RabInfo.
        :type request_id: str
        """
        if request_id is None:
            raise ValueError("Invalid value for `request_id`, must not be `None`")  # noqa: E501

        self._request_id = request_id

    @property
    def time_stamp(self) -> TimeStamp:
        """Gets the time_stamp of this RabInfo.


        :return: The time_stamp of this RabInfo.
        :rtype: TimeStamp
        """
        return self._time_stamp

    @time_stamp.setter
    def time_stamp(self, time_stamp: TimeStamp):
        """Sets the time_stamp of this RabInfo.


        :param time_stamp: The time_stamp of this RabInfo.
        :type time_stamp: TimeStamp
        """

        self._time_stamp = time_stamp
