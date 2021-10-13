import queue
import logging

from swagger_server.models.internal.service_subscription_event import ServiceSubscriptionEvent, ServiceRegistered, \
	ServiceUpdated, ServiceDeleted

task_queue = queue.Queue()


def update_subscriber(event: ServiceSubscriptionEvent):
	task_queue.put(event)


def manager():
	while True:
		event = task_queue.get()
		if isinstance(event, ServiceRegistered):
			logging.debug('Service registered')
		elif isinstance(event, ServiceUpdated):
			logging.debug('Service updated')
		elif isinstance(event, ServiceDeleted):
			logging.debug('Service deleted')
		task_queue.task_done()
