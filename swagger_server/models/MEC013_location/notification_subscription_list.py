# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.MEC013_location.circle_notification_subscription import CircleNotificationSubscription  # noqa: F401,E501
from swagger_server.models.MEC013_location.distance_notification_subscription import DistanceNotificationSubscription  # noqa: F401,E501
from swagger_server.models.MEC013_location.periodic_notification_subscription import PeriodicNotificationSubscription  # noqa: F401,E501
from swagger_server.models.MEC013_location.user_tracking_subscription import UserTrackingSubscription  # noqa: F401,E501
from swagger_server.models.MEC013_location.zonal_traffic_subscription import ZonalTrafficSubscription  # noqa: F401,E501
from swagger_server.models.MEC013_location.zone_status_subscription import ZoneStatusSubscription  # noqa: F401,E501
from swagger_server import util


class NotificationSubscriptionList(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, circle_notification_subscription: List[CircleNotificationSubscription]=None, distance_notification_subscription: List[DistanceNotificationSubscription]=None, periodic_notification_subscription: List[PeriodicNotificationSubscription]=None, resource_url: str=None, user_tracking_subscription: List[UserTrackingSubscription]=None, zonal_traffic_subscription: List[ZonalTrafficSubscription]=None, zone_status_subscription: List[ZoneStatusSubscription]=None):  # noqa: E501
        """NotificationSubscriptionList - a model defined in Swagger

        :param circle_notification_subscription: The circle_notification_subscription of this NotificationSubscriptionList.  # noqa: E501
        :type circle_notification_subscription: List[CircleNotificationSubscription]
        :param distance_notification_subscription: The distance_notification_subscription of this NotificationSubscriptionList.  # noqa: E501
        :type distance_notification_subscription: List[DistanceNotificationSubscription]
        :param periodic_notification_subscription: The periodic_notification_subscription of this NotificationSubscriptionList.  # noqa: E501
        :type periodic_notification_subscription: List[PeriodicNotificationSubscription]
        :param resource_url: The resource_url of this NotificationSubscriptionList.  # noqa: E501
        :type resource_url: str
        :param user_tracking_subscription: The user_tracking_subscription of this NotificationSubscriptionList.  # noqa: E501
        :type user_tracking_subscription: List[UserTrackingSubscription]
        :param zonal_traffic_subscription: The zonal_traffic_subscription of this NotificationSubscriptionList.  # noqa: E501
        :type zonal_traffic_subscription: List[ZonalTrafficSubscription]
        :param zone_status_subscription: The zone_status_subscription of this NotificationSubscriptionList.  # noqa: E501
        :type zone_status_subscription: List[ZoneStatusSubscription]
        """
        self.swagger_types = {
            'circle_notification_subscription': List[CircleNotificationSubscription],
            'distance_notification_subscription': List[DistanceNotificationSubscription],
            'periodic_notification_subscription': List[PeriodicNotificationSubscription],
            'resource_url': str,
            'user_tracking_subscription': List[UserTrackingSubscription],
            'zonal_traffic_subscription': List[ZonalTrafficSubscription],
            'zone_status_subscription': List[ZoneStatusSubscription]
        }

        self.attribute_map = {
            'circle_notification_subscription': 'circleNotificationSubscription',
            'distance_notification_subscription': 'distanceNotificationSubscription',
            'periodic_notification_subscription': 'periodicNotificationSubscription',
            'resource_url': 'resourceURL',
            'user_tracking_subscription': 'userTrackingSubscription',
            'zonal_traffic_subscription': 'zonalTrafficSubscription',
            'zone_status_subscription': 'zoneStatusSubscription'
        }
        self._circle_notification_subscription = circle_notification_subscription
        self._distance_notification_subscription = distance_notification_subscription
        self._periodic_notification_subscription = periodic_notification_subscription
        self._resource_url = resource_url
        self._user_tracking_subscription = user_tracking_subscription
        self._zonal_traffic_subscription = zonal_traffic_subscription
        self._zone_status_subscription = zone_status_subscription

    @classmethod
    def from_dict(cls, dikt) -> 'NotificationSubscriptionList':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The NotificationSubscriptionList of this NotificationSubscriptionList.  # noqa: E501
        :rtype: NotificationSubscriptionList
        """
        return util.deserialize_model(dikt, cls)

    @property
    def circle_notification_subscription(self) -> List[CircleNotificationSubscription]:
        """Gets the circle_notification_subscription of this NotificationSubscriptionList.

        Collection of CircleNotificationSubscription elements, see note 2.  # noqa: E501

        :return: The circle_notification_subscription of this NotificationSubscriptionList.
        :rtype: List[CircleNotificationSubscription]
        """
        return self._circle_notification_subscription

    @circle_notification_subscription.setter
    def circle_notification_subscription(self, circle_notification_subscription: List[CircleNotificationSubscription]):
        """Sets the circle_notification_subscription of this NotificationSubscriptionList.

        Collection of CircleNotificationSubscription elements, see note 2.  # noqa: E501

        :param circle_notification_subscription: The circle_notification_subscription of this NotificationSubscriptionList.
        :type circle_notification_subscription: List[CircleNotificationSubscription]
        """

        self._circle_notification_subscription = circle_notification_subscription

    @property
    def distance_notification_subscription(self) -> List[DistanceNotificationSubscription]:
        """Gets the distance_notification_subscription of this NotificationSubscriptionList.

        Collection of DistanceNotificationSubscription elements, see note 2.  # noqa: E501

        :return: The distance_notification_subscription of this NotificationSubscriptionList.
        :rtype: List[DistanceNotificationSubscription]
        """
        return self._distance_notification_subscription

    @distance_notification_subscription.setter
    def distance_notification_subscription(self, distance_notification_subscription: List[DistanceNotificationSubscription]):
        """Sets the distance_notification_subscription of this NotificationSubscriptionList.

        Collection of DistanceNotificationSubscription elements, see note 2.  # noqa: E501

        :param distance_notification_subscription: The distance_notification_subscription of this NotificationSubscriptionList.
        :type distance_notification_subscription: List[DistanceNotificationSubscription]
        """

        self._distance_notification_subscription = distance_notification_subscription

    @property
    def periodic_notification_subscription(self) -> List[PeriodicNotificationSubscription]:
        """Gets the periodic_notification_subscription of this NotificationSubscriptionList.

        Collection of PeriodicNotificationSubscription elements, see note 2.  # noqa: E501

        :return: The periodic_notification_subscription of this NotificationSubscriptionList.
        :rtype: List[PeriodicNotificationSubscription]
        """
        return self._periodic_notification_subscription

    @periodic_notification_subscription.setter
    def periodic_notification_subscription(self, periodic_notification_subscription: List[PeriodicNotificationSubscription]):
        """Sets the periodic_notification_subscription of this NotificationSubscriptionList.

        Collection of PeriodicNotificationSubscription elements, see note 2.  # noqa: E501

        :param periodic_notification_subscription: The periodic_notification_subscription of this NotificationSubscriptionList.
        :type periodic_notification_subscription: List[PeriodicNotificationSubscription]
        """

        self._periodic_notification_subscription = periodic_notification_subscription

    @property
    def resource_url(self) -> str:
        """Gets the resource_url of this NotificationSubscriptionList.

        Self-referring URL, see note 1.  # noqa: E501

        :return: The resource_url of this NotificationSubscriptionList.
        :rtype: str
        """
        return self._resource_url

    @resource_url.setter
    def resource_url(self, resource_url: str):
        """Sets the resource_url of this NotificationSubscriptionList.

        Self-referring URL, see note 1.  # noqa: E501

        :param resource_url: The resource_url of this NotificationSubscriptionList.
        :type resource_url: str
        """
        if resource_url is None:
            raise ValueError("Invalid value for `resource_url`, must not be `None`")  # noqa: E501

        self._resource_url = resource_url

    @property
    def user_tracking_subscription(self) -> List[UserTrackingSubscription]:
        """Gets the user_tracking_subscription of this NotificationSubscriptionList.

        Collection of UserTrackingSubscription elements, see note 1.  # noqa: E501

        :return: The user_tracking_subscription of this NotificationSubscriptionList.
        :rtype: List[UserTrackingSubscription]
        """
        return self._user_tracking_subscription

    @user_tracking_subscription.setter
    def user_tracking_subscription(self, user_tracking_subscription: List[UserTrackingSubscription]):
        """Sets the user_tracking_subscription of this NotificationSubscriptionList.

        Collection of UserTrackingSubscription elements, see note 1.  # noqa: E501

        :param user_tracking_subscription: The user_tracking_subscription of this NotificationSubscriptionList.
        :type user_tracking_subscription: List[UserTrackingSubscription]
        """

        self._user_tracking_subscription = user_tracking_subscription

    @property
    def zonal_traffic_subscription(self) -> List[ZonalTrafficSubscription]:
        """Gets the zonal_traffic_subscription of this NotificationSubscriptionList.

        Collection of ZonalTrafficSubscription elements, see note 1.  # noqa: E501

        :return: The zonal_traffic_subscription of this NotificationSubscriptionList.
        :rtype: List[ZonalTrafficSubscription]
        """
        return self._zonal_traffic_subscription

    @zonal_traffic_subscription.setter
    def zonal_traffic_subscription(self, zonal_traffic_subscription: List[ZonalTrafficSubscription]):
        """Sets the zonal_traffic_subscription of this NotificationSubscriptionList.

        Collection of ZonalTrafficSubscription elements, see note 1.  # noqa: E501

        :param zonal_traffic_subscription: The zonal_traffic_subscription of this NotificationSubscriptionList.
        :type zonal_traffic_subscription: List[ZonalTrafficSubscription]
        """

        self._zonal_traffic_subscription = zonal_traffic_subscription

    @property
    def zone_status_subscription(self) -> List[ZoneStatusSubscription]:
        """Gets the zone_status_subscription of this NotificationSubscriptionList.

        Collection of ZoneStatusSubscription elements, see note 1.  # noqa: E501

        :return: The zone_status_subscription of this NotificationSubscriptionList.
        :rtype: List[ZoneStatusSubscription]
        """
        return self._zone_status_subscription

    @zone_status_subscription.setter
    def zone_status_subscription(self, zone_status_subscription: List[ZoneStatusSubscription]):
        """Sets the zone_status_subscription of this NotificationSubscriptionList.

        Collection of ZoneStatusSubscription elements, see note 1.  # noqa: E501

        :param zone_status_subscription: The zone_status_subscription of this NotificationSubscriptionList.
        :type zone_status_subscription: List[ZoneStatusSubscription]
        """

        self._zone_status_subscription = zone_status_subscription
