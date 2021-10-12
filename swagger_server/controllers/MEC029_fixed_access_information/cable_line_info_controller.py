import connexion

from swagger_server.models.MEC029_fixed_access_information.cp_info import CpInfo  # noqa: E501


def cable_line_info_get(customer_premises_info=None, cm_id=None):  # noqa: E501
	"""It Queries information about the cable line of a fixed access network.

	It Queries information about the cable line of a fixed access network. # noqa: E501

	:param customer_premises_info: Comma separated list of customer premises information
	:type customer_premises_info: list | bytes
	:param cm_id: Comma separated list of Cable Modem identifiers.
	:type cm_id: List[str]

	:rtype: CableLineInfo
	"""
	if connexion.request.is_json:
		customer_premises_info = [CpInfo.from_dict(d) for d in connexion.request.get_json()]  # noqa: E501
	return 'do some magic!'
