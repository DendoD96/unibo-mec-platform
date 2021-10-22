import connexion

from swagger_server.models.MEC013_location.area_circle_body import AreaCircleBody  # noqa: E501
from swagger_server.models.MEC013_location.circle_subscription_id_body import CircleSubscriptionIdBody  # noqa: E501
from swagger_server.models.MEC013_location.distance_subscription_id_body import DistanceSubscriptionIdBody  # noqa: E501
from swagger_server.models.MEC013_location.periodic_subscription_id_body import PeriodicSubscriptionIdBody  # noqa: E501
from swagger_server.models.MEC013_location.subscriptions_distance_body import SubscriptionsDistanceBody  # noqa: E501
from swagger_server.models.MEC013_location.subscriptions_periodic_body import SubscriptionsPeriodicBody  # noqa: E501
from swagger_server.models.MEC013_location.subscriptions_user_tracking_body import \
	SubscriptionsUserTrackingBody  # noqa: E501
from swagger_server.models.MEC013_location.subscriptions_zonal_traffic_body import \
	SubscriptionsZonalTrafficBody  # noqa: E501
from swagger_server.models.MEC013_location.subscriptions_zone_status_body import \
	SubscriptionsZoneStatusBody  # noqa: E501
from swagger_server.models.MEC013_location.user_tracking_subscription_id_body import \
	UserTrackingSubscriptionIdBody  # noqa: E501
from swagger_server.models.MEC013_location.zonal_traffic_subscription_id_body import \
	ZonalTrafficSubscriptionIdBody  # noqa: E501
from swagger_server.models.MEC013_location.zone_status_subscription_id_body import \
	ZoneStatusSubscriptionIdBody  # noqa: E501


def ap_by_id_get(zone_id, access_point_id):  # noqa: E501
	"""Radio Node Location Lookup

    Radio Node Location Lookup to retrieve a radio node associated to a zone. # noqa: E501

    :param zone_id: Indentifier of zone
    :type zone_id: str
    :param access_point_id: Identifier of access Point
    :type access_point_id: str

    :rtype: InlineResponse2005
    """

	return 'do some magic!'


def ap_get(zone_id, interest_realm=None):  # noqa: E501
	"""Radio Node Location Lookup

    Radio Node Location Lookup to retrieve a list of radio nodes associated to a zone. # noqa: E501

    :param zone_id: Indentifier of zone
    :type zone_id: str
    :param interest_realm: Interest realm of access point (e.g. geographical area, a type of industry etc.).
    :type interest_realm: str

    :rtype: InlineResponse2004
    """
	return 'do some magic!'


def area_circle_sub_delete(subscription_id):  # noqa: E501
	"""Cancel a subscription

    Method to delete a subscription. # noqa: E501

    :param subscription_id: Subscription Identifier, specifically the 'self' returned in the subscription request
    :type subscription_id: str

    :rtype: None
    """
	return 'do some magic!'


def area_circle_sub_get(subscription_id):  # noqa: E501
	"""Retrieve subscription information

    Get subscription information. # noqa: E501

    :param subscription_id: Subscription Identifier, specifically the 'self' returned in the subscription request
    :type subscription_id: str

    :rtype: InlineResponse2007
    """
	return 'do some magic!'


def area_circle_sub_list_get():  # noqa: E501
	"""Retrieves all active subscriptions to area change notifications

    This operation is used for retrieving all active subscriptions to area change notifications. # noqa: E501


    :rtype: InlineResponse2006
    """
	return 'do some magic!'


def area_circle_sub_post(body):  # noqa: E501
	"""Creates a subscription for area change notification

    Creates a subscription to the Location Service for an area change notification. # noqa: E501

    :param body: Subscription to be created
    :type body: dict | bytes

    :rtype: InlineResponse201
    """
	if connexion.request.is_json:
		body = AreaCircleBody.from_dict(connexion.request.get_json())  # noqa: E501
	return 'do some magic!'


