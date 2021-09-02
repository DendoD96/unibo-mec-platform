import connexion

from swagger_server.models.MEC028_wlan_access_information.inline_subscription import InlineSubscription  # noqa: E501
from swagger_server.models.MEC028_wlan_access_information.measurement_config import MeasurementConfig  # noqa: E501
from swagger_server.models.MEC028_wlan_access_information.measurement_config_link_list import \
	MeasurementConfigLinkList  # noqa: E501
from swagger_server.models.MEC028_wlan_access_information.subscription_link_list import \
	SubscriptionLinkList  # noqa: E501


def ap_info_get(filter=None, all_fields=None, fields=None, exclude_fields=None, exclude_default=None):  # noqa: E501
	"""Retrieve information on existing Access Points

	Queries information about existing WLAN Access Points # noqa: E501

	:param filter: Attribute-based filtering expression according to clause 6.19 of ETSI GS MEC 009. .
	:type filter: str
	:param all_fields: Include all complex attributes in the response. See clause 6.18 of ETSI GS MEC 009 for details.
	:type all_fields: str
	:param fields: Complex attributes to be included into the response. See clause 6.18 of ETSI GS MEC 009 for details.
	:type fields: List[str]
	:param exclude_fields: Complex attributes to be excluded from the response. See clause 6.18 of ETSI GS MEC 009 for details.
	:type exclude_fields: List[str]
	:param exclude_default: Indicates to exclude the following complex attributes from the response. See clause 6.18 of ETSI GS MEC 009 for details. The following attributes shall be excluded from the structure in the response body if this parameter is provided, or none of the parameters 'all_fields', 'fields', 'exclude_fields', 'exclude_default' are provided: Not applicable
	:type exclude_default: List[str]

	:rtype: List[ApInfo]
	"""
	return 'do some magic!'


def measurement_link_list_measurements_get():  # noqa: E501
	"""Retrieve information on measurements configuration

	Queries information on measurements configuration # noqa: E501


	:rtype: MeasurementConfigLinkList
	"""
	return 'do some magic!'


def measurements_delete(measurementConfigId):  # noqa: E501
	"""Cancel a measurement configuration

	Cancels an existing measurement configuration, identified by its self-referring URI returned on creation (initial POST) # noqa: E501

	:param measurementConfigId: Measurement configuration Id, specifically the 'self' returned in the measurement configuration request
	:type measurementConfigId: str

	:rtype: None
	"""
	return 'do some magic!'


def measurements_get(measurementConfigId):  # noqa: E501
	"""Retrieve information on an existing measurement configuration

	Queries information about an existing measurement configuration, identified by its self-referring URI returned on creation (initial POST) # noqa: E501

	:param measurementConfigId: Measurement configuration Id, specifically the 'self' returned in the measurement configuration request
	:type measurementConfigId: str

	:rtype: MeasurementConfig
	"""
	return 'do some magic!'


def measurements_post(body):  # noqa: E501
	"""Create a new measurement configuration

	Creates a new measurement configuration # noqa: E501

	:param body: Measurement configuration information
	:type body: dict | bytes

	:rtype: MeasurementConfig
	"""
	if connexion.request.is_json:
		body = MeasurementConfig.from_dict(connexion.request.get_json())  # noqa: E501
	return 'do some magic!'


def measurements_put(body, measurementConfigId):  # noqa: E501
	"""Modify an existing measurement configuration

	Updates an existing measurement configuration, identified by its self-referring URI returned on creation (initial POST) # noqa: E501

	:param body: Measurement configuration to be modified
	:type body: dict | bytes
	:param measurementConfigId: Measurement configuration Id, specifically the 'self' returned in the measurement configuration request
	:type measurementConfigId: str

	:rtype: MeasurementConfig
	"""
	if connexion.request.is_json:
		body = MeasurementConfig.from_dict(connexion.request.get_json())  # noqa: E501
	return 'do some magic!'


def sta_info_get(filter=None, all_fields=None, fields=None, exclude_fields=None, exclude_default=None):  # noqa: E501
	"""Retrieve information on existing Stations

	Queries information about existing WLAN stations # noqa: E501

	:param filter: Attribute-based filtering expression according to clause 6.19 of ETSI GS MEC 009. .
	:type filter: str
	:param all_fields: Include all complex attributes in the response. See clause 6.18 of ETSI GS MEC 009 for details.
	:type all_fields: str
	:param fields: Complex attributes to be included into the response. See clause 6.18 of ETSI GS MEC 009 for details.
	:type fields: List[str]
	:param exclude_fields: Complex attributes to be excluded from the response. See clause 6.18 of ETSI GS MEC 009 for details.
	:type exclude_fields: List[str]
	:param exclude_default: Indicates to exclude the following complex attributes from the response. See clause 6.18 of ETSI GS MEC 009 for details. The following attributes shall be excluded from the structure in the response body if this parameter is provided, or none of the parameters 'all_fields', 'fields', 'exclude_fields', 'exclude_default' are provided: Not applicable
	:type exclude_default: List[str]

	:rtype: List[StaInfo]
	"""
	return 'do some magic!'


def subscription_link_list_subscriptions_get(subscription_type=None):  # noqa: E501
	"""Retrieve information on subscriptions for notifications

	Queries information on subscriptions for notifications # noqa: E501

	:param subscription_type: Filter on a specific subscription type. Permitted values: assoc_sta, sta_data_rate, measure_report.
	:type subscription_type: str

	:rtype: SubscriptionLinkList
	"""
	return 'do some magic!'


def subscriptions_delete(subscriptionId):  # noqa: E501
	"""Cancel an existing subscription

	Cancels an existing subscription, identified by its self-referring URI returned on creation (initial POST) # noqa: E501

	:param subscriptionId: Subscription Id, specifically the 'self' returned in the subscription request
	:type subscriptionId: str

	:rtype: None
	"""
	return 'do some magic!'


def subscriptions_get(subscriptionId):  # noqa: E501
	"""Retrieve information on current specific subscription

	Queries information about an existing subscription, identified by its self-referring URI returned on creation (initial POST) # noqa: E501

	:param subscriptionId: Subscription Id, specifically the 'self' returned in the subscription request
	:type subscriptionId: str

	:rtype: InlineSubscription
	"""
	return 'do some magic!'


def subscriptions_post(body):  # noqa: E501
	"""Create a new subscription

	Creates a new subscription to WLAN Access Information notifications # noqa: E501

	:param body: Subscription to be created
	:type body: dict | bytes

	:rtype: InlineSubscription
	"""
	if connexion.request.is_json:
		body = InlineSubscription.from_dict(connexion.request.get_json())  # noqa: E501
	return 'do some magic!'


def subscriptions_put(body, subscriptionId):  # noqa: E501
	"""Modify an existing subscription

	Updates an existing subscription, identified by its self-referring URI returned on creation (initial POST) # noqa: E501

	:param body: Subscription to be modified
	:type body: dict | bytes
	:param subscriptionId: Subscription Id, specifically the 'self' returned in the subscription request
	:type subscriptionId: str

	:rtype: InlineSubscription
	"""
	if connexion.request.is_json:
		body = InlineSubscription.from_dict(connexion.request.get_json())  # noqa: E501
	return 'do some magic!'
