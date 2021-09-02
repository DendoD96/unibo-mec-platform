# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.MEC029_fixed_access_information.trace_route_diagnostics_diagnostics_state import TraceRouteDiagnosticsDiagnosticsState  # noqa: F401,E501
from swagger_server import util


class TraceRouteDiagnostics(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, data_block_size: int=None, diagnostics_state: TraceRouteDiagnosticsDiagnosticsState=None, host: str=None, max_hop_count: int=None, number_of_route_hops: int=None, response_time: int=None, timeout: int=None):  # noqa: E501
        """TraceRouteDiagnostics - a model defined in Swagger

        :param data_block_size: The data_block_size of this TraceRouteDiagnostics.  # noqa: E501
        :type data_block_size: int
        :param diagnostics_state: The diagnostics_state of this TraceRouteDiagnostics.  # noqa: E501
        :type diagnostics_state: TraceRouteDiagnosticsDiagnosticsState
        :param host: The host of this TraceRouteDiagnostics.  # noqa: E501
        :type host: str
        :param max_hop_count: The max_hop_count of this TraceRouteDiagnostics.  # noqa: E501
        :type max_hop_count: int
        :param number_of_route_hops: The number_of_route_hops of this TraceRouteDiagnostics.  # noqa: E501
        :type number_of_route_hops: int
        :param response_time: The response_time of this TraceRouteDiagnostics.  # noqa: E501
        :type response_time: int
        :param timeout: The timeout of this TraceRouteDiagnostics.  # noqa: E501
        :type timeout: int
        """
        self.swagger_types = {
            'data_block_size': int,
            'diagnostics_state': TraceRouteDiagnosticsDiagnosticsState,
            'host': str,
            'max_hop_count': int,
            'number_of_route_hops': int,
            'response_time': int,
            'timeout': int
        }

        self.attribute_map = {
            'data_block_size': 'dataBlockSize',
            'diagnostics_state': 'diagnosticsState',
            'host': 'host',
            'max_hop_count': 'maxHopCount',
            'number_of_route_hops': 'numberOfRouteHops',
            'response_time': 'responseTime',
            'timeout': 'timeout'
        }
        self._data_block_size = data_block_size
        self._diagnostics_state = diagnostics_state
        self._host = host
        self._max_hop_count = max_hop_count
        self._number_of_route_hops = number_of_route_hops
        self._response_time = response_time
        self._timeout = timeout

    @classmethod
    def from_dict(cls, dikt) -> 'TraceRouteDiagnostics':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The TraceRouteDiagnostics of this TraceRouteDiagnostics.  # noqa: E501
        :rtype: TraceRouteDiagnostics
        """
        return util.deserialize_model(dikt, cls)

    @property
    def data_block_size(self) -> int:
        """Gets the data_block_size of this TraceRouteDiagnostics.

        Size of the data block in bytes to be sent for each trace route.  # noqa: E501

        :return: The data_block_size of this TraceRouteDiagnostics.
        :rtype: int
        """
        return self._data_block_size

    @data_block_size.setter
    def data_block_size(self, data_block_size: int):
        """Sets the data_block_size of this TraceRouteDiagnostics.

        Size of the data block in bytes to be sent for each trace route.  # noqa: E501

        :param data_block_size: The data_block_size of this TraceRouteDiagnostics.
        :type data_block_size: int
        """

        self._data_block_size = data_block_size

    @property
    def diagnostics_state(self) -> TraceRouteDiagnosticsDiagnosticsState:
        """Gets the diagnostics_state of this TraceRouteDiagnostics.


        :return: The diagnostics_state of this TraceRouteDiagnostics.
        :rtype: TraceRouteDiagnosticsDiagnosticsState
        """
        return self._diagnostics_state

    @diagnostics_state.setter
    def diagnostics_state(self, diagnostics_state: TraceRouteDiagnosticsDiagnosticsState):
        """Sets the diagnostics_state of this TraceRouteDiagnostics.


        :param diagnostics_state: The diagnostics_state of this TraceRouteDiagnostics.
        :type diagnostics_state: TraceRouteDiagnosticsDiagnosticsState
        """
        if diagnostics_state is None:
            raise ValueError("Invalid value for `diagnostics_state`, must not be `None`")  # noqa: E501

        self._diagnostics_state = diagnostics_state

    @property
    def host(self) -> str:
        """Gets the host of this TraceRouteDiagnostics.

        Host name or address of the host to find a route to.  # noqa: E501

        :return: The host of this TraceRouteDiagnostics.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host: str):
        """Sets the host of this TraceRouteDiagnostics.

        Host name or address of the host to find a route to.  # noqa: E501

        :param host: The host of this TraceRouteDiagnostics.
        :type host: str
        """

        self._host = host

    @property
    def max_hop_count(self) -> int:
        """Gets the max_hop_count of this TraceRouteDiagnostics.

        The maximum number of hop used in outgoing probe packets. The default is 30 hops.  # noqa: E501

        :return: The max_hop_count of this TraceRouteDiagnostics.
        :rtype: int
        """
        return self._max_hop_count

    @max_hop_count.setter
    def max_hop_count(self, max_hop_count: int):
        """Sets the max_hop_count of this TraceRouteDiagnostics.

        The maximum number of hop used in outgoing probe packets. The default is 30 hops.  # noqa: E501

        :param max_hop_count: The max_hop_count of this TraceRouteDiagnostics.
        :type max_hop_count: int
        """

        self._max_hop_count = max_hop_count

    @property
    def number_of_route_hops(self) -> int:
        """Gets the number_of_route_hops of this TraceRouteDiagnostics.

        Result parameter indicating the number of hops within the discovered route.  If a route could not be determined, this value shall be zero.  # noqa: E501

        :return: The number_of_route_hops of this TraceRouteDiagnostics.
        :rtype: int
        """
        return self._number_of_route_hops

    @number_of_route_hops.setter
    def number_of_route_hops(self, number_of_route_hops: int):
        """Sets the number_of_route_hops of this TraceRouteDiagnostics.

        Result parameter indicating the number of hops within the discovered route.  If a route could not be determined, this value shall be zero.  # noqa: E501

        :param number_of_route_hops: The number_of_route_hops of this TraceRouteDiagnostics.
        :type number_of_route_hops: int
        """

        self._number_of_route_hops = number_of_route_hops

    @property
    def response_time(self) -> int:
        """Gets the response_time of this TraceRouteDiagnostics.

        Result parameter indicating the response time in milliseconds the most recent trace route test.  If a route could not be determined, this value shall be zero.  # noqa: E501

        :return: The response_time of this TraceRouteDiagnostics.
        :rtype: int
        """
        return self._response_time

    @response_time.setter
    def response_time(self, response_time: int):
        """Sets the response_time of this TraceRouteDiagnostics.

        Result parameter indicating the response time in milliseconds the most recent trace route test.  If a route could not be determined, this value shall be zero.  # noqa: E501

        :param response_time: The response_time of this TraceRouteDiagnostics.
        :type response_time: int
        """

        self._response_time = response_time

    @property
    def timeout(self) -> int:
        """Gets the timeout of this TraceRouteDiagnostics.

        Timeout in milliseconds for the trace route test.  # noqa: E501

        :return: The timeout of this TraceRouteDiagnostics.
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout: int):
        """Sets the timeout of this TraceRouteDiagnostics.

        Timeout in milliseconds for the trace route test.  # noqa: E501

        :param timeout: The timeout of this TraceRouteDiagnostics.
        :type timeout: int
        """

        self._timeout = timeout