def area_circle_sub_put(body, subscription_id):  # noqa: E501
	"""Updates a subscription information

    Updates a subscription. # noqa: E501

    :param body: Subscription to be modified
    :type body: dict | bytes
    :param subscription_id: Subscription Identifier, specifically the 'self' returned in the subscription request
    :type subscription_id: str

    :rtype: CircleSubscriptionIdBody
    """
	if connexion.request.is_json:
		body = CircleSubscriptionIdBody.from_dict(connexion.request.get_json())  # noqa: E501
	return 'do some magic!'


def distance_get(address, requester=None, latitude=None, longitude=None):  # noqa: E501
	"""UE Distance Lookup of a specific UE

    UE Distance Lookup between terminals or a terminal and a location # noqa: E501

    :param address: address of users (e.g. 'sip' URI, 'tel' URI, 'acr' URI)
    :type address: List[str]
    :param requester: Entity that is requesting the information
    :type requester: str
    :param latitude: Latitude geo position
    :type latitude: float
    :param longitude: Longitude geo position
    :type longitude: float

    :rtype: InlineResponse200
    """
	return 'do some magic!'


def distance_sub_delete(subscription_id):  # noqa: E501
	"""Cancel a subscription

    Method to delete a subscription. # noqa: E501

    :param subscription_id: Subscription Identifier, specifically the 'self' returned in the subscription request
    :type subscription_id: str

    :rtype: None
    """
	return 'do some magic!'


def distance_sub_get(subscription_id):  # noqa: E501
	"""Retrieve subscription information

    Get subscription information. # noqa: E501

    :param subscription_id: Subscription Identifier, specifically the 'self' returned in the subscription request
    :type subscription_id: str

    :rtype: InlineResponse2009
    """
	return 'do some magic!'


def distance_sub_list_get():  # noqa: E501
	"""Retrieves all active subscriptions to distance change notifications

    This operation is used for retrieving all active subscriptions to a distance change notifications. # noqa: E501


    :rtype: InlineResponse2008
    """
	return 'do some magic!'


def distance_sub_post(body):  # noqa: E501
	"""Creates a subscription for distance change notification

    Creates a subscription to the Location Service for a distance change notification. # noqa: E501

    :param body: Subscription to be created
    :type body: dict | bytes

    :rtype: InlineResponse2011
    """
	if connexion.request.is_json:
		body = SubscriptionsDistanceBody.from_dict(connexion.request.get_json())  # noqa: E501
	return 'do some magic!'


def distance_sub_put(body, subscription_id):  # noqa: E501
	"""Updates a subscription information

    Updates a subscription. # noqa: E501

    :param body: Subscription to be modified
    :type body: dict | bytes
    :param subscription_id: Subscription Identifier, specifically the 'self' returned in the subscription request
    :type subscription_id: str

    :rtype: DistanceSubscriptionIdBody
    """
	if connexion.request.is_json:
		body = DistanceSubscriptionIdBody.from_dict(connexion.request.get_json())  # noqa: E501
	return 'do some magic!'


def periodic_sub_delete(subscription_id):  # noqa: E501
	"""Cancel a subscription

    Method to delete a subscription. # noqa: E501

    :param subscription_id: Subscription Identifier, specifically the 'self' returned in the subscription request
    :type subscription_id: str

    :rtype: None
    """
	return 'do some magic!'


def periodic_sub_get(subscription_id):  # noqa: E501
	"""Retrieve subscription information

    Get subscription information. # noqa: E501

    :param subscription_id: Subscription Identifier, specifically the 'self' returned in the subscription request
    :type subscription_id: str

    :rtype: InlineResponse20011
    """
	return 'do some magic!'


def periodic_sub_list_get():  # noqa: E501
	"""Retrieves all active subscriptions to periodic notifications

    This operation is used for retrieving all active subscriptions to periodic notifications. # noqa: E501


    :rtype: InlineResponse20010
    """
	return 'do some magic!'


