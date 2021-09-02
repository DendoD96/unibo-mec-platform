import connexion

from swagger_server.models.MEC011_service_management.service_info import ServiceInfo  # noqa: E501
from swagger_server.models.MEC011_service_management.service_info_post import ServiceInfoPost  # noqa: E501


def app_services_get(appInstanceId, ser_instance_id=None, ser_name=None, ser_category_id=None, consumed_local_only=None, is_local=None, scope_of_locality=None):  # noqa: E501
    """app_services_get

    This method retrieves information about a list of mecService resources. This method is typically used in 'service availability query' procedure # noqa: E501

    :param appInstanceId: Represents a MEC application instance. Note that the appInstanceId is allocated by the MEC platform manager.
    :type appInstanceId: str
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
    return 'do some magic!'


def app_services_post(body, appInstanceId):  # noqa: E501
    """app_services_post

    This method is used to create a mecService resource. This method is typically used in 'service availability update and new service registration' procedure # noqa: E501

    :param body: New ServiceInfo with updated &quot;state&quot; is included as entity body of the request
    :type body: dict | bytes
    :param appInstanceId: Represents a MEC application instance. Note that the appInstanceId is allocated by the MEC platform manager.
    :type appInstanceId: str

    :rtype: ServiceInfo
    """
    if connexion.request.is_json:
        body = ServiceInfoPost.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def app_services_service_id_delete(appInstanceId, serviceId):  # noqa: E501
    """app_services_service_id_delete

    This method deletes a mecService resource. This method is typically used in the service deregistration procedure.  # noqa: E501

    :param appInstanceId: Represents a MEC application instance. Note that the appInstanceId is allocated by the MEC platform manager.
    :type appInstanceId: str
    :param serviceId: Represents a MEC service instance.
    :type serviceId: str

    :rtype: None
    """
    return 'do some magic!'


def app_services_service_id_get(appInstanceId, serviceId):  # noqa: E501
    """app_services_service_id_get

    This method retrieves information about a mecService resource. This method is typically used in 'service availability query' procedure # noqa: E501

    :param appInstanceId: Represents a MEC application instance. Note that the appInstanceId is allocated by the MEC platform manager.
    :type appInstanceId: str
    :param serviceId: Represents a MEC service instance.
    :type serviceId: str

    :rtype: ServiceInfo
    """
    return 'do some magic!'


def app_services_service_id_put(body, appInstanceId, serviceId):  # noqa: E501
    """app_services_service_id_put

    This method updates the information about a mecService resource # noqa: E501

    :param body: New ServiceInfo with updated &quot;state&quot; is included as entity body of the request
    :type body: dict | bytes
    :param appInstanceId: Represents a MEC application instance. Note that the appInstanceId is allocated by the MEC platform manager.
    :type appInstanceId: str
    :param serviceId: Represents a MEC service instance.
    :type serviceId: str

    :rtype: ServiceInfo
    """
    if connexion.request.is_json:
        body = ServiceInfo.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
