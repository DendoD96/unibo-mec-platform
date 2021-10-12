import connexion

from swagger_server.models.MEC011_service_management.service_info import ServiceInfo
from swagger_server.models.MEC011_service_management.service_info_post import ServiceInfoPost  # noqa: E501
from swagger_server.models.internal.applications_services_data import add_app_service, delete_app_service
from swagger_server.models.internal.applications_services_data import get_application_services
from swagger_server.models.internal.applications_services_data import update_app_service
from swagger_server.models.problem_details import ProblemDetails


def app_services_get(app_instance_id, ser_instance_id=None, ser_name=None, ser_category_id=None,
                     consumed_local_only=None,
                     is_local=None, scope_of_locality=None):  # noqa: E501
	"""app_services_get

	This method retrieves information about a list of mecService resources. This method is typically used in 'service availability query' procedure # noqa: E501

	:param app_instance_id: Represents a MEC application instance. Note that the app_instance_id is allocated by the MEC platform manager.
	:type app_instance_id: str
	:param ser_instance_id: A MEC application instance may use multiple ser_instance_ids as an input parameter to query the availability of a list of MEC service instances. Either 'ser_instance_id' or 'ser_name' or 'ser_category_id' or none of them shall be present.
	:type ser_instance_id: List[str]
	:param ser_name: A MEC application instance may use multiple ser_names as an input parameter to query the availability of a list of MEC service instances. Either 'ser_instance_id' or 'ser_name' or 'ser_category_id' or none of them shall be present.
	:type ser_name: List[str]
	:param ser_category_id: A MEC application instance may use ser_category_id as an input parameter to query the availability of a list of MEC service instances in a serCategory. Either 'ser_instance_id' or 'ser_name' or 'ser_category_id' or none of them shall be present.
	:type ser_category_id: str
	:param consumed_local_only: Indicate whether the service can only be consumed by the MEC  applications located in the same locality (as defined by  scopeOfLocality) as this service instance.
	:type consumed_local_only: bool
	:param is_local: Indicate whether the service is located in the same locality (as  defined by scopeOfLocality) as the consuming MEC application.
	:type is_local: bool
	:param scope_of_locality: A MEC application instance may use scope_of_locality as an input  parameter to query the availability of a list of MEC service instances  with a certain scope of locality.
	:type scope_of_locality: str

	:rtype: List[ServiceInfo]
	"""
	return get_application_services(app_instance_id=app_instance_id, ser_instance_id=ser_instance_id, ser_name=ser_name,
	                                ser_category_id=ser_category_id, consumed_local_only=consumed_local_only,
	                                is_local=is_local,
	                                scope_of_locality=scope_of_locality)


def app_services_post(body, app_instance_id):  # noqa: E501
	"""app_services_post

	This method is used to create a mecService resource. This method is typically used in 'service availability update and new service registration' procedure # noqa: E501

	:param body: New ServiceInfo with updated &quot;state&quot; is included as entity body of the request
	:type body: dict | bytes
	:param app_instance_id: Represents a MEC application instance. Note that the app_instance_id is allocated by the MEC platform manager.
	:type app_instance_id: str

	:rtype: ServiceInfo
	"""
	if connexion.request.is_json:
		body = ServiceInfoPost.from_dict(connexion.request.get_json())  # noqa: E501
	return add_app_service(app_instance_id, body), 201


def app_services_service_id_delete(app_instance_id, service_id):  # noqa: E501
	"""app_services_service_id_delete

	This method deletes a mecService resource. This method is typically used in the service deregistration procedure.  # noqa: E501

	:param app_instance_id: Represents a MEC application instance. Note that the app_instance_id is allocated by the MEC platform manager.
	:type app_instance_id: str
	:param service_id: Represents a MEC service instance.
	:type service_id: str

	:rtype: None
	"""
	result = delete_app_service(app_instance_id=app_instance_id, ser_instance_id=service_id)
	if result is not None:
		return "Done", 204
	return ProblemDetails(title="service not found", status=404), 404


def app_services_service_id_get(app_instance_id, service_id):  # noqa: E501
	"""app_services_service_id_get

	This method retrieves information about a mecService resource. This method is typically used in 'service availability query' procedure # noqa: E501

	:param app_instance_id: Represents a MEC application instance. Note that the app_instance_id is allocated by the MEC platform manager.
	:type app_instance_id: str
	:param service_id: Represents a MEC service instance.
	:type service_id: str

	:rtype: ServiceInfo
	"""
	service_info = get_application_services(app_instance_id=app_instance_id, ser_instance_id=[service_id])
	if len(service_info) == 1:
		return service_info[0]
	else:
		return ProblemDetails(title="service not found", status=404), 404


def app_services_service_id_put(body, app_instance_id, service_id):  # noqa: E501
	"""app_services_service_id_put

	This method updates the information about a mecService resource # noqa: E501

	:param body: New ServiceInfo with updated &quot;state&quot; is included as entity body of the request
	:type body: dict | bytes
	:param app_instance_id: Represents a MEC application instance. Note that the app_instance_id is allocated by the MEC platform manager.
	:type app_instance_id: str
	:param service_id: Represents a MEC service instance.
	:type service_id: str

	:rtype: ServiceInfo
	"""
	if connexion.request.is_json:
		body = ServiceInfo.from_dict(connexion.request.get_json())  # noqa: E501
	result = update_app_service(app_instance_id=app_instance_id, ser_instance_id=service_id, service=body)
	if result:
		return result
	return ProblemDetails(title="service not found", status=404), 404
