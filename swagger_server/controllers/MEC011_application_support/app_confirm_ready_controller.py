import connexion

from swagger_server.models.MEC011_application_support.app_ready_confirmation import AppReadyConfirmation  # noqa: E501


def applications_confirm_ready_post(appInstanceId, body=None):  # noqa: E501
    """applications_confirm_ready_post

    This method may be used by the MEC application instance to notify the MEC platform that it is up and running.  # noqa: E501

    :param app_instance_id: Represents a MEC application instance. Note that the appInstanceId is allocated by the MEC platform manager.
    :type app_instance_id: str
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = AppReadyConfirmation.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
