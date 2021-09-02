# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.MEC011_application_support.app_termination_notification_subscription import AppTerminationNotificationSubscription  # noqa: E501
from swagger_server.models.MEC011_application_support.mec_app_supt_api_subscription_link_list import MecAppSuptApiSubscriptionLinkList  # noqa: E501
from swagger_server.models.problem_details import ProblemDetails  # noqa: E501
from swagger_server.test import BaseTestCase


class TestAppSubscriptionsController(BaseTestCase):
    """AppSubscriptionsController integration test stubs"""

    def test_applications_subscription_delete(self):
        """Test case for applications_subscription_delete

        
        """
        response = self.client.open(
            '/mec_app_support/v1/applications/{appInstanceId}/subscriptions/{subscriptionId}'.format(appInstanceId='app_instance_id_example', subscriptionId='subscription_id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_applications_subscription_get(self):
        """Test case for applications_subscription_get

        
        """
        response = self.client.open(
            '/mec_app_support/v1/applications/{appInstanceId}/subscriptions/{subscriptionId}'.format(appInstanceId='app_instance_id_example', subscriptionId='subscription_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_applications_subscriptions_get(self):
        """Test case for applications_subscriptions_get

        
        """
        response = self.client.open(
            '/mec_app_support/v1/applications/{appInstanceId}/subscriptions'.format(appInstanceId='app_instance_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_applications_subscriptions_post(self):
        """Test case for applications_subscriptions_post

        
        """
        body = AppTerminationNotificationSubscription(app_instance_id="app_instance_id",
                                                      callback_reference="callback_uri",
                                                      subscription_type="type"
                                                      )
        response = self.client.open(
            '/mec_app_support/v1/applications/{appInstanceId}/subscriptions'.format(appInstanceId='app_instance_id_example'),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
