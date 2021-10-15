import string
import random

from swagger_server.models.MEC011_service_management.ser_availability_notification_subscription import \
	SerAvailabilityNotificationSubscription
from swagger_server.models.MEC011_service_management.service_info_post import ServiceInfoPost

RANDOM_STRING_LENGTH = 10
SERVICE_INFORMATIONS_TEMPLATE = {
	"serName": "name",
	"version": "2.0.0",
	"state": "ACTIVE",
	"transportInfo": {
		"id": "TransId12345",
		"name": "REST",
		"description": "REST API",
		"type": "REST_HTTP",
		"protocol": "HTTP",
		"version": "2.0",
		"endpoint": {
			"uris": [

			]
		},
		"security": {
			"oAuth2Info": {
				"grantTypes": [
					"OAUTH2_CLIENT_CREDENTIALS"
				],
				"tokenEndpoint": "/mecSerMgmtApi/security/TokenEndPoint"
			}
		},
		"implSpecificInfo": {

		}
	},
	"serializer": "JSON",
	"consumedLocalOnly": True,
	"isLocal": True
}
APP_INSTANCE_ID = 'app_instance_id_example'
SERVICE_ID = 'service_id_example'
SUBSCRIPTION_ID = 'subscription_id_example'


def get_random_string():
	letters = string.ascii_lowercase
	return ''.join(random.choice(letters) for _ in range(RANDOM_STRING_LENGTH))


def get_random_service_informations():
	service_information = SERVICE_INFORMATIONS_TEMPLATE.copy()
	service_information['serName'] = get_random_string()
	return service_information


def get_random_application_id():
	return get_random_string()


def get_service_info_post():
	return ServiceInfoPost.from_dict(SERVICE_INFORMATIONS_TEMPLATE)


def get_service_availability_notification_subscription():
	return SerAvailabilityNotificationSubscription(subscription_type="SerAvailabilityNotificationSubscription",
	                                               callback_reference="callbackURI",
	                                               )
