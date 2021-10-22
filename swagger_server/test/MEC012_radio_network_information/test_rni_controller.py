# coding: utf-8

from __future__ import absolute_import

from flask import json

from swagger_server.models.MEC012_radio_network_information.cell_change_subscription import CellChangeSubscription
from swagger_server.models.MEC012_radio_network_information.cell_change_subscription_filter_criteria_assoc_ho import \
	CellChangeSubscriptionFilterCriteriaAssocHo
from swagger_server.test import BaseTestCase


class TestRniController(BaseTestCase):
	"""RniController integration test stubs"""

	def test_layer2_meas_info_get(self):
		"""Test case for layer2_meas_info_get

		Retrieve information on layer 2 measurements
		"""
		query_string = [('app_ins_id', 'app_ins_id_example'),
		                ('cell_id', 'cell_id_example'),
		                ('ue_ipv4_address', 'ue_ipv4_address_example'),
		                ('ue_ipv6_address', 'ue_ipv6_address_example'),
		                ('nated_ip_address', 'nated_ip_address_example'),
		                ('gtp_teid', 'gtp_teid_example'),
		                ('dl_gbr_prb_usage_cell', 56),
		                ('ul_gbr_prb_usage_cell', 56),
		                ('dl_nongbr_prb_usage_cell', 56),
		                ('ul_nongbr_prb_usage_cell', 56),
		                ('dl_total_prb_usage_cell', 56),
		                ('ul_total_prb_usage_cell', 56),
		                ('received_dedicated_preambles_cell', 56),
		                ('received_randomly_selected_preambles_low_range_cell', 56),
		                ('received_randomly_selected_preambles_high_range_cell', 56),
		                ('number_of_active_ue_dl_gbr_cell', 56),
		                ('number_of_active_ue_ul_gbr_cell', 56),
		                ('number_of_active_ue_dl_nongbr_cell', 56),
		                ('number_of_active_ue_ul_nongbr_cell', 56),
		                ('dl_gbr_pdr_cell', 56),
		                ('ul_gbr_pdr_cell', 56),
		                ('dl_nongbr_pdr_cell', 56),
		                ('ul_nongbr_pdr_cell', 56),
		                ('dl_gbr_delay_ue', 56),
		                ('ul_gbr_delay_ue', 56),
		                ('dl_nongbr_delay_ue', 56),
		                ('ul_nongbr_delay_ue', 56),
		                ('dl_gbr_pdr_ue', 56),
		                ('ul_gbr_pdr_ue', 56),
		                ('dl_nongbr_pdr_ue', 56),
		                ('ul_nongbr_pdr_ue', 56),
		                ('dl_gbr_throughput_ue', 56),
		                ('ul_gbr_throughput_ue', 56),
		                ('dl_nongbr_throughput_ue', 56),
		                ('ul_nongbr_throughput_ue', 56),
		                ('dl_gbr_data_volume_ue', 56),
		                ('ul_gbr_data_volume_ue', 56),
		                ('dl_nongbr_data_volume_ue', 56),
		                ('ul_nongbr_data_volume_ue', 56)]
		response = self.client.open(
			'/rni/v2/queries/layer2_meas',
			method='GET',
			query_string=query_string)
		self.assert200(response,
		               'Response body is : ' + response.data.decode('utf-8'))

	def test_plmn_info_get(self):
		"""Test case for plmn_info_get

		Retrieve information on the underlying Mobile Network that the MEC application is associated to
		"""
		query_string = [('app_ins_id', 'app_ins_id_example')]
		response = self.client.open(
			'/rni/v2/queries/plmn_info',
			method='GET',
			query_string=query_string)
		self.assert200(response,
		               'Response body is : ' + response.data.decode('utf-8'))

	def test_rab_info_get(self):
		"""Test case for rab_info_get

		Retrieve information on Radio Access Bearers
		"""
		query_string = [('app_ins_id', 'app_ins_id_example'),
		                ('cell_id', 'cell_id_example'),
		                ('ue_ipv4_address', 'ue_ipv4_address_example'),
		                ('ue_ipv6_address', 'ue_ipv6_address_example'),
		                ('nated_ip_address', 'nated_ip_address_example'),
		                ('gtp_teid', 'gtp_teid_example'),
		                ('erab_id', 56),
		                ('qci', 56),
		                ('erab_mbr_dl', 56),
		                ('erab_mbr_ul', 56),
		                ('erab_gbr_dl', 56),
		                ('erab_gbr_ul', 56)]
		response = self.client.open(
			'/rni/v2/queries/rab_info',
			method='GET',
			query_string=query_string)
		self.assert200(response,
		               'Response body is : ' + response.data.decode('utf-8'))

	def test_s1_bearer_info_get(self):
		"""Test case for s1_bearer_info_get

		Retrieve S1-U bearer information related to specific UE(s)
		"""
		query_string = [('temp_ue_id', 'temp_ue_id_example'),
		                ('ue_ipv4_address', 'ue_ipv4_address_example'),
		                ('ue_ipv6_address', 'ue_ipv6_address_example'),
		                ('nated_ip_address', 'nated_ip_address_example'),
		                ('gtp_teid', 'gtp_teid_example'),
		                ('cell_id', 'cell_id_example'),
		                ('erab_id', 56)]
		response = self.client.open(
			'/rni/v2/queries/s1_bearer_info',
			method='GET',
			query_string=query_string)
		self.assert200(response,
		               'Response body is : ' + response.data.decode('utf-8'))

	def test_subscription_link_list_subscriptions_get(self):
		"""Test case for subscription_link_list_subscriptions_get

		Retrieve information on subscriptions for notifications
		"""
		query_string = [('subscription_type', 'subscription_type_example')]
		response = self.client.open(
			'/rni/v2/subscriptions',
			method='GET',
			query_string=query_string)
		self.assert200(response,
		               'Response body is : ' + response.data.decode('utf-8'))

	def test_subscriptions_delete(self):
		"""Test case for subscriptions_delete

		Cancel an existing subscription
		"""
		response = self.client.open(
			'/rni/v2/subscriptions/{subscriptionId}'.format(subscriptionId='subscription_id_example'),
			method='DELETE')
		self.assert200(response,
		               'Response body is : ' + response.data.decode('utf-8'))

	def test_subscriptions_get(self):
		"""Test case for subscriptions_get

		Retrieve information on current specific subscription
		"""
		response = self.client.open(
			'/rni/v2/subscriptions/{subscriptionId}'.format(subscriptionId='subscription_id_example'),
			method='GET')
		self.assert200(response,
		               'Response body is : ' + response.data.decode('utf-8'))

	def test_subscriptions_post(self):
		"""Test case for subscriptions_post

		Create a new subscription
		"""
		body = CellChangeSubscription(callback_reference="callbackURI",
		                              subscription_type="CellChangeSubscription",
		                              filter_criteria_assoc_ho=CellChangeSubscriptionFilterCriteriaAssocHo())
		response = self.client.open(
			'/rni/v2/subscriptions',
			method='POST',
			data=json.dumps(body),
			content_type='application/json')
		self.assert200(response,
		               'Response body is : ' + response.data.decode('utf-8'))

	def test_subscriptions_put(self):
		"""Test case for subscriptions_put

		Modify an existing subscription
		"""
		body = CellChangeSubscription(callback_reference="callbackURI",
		                              subscription_type="CellChangeSubscription",
		                              filter_criteria_assoc_ho=CellChangeSubscriptionFilterCriteriaAssocHo())
		response = self.client.open(
			'/rni/v2/subscriptions/{subscriptionId}'.format(subscriptionId='subscription_id_example'),
			method='PUT',
			data=json.dumps(body),
			content_type='application/json')
		self.assert200(response,
		               'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
	import unittest

	unittest.main()
