import connexion

from swagger_server.models.MEC015_traffic_steering.mts_capability_info import MtsCapabilityInfo  # noqa: E501
from swagger_server.models.MEC015_traffic_steering.mts_session_info import MtsSessionInfo  # noqa: E501


def mts_capability_info_get():  # noqa: E501
    """Retrieve the MTS capability informations

    Used to query information about the MTS information. Typically used in the &#x27;Get MTS service Info from the MTS Service&#x27; procedure as described in clause 6.2.6. # noqa: E501


    :rtype: MtsCapabilityInfo
    """
    return 'do some magic!'


def mts_session_delete(sessionId):  # noqa: E501
    """Remove specific MTS session

    DELETE method is typically used in &#x27;Unregister from the MTS Service&#x27; procedure as described in clause 6.2.8. # noqa: E501

    :param sessionId: Represents a MTS session instance
    :type sessionId: str

    :rtype: None
    """
    return 'do some magic!'


def mts_session_get(sessionId):  # noqa: E501
    """Retrieve information about specific MTS session

    Retrieves information about an individual MTS session. Typically used in the &#x27;Get configured MTS Session Info from the MTS Service&#x27; procedure as described in clause 6.2.10. # noqa: E501

    :param sessionId: Represents a MTS session instance
    :type sessionId: str

    :rtype: MtsSessionInfo
    """
    return 'do some magic!'


def mts_session_post(body):  # noqa: E501
    """Create a MTS session

    Used to create a MTS session. This method is typically used in &#x27;Register application to the MTS Service&#x27; procedure as described in clause 6.2.7. # noqa: E501

    :param body: Entity body in the request contains MtsSessionInfo to be created.
    :type body: dict | bytes

    :rtype: MtsSessionInfo
    """
    if connexion.request.is_json:
        body = MtsSessionInfo.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def mts_session_put(body, sessionId):  # noqa: E501
    """Update the information about specific MTS session

    Updates the information about an individual MTS session. As specified in ETSI GS MEC 009 [6], the PUT HTTP method has &#x27;replace&#x27; semantics.  # noqa: E501

    :param body: MtsSessionInfo with updated information is included as entity body of the request.
    :type body: dict | bytes
    :param sessionId: Represents a MTS session instance
    :type sessionId: str

    :rtype: MtsSessionInfo
    """
    if connexion.request.is_json:
        body = MtsSessionInfo.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def mts_sessions_list_get(app_instance_id=None, app_name=None, session_id=None):  # noqa: E501
    """Retrieve information about a list of MTS sessions

    Retrieves information about a list of MTS sessions. Typically used in the &#x27;Get configured MTS Session Info from the MTS Service&#x27; procedure as described in clause 6.2.10. # noqa: E501

    :param app_instance_id: A MEC application instance may use multiple app_instance_ids as an input parameter to query the MTS session of a list of MEC application instances. See note.
    :type app_instance_id: List[str]
    :param app_name: A MEC application instance may use multiple app_names as an input parameter to query the MTS session of a list of MEC application instances. See note.
    :type app_name: List[str]
    :param session_id: A MEC application instance may use session_id as an input parameter to query the information of a list of MTS sessions. See note.
    :type session_id: List[str]

    :rtype: List[MtsSessionInfo]
    """
    return 'do some magic!'
