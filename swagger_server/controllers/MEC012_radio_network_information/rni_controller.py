import connexion

from swagger_server.models.MEC012_radio_network_information.inline_subscription import InlineSubscription  # noqa: E501


def layer2_meas_info_get(app_ins_id=None, cell_id=None, ue_ipv4_address=None, ue_ipv6_address=None,
                         nated_ip_address=None, gtp_teid=None, dl_gbr_prb_usage_cell=None, ul_gbr_prb_usage_cell=None,
                         dl_nongbr_prb_usage_cell=None, ul_nongbr_prb_usage_cell=None, dl_total_prb_usage_cell=None,
                         ul_total_prb_usage_cell=None, received_dedicated_preambles_cell=None,
                         received_randomly_selected_preambles_low_range_cell=None,
                         received_randomly_selected_preambles_high_range_cell=None,
                         number_of_active_ue_dl_gbr_cell=None, number_of_active_ue_ul_gbr_cell=None,
                         number_of_active_ue_dl_nongbr_cell=None, number_of_active_ue_ul_nongbr_cell=None,
                         dl_gbr_pdr_cell=None, ul_gbr_pdr_cell=None, dl_nongbr_pdr_cell=None, ul_nongbr_pdr_cell=None,
                         dl_gbr_delay_ue=None, ul_gbr_delay_ue=None, dl_nongbr_delay_ue=None, ul_nongbr_delay_ue=None,
                         dl_gbr_pdr_ue=None, ul_gbr_pdr_ue=None, dl_nongbr_pdr_ue=None, ul_nongbr_pdr_ue=None,
                         dl_gbr_throughput_ue=None, ul_gbr_throughput_ue=None, dl_nongbr_throughput_ue=None,
                         ul_nongbr_throughput_ue=None, dl_gbr_data_volume_ue=None, ul_gbr_data_volume_ue=None,
                         dl_nongbr_data_volume_ue=None, ul_nongbr_data_volume_ue=None):  # noqa: E501
	"""Retrieve information on layer 2 measurements

	Queries information about the layer 2 measurements. # noqa: E501

	:param app_ins_id: Application instance identifier
	:type app_ins_id: str
	:param cell_id: Comma separated list of E-UTRAN Cell Identities
	:type cell_id: List[str]
	:param ue_ipv4_address: Comma separated list of IE IPv4 addresses as defined for the type for AssociateId
	:type ue_ipv4_address: List[str]
	:param ue_ipv6_address: Comma separated list of IE IPv6 addresses as defined for the type for AssociateId
	:type ue_ipv6_address: List[str]
	:param nated_ip_address: Comma separated list of IE NATed IP addresses as defined for the type for AssociateId
	:type nated_ip_address: List[str]
	:param gtp_teid: Comma separated list of GTP TEID addresses as defined for the type for AssociateId
	:type gtp_teid: List[str]
	:param dl_gbr_prb_usage_cell: PRB usage for downlink GBR traffic in percentage as defined in ETSI TS 136 314
	:type dl_gbr_prb_usage_cell: int
	:param ul_gbr_prb_usage_cell: PRB usage for uplink GBR traffic in percentage as defined in ETSI TS 136 314
	:type ul_gbr_prb_usage_cell: int
	:param dl_nongbr_prb_usage_cell: PRB usage for downlink non-GBR traffic in percentage as defined in ETSI TS 136 314
	:type dl_nongbr_prb_usage_cell: int
	:param ul_nongbr_prb_usage_cell: PRB usage for uplink non-GBR traffic in percentage as defined in ETSI TS 136 314
	:type ul_nongbr_prb_usage_cell: int
	:param dl_total_prb_usage_cell: PRB usage for total downlink traffic in percentage as defined in ETSI TS 136 314
	:type dl_total_prb_usage_cell: int
	:param ul_total_prb_usage_cell: PRB usage for total uplink traffic in percentage as defined in ETSI TS 136 314
	:type ul_total_prb_usage_cell: int
	:param received_dedicated_preambles_cell: Received dedicated preambles in percentage as defined in ETSI TS 136 314
	:type received_dedicated_preambles_cell: int
	:param received_randomly_selected_preambles_low_range_cell: Received randomly selected preambles in the low range in percentage as defined in ETSI TS 136 314
	:type received_randomly_selected_preambles_low_range_cell: int
	:param received_randomly_selected_preambles_high_range_cell: Received rendomly selected preambles in the high range in percentage as defined in ETSI TS 136 314
	:type received_randomly_selected_preambles_high_range_cell: int
	:param number_of_active_ue_dl_gbr_cell: Number of active UEs with downlink GBR traffic as defined in ETSI TS 136 314
	:type number_of_active_ue_dl_gbr_cell: int
	:param number_of_active_ue_ul_gbr_cell: Number of active UEs with uplink GBR traffic as defined in ETSI TS 136 314
	:type number_of_active_ue_ul_gbr_cell: int
	:param number_of_active_ue_dl_nongbr_cell: Number of active UEs with downlink non-GBR traffic as defined in ETSI TS 136 314
	:type number_of_active_ue_dl_nongbr_cell: int
	:param number_of_active_ue_ul_nongbr_cell: Number of active UEs with uplink non-GBR traffic as defined in ETSI TS 136 314
	:type number_of_active_ue_ul_nongbr_cell: int
	:param dl_gbr_pdr_cell: Packet discard rate for downlink GBR traffic in percentage as defined in ETSI TS 136 314
	:type dl_gbr_pdr_cell: int
	:param ul_gbr_pdr_cell: Packet discard rate for uplink GBR traffic in percentage as defined in ETSI TS 136 314
	:type ul_gbr_pdr_cell: int
	:param dl_nongbr_pdr_cell: Packet discard rate for downlink non-GBR traffic in percentage as defined in ETSI TS 136 314
	:type dl_nongbr_pdr_cell: int
	:param ul_nongbr_pdr_cell: Packet discard rate for uplink non-GBR traffic in percentage as defined in ETSI TS 136 314
	:type ul_nongbr_pdr_cell: int
	:param dl_gbr_delay_ue: Packet delay of downlink GBR traffic of a UE as defined in ETSI TS 136 314
	:type dl_gbr_delay_ue: int
	:param ul_gbr_delay_ue: Packet delay of uplink GBR traffic of a UE as defined in ETSI TS 136 314
	:type ul_gbr_delay_ue: int
	:param dl_nongbr_delay_ue: Packet delay of downlink non-GBR traffic of a UE as defined in ETSI TS 136 314
	:type dl_nongbr_delay_ue: int
	:param ul_nongbr_delay_ue: Packet delay of uplink non-GBR traffic of a UE as defined in ETSI TS 136 314
	:type ul_nongbr_delay_ue: int
	:param dl_gbr_pdr_ue: Packet discard rate of downlink GBR traffic of a UE in percentage as defined in ETSI TS 136 314
	:type dl_gbr_pdr_ue: int
	:param ul_gbr_pdr_ue: Packet discard rate of uplink GBR traffic of a UE in percentage as defined in ETSI TS 136 314
	:type ul_gbr_pdr_ue: int
	:param dl_nongbr_pdr_ue: Packet discard rate of downlink non-GBR traffic of a UE in percentage as defined in ETSI TS 136 314
	:type dl_nongbr_pdr_ue: int
	:param ul_nongbr_pdr_ue: Packet discard rate of uplink non-GBR traffic of a UE in percentage as defined in ETSI TS 136 314
	:type ul_nongbr_pdr_ue: int
	:param dl_gbr_throughput_ue: Scheduled throughput of downlink GBR traffic of a UE as defined in ETSI TS 136 314
	:type dl_gbr_throughput_ue: int
	:param ul_gbr_throughput_ue: Scheduled throughput of uplink GBR traffic of a UE as defined in ETSI TS 136 314
	:type ul_gbr_throughput_ue: int
	:param dl_nongbr_throughput_ue: Scheduled throughput of downlink non-GBR traffic of a UE as defined in ETSI TS 136 314
	:type dl_nongbr_throughput_ue: int
	:param ul_nongbr_throughput_ue: Scheduled throughput of uplink non-GBR traffic of a UE as defined in ETSI TS 136 314
	:type ul_nongbr_throughput_ue: int
	:param dl_gbr_data_volume_ue: Data volume of downlink GBR traffic of a UE as defined in ETSI TS 136 314
	:type dl_gbr_data_volume_ue: int
	:param ul_gbr_data_volume_ue: Data volume of uplink GBR traffic of a UE as defined in ETSI TS 136 314
	:type ul_gbr_data_volume_ue: int
	:param dl_nongbr_data_volume_ue: Data volume of downlink non-GBR traffic of a UE as defined in ETSI TS 136 314
	:type dl_nongbr_data_volume_ue: int
	:param ul_nongbr_data_volume_ue: Data volume of uplink non-GBR traffic of a UE as defined in ETSI TS 136 314
	:type ul_nongbr_data_volume_ue: int

	:rtype: L2Meas
	"""
	return 'do some magic!'


