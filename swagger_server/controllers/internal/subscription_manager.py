import os
import queue
import logging

from swagger_server.models.internal.service_subscription_event import ServiceSubscriptionEvent, ServiceRegistered, \
	ServiceUpdated, ServiceDeleted

task_queue = queue.Queue()
logger = logging.getLogger('console')


def update_subscriber(event: ServiceSubscriptionEvent):
	task_queue.put(event)


def manager():
	while True:
		event = task_queue.get()
		if isinstance(event, ServiceRegistered):
			logger.debug('Service registered')
		elif isinstance(event, ServiceUpdated):
			logger.debug('Service updated')
		elif isinstance(event, ServiceDeleted):
			logger.debug('Service deleted')
		task_queue.task_done()
