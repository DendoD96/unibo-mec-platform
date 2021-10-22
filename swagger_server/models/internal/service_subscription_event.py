class ServiceSubscriptionEvent:
	def __init__(self, app_instance_id, service_information, change_type):
		self.app_instance_id = app_instance_id
		self.service_information = service_information
		self.change_type = change_type
