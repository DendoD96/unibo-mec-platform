import re
from functools import partial

from swagger_server.models.MEC011_service_management.ser_availability_notification_subscription import \
	SerAvailabilityNotificationSubscription

REGEX_FOR_SUBSCRIPTION_ID = r"\/mec_service_mgmt\/v1\/applications\/.*\/subscriptions\/(.*)"
app_ids = {}


class AppNotReady(Exception):
	pass


class NoAppInformationFound(Exception):
	pass


class AppAlreadyExists(Exception):
	pass


def add_application(application_instance_id):
	if application_instance_id not in app_ids:
		app_ids.setdefault(application_instance_id, {})
	else:
		raise AppAlreadyExists(f"Application with id {application_instance_id} is not in ready state")


def delete_application(application_instance_id):
	if application_instance_id in app_ids:
		del app_ids[application_instance_id]
	else:
		raise AppNotReady(f"Application with id {application_instance_id} is not in ready state")


def add_application_service(application_instance_id, service_information):
	if application_instance_id in app_ids:
		app_ids[application_instance_id].setdefault('servicelist', []).append(service_information)
	else:
		raise AppNotReady(f"Application with id {application_instance_id} is not in ready state")


def add_application_subscription(application_instance_id, subscription_information):
	if application_instance_id in app_ids:
		app_ids[application_instance_id].setdefault('subscriptionlist', []).append(subscription_information)
	else:
		raise AppNotReady(f"Application with id {application_instance_id} is not in ready state")


def get_application_services(application_instance_id, filter_parameters_dictionary):
	return __get_application_informations(app_instance_id=application_instance_id,
	                                      filter_parameters_dictionary=filter_parameters_dictionary,
	                                      information='servicelist')


def get_application_subscriptions(application_instance_id, subscription_id):
	if application_instance_id in app_ids:
		subscriptions = app_ids[application_instance_id].get("subscriptionlist", [])
		if subscription_id is not None:
			subscriptions = list(
				filter(partial(__subscription_match_subscription_id, subscription_id=subscription_id), subscriptions))
		return subscriptions
	else:
		raise AppNotReady(f"{application_instance_id}  is not in ready applications list")


def get_all_services(filter_parameters_dictionary):
	app_services = []
	for app_id in app_ids:
		# No AppNotReady exception can be raised because app_id in in app_ids (i.e the app is in ready state).
		app_services.extend(get_application_services(application_instance_id=app_id,
		                                             filter_parameters_dictionary=filter_parameters_dictionary))
	return app_services


def delete_application_service(application_instance_id, service_instance_id):
	return __delete_app_information(application_instance_id, 'servicelist',
	                                lambda service: service.ser_instance_id != service_instance_id)


def delete_application_subscription(application_instance_id, subscription_id):
	if application_instance_id in app_ids:
		subscriptions = app_ids[application_instance_id].get("subscriptionlist", [])
		subscriptions_length = len(subscriptions)
		if subscriptions_length > 0:
			subscriptions = list(
				filter(lambda subscription: not __subscription_match_subscription_id(subscription=subscription,
				                                                                     subscription_id=subscription_id),
				       subscriptions))
			if len(subscriptions) < subscriptions_length:
				app_ids[application_instance_id]["subscriptionlist"] = subscriptions
				return subscriptions
		raise NoAppInformationFound(f"{application_instance_id} does not have the information to delete.")
	else:
		raise AppNotReady(f"{application_instance_id} is not in ready applications list.")


def update_application_service(application_instance_id, service_instance_id, service):
	services = delete_application_service(application_instance_id=application_instance_id,
	                                      service_instance_id=service_instance_id)
	service.ser_instance_id = service_instance_id
	services.append(service)
	return service


def get_entity_to_update(service_info):
	callback_urls = []
	for _, app_info in app_ids.items():
		try:
			subscriptions = app_info['subscriptionlist']
			for subscription in subscriptions:
				if __check_match_between_service_and_subscription(service_info, subscription):
					callback_urls.append({'uri': getattr(subscription, 'callback_reference'),
					                      'subscription_link': getattr(getattr(subscription, 'links'), '_self')})
		except KeyError:
			pass
	return callback_urls


def __check_match_between_service_and_subscription(service_information, subscription):
	def service_category_to_dict(service_category):
		return {'href': getattr(service_category, 'href'),
		        'id': getattr(service_category, 'id'),
		        'name': getattr(service_category, 'name'),
		        'version': getattr(service_category, 'version')}

	filtering_criteria = getattr(subscription, 'filtering_criteria')
	service_instance_ids = getattr(filtering_criteria, 'ser_instance_ids')
	service_names = getattr(filtering_criteria, 'ser_names')
	service_categories = getattr(filtering_criteria, 'ser_categories')
	service_states = getattr(filtering_criteria, 'states')
	service_is_local = getattr(filtering_criteria, 'is_local')
	tests = [service_instance_ids is None or getattr(service_information, 'ser_instance_id') in service_instance_ids,
	         service_names is None or getattr(service_information, 'ser_name') in service_names,
	         service_categories is None or service_category_to_dict(
		         getattr(service_information, 'ser_category')) in service_categories,
	         service_states is None or getattr(service_information, 'state') in service_states,
	         service_is_local is None or getattr(service_information, 'is_local') == service_is_local]
	return all(tests)


def __delete_app_information(app_instance_id, information, filter_lambda):
	"""Return the new informations without the deleted ones. If the specified application id does not correspond to a
	ready application the method raise an exception. If the application does
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


def __subscription_match_subscription_id(subscription: SerAvailabilityNotificationSubscription, subscription_id):
	return re.search(pattern=REGEX_FOR_SUBSCRIPTION_ID, string=str(subscription.links._self.href)).group(1) \
	       == subscription_id