def periodic_sub_post(body):  # noqa: E501
	"""Creates a subscription for periodic notification

    Creates a subscription to the Location Service for a periodic notification. # noqa: E501

    :param body: Subscription to be created
    :type body: dict | bytes

    :rtype: InlineResponse2012
    """
	if connexion.request.is_json:
		body = SubscriptionsPeriodicBody.from_dict(connexion.request.get_json())  # noqa: E501
	return 'do some magic!'


def periodic_sub_put(body, subscription_id):  # noqa: E501
	"""Updates a subscription information

    Updates a subscription. # noqa: E501

    :param body: Subscription to be modified
    :type body: dict | bytes
    :param subscription_id: Subscription Identifier, specifically the 'self' returned in the subscription request
    :type subscription_id: str

    :rtype: PeriodicSubscriptionIdBody
    """
	if connexion.request.is_json:
		body = PeriodicSubscriptionIdBody.from_dict(connexion.request.get_json())  # noqa: E501
	return 'do some magic!'


def user_tracking_sub_delete(subscription_id):  # noqa: E501
	"""Cancel a subscription

    Method to delete a subscription. # noqa: E501

    :param subscription_id: Subscription Identifier, specifically the 'self' returned in the subscription request
    :type subscription_id: str

    :rtype: None
    """
	return 'do some magic!'


def user_tracking_sub_get(subscription_id):  # noqa: E501
	"""Retrieve subscription information

    Get subscription information. # noqa: E501

    :param subscription_id: Subscription Identifier, specifically the 'self' returned in the subscription request
    :type subscription_id: str

    :rtype: InlineResponse20013
    """
	return 'do some magic!'


def user_tracking_sub_list_get():  # noqa: E501
	"""Retrieves all active subscriptions to user tracking notifications

    This operation is used for retrieving all active subscriptions to user tracking notifications. # noqa: E501


    :rtype: InlineResponse20012
    """
	return 'do some magic!'


def user_tracking_sub_post(body):  # noqa: E501
	"""Creates a subscription for user tracking notification

    Creates a subscription to the Location Service for user tracking change notification. # noqa: E501

    :param body: Subscription to be created
    :type body: dict | bytes

    :rtype: InlineResponse2013
    """
	if connexion.request.is_json:
		body = SubscriptionsUserTrackingBody.from_dict(connexion.request.get_json())  # noqa: E501
	return 'do some magic!'


def user_tracking_sub_put(body, subscription_id):  # noqa: E501
	"""Updates a subscription information

    Updates a subscription. # noqa: E501

    :param body: Subscription to be modified
    :type body: dict | bytes
    :param subscription_id: Subscription Identifier, specifically the 'self' returned in the subscription request
    :type subscription_id: str

    :rtype: InlineResponse20014
    """
	if connexion.request.is_json:
		body = UserTrackingSubscriptionIdBody.from_dict(connexion.request.get_json())  # noqa: E501
	return 'do some magic!'


def users_get(zone_id=None, access_point_id=None, address=None):  # noqa: E501
	"""UE Location Lookup of a specific UE or group of UEs

    UE Location Lookup of a specific UE or group of UEs # noqa: E501

    :param zone_id: Identifier of zone
    :type zone_id: List[str]
    :param access_point_id: Identifier of access point
    :type access_point_id: List[str]
    :param address: address of users (e.g. 'sip' URI, 'tel' URI, 'acr' URI)
    :type address: List[str]

    :rtype: InlineResponse2001
    """
	return 'do some magic!'


def zonal_traffic_sub_delete(subscription_id):  # noqa: E501
	"""Cancel a subscription

    Method to delete a subscription. # noqa: E501

    :param subscription_id: Subscription Identifier, specifically the 'self' returned in the subscription request
    :type subscription_id: str

    :rtype: None
    """
	return 'do some magic!'


