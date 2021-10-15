from swagger_server.controllers.internal.subscription_manager import update_subscriber
from swagger_server.models.MEC011_service_management.service_info import ServiceInfo  # noqa: E501
from swagger_server.models.MEC011_service_management.service_info_post import ServiceInfoPost
from swagger_server.models.MEC011_application_support.current_time import CurrentTime
from swagger_server.models.MEC011_service_management.ser_availability_notification_subscription import \
	SerAvailabilityNotificationSubscription
from datetime import datetime, timezone
import uuid

from swagger_server.models.internal.service_subscription_event import ServiceRegistered, ServiceDeleted
from swagger_server.models.problem_details import ProblemDetails

app_ids = {}


class AppNotReady(Exception):
	pass


class NoAppInformationFound(Exception):
	pass


def app_confirm_ready(app_instance_id):
	if app_instance_id not in app_ids:
		app_ids.setdefault(app_instance_id, {})
		return 'Done', 204
	return ProblemDetails(title="Application Id is already in ready state", status=404), 404


def app_termination_ready(app_instance_id):
	if app_instance_id in app_ids:
		del app_ids[app_instance_id]
		return 'Done', 204
	return ProblemDetails(title="Application Id is not in ready state", status=404), 404


def add_app_service(app_instance_id, service: ServiceInfoPost):
	"""Add an exposed service for a specific application. If the application does not correspond to a ready one
	the method returns a ProblemDetails object."""

	if app_instance_id in app_ids:
		service_id = str(uuid.uuid4())
		service_info = ServiceInfo(ser_instance_id=service_id, ser_name=service.ser_name,
		                           ser_category=service.ser_category, version=service.version, state=service.state,
		                           transport_info=service.transport_info, serializer=service.serializer,
		                           scope_of_locality=service.scope_of_locality,
		                           consumed_local_only=service.consumed_local_only, is_local=service.is_local)
		app_ids[app_instance_id].setdefault('servicelist', []).append(service_info)
		update_subscriber(ServiceRegistered(app_instance_id=app_instance_id, service_information=service_info))
		return service_info, 201, {
			"Location": f"/mec_service_mgmt/v1/applications/{app_instance_id}/services/{service_id}"}
	else:
		return ProblemDetails(title="Application Id not found",
		                      detail=f"{app_instance_id}  is not in ready applications list.", status=404), 404


def add_application_subscription(app_instance_id, subscription: SerAvailabilityNotificationSubscription):
	"""Add a subscription for a specific application. If the application does not correspond to a ready one
	the method returns a ProblemDetails object."""

	if app_instance_id in app_ids:
		subscription_id = str(uuid.uuid4())
		subscription.ser_availability_notification_subscription_id = subscription_id
		app_ids.setdefault(app_instance_id, {}).setdefault('subscriptionlist', []).append(subscription)
		return subscription, 201, {
			"Location": f"/mec_service_mgmt/v1/applications/{app_instance_id}/subscriptions/{subscription_id}"}
	else:
		return ProblemDetails(title="Application Id not found",
		                      detail=f"{app_instance_id}  is not in ready applications list.", status=404), 404


def get_application_services(app_instance_id, ser_instance_id=None, ser_name=None, ser_category_id=None,
                             consumed_local_only=None,
                             is_local=None, scope_of_locality=None):
	"""Return the list of application exposed services that match some filters. If the application does not correspond
	to a ready one the method returns a ProblemDetails object."""

	try:
		return __get_application_informations(app_instance_id=app_instance_id, filter_parameters_dictionary=locals(),
		                                      information='servicelist')
	except AppNotReady as exception:
		return ProblemDetails(title="service not found", detail=str(exception), status=404), 404


def get_application_subscriptions(app_instance_id, ser_availability_notification_subscription_id=None):
	"""Return the list of application subscription that match some filters. If the application does not correspond
	to a ready one the method returns a ProblemDetails object."""

	try:
		return __get_application_informations(app_instance_id=app_instance_id, filter_parameters_dictionary=locals(),
		                                      information='subscriptionlist')
	except AppNotReady as exception:
		return ProblemDetails(title="service not found", detail=str(exception), status=404), 404


def get_services(ser_instance_id=None, ser_name=None, ser_category_id=None, consumed_local_only=None,
                 is_local=None, scope_of_locality=None):
	"""Returns the list of all exposed services."""
	app_services = []
	for app_id in app_ids:
		# No AppNotReady exception can be raised because app_id in in app_ids (i.e the app is in ready state).
		app_services.extend(get_application_services(app_id, ser_instance_id=ser_instance_id, ser_name=ser_name,
		                                             ser_category_id=ser_category_id,
		                                             consumed_local_only=consumed_local_only, is_local=is_local,
		                                             scope_of_locality=scope_of_locality))
	return app_services


