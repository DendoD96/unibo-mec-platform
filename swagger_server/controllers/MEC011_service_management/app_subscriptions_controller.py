import connexion

from swagger_server.models.MEC011_service_management.mec_service_mgmt_api_subscription_link_list import MecServiceMgmtApiSubscriptionLinkList  # noqa: E501
from swagger_server.models.MEC011_service_management.ser_availability_notification_subscription import SerAvailabilityNotificationSubscription  # noqa: E501


def applications_subscription_delete(appInstanceId, subscriptionId):  # noqa: E501
    """applications_subscription_delete

    This method deletes a mecSrvMgmtSubscription. This method is typically used in 'Unsubscribing from service availability event notifications' procedure. # noqa: E501

    :param appInstanceId: Represents a MEC application instance. Note that the appInstanceId is allocated by the MEC platform manager.
    :type appInstanceId: str
    :param subscriptionId: Represents a subscription to the notifications from the MEC platform.
    :type subscriptionId: str

    :rtype: None
    """
    return 'do some magic!'


def applications_subscription_get(appInstanceId, subscriptionId):  # noqa: E501
    """applications_subscription_get

    The GET method requests information about a subscription for this requestor. Upon success, the response contains entity body with the subscription for the requestor. # noqa: E501

    :param appInstanceId: Represents a MEC application instance. Note that the appInstanceId is allocated by the MEC platform manager.
    :type appInstanceId: str
    :param subscriptionId: Represents a subscription to the notifications from the MEC platform.
    :type subscriptionId: str

    :rtype: SerAvailabilityNotificationSubscription
    """
    return 'do some magic!'


def applications_subscriptions_get(appInstanceId):  # noqa: E501
    """applications_subscriptions_get

    The GET method may be used to request information about all subscriptions for this requestor. Upon success, the response contains entity body with all the subscriptions for the requestor. # noqa: E501

    :param appInstanceId: Represents a MEC application instance. Note that the appInstanceId is allocated by the MEC platform manager.
    :type appInstanceId: str

    :rtype: MecServiceMgmtApiSubscriptionLinkList
    """
    return 'do some magic!'


def applications_subscriptions_post(body, appInstanceId):  # noqa: E501
    """applications_subscriptions_post

    The POST method may be used to create a new subscription. One example use case is to create a new subscription to the MEC service availability notifications. Upon success, the response contains entity body describing the created subscription. # noqa: E501

    :param body: Entity body in the request contains a subscription to the MEC application termination notifications that is to be created.
    :type body: dict | bytes
    :param appInstanceId: Represents a MEC application instance. Note that the appInstanceId is allocated by the MEC platform manager.
    :type appInstanceId: str

    :rtype: SerAvailabilityNotificationSubscription
    """
    if connexion.request.is_json:
        body = SerAvailabilityNotificationSubscription.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
