class ServiceSubscriptionEvent:
	def __init__(self, app_instance_id, service_information=None):
		self.app_instance_id = app_instance_id
		self.service_information = service_information


class ServiceRegistered(ServiceSubscriptionEvent):
	def __init__(self, app_instance_id, service_information):
		super().__init__(app_instance_id=app_instance_id, service_information=service_information)


class ServiceUpdated(ServiceSubscriptionEvent):
	def __init__(self, app_instance_id, service_information):
		super().__init__(app_instance_id=app_instance_id, service_information=service_information)


class ServiceDeleted(ServiceSubscriptionEvent):
	def __init__(self, app_instance_id):
		super().__init__(app_instance_id=app_instance_id)
