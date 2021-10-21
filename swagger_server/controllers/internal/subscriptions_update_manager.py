import queue
import logging
import requests
import swagger_server.encoder
from flask import json

from swagger_server.models.MEC011_service_management.service_availability_notification import \
	ServiceAvailabilityNotification
from swagger_server.models.MEC011_service_management.service_availability_notification_service_references import \
	ServiceAvailabilityNotificationServiceReferences
from swagger_server.models.MEC011_service_management.subscription import Subscription
from swagger_server.models.internal.applications_information_data import get_entity_to_update
from swagger_server.models.internal.service_subscription_event import ServiceSubscriptionEvent, ServiceRegistered, \
	ServiceUpdated, ServiceDeleted

task_queue = queue.Queue()


def update_subscriber(event: ServiceSubscriptionEvent):
	task_queue.put(event)


def service_registered_update(event):
	service_information = event.service_information
	callback_uris_and_links = get_entity_to_update(service_information)
	for callback_uri_and_link in callback_uris_and_links:
		service_registered_notification = ServiceAvailabilityNotification(
			notification_type="SerAvailabilityNotification",
			service_references=[
				ServiceAvailabilityNotificationServiceReferences(
					ser_name=getattr(service_information,
					                 'ser_name'),
					ser_instance_id=getattr(
						service_information,
						'ser_instance_id'),
					change_type="ADDED",
					state=getattr(service_information,
					              'state'),
					link={
						'href': f'/mec_service_mgmt/v1/applications/{event.app_instance_id}/services/{getattr(service_information, "ser_instance_id")}'})],
			links=Subscription(subscription=callback_uri_and_link['subscription_link']))
		requests.post(url=callback_uri_and_link['uri'],
		              data=json.dumps(service_registered_notification, cls=swagger_server.encoder.JSONEncoder,
		                              sort_keys=True))


def manager():
	while True:
		event = task_queue.get()
		if isinstance(event, ServiceRegistered):
			service_registered_update(event)
		elif isinstance(event, ServiceUpdated):
			logging.debug('Service updated')
		elif isinstance(event, ServiceDeleted):
			logging.debug('Service deleted')
		task_queue.task_done()
