import connexion

from swagger_server.models.MEC011_application_support.app_termination_confirmation import AppTerminationConfirmation  # noqa: E501


def applications_confirm_termination_post(appInstanceId, body=None):  # noqa: E501
    """applications_confirm_termination_post

    This method is used to confirm the application level termination  of an application instance. # noqa: E501

    :param app_instance_id: Represents a MEC application instance. Note that the appInstanceId is allocated by the MEC platform manager.
    :type app_instance_id: str
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = AppTerminationConfirmation.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
