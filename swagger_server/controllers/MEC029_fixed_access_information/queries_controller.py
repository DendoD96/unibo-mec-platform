import connexion

from swagger_server.models.MEC029_fixed_access_information.cp_info import CpInfo  # noqa: E501
from swagger_server.models.MEC029_fixed_access_information.fa_info import FaInfo  # noqa: E501


def device_info_get(gw_id=None, device_id=None, device_status=None):  # noqa: E501
    """retrieve information on the devices that are connected to a fixed access network.

    retrieve information on the devices that are connected to a fixed access network. # noqa: E501

    :param gw_id: Comma separated list of gateway identifier
    :type gw_id: List[str]
    :param device_id: Comma separated list of device identifier.
    :type device_id: List[str]
    :param device_status: Comma separated list of device status.
    :type device_status: List[int]

    :rtype: DeviceInfo
    """
    return 'do some magic!'


def fa_info_get(customer_premises_info=None, last_mile_tech=None, interface_type=None, dsbw=None, usbw=None, latency=None):  # noqa: E501
    """Retrieve information on the available fixed access networks.

    Retrieve information on the available fixed access networks. # noqa: E501

    :param customer_premises_info: Comma separated list of customer premises information
    :type customer_premises_info: list | bytes
    :param last_mile_tech: Comma separated list of last mile technologies.
    :type last_mile_tech: List[int]
    :param interface_type: Comma separated list of interface types.
    :type interface_type: List[int]
    :param dsbw: Comma separated list of the bandwidth (in Mbps) from the network towards the customer site.
    :type dsbw: List[int]
    :param usbw: Comma separated list of the bandwidth (in Mbps) from the customer site towards the network.
    :type usbw: List[int]
    :param latency: Comma separated list of the maximum baseline latency (in ms) between customer site and service edge node.
    :type latency: List[int]

    :rtype: FaInfo
    """
    if connexion.request.is_json:
        customer_premises_info = [CpInfo.from_dict(d) for d in connexion.request.get_json()]  # noqa: E501
    return 'do some magic!'
