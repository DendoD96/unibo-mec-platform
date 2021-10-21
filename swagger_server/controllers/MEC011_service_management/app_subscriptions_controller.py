import connexion

from swagger_server.models.MEC011_service_management.ser_availability_notification_subscription import \
	SerAvailabilityNotificationSubscription  # noqa: E501
from swagger_server.controllers.internal.applications_information_manager import manage_get_application_subscriptions
from swagger_server.controllers.internal.applications_information_manager import manage_add_application_subscription
from swagger_server.controllers.internal.applications_information_manager import manage_delete_application_subscription
from swagger_server.models.problem_details import ProblemDetails


def applications_subscription_delete(app_instance_id, subscription_id):  # noqa: E501
	"""applications_subscription_delete

    This method deletes a mecSrvMgmtSubscription. This method is typically used in 'Unsubscribing from service availability event notifications' procedure. # noqa: E501

    :param app_instance_id: Represents a MEC application instance. Note that the app_instance_id is allocated by the MEC platform manager.
    :type app_instance_id: str
    :param subscription_id: Represents a subscription to the notifications from the MEC platform.
    :type subscription_id: str

    :rtype: None
    """
	return manage_delete_application_subscription(app_instance_id=app_instance_id,
	                                              ser_availability_notification_subscription_id=subscription_id)


def applications_subscription_get(app_instance_id, subscription_id):  # noqa: E501
	"""applications_subscription_get

    The GET method requests information about a subscription for this requestor. Upon success, the response contains entity body with the subscription for the requestor. # noqa: E501

    :param app_instance_id: Represents a MEC application instance. Note that the app_instance_id is allocated by the MEC platform manager.
    :type app_instance_id: str
    :param subscription_id: Represents a subscription to the notifications from the MEC platform.
    :type subscription_id: str

    :rtype: SerAvailabilityNotificationSubscription
    """
	# result can be:
	#   a tuple2 (ProblemDetails,status_code) if the application is not in ready state
	#   an empty list if the service does not exist
	#   a list of one element that contains the service
	result = manage_get_application_subscriptions(app_instance_id=app_instance_id,
	                                              ser_availability_notification_subscription_id=subscription_id)
	if len(result) == 1:
		return result[0]
	elif len(result) == 0:
		return ProblemDetails(title="subscription not found",
		                      detail=f"Subscription with id {subscription_id} is not exposed by app with id "
		                             f"{app_instance_id}",
		                      status=404), 404
	elif isinstance(result, tuple):
		return result


def applications_subscriptions_get(app_instance_id):  # noqa: E501
	"""applications_subscriptions_get

    The GET method may be used to request information about all subscriptions for this requestor. Upon success, the response contains entity body with all the subscriptions for the requestor. # noqa: E501

    :param app_instance_id: Represents a MEC application instance. Note that the app_instance_id is allocated by the MEC platform manager.
    :type app_instance_id: str

    :rtype: MecServiceMgmtApiSubscriptionLinkList
    """
	result = manage_get_application_subscriptions(app_instance_id=app_instance_id)
	# TODO: Compose the correct response
	return result


def applications_subscriptions_post(body, app_instance_id):  # noqa: E501
	"""applications_subscriptions_post

    The POST method may be used to create a new subscription. One example use case is to create a new subscription to the MEC service availability notifications. Upon success, the response contains entity body describing the created subscription. # noqa: E501

    :param body: Entity body in the request contains a subscription to the MEC application termination notifications that is to be created.
    :type body: dict | bytes
    :param app_instance_id: Represents a MEC application instance. Note that the app_instance_id is allocated by the MEC platform manager.
    :type app_instance_id: str

    :rtype: SerAvailabilityNotificationSubscription
    """
	if connexion.request.is_json:
		body = SerAvailabilityNotificationSubscription.from_dict(connexion.request.get_json())  # noqa: E501
	return manage_add_application_subscription(app_instance_id, body)
