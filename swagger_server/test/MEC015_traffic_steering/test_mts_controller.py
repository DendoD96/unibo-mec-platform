# coding: utf-8

from __future__ import absolute_import

from flask import json

from swagger_server.models.MEC015_traffic_steering.mts_session_info import MtsSessionInfo  # noqa: E501
from swagger_server.models.MEC015_traffic_steering.mts_session_info_flow_filter import MtsSessionInfoFlowFilter
from swagger_server.models.MEC015_traffic_steering.mts_session_info_qos_d import MtsSessionInfoQosD
from swagger_server.test import BaseTestCase


class TestMtsController(BaseTestCase):
	"""MtsController integration test stubs"""

	def test_mts_capability_info_get(self):
		"""Test case for mts_capability_info_get

		Retrieve the MTS capability informations
		"""
		response = self.client.open(
			'/mts/v1/mts_capability_info',
			method='GET')
		self.assert200(response,
		               'Response body is : ' + response.data.decode('utf-8'))

	def test_mts_session_delete(self):
		"""Test case for mts_session_delete

		Remove specific MTS session
		"""
		response = self.client.open(
			'/mts/v1/mts_sessions/{sessionId}'.format(sessionId='session_id_example'),
			method='DELETE')
		self.assert200(response,
		               'Response body is : ' + response.data.decode('utf-8'))

	def test_mts_session_get(self):
		"""Test case for mts_session_get

		Retrieve information about specific MTS session
		"""
		response = self.client.open(
			'/mts/v1/mts_sessions/{sessionId}'.format(sessionId='session_id_example'),
			method='GET')
		self.assert200(response,
		               'Response body is : ' + response.data.decode('utf-8'))

	def test_mts_session_post(self):
		"""Test case for mts_session_post

		Create a MTS session
		"""
		body = MtsSessionInfo(app_ins_id="id", flow_filter=[MtsSessionInfoFlowFilter()], mts_mode=1,
		                      qos_d=MtsSessionInfoQosD(),
		                      request_type=1, traffic_direction="trafficDirection")
		response = self.client.open(
			'/mts/v1/mts_sessions',
			method='POST',
			data=json.dumps(body),
			content_type='application/json')
		self.assert200(response,
		               'Response body is : ' + response.data.decode('utf-8'))

	def test_mts_session_put(self):
		"""Test case for mts_session_put

		Update the information about specific MTS session
		"""
		body = MtsSessionInfo(app_ins_id="id", flow_filter=[MtsSessionInfoFlowFilter()], mts_mode=1,
		                      qos_d=MtsSessionInfoQosD(),
		                      request_type=1, traffic_direction="trafficDirection")
		response = self.client.open(
			'/mts/v1/mts_sessions/{sessionId}'.format(sessionId='session_id_example'),
			method='PUT',
			data=json.dumps(body),
			content_type='application/json')
		self.assert200(response,
		               'Response body is : ' + response.data.decode('utf-8'))

	def test_mts_sessions_list_get(self):
		"""Test case for mts_sessions_list_get

		Retrieve information about a list of MTS sessions
		"""
		query_string = [('app_instance_id', 'app_instance_id_example'),
		                ('app_name', 'app_name_example'),
		                ('session_id', 'session_id_example')]
		response = self.client.open(
			'/mts/v1/mts_sessions',
			method='GET',
			query_string=query_string)
		self.assert200(response,
		               'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
	import unittest

	unittest.main()
