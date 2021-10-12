# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401 # pylint: disable=unused-import

from typing import List, Dict  # noqa: F401 # pylint: disable=unused-import

from swagger_server.models.base_model_ import Model
from swagger_server import util


class WebsockNotifConfig(Model):
	"""NOTE: This class is auto generated by the swagger code generator program.

	Do not edit the class manually.
	"""

	def __init__(self, request_websocket_uri: bool = None, websocket_uri: str = None):  # noqa: E501
		"""WebsockNotifConfig - a model defined in Swagger

		:param request_websocket_uri: The request_websocket_uri of this WebsockNotifConfig.  # noqa: E501
		:type request_websocket_uri: bool
		:param websocket_uri: The websocket_uri of this WebsockNotifConfig.  # noqa: E501
		:type websocket_uri: str
		"""
		self.swagger_types = {
			'request_websocket_uri': bool,
			'websocket_uri': str
		}

		self.attribute_map = {
			'request_websocket_uri': 'requestWebsocketUri',
			'websocket_uri': 'websocketUri'
		}
		self._request_websocket_uri = request_websocket_uri
		self._websocket_uri = websocket_uri

	@classmethod
	def from_dict(cls, dikt) -> 'WebsockNotifConfig':
		"""Returns the dict as a model

		:param dikt: A dict.
		:type: dict
		:return: The WebsockNotifConfig of this WebsockNotifConfig.  # noqa: E501
		:rtype: WebsockNotifConfig
		"""
		return util.deserialize_model(dikt, cls)

	@property
	def request_websocket_uri(self) -> bool:
		"""Gets the request_websocket_uri of this WebsockNotifConfig.

		Set to true by the service consumer to indicate that Websocket delivery is requested.  # noqa: E501

		:return: The request_websocket_uri of this WebsockNotifConfig.
		:rtype: bool
		"""
		return self._request_websocket_uri

	@request_websocket_uri.setter
	def request_websocket_uri(self, request_websocket_uri: bool):
		"""Sets the request_websocket_uri of this WebsockNotifConfig.

		Set to true by the service consumer to indicate that Websocket delivery is requested.  # noqa: E501

		:param request_websocket_uri: The request_websocket_uri of this WebsockNotifConfig.
		:type request_websocket_uri: bool
		"""

		self._request_websocket_uri = request_websocket_uri

	@property
	def websocket_uri(self) -> str:
		"""Gets the websocket_uri of this WebsockNotifConfig.

		Set by WAIS to indicate to the service consumer the Websocket URI to be used for delivering notifications.  # noqa: E501

		:return: The websocket_uri of this WebsockNotifConfig.
		:rtype: str
		"""
		return self._websocket_uri

	@websocket_uri.setter
	def websocket_uri(self, websocket_uri: str):
		"""Sets the websocket_uri of this WebsockNotifConfig.

		Set by WAIS to indicate to the service consumer the Websocket URI to be used for delivering notifications.  # noqa: E501

		:param websocket_uri: The websocket_uri of this WebsockNotifConfig.
		:type websocket_uri: str
		"""

		self._websocket_uri = websocket_uri
