import connexion

from swagger_server.models.MEC015_bandwidth.bw_info import BwInfo  # noqa: E501
from swagger_server.models.MEC015_bandwidth.bw_info_deltas import BwInfoDeltas  # noqa: E501


def bandwidth_allocation_delete(allocation_id):  # noqa: E501
	"""Remove a specific bandwidthAllocation

	Used in &#x27;Unregister from Bandwidth Management Service&#x27; procedure as described in clause 6.2.3. # noqa: E501

	:param allocation_id: Represents a bandwidth allocation instance
	:type allocation_id: str

	:rtype: None
	"""
	return 'do some magic!'


def bandwidth_allocation_get(allocation_id):  # noqa: E501
	"""Retrieve information about a specific bandwidthAllocation

	Retrieves information about a bandwidthAllocation resource. Typically used in &#x27;Get configured bandwidth allocation from Bandwidth Management Service&#x27; procedure as described in clause 6.2.5. # noqa: E501

	:param allocation_id: Represents a bandwidth allocation instance
	:type allocation_id: str

	:rtype: BwInfo
	"""
	return 'do some magic!'


def bandwidth_allocation_list_get(app_instance_id=None, app_name=None, session_id=None):  # noqa: E501
	"""Retrieve information about a list of bandwidthAllocation resources

	Retrieves information about a list of bandwidthAllocation resources. Typically used in &#x27;Get configured bandwidth allocation from Bandwidth Management Service&#x27; procedure as described in clause 6.2.5. # noqa: E501

	:param app_instance_id: A MEC application instance may use multiple app_instance_ids as an input parameter to query the bandwidth allocation of a list of MEC application instances. See note.
	:type app_instance_id: List[str]
	:param app_name: A MEC application instance may use multiple app_names as an input parameter to query the bandwidth allocation of a list of MEC application instances. See note.
	:type app_name: List[str]
	:param session_id: A MEC application instance may use session_id as an input parameter to query the bandwidth allocation of a list of sessions. See note.
	:type session_id: List[str]

	:rtype: List[BwInfo]
	"""
	return 'do some magic!'


def bandwidth_allocation_patch(body, allocation_id):  # noqa: E501
	"""Modify the information about a specific existing bandwidthAllocation by sending updates on the data structure

	Updates the information about a bandwidthAllocation resource. As specified in ETSI GS MEC 009 [6], the PATCH HTTP method updates a resource on top of the existing resource state by just including the changes (&#x27;deltas&#x27;) in the request body. # noqa: E501

	:param body: Description of the changes to instruct the server how to modify the resource representation.
	:type body: dict | bytes
	:param allocation_id: Represents a bandwidth allocation instance
	:type allocation_id: str

	:rtype: BwInfo
	"""
	if connexion.request.is_json:
		body = BwInfoDeltas.from_dict(connexion.request.get_json())  # noqa: E501
	return 'do some magic!'


def bandwidth_allocation_post(body):  # noqa: E501
	"""Create a bandwidthAllocation resource

	Used to create a bandwidthAllocation resource. Typically used in &#x27;Register to Bandwidth Management Service&#x27; procedure as described in clause 6.2.1. # noqa: E501

	:param body: Entity body in the request contains BwInfo to be created.
	:type body: dict | bytes

	:rtype: BwInfo
	"""
	if connexion.request.is_json:
		body = BwInfo.from_dict(connexion.request.get_json())  # noqa: E501
	return 'do some magic!'


def bandwidth_allocation_put(body, allocation_id):  # noqa: E501
	"""Update the information about a specific bandwidthAllocation

	Updates the information about a bandwidthAllocation resource. As specified in ETSI GS MEC 009 [6], the PUT HTTP method has &#x27;replace&#x27; semantics. # noqa: E501

	:param body: BwInfo with updated information is included as entity body of the request.
	:type body: dict | bytes
	:param allocation_id: Represents a bandwidth allocation instance
	:type allocation_id: str

	:rtype: BwInfo
	"""
	if connexion.request.is_json:
		body = BwInfo.from_dict(connexion.request.get_json())  # noqa: E501
	return 'do some magic!'
