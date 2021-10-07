from swagger_server.models.MEC011_service_management.service_info import ServiceInfo  # noqa: E501
from swagger_server.models.internal.applications_services_data import get_services

def services_get(ser_instance_id=None, ser_name=None, ser_category_id=None, consumed_local_only=None, is_local=None, scope_of_locality=None):  # noqa: E501
    """services_get

    This method retrieves information about a list of mecService resources. This method is typically used in 'service availability query' procedure # noqa: E501

    :param ser_instance_id: A MEC application instance may use multiple ser_instance_ids as an input parameter to query the availability of a list of MEC service instances. Either 'ser_instance_id' or 'ser_name' or 'ser_category_id' or none of them shall be present.
    :type ser_instance_id: List[str]
    :param ser_name: A MEC application instance may use multiple ser_names as an input parameter to query the availability of a list of MEC service instances. Either 'ser_instance_id' or 'ser_name' or 'ser_category_id' or none of them shall be present.
    :type ser_name: List[str]
    :param ser_category_id: A MEC application instance may use ser_category_id as an input parameter to query the availability of a list of MEC service instances in a serCategory. Either 'ser_instance_id' or 'ser_name' or 'ser_category_id' or none of them shall be present.
    :type ser_category_id: str
    :param consumed_local_only: Indicate whether the service can only be consumed by the MEC  applications located in the same locality (as defined by  scopeOfLocality) as this service instance.
    :type consumed_local_only: bool
    :param is_local: Indicate whether the service is located in the same locality (as  defined by scopeOfLocality) as the consuming MEC application.
    :type is_local: bool
    :param scope_of_locality: A MEC application instance may use scope_of_locality as an input  parameter to query the availability of a list of MEC service instances  with a certain scope of locality.
    :type scope_of_locality: str 

    :rtype: List[ServiceInfo]
    """
    return get_services(ser_instance_id=ser_instance_id, ser_name=ser_name, ser_category_id=ser_category_id, consumed_local_only=consumed_local_only,
				 is_local=is_local, scope_of_locality=scope_of_locality)


def services_service_id_get(service_id):  # noqa: E501
    """services_service_id_get

    This method retrieves information about a mecService resource. This method is typically used in 'service availability query' procedure # noqa: E501

    :param service_id: Represents a MEC service instance.
    :type service_id: str

    :rtype: ServiceInfo
    """
    return get_services(ser_instance_id=[service_id])
