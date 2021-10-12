import connexion

from swagger_server.models.MEC016_device_application_interface.app_context import AppContext  # noqa: E501
from swagger_server.models.MEC016_device_application_interface.application_location_availability import \
	ApplicationLocationAvailability  # noqa: E501


def app_location_availability_post(body):  # noqa: E501
	"""Obtain the location constraints for a new application context.

	Used to obtain the locations available for instantiation of a specific user application in the MEC system. # noqa: E501

	:param body: Entity body in the request contains the user application information for the MEC system to evaluate the locations available for instantiation of that application.
	:type body: dict | bytes

	:rtype: ApplicationLocationAvailability
	"""
	if connexion.request.is_json:
		body = ApplicationLocationAvailability.from_dict(connexion.request.get_json())  # noqa: E501
	return 'do some magic!'


def dev_app_context_delete(context_id):  # noqa: E501
	"""Deletion of an existing application context.

	Used to delete the resource that represents the existing application context. # noqa: E501

	:param context_id: Uniquely identifies the application context in the MEC system. It is assigned by the MEC system.
	:type context_id: str

	:rtype: None
	"""
	return 'do some magic!'


def dev_app_context_put(body, context_id):  # noqa: E501
	"""Updating the callbackReference and/or appLocation of an existing application context.

	Used to update the callback reference and/or application location constraints of an existing application context. Upon successful operation, the target resource is updated with the new application context information. # noqa: E501

	:param body: Only the callbackReference and/or appLocation attribute values are allowed to be updated. Other attributes and their values shall remain untouched.
	:type body: dict | bytes
	:param context_id: Uniquely identifies the application context in the MEC system. It is assigned by the MEC system.
	:type context_id: str

	:rtype: None
	"""
	if connexion.request.is_json:
		body = AppContext.from_dict(connexion.request.get_json())  # noqa: E501
	return 'do some magic!'


def dev_app_contexts_get(body):  # noqa: E501
	"""Creation of a new application context.

	Used to create a new application context. Upon success, the response contains entity body describing the created application context. # noqa: E501

	:param body: Entity body in the request contains the Application Context as requested by the device application.
	:type body: dict | bytes

	:rtype: AppContext
	"""
	if connexion.request.is_json:
		body = AppContext.from_dict(connexion.request.get_json())  # noqa: E501
	return 'do some magic!'


def me_app_list_get(app_name=None, app_provider=None, app_soft_version=None, vendor_id=None,
                    service_cont=None):  # noqa: E501
	"""Get available application information.

	Used to query information about the available MEC applications. # noqa: E501

	:param app_name: Name to identify the MEC application.
	:type app_name: List[str]
	:param app_provider: Provider of the MEC application.
	:type app_provider: List[str]
	:param app_soft_version: Software version of the MEC application.
	:type app_soft_version: List[str]
	:param vendor_id: Vendor identifier
	:type vendor_id: List[str]
	:param service_cont: Required service continuity mode for this application. Permitted values: 0 &#x3D; SERVICE_CONTINUITY_NOT_REQUIRED. 1 &#x3D; SERVICE_CONTINUITY_REQUIRED.
	:type service_cont: int

	:rtype: ApplicationList
	"""
	return 'do some magic!'
