from swagger_server.controllers.internal.subscriptions_update_manager import update_subscriber
from swagger_server.models.MEC011_service_management.link_type import LinkType
from swagger_server.models.MEC011_service_management.model_self import ModelSelf
from swagger_server.models.MEC011_service_management.service_info import ServiceInfo  # noqa: E501
from swagger_server.models.MEC011_service_management.service_info_post import ServiceInfoPost
from swagger_server.models.MEC011_application_support.current_time import CurrentTime
from swagger_server.models.MEC011_service_management.ser_availability_notification_subscription import \
	SerAvailabilityNotificationSubscription
from datetime import datetime, timezone
import uuid

from swagger_server.models.internal.applications_information_data import add_application, AppAlreadyExists, \
	delete_application, AppNotReady, add_application_service, add_application_subscription, get_application_services, \
	get_application_subscriptions, get_all_services, delete_application_service, NoAppInformationFound, \
	delete_application_subscription, update_application_service
from swagger_server.models.internal.service_subscription_event import ServiceRegistered, ServiceDeleted, ServiceUpdated
from swagger_server.models.problem_details import ProblemDetails


def manage_application_confirm_ready(app_instance_id):
	try:
		add_application(app_instance_id)
		return 'Done', 204
	except AppAlreadyExists as exception:
		return ProblemDetails(title="Application already in ready state", detail=str(exception), status=404), 404


def manage_application_termination_ready(app_instance_id):
	try:
		delete_application(app_instance_id)
		return 'Done', 204
	except AppNotReady as exception:
		return ProblemDetails(title="Application is not in ready state", detail=str(exception), status=404), 404


def manage_add_application_service(app_instance_id, service: ServiceInfoPost):
	"""Add an exposed service for a specific application. If the application does not correspond to a ready one
	the method returns a ProblemDetails object."""

	try:
		service_id = str(uuid.uuid4())
		service_info = ServiceInfo(ser_instance_id=service_id, ser_name=service.ser_name,
		                           ser_category=service.ser_category, version=service.version, state=service.state,
		                           transport_info=service.transport_info, serializer=service.serializer,
		                           scope_of_locality=service.scope_of_locality,
		                           consumed_local_only=service.consumed_local_only, is_local=service.is_local)
		add_application_service(application_instance_id=app_instance_id, service_information=service_info)
		update_subscriber(ServiceRegistered(app_instance_id=app_instance_id, service_information=service_info))
		return service_info, 201, {
			"Location": f"/mec_service_mgmt/v1/applications/{app_instance_id}/services/{service_id}"}
	except AppNotReady as exception:
		return ProblemDetails(title="Application Id not found",
		                      detail=str(exception), status=404), 404


def manage_add_application_subscription(app_instance_id, subscription: SerAvailabilityNotificationSubscription):
	"""Add a subscription for a specific application. If the application does not correspond to a ready one
	the method returns a ProblemDetails object."""

	try:
		subscription_id = str(uuid.uuid4())
		subscription.ser_availability_notification_subscription_id = subscription_id
		subscription.links = ModelSelf(
			_self=LinkType(href=f"/mec_service_mgmt/v1/applications/{app_instance_id}/subscriptions/{subscription_id}"))
		add_application_subscription(application_instance_id=app_instance_id, subscription_information=subscription)
		return subscription, 201, {
			"Location": f"/mec_service_mgmt/v1/applications/{app_instance_id}/subscriptions/{subscription_id}"}
	except AppNotReady as exception:
		return ProblemDetails(title="Application Id not found",
		                      detail=str(exception), status=404), 404


def manage_get_application_services(app_instance_id, ser_instance_id=None, ser_name=None, ser_category_id=None,
                                    consumed_local_only=None,
                                    is_local=None, scope_of_locality=None):
	"""Return the list of application exposed services that match some filters. If the application does not correspond
	to a ready one the method returns a ProblemDetails object."""

	try:
		return get_application_services(application_instance_id=app_instance_id, filter_parameters_dictionary=locals())
	except AppNotReady as exception:
		return ProblemDetails(title="service not found", detail=str(exception), status=404), 404


def manage_get_application_subscriptions(app_instance_id, ser_availability_notification_subscription_id=None):
	"""Return the list of application subscription that match some filters. If the application does not correspond
	to a ready one the method returns a ProblemDetails object."""

	try:
		return get_application_subscriptions(application_instance_id=app_instance_id,
		                                     filter_parameters_dictionary=locals())
	except AppNotReady as exception:
		return ProblemDetails(title="service not found", detail=str(exception), status=404), 404


def manage_get_services(ser_instance_id=None, ser_name=None, ser_category_id=None, consumed_local_only=None,
                        is_local=None, scope_of_locality=None):
	"""Returns the list of all exposed services."""
	return get_all_services(locals())


def manage_delete_app_service(app_instance_id, ser_instance_id):
	"""Return an empty 204 message if the service elimination was performed correctly. If the application does not
	correspond to a ready one the method returns a ProblemDetails object. If the service is not exposed by application
	returns a ProblemDetails object."""

	try:
		delete_application_service(application_instance_id=app_instance_id, service_instance_id=ser_instance_id)
		update_subscriber(ServiceDeleted(app_instance_id=app_instance_id))
		return "Done", 204
	except AppNotReady as exception:
		return ProblemDetails(title="service not found", detail=str(exception), status=404), 404
	except NoAppInformationFound as exception:
		return ProblemDetails(title="service not found", detail=str(exception), status=404), 404


def manage_delete_application_subscription(app_instance_id, ser_availability_notification_subscription_id):
	"""Return an empty 204 message if the subscription elimination was performed correctly. If the application does not
	correspond to a ready one the method returns a ProblemDetails object. If the subscriptionId does not exists for
	specified application returns a ProblemDetails object."""
	try:
		delete_application_subscription(application_instance_id=app_instance_id,
		                                ser_availability_notification_subscription_id=ser_availability_notification_subscription_id)
		return "Done", 204
	except AppNotReady as exception:
		return ProblemDetails(title="subscription not found", detail=str(exception), status=404), 404
	except NoAppInformationFound as exception:
		return ProblemDetails(title="subscription not found", detail=str(exception), status=404), 404


def manage_update_application_service(app_instance_id, ser_instance_id, service):
	"""Return the updated service if the update procedure was performed correctly. If the application does not
	correspond to a ready one the method returns a ProblemDetails object. If the service is not exposed by application
	returns a ProblemDetails object."""

	try:
		updated_service = update_application_service(application_instance_id=app_instance_id,
		                                             service=service,
		                                             service_instance_id=ser_instance_id)
		update_subscriber(ServiceUpdated(app_instance_id=app_instance_id, service_information=updated_service))
		return updated_service
	except AppNotReady as exception:
		return ProblemDetails(title="service not found", detail=str(exception), status=404), 404
	except NoAppInformationFound as exception:
		return ProblemDetails(title="service not found", detail=str(exception), status=404), 404


def get_current_time():
	date = datetime.now(timezone.utc)
	current_time = CurrentTime(seconds=int(date.timestamp()), nano_seconds=0, time_source_status='TRACEABLE')
	return current_time
