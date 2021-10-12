import connexion

from swagger_server.models.MEC029_fixed_access_information.cp_info import CpInfo  # noqa: E501


def optical_network_info_get(customer_premises_info=None, pon_ys_id=None, onu_id=None):  # noqa: E501
	"""used to query information about the optical network.

	used to query information about the optical network. # noqa: E501

	:param customer_premises_info: Comma separated list of customer premises information
	:type customer_premises_info: list | bytes
	:param pon_ys_id: Comma separated list of optical system identifiers.
	:type pon_ys_id: List[str]
	:param onu_id: Comma separated list of optical network unit identifiers.
	:type onu_id: List[str]

	:rtype: List[PonInfo]
	"""
	if connexion.request.is_json:
		customer_premises_info = [CpInfo.from_dict(d) for d in connexion.request.get_json()]  # noqa: E501
	return 'do some magic!'
