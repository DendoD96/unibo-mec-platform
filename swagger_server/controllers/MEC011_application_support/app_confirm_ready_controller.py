import connexion

from swagger_server.models.MEC011_application_support.app_ready_confirmation import AppReadyConfirmation  # noqa: E501
from swagger_server.controllers.internal.applications_information_manager import manage_application_confirm_ready


def applications_confirm_ready_post(app_instance_id, body=None):  # noqa: E501
	"""applications_confirm_ready_post

	This method may be used by the MEC application instance to notify the MEC platform that it is up and running.  # noqa: E501

	:param app_instance_id: Represents a MEC application instance. Note that the app_instance_id is allocated by the MEC platform manager.
	:type app_instance_id: str
	:param body:
	:type body: dict | bytes

	:rtype: None
	"""
	if connexion.request.is_json:
		body = AppReadyConfirmation.from_dict(connexion.request.get_json())  # noqa: E501
	return manage_application_confirm_ready(app_instance_id)
