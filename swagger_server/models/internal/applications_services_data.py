from swagger_server.models.MEC011_service_management.service_info import ServiceInfo  # noqa: E501
from swagger_server.models.MEC011_service_management.service_info_post import ServiceInfoPost
from swagger_server.models.MEC011_application_support.current_time import CurrentTime
from swagger_server.models.MEC011_service_management.ser_availability_notification_subscription import SerAvailabilityNotificationSubscription
from datetime import datetime, timezone
import uuid

app_ids = {}


def add_app_service(app_instance_id, service: ServiceInfoPost):
	service_info = ServiceInfo(ser_instance_id=str(uuid.uuid4()), ser_name=service.ser_name,
	                           ser_category=service.ser_category, version=service.version, state=service.state,
	                           transport_info=service.transport_info, serializer=service.serializer,
	                           scope_of_locality=service.scope_of_locality,
	                           consumed_local_only=service.consumed_local_only, is_local=service.is_local)
	app_ids.setdefault(app_instance_id, {}).setdefault('servicelist', []).append(service_info)
	return service_info


def get_app_service(app_instance_id, ser_instance_id=None, ser_name=None, ser_category_id=None,
                    consumed_local_only=None,
                    is_local=None, scope_of_locality=None):
	app_services = app_ids.get(app_instance_id, {}).get('servicelist', [])
	if ser_instance_id:
		app_services = list(
			filter(lambda service_info: (service_info.ser_instance_id in ser_instance_id), app_services))
	if ser_name:
		app_services = list(
			filter(lambda service_info: (service_info.ser_name in ser_name), app_services))
	if ser_category_id:
		app_services = list(
			filter(lambda service_info: (service_info.ser_category_id == ser_category_id), app_services))
	if consumed_local_only:
		app_services = list(
			filter(lambda service_info: (service_info.consumed_local_only == consumed_local_only), app_services))
	if is_local:
		app_services = list(
			filter(lambda service_info: (service_info.is_local == is_local), app_services))
	if scope_of_locality:
		app_services = list(
			filter(lambda service_info: (service_info.scope_of_locality == scope_of_locality), app_services))

	return app_services


def get_services(ser_instance_id=None, ser_name=None, ser_category_id=None, consumed_local_only=None,
				 is_local=None, scope_of_locality=None):
	app_services = []
	for app_id in app_ids:
		app_services.extend(app_ids.get(app_id, {}).get('servicelist', []))
	if ser_instance_id:
		app_services = list(
			filter(lambda service_info: (service_info.ser_instance_id in ser_instance_id), app_services))
	if ser_name:
		app_services = list(
			filter(lambda service_info: (service_info.ser_name in ser_name), app_services))
	if ser_category_id:
		app_services = list(
			filter(lambda service_info: (service_info.ser_category_id == ser_category_id), app_services))
	if consumed_local_only:
		app_services = list(
			filter(lambda service_info: (service_info.consumed_local_only == consumed_local_only), app_services))
	if is_local:
		app_services = list(
			filter(lambda service_info: (service_info.is_local == is_local), app_services))
	if scope_of_locality:
		app_services = list(
			filter(lambda service_info: (service_info.scope_of_locality == scope_of_locality), app_services))
	return app_services


def __delete_service(app_instance_id, ser_instance_id):
	services = app_ids.get(app_instance_id, {}).get('servicelist', [])
	if len(services) > 0:
		services = [service for service in services if service.ser_instance_id != ser_instance_id]
		app_ids[app_instance_id]['servicelist']=services
		#TODO if len(services) > 0 but ser_instance_id not in services still replies with 204 instead of 404
		return services
	return None

def __delete_app_subscription(app_instance_id, subscription_id):
	subscriptions = app_ids.get(app_instance_id, {}).get('subscriptionlist', [])
	if len(subscriptions) > 0:
		subscriptions = [subscription for subscription in subscriptions if subscription.ser_availability_notification_subscription_id != subscription_id]
		app_ids[app_instance_id]['subscriptionlist']=subscriptions
		#TODO if len(subscriptions) > 0 but subscription_id not in app_sub still replies with 204 instead of 404
		return subscriptions
	return None

def delete_app_service(app_instance_id, ser_instance_id):
	return __delete_service(app_instance_id, ser_instance_id)


def update_app_service(app_instance_id, ser_instance_id, service):
	services = __delete_service(app_instance_id, ser_instance_id)
	if services is not None:
		service.ser_instance_id = ser_instance_id
		services.append(service)
		return service
	return None

def get_current_time():
	date =  datetime.now(timezone.utc)
	current_time = CurrentTime(seconds=int(date.timestamp()),nano_seconds=0,time_source_status='TRACEABLE')
	return current_time

def clean_up():
	app_ids.clear()

def get_application_subscriptions(app_instance_id, subscription_id=None):
	app_subscriptions = app_ids.get(app_instance_id, {}).get('subscriptionlist', [])
	if subscription_id:
	#TODO the subscription_id is not part of the standard MEC011 Subscription model (in v2.1.1)
	#TODO v2 added ser_availability_notification_subscription_id in the openAPI definition
		app_subscriptions = list(
			filter(lambda subscription_info: (subscription_info.ser_availability_notification_subscription_id == subscription_id), app_subscriptions))
	return subscription_id

def add_application_subscription(app_instance_id, subscription: SerAvailabilityNotificationSubscription):
	subscription.ser_availability_notification_subscription_id = str(uuid.uuid4())
	app_ids.setdefault(app_instance_id, {}).setdefault('subscriptionlist', []).append(subscription)
	return subscription

def delete_application_subscription(app_instance_id, subscription_id):
	return __delete_app_subscription(app_instance_id, subscription_id)