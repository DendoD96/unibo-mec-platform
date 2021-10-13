import connexion

from swagger_server.models.MEC011_application_support.app_termination_confirmation import \
	AppTerminationConfirmation  # noqa: E501
from swagger_server.models.internal.applications_services_data import app_termination_ready
from swagger_server.models.problem_details import ProblemDetails

def applications_confirm_termination_post(app_instance_id, body=None):  # noqa: E501
	"""applications_confirm_termination_post

	This method is used to confirm the application level termination  of an application instance. # noqa: E501

	:param app_instance_id: Represents a MEC application instance. Note that the app_instance_id is allocated by the MEC platform manager.
	:type app_instance_id: str
	:param body:
	:type body: dict | bytes

	:rtype: None
	"""
	if connexion.request.is_json:
		body = AppTerminationConfirmation.from_dict(connexion.request.get_json())  # noqa: E501
	status = app_termination_ready(app_instance_id)
	if status == '204':
		return 'Done', 204
	return ProblemDetails(title="Application Id not valid", status=404), 404