def plmn_info_get(app_ins_id):  # noqa: E501
	"""Retrieve information on the underlying Mobile Network that the MEC application is associated to

	Queries information about the Mobile Network # noqa: E501

	:param app_ins_id: Comma separated list of Application instance identifiers
	:type app_ins_id: List[str]

	:rtype: List[PlmnInfo]
	"""
	return 'do some magic!'


def rab_info_get(app_ins_id=None, cell_id=None, ue_ipv4_address=None, ue_ipv6_address=None, nated_ip_address=None,
                 gtp_teid=None, erab_id=None, qci=None, erab_mbr_dl=None, erab_mbr_ul=None, erab_gbr_dl=None,
                 erab_gbr_ul=None):  # noqa: E501
	"""Retrieve information on Radio Access Bearers

	Queries information about the Radio Access Bearers # noqa: E501

	:param app_ins_id: Application instance identifier
	:type app_ins_id: str
	:param cell_id: Comma separated list of E-UTRAN Cell Identities
	:type cell_id: List[str]
	:param ue_ipv4_address: Comma separated list of IE IPv4 addresses as defined for the type for AssociateId
	:type ue_ipv4_address: List[str]
	:param ue_ipv6_address: Comma separated list of IE IPv6 addresses as defined for the type for AssociateId
	:type ue_ipv6_address: List[str]
	:param nated_ip_address: Comma separated list of IE NATed IP addresses as defined for the type for AssociateId
	:type nated_ip_address: List[str]
	:param gtp_teid: Comma separated list of GTP TEID addresses as defined for the type for AssociateId
	:type gtp_teid: List[str]
	:param erab_id: E-RAB identifier
	:type erab_id: int
	:param qci: QoS Class Identifier as defined in ETSI TS 123 401
	:type qci: int
	:param erab_mbr_dl: Maximum downlink E-RAB Bit Rate as defined in ETSI TS 123 401
	:type erab_mbr_dl: int
	:param erab_mbr_ul: Maximum uplink E-RAB Bit Rate as defined in ETSI TS 123 401
	:type erab_mbr_ul: int
	:param erab_gbr_dl: Guaranteed downlink E-RAB Bit Rate as defined in ETSI TS 123 401
	:type erab_gbr_dl: int
	:param erab_gbr_ul: Guaranteed uplink E-RAB Bit Rate as defined in ETSI TS 123 401
	:type erab_gbr_ul: int

	:rtype: RabInfo
	"""
	return 'do some magic!'


