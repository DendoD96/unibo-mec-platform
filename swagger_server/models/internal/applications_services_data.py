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


def app_confirm_ready(app_instance_id):
	if app_instance_id not in app_ids:
		app_ids.setdefault(app_instance_id, {})
		return '204'
	return '404'


def app_termination_ready(app_instance_id):
	if app_instance_id in app_ids:
		del app_ids[app_instance_id]
		return '204'
	return '404'


def add_app_service(app_instance_id, service: ServiceInfoPost):
	if app_instance_id in app_ids:
		service_info = ServiceInfo(ser_instance_id=str(uuid.uuid4()), ser_name=service.ser_name,
		                           ser_category=service.ser_category, version=service.version, state=service.state,
		                           transport_info=service.transport_info, serializer=service.serializer,
		                           scope_of_locality=service.scope_of_locality,
		                           consumed_local_only=service.consumed_local_only, is_local=service.is_local)
		app_ids[app_instance_id].setdefault('servicelist', []).append(service_info)
		update_subscriber(ServiceRegistered(app_instance_id=app_instance_id, service_information=service_info))
		return service_info
	else:
		return ProblemDetails(title="Application Id not found", status=404)


def add_application_subscription(app_instance_id, subscription: SerAvailabilityNotificationSubscription):
	subscription.ser_availability_notification_subscription_id = str(uuid.uuid4())
	app_ids.setdefault(app_instance_id, {}).setdefault('subscriptionlist', []).append(subscription)
	return subscription


def get_application_services(app_instance_id, ser_instance_id=None, ser_name=None, ser_category_id=None,
                             consumed_local_only=None,
                             is_local=None, scope_of_locality=None):
	return __get_application_informations(app_instance_id=app_instance_id, parameters_dictionary=locals(),
	                                      information='servicelist')


def get_application_subscriptions(app_instance_id, subscription_id=None):
	return __get_application_informations(app_instance_id=app_instance_id, parameters_dictionary=locals(),
	                                      information='subscriptionlist')


def get_services(ser_instance_id=None, ser_name=None, ser_category_id=None, consumed_local_only=None,
                 is_local=None, scope_of_locality=None):
	app_services = []
	for app_id in app_ids:
		app_services.extend(
			get_application_services(app_id, ser_instance_id=ser_instance_id, ser_name=ser_name,
			                         ser_category_id=ser_category_id,
			                         consumed_local_only=consumed_local_only, is_local=is_local,
			                         scope_of_locality=scope_of_locality))
	return app_services


def delete_app_service(app_instance_id, ser_instance_id):
	result = __delete_service(app_instance_id, ser_instance_id)
	if result is not None:
		update_subscriber(ServiceDeleted(app_instance_id=app_instance_id))
	return result


def delete_application_subscription(app_instance_id, subscription_id):
	return __delete_app_subscription(app_instance_id, subscription_id)


def update_app_service(app_instance_id, ser_instance_id, service):
	services = __delete_service(app_instance_id, ser_instance_id)
	if services is not None:
		service.ser_instance_id = ser_instance_id
		services.append(service)
		update_subscriber(ServiceRegistered(app_instance_id=app_instance_id, service_information=service))
		return service
	return None


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
	informations = app_ids.get(app_instance_id, {}).get(information, [])
	information_length = len(informations)
	if information_length > 0:
		informations = [information for information in informations if filter_lambda(information)]
		if len(informations) < information_length:
			app_ids[app_instance_id][information] = informations
			return informations
	return None


def __get_application_informations(app_instance_id, parameters_dictionary, information):
	parameters = {k: v for k, v in parameters_dictionary.items() if v is not None and k != 'app_instance_id'}
	informations = app_ids.get(app_instance_id, {}).get(information, [])
	for k, v in parameters.items():
		if isinstance(v, list):
			informations = list(filter(lambda information: (getattr(information, k) in v), informations))
		else:
			informations = list(filter(lambda information: (getattr(information, k) == v), informations))
	return informations