def delete_app_service(app_instance_id, ser_instance_id):
	"""Return an empty 204 message if the service elimination was performed correctly. If the application does not
	correspond to a ready one the method returns a ProblemDetails object. If the service is not exposed by application
	returns a ProblemDetails object."""

	try:
		__delete_service(app_instance_id, ser_instance_id)
		update_subscriber(ServiceDeleted(app_instance_id=app_instance_id))
		return "Done", 204
	except AppNotReady as exception:
		return ProblemDetails(title="service not found", detail=str(exception), status=404), 404
	except NoAppInformationFound as exception:
		return ProblemDetails(title="service not found", detail=str(exception), status=404), 404


def delete_application_subscription(app_instance_id, ser_availability_notification_subscription_id):
	"""Return an empty 204 message if the subscription elimination was performed correctly. If the application does not
	correspond to a ready one the method returns a ProblemDetails object. If the subscriptionId does not exists for
	specified application returns a ProblemDetails object."""
	try:
		__delete_app_subscription(app_instance_id, ser_availability_notification_subscription_id)
		return "Done", 204
	except AppNotReady as exception:
		return ProblemDetails(title="subscription not found", detail=str(exception), status=404), 404
	except NoAppInformationFound as exception:
		return ProblemDetails(title="subscription not found", detail=str(exception), status=404), 404


def update_app_service(app_instance_id, ser_instance_id, service):
	"""Return the updated service if the update procedure was performed correctly. If the application does not
	correspond to a ready one the method returns a ProblemDetails object. If the service is not exposed by application
	returns a ProblemDetails object."""

	try:
		services = __delete_service(app_instance_id, ser_instance_id)
		service.ser_instance_id = ser_instance_id
		services.append(service)
		update_subscriber(ServiceRegistered(app_instance_id=app_instance_id, service_information=service))
		return service
	except AppNotReady as exception:
		return ProblemDetails(title="service not found", detail=str(exception), status=404), 404
	except NoAppInformationFound as exception:
		return ProblemDetails(title="service not found", detail=str(exception), status=404), 404


def get_current_time():
	date = datetime.now(timezone.utc)
	current_time = CurrentTime(seconds=int(date.timestamp()), nano_seconds=0, time_source_status='TRACEABLE')
	return current_time


def __delete_service(app_instance_id, ser_instance_id):
	return __delete_app_information(app_instance_id, 'servicelist',
	                                lambda service: service.ser_instance_id != ser_instance_id)


def __delete_app_subscription(app_instance_id, subscription_id):
	return __delete_app_information(app_instance_id, 'subscriptionlist', lambda
		subscription: subscription.ser_availability_notification_subscription_id != subscription_id)


def __delete_app_information(app_instance_id, information, filter_lambda):
	"""Return the deleted informations that match some filters about a specific application. If the specified
	application id does not correspond to a ready application the method raise an exception. If the application does
	not have the information to delete it raise an exception."""

	if app_instance_id in app_ids:
		informations = app_ids[app_instance_id].get(information, [])
		information_length = len(informations)
		if information_length > 0:
			informations = [information for information in informations if filter_lambda(information)]
			if len(informations) < information_length:
				app_ids[app_instance_id][information] = informations
				return informations
		raise NoAppInformationFound(f"{app_instance_id} does not have the information to delete.")
	else:
		raise AppNotReady(f"{app_instance_id} is not in ready applications list.")


def __get_application_informations(app_instance_id, filter_parameters_dictionary, information):
	"""Return informations that match some filters about a specific application. If the specified application id
	does not correspond to a ready application the method raise an exception."""
	if app_instance_id in app_ids:
		parameters = {parameter_name: parameter_value for parameter_name, parameter_value in
		              filter_parameters_dictionary.items() if
		              parameter_value is not None and parameter_name != 'app_instance_id'}
		informations = app_ids[app_instance_id].get(information, [])
		for parameter_key, parameter_value in parameters.items():
			if isinstance(parameter_value, list):
				informations = list(
					filter(lambda information_attribute: (
							getattr(information_attribute, parameter_key) in parameter_value), informations))
			else:
				informations = list(
					filter(lambda information_attribute: (
							getattr(information_attribute, parameter_key) == parameter_value), informations))
		return informations
	else:
		raise AppNotReady(f"{app_instance_id}  is not in ready applications list")