def s1_bearer_info_get(temp_ue_id=None, ue_ipv4_address=None, ue_ipv6_address=None, nated_ip_address=None,
                       gtp_teid=None, cell_id=None, erab_id=None):  # noqa: E501
	"""Retrieve S1-U bearer information related to specific UE(s)

	Queries information about the S1 bearer(s) # noqa: E501

	:param temp_ue_id: Comma separated list of temporary identifiers allocated for the specific UE as defined in   ETSI TS 136 413
	:type temp_ue_id: List[str]
	:param ue_ipv4_address: Comma separated list of IE IPv4 addresses as defined for the type for AssociateId
	:type ue_ipv4_address: List[str]
	:param ue_ipv6_address: Comma separated list of IE IPv6 addresses as defined for the type for AssociateId
	:type ue_ipv6_address: List[str]
	:param nated_ip_address: Comma separated list of IE NATed IP addresses as defined for the type for AssociateId
	:type nated_ip_address: List[str]
	:param gtp_teid: Comma separated list of GTP TEID addresses as defined for the type for AssociateId
	:type gtp_teid: List[str]
	:param cell_id: Comma separated list of E-UTRAN Cell Identities
	:type cell_id: List[str]
	:param erab_id: Comma separated list of E-RAB identifiers
	:type erab_id: List[int]

	:rtype: S1BearerInfo
	"""
	return 'do some magic!'


def subscription_link_list_subscriptions_get(subscription_type=None):  # noqa: E501
	"""Retrieve information on subscriptions for notifications

	Queries information on subscriptions for notifications # noqa: E501

	:param subscription_type: Filter on a specific subscription type. Permitted values: cell_change, rab_est, rab_mod, rab_rel, meas_rep_ue, nr_meas_rep_ue, timing_advance_ue, ca_reconf, s1_bearer.
	:type subscription_type: str

	:rtype: SubscriptionLinkList
	"""
	return 'do some magic!'


def subscriptions_delete(subscription_id):  # noqa: E501
	"""Cancel an existing subscription

	Cancels an existing subscription, identified by its self-referring URI returned on creation (initial POST) # noqa: E501

	:param subscription_id: Subscription Id, specifically the 'Self-referring URI' returned in the subscription request
	:type subscription_id: str

	:rtype: None
	"""
	return 'do some magic!'


def subscriptions_get(subscription_id):  # noqa: E501
	"""Retrieve information on current specific subscription

	Queries information about an existing subscription, identified by its self-referring URI returned on creation (initial POST) # noqa: E501

	:param subscription_id: Subscription Id, specifically the 'Self-referring URI' returned in the subscription request
	:type subscription_id: str

	:rtype: InlineSubscription
	"""
	return 'do some magic!'


def subscriptions_post(body):  # noqa: E501
	"""Create a new subscription

	Creates a new subscription to Radio Network Information notifications # noqa: E501

	:param body: Subscription to be created
	:type body: dict | bytes

	:rtype: InlineSubscription
	"""
	if connexion.request.is_json:
		body = InlineSubscription.from_dict(connexion.request.get_json())  # noqa: E501
	return 'do some magic!'


def subscriptions_put(body, subscription_id):  # noqa: E501
	"""Modify an existing subscription

	Updates an existing subscription, identified by its self-referring URI returned on creation (initial POST) # noqa: E501

	:param body: Subscription to be modified
	:type body: dict | bytes
	:param subscription_id: Subscription Id, specifically the 'Self-referring URI' returned in the subscription request
	:type subscription_id: str

	:rtype: InlineSubscription
	"""
	if connexion.request.is_json:
		body = InlineSubscription.from_dict(connexion.request.get_json())  # noqa: E501
	return 'do some magic!'
