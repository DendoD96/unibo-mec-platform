import connexion

from swagger_server.models.MEC014_ue_identity.ue_identity_tag_info import UeIdentityTagInfo  # noqa: E501


def ue_identity_tag_info_get(appInstanceId, ueIdentityTag):  # noqa: E501
	"""ue_identity_tag_info_get

	Retrieves information about a specific UeIdentityTagInfo resource # noqa: E501

	:param appInstanceId: Represents a mobile edge application instance
	:type appInstanceId: str
	:param ueIdentityTag: Represents a UE
	:type ueIdentityTag: List[str]

	:rtype: UeIdentityTagInfo
	"""
	return 'do some magic!'


def ue_identity_tag_info_put(body, appInstanceId):  # noqa: E501
	"""ue_identity_tag_info_put

	Register/De-register the information about specific a UeIdentityTagInfo resource # noqa: E501

	:param body: &#x27;The updated &quot;state&quot; for each included UE Identity tag is included in the entity body of the request&#x27;
	:type body: dict | bytes
	:param appInstanceId: Represents a mobile edge application instance
	:type appInstanceId: str

	:rtype: UeIdentityTagInfo
	"""
	if connexion.request.is_json:
		body = UeIdentityTagInfo.from_dict(connexion.request.get_json())  # noqa: E501
	return 'do some magic!'