def zonal_traffic_sub_get(subscription_id):  # noqa: E501
	"""Retrieve subscription information

    Get subscription information. # noqa: E501

    :param subscription_id: Subscription Identifier, specifically the 'self' returned in the subscription request
    :type subscription_id: str

    :rtype: InlineResponse20016
    """
	return 'do some magic!'


def zonal_traffic_sub_list_get():  # noqa: E501
	"""Retrieves all active subscriptions to zonal traffic notifications

    This operation is used for retrieving all active subscriptions to zonal traffic change notifications. # noqa: E501


    :rtype: InlineResponse20015
    """
	return 'do some magic!'


def zonal_traffic_sub_post(body):  # noqa: E501
	"""Creates a subscription for zonal traffic notification

    Creates a subscription to the Location Service for zonal traffic change notification. # noqa: E501

    :param body: Subscription to be created
    :type body: dict | bytes

    :rtype: InlineResponse2014
    """
	if connexion.request.is_json:
		body = SubscriptionsZonalTrafficBody.from_dict(connexion.request.get_json())  # noqa: E501
	return 'do some magic!'


def zonal_traffic_sub_put(body, subscription_id):  # noqa: E501
	"""Updates a subscription information

    Updates a subscription. # noqa: E501

    :param body: Subscription to be modified
    :type body: dict | bytes
    :param subscription_id: Subscription Identifier, specifically the 'self' returned in the subscription request
    :type subscription_id: str

    :rtype: InlineResponse20017
    """
	if connexion.request.is_json:
		body = ZonalTrafficSubscriptionIdBody.from_dict(connexion.request.get_json())  # noqa: E501
	return 'do some magic!'


def zone_status_sub_delete(subscription_id):  # noqa: E501
	"""Cancel a subscription

    Method to delete a subscription. # noqa: E501

    :param subscription_id: Subscription Identifier, specifically the 'self' returned in the subscription request
    :type subscription_id: str

    :rtype: None
    """
	return 'do some magic!'


def zone_status_sub_get(subscription_id):  # noqa: E501
	"""Retrieve subscription information

    Get subscription information. # noqa: E501

    :param subscription_id: Subscription Identifier, specifically the 'self' returned in the subscription request
    :type subscription_id: str

    :rtype: InlineResponse20019
    """
	return 'do some magic!'


def zone_status_sub_list_get():  # noqa: E501
	"""Retrieves all active subscriptions to zone status notifications

    This operation is used for retrieving all active subscriptions to zone status change notifications. # noqa: E501


    :rtype: InlineResponse20018
    """
	return 'do some magic!'


def zone_status_sub_post(body):  # noqa: E501
	"""Creates a subscription for zone status notification

    Creates a subscription to the Location Service for zone status change notification. # noqa: E501

    :param body: Subscription to be created
    :type body: dict | bytes

    :rtype: InlineResponse2015
    """
	if connexion.request.is_json:
		body = SubscriptionsZoneStatusBody.from_dict(connexion.request.get_json())  # noqa: E501
	return 'do some magic!'


def zone_status_sub_put(body, subscription_id):  # noqa: E501
	"""Updates a subscription information

    Updates a subscription. # noqa: E501

    :param body: Subscription to be modified
    :type body: dict | bytes
    :param subscription_id: Subscription Identifier, specifically the 'self' returned in the subscription request
    :type subscription_id: str

    :rtype: InlineResponse20020
    """
	if connexion.request.is_json:
		body = ZoneStatusSubscriptionIdBody.from_dict(connexion.request.get_json())  # noqa: E501
	return 'do some magic!'


def zones_get():  # noqa: E501
	"""Zones information Lookup

    Used to get a list of identifiers for zones authorized for use by the application. # noqa: E501


    :rtype: InlineResponse2002
    """
	return 'do some magic!'


def zones_get_by_id(zone_id):  # noqa: E501
	"""Zones information Lookup

    Used to get the information for an authorized zone for use by the application. # noqa: E501

    :param zone_id: Indentifier of zone
    :type zone_id: str

    :rtype: InlineResponse2003
    """
	return 'do some magic!'
