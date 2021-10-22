import queue
import requests
import swagger_server.encoder
from flask import json

from swagger_server.models.MEC011_service_management.service_availability_notification import \
	ServiceAvailabilityNotification
from swagger_server.models.MEC011_service_management.service_availability_notification_service_references import \
	ServiceAvailabilityNotificationServiceReferences
from swagger_server.models.MEC011_service_management.subscription import Subscription
from swagger_server.models.internal.applications_information_data import get_entity_to_update
from swagger_server.models.internal.service_subscription_event import ServiceSubscriptionEvent

task_queue = queue.Queue()


def update_subscriber(event: ServiceSubscriptionEvent):
	task_queue.put(event)


def service_update(event):
	def get_service_availability_notification_service_references():
		service_references = ServiceAvailabilityNotificationServiceReferences(
			ser_name=getattr(service_information,
			                 'ser_name'),
			ser_instance_id=getattr(
				service_information,
				'ser_instance_id'),
			change_type=event.change_type,
			state=getattr(service_information,
			              'state'))
		if event.change_type != "REMOVED":
			service_references.link = {
				'href': f'/mec_service_mgmt/v1/applications/{event.app_instance_id}/services/{getattr(service_information, "ser_instance_id")}'}
		return service_references

	def get_service_availability_notification():
		return ServiceAvailabilityNotification(
			notification_type="SerAvailabilityNotification",
			service_references=[get_service_availability_notification_service_references()],
			links=Subscription(subscription=callback_uri_and_link['subscription_link']))

	service_information = event.service_information
	callback_uris_and_links = get_entity_to_update(service_information)
	for callback_uri_and_link in callback_uris_and_links:
		requests.post(url=callback_uri_and_link['uri'],
		              data=json.dumps(get_service_availability_notification(),
		                              cls=swagger_server.encoder.JSONEncoder,
		                              sort_keys=True))


def manager():
	while True:
		event = task_queue.get()
		service_update(event)
		task_queue.task_done()
