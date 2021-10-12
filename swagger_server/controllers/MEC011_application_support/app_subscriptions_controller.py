import connexion

from swagger_server.models.MEC011_application_support.app_termination_notification_subscription import \
	AppTerminationNotificationSubscription  # noqa: E501


def applications_subscription_delete(app_instance_id, subscription_id):  # noqa: E501
	"""applications_subscription_delete

	This method deletes a mecAppSuptApiSubscription. This method is typically used in 'Unsubscribing from service availability event notifications' procedure. # noqa: E501

	:param app_instance_id: Represents a MEC application instance. Note that the app_instance_id is allocated by the MEC platform manager.
	:type app_instance_id: str
	:param subscription_id: Represents a subscription to the notifications from the MEC platform.
	:type subscription_id: str

	:rtype: None
	"""
	return 'do some magic!'


def applications_subscription_get(app_instance_id, subscription_id):  # noqa: E501
	"""applications_subscription_get

	The GET method requests information about a subscription for this requestor. Upon success, the response contains entity body with the subscription for the requestor. # noqa: E501

	:param app_instance_id: Represents a MEC application instance. Note that the app_instance_id is allocated by the MEC platform manager.
	:type app_instance_id: str
	:param subscription_id: Represents a subscription to the notifications from the MEC platform.
	:type subscription_id: str

	:rtype: AppTerminationNotificationSubscription
	"""
	return 'do some magic!'


def applications_subscriptions_get(app_instance_id):  # noqa: E501
	"""applications_subscriptions_get

	The GET method may be used to request information about all subscriptions for this requestor. Upon success, the response contains entity body with all the subscriptions for the requestor. # noqa: E501

	:param app_instance_id: Represents a MEC application instance. Note that the app_instance_id is allocated by the MEC platform manager.
	:type app_instance_id: str

	:rtype: MecAppSuptApiSubscriptionLinkList
	"""
	return 'do some magic!'


def applications_subscriptions_post(body, app_instance_id):  # noqa: E501
	"""applications_subscriptions_post

	The POST method may be used to create a new subscription. One example use case is to create a new subscription to the MEC service availability notifications. Upon success, the response contains entity body describing the created subscription. # noqa: E501

	:param body: Entity body in the request contains a subscription to the MEC application termination notifications that is to be created.
	:type body: dict | bytes
	:param app_instance_id: Represents a MEC application instance. Note that the app_instance_id is allocated by the MEC platform manager.
	:type app_instance_id: str

	:rtype: AppTerminationNotificationSubscription
	"""
	if connexion.request.is_json:
		body = AppTerminationNotificationSubscription.from_dict(connexion.request.get_json())  # noqa: E501
	return 'do some magic!'
