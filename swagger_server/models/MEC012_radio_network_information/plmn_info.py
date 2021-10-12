# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401 # pylint: disable=unused-import

from typing import List, Dict  # noqa: F401 # pylint: disable=unused-import

from swagger_server.models.base_model_ import Model
from swagger_server.models.MEC012_radio_network_information.plmn import \
	Plmn  # noqa: F401 # pylint: disable=unused-import,E501
from swagger_server.models.MEC012_radio_network_information.time_stamp import \
	TimeStamp  # noqa: F401 # pylint: disable=unused-import,E501
from swagger_server import util


class PlmnInfo(Model):
	"""NOTE: This class is auto generated by the swagger code generator program.

	Do not edit the class manually.
	"""

	def __init__(self, app_instance_id: str = None, plmn: List[Plmn] = None,
	             time_stamp: TimeStamp = None):  # noqa: E501
		"""PlmnInfo - a model defined in Swagger

		:param app_instance_id: The app_instance_id of this PlmnInfo.  # noqa: E501
		:type app_instance_id: str
		:param plmn: The plmn of this PlmnInfo.  # noqa: E501
		:type plmn: List[Plmn]
		:param time_stamp: The time_stamp of this PlmnInfo.  # noqa: E501
		:type time_stamp: TimeStamp
		"""
		self.swagger_types = {
			'app_instance_id': str,
			'plmn': List[Plmn],
			'time_stamp': TimeStamp
		}

		self.attribute_map = {
			'app_instance_id': 'appInstanceId',
			'plmn': 'plmn',
			'time_stamp': 'timeStamp'
		}
		self._app_instance_id = app_instance_id
		self._plmn = plmn
		self._time_stamp = time_stamp

	@classmethod
	def from_dict(cls, dikt) -> 'PlmnInfo':
		"""Returns the dict as a model

		:param dikt: A dict.
		:type: dict
		:return: The PlmnInfo of this PlmnInfo.  # noqa: E501
		:rtype: PlmnInfo
		"""
		return util.deserialize_model(dikt, cls)

	@property
	def app_instance_id(self) -> str:
		"""Gets the app_instance_id of this PlmnInfo.

		Unique identifier for the MEC application instance.  # noqa: E501

		:return: The app_instance_id of this PlmnInfo.
		:rtype: str
		"""
		return self._app_instance_id

	@app_instance_id.setter
	def app_instance_id(self, app_instance_id: str):
		"""Sets the app_instance_id of this PlmnInfo.

		Unique identifier for the MEC application instance.  # noqa: E501

		:param app_instance_id: The app_instance_id of this PlmnInfo.
		:type app_instance_id: str
		"""
		if app_instance_id is None:
			raise ValueError("Invalid value for `app_instance_id`, must not be `None`")  # noqa: E501

		self._app_instance_id = app_instance_id

	@property
	def plmn(self) -> List[Plmn]:
		"""Gets the plmn of this PlmnInfo.

		Public Land Mobile Network Identity.  # noqa: E501

		:return: The plmn of this PlmnInfo.
		:rtype: List[Plmn]
		"""
		return self._plmn

	@plmn.setter
	def plmn(self, plmn: List[Plmn]):
		"""Sets the plmn of this PlmnInfo.

		Public Land Mobile Network Identity.  # noqa: E501

		:param plmn: The plmn of this PlmnInfo.
		:type plmn: List[Plmn]
		"""
		if plmn is None:
			raise ValueError("Invalid value for `plmn`, must not be `None`")  # noqa: E501

		self._plmn = plmn

	@property
	def time_stamp(self) -> TimeStamp:
		"""Gets the time_stamp of this PlmnInfo.


		:return: The time_stamp of this PlmnInfo.
		:rtype: TimeStamp
		"""
		return self._time_stamp

	@time_stamp.setter
	def time_stamp(self, time_stamp: TimeStamp):
		"""Sets the time_stamp of this PlmnInfo.


		:param time_stamp: The time_stamp of this PlmnInfo.
		:type time_stamp: TimeStamp
		"""

		self._time_stamp = time_stamp
