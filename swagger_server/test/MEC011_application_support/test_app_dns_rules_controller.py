# coding: utf-8

from __future__ import absolute_import

from flask import json

from swagger_server.models.MEC011_application_support.dns_rule import DnsRule  # noqa: E501
from swagger_server.test import BaseTestCase


class TestAppDnsRulesController(BaseTestCase):
	"""AppDnsRulesController integration test stubs"""

	def test_applications_dns_rule_get(self):
		"""Test case for applications_dns_rule_get


		"""
		response = self.client.open(
			'/mec_app_support/v1/applications/{appInstanceId}/dns_rules/{dnsRuleId}'.format(
				appInstanceId='app_instance_id_example', dnsRuleId='dns_rule_id_example'),
			method='GET')
		self.assert200(response,
		               'Response body is : ' + response.data.decode('utf-8'))

	def test_applications_dns_rule_put(self):
		"""Test case for applications_dns_rule_put


		"""
		body = DnsRule(dns_rule_id="ruleID", domain_name="www.example.com",
		               ip_address_type="IP_V6",
		               ip_address="192.0.2.0",
		               state="ACTIVE")
		response = self.client.open(
			'/mec_app_support/v1/applications/{appInstanceId}/dns_rules/{dnsRuleId}'.format(
				appInstanceId='app_instance_id_example', dnsRuleId='dns_rule_id_example'),
			method='PUT',
			data=json.dumps(body),
			content_type='application/json')
		self.assert200(response,
		               'Response body is : ' + response.data.decode('utf-8'))

	def test_applications_dns_rules_get(self):
		"""Test case for applications_dns_rules_get


		"""
		response = self.client.open(
			'/mec_app_support/v1/applications/{appInstanceId}/dns_rules'.format(
				appInstanceId='app_instance_id_example'),
			method='GET')
		self.assert200(response,
		               'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
	import unittest

	unittest.main()
