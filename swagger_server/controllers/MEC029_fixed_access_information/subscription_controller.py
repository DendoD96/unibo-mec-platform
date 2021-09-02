import connexion

from swagger_server.models.MEC029_fixed_access_information.subscriptions_body import SubscriptionsBody  # noqa: E501
from swagger_server.models.MEC029_fixed_access_information.subscriptions_subscription_id_body import SubscriptionsSubscriptionIdBody  # noqa: E501


def individual_subscription_delete(subscriptionId):  # noqa: E501
    """Used to cancel the existing subscription.

    Used to cancel the existing subscription. # noqa: E501

    :param subscriptionId: Refers to created subscription, where the FAI API allocates a unique resource name for this subscription
    :type subscriptionId: str

    :rtype: None
    """
    return 'do some magic!'


def individual_subscription_get(subscriptionId):  # noqa: E501
    """Retrieve information about this subscription.

    Retrieve information about this subscription. # noqa: E501

    :param subscriptionId: Refers to created subscription, where the FAI API allocates a unique resource name for this subscription
    :type subscriptionId: str

    :rtype: SubscriptionsBody
    """
    return 'do some magic!'


def individual_subscription_put(body, subscriptionId):  # noqa: E501
    """Used to update the existing subscription.

    Used to update the existing subscription. # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param subscriptionId: Refers to created subscription, where the FAI API allocates a unique resource name for this subscription
    :type subscriptionId: str

    :rtype: SubscriptionsSubscriptionIdBody
    """
    if connexion.request.is_json:
        body = SubscriptionsSubscriptionIdBody.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def sub_get(subscription_type=None):  # noqa: E501
    """request information about the subscriptions for this requestor.

    request information about the subscriptions for this requestor. # noqa: E501

    :param subscription_type: Query parameter to filter on a specific subscription type. Permitted values: ONU_ALARM. DEVICE_ABNORMAL_ALERT. CM_CONNECTIVITY_STATE.  ANI_ALARM.
    :type subscription_type: str

    :rtype: SubscriptionLinkList
    """
    return 'do some magic!'


def sub_post(body):  # noqa: E501
    """ create a new subscription to FAI notifications.

     create a new subscription to FAI notifications. # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: SubscriptionsBody
    """
    if connexion.request.is_json:
        body = SubscriptionsBody.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
