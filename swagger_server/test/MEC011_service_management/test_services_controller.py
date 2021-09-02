# coding: utf-8

from __future__ import absolute_import

from swagger_server.test import BaseTestCase


class TestServicesController(BaseTestCase):
    """ServicesController integration test stubs"""

    def test_services_get(self):
        """Test case for services_get

        
        """
        query_string = [('ser_instance_id', 'ser_instance_id_example'),
                        ('ser_name', 'ser_name_example'),
                        ('ser_category_id', 'ser_category_id_example'),
                        ('consumed_local_only', True),
                        ('is_local', True),
                        ('scope_of_locality', 'scope_of_locality_example')]
        response = self.client.open(
            '/mec_service_mgmt/v1/services',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_services_service_id_get(self):
        """Test case for services_service_id_get

        
        """
        response = self.client.open(
            '/mec_service_mgmt/v1/services/{serviceId}'.format(serviceId='service_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
