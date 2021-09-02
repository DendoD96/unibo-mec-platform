# coding: utf-8

from __future__ import absolute_import

from flask import json

from swagger_server.models.MEC011_application_support.traffic_rule import TrafficRule  # noqa: E501
from swagger_server.test import BaseTestCase


class TestAppTrafficRulesController(BaseTestCase):
	"""AppTrafficRulesController integration test stubs"""

	def test_applications_traffic_rule_get(self):
		"""Test case for applications_traffic_rule_get


		"""
		response = self.client.open(
			'/mec_app_support/v1/applications/{appInstanceId}/traffic_rules/{trafficRuleId}'.format(
				appInstanceId='app_instance_id_example', trafficRuleId='traffic_rule_id_example'),
			method='GET')
		self.assert200(response,
		               'Response body is : ' + response.data.decode('utf-8'))

	def test_applications_traffic_rule_put(self):
		"""Test case for applications_traffic_rule_put


		"""
		body = TrafficRule(traffic_rule_id="ruleId", action="PASSTHROUGH", filter_type="FLOW", priority=1,
		                   state="ACTIVE", traffic_filter=[
				{
					"srcAddress": [
						"192.168.1.1"
					],
					"dstAddress": [
						"192.168.1.1"
					],
					"srcPort": [
						"8080"
					],
					"dstPort": [
						"8080"
					],
					"protocol": [
						"?"
					],
					"token": [
						"?"
					],
					"srcTunnelAddress": [
						"?"
					],
					"tgtTunnelAddress": [
						"?"
					],
					"srcTunnelPort": [
						"?"
					],
					"dstTunnelPort": [
						"?"
					],
					"qCI": 1,
					"dSCP": 0,
					"tC": 1
				}
			])
		response = self.client.open(
			'/mec_app_support/v1/applications/{appInstanceId}/traffic_rules/{trafficRuleId}'.format(
				appInstanceId='app_instance_id_example', trafficRuleId='traffic_rule_id_example'),
			method='PUT',
			data=json.dumps(body),
			content_type='application/json')
		self.assert200(response,
		               'Response body is : ' + response.data.decode('utf-8'))

	def test_applications_traffic_rules_get(self):
		"""Test case for applications_traffic_rules_get


		"""
		response = self.client.open(
			'/mec_app_support/v1/applications/{appInstanceId}/traffic_rules'.format(
				appInstanceId='app_instance_id_example'),
			method='GET')
		self.assert200(response,
		               'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
	import unittest

	unittest.main()
