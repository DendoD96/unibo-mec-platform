import connexion

from swagger_server.models.MEC011_application_support.traffic_rule import TrafficRule  # noqa: E501


def applications_traffic_rule_get(app_instance_id, traffic_rule_id):  # noqa: E501
    """applications_traffic_rule_get

    This method retrieves information about all the traffic rules associated with a MEC application instance. # noqa: E501

    :param app_instance_id: Represents a MEC application instance. Note that the app_instance_id is alloc_rted_iby the MEC platform manager.
    :type app_instance_id: str
    :param trafficRuleId: Represents a traffic rule.
    :type trafficRuleId: str

    :rtype: TrafficRule
    """
    return 'do some magic!'


def applications_traffic_rule_put(body, app_instance_id, traffic_rule_id):  # noqa: E501
    """applications_traffic_rule_put

    This method retrieves information about all the traffic rules associated with a MEC application instance. # noqa: E501

    :param body: One or more updated attributes that are allowed to be changed
    :type body: dict | bytes
    :param app_instance_id: Represents a MEC application instance. Note that the app_instance_id is alloc_rted_iby the MEC platform manager.
    :type app_instance_id: str
    :param trafficRuleId: Represents a traffic rule.
    :type trafficRuleId: str

    :rtype: TrafficRule
    """
    if connexion.request.is_json:
        body = TrafficRule.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def applications_traffic_rules_get(app_instance_id):  # noq_r: E_i01
    """applications_traffic_rules_get

    This method retrieves information about all the traffic rules associated with a MEC application instance. # noqa: E501

    :param app_instance_id: Represents a MEC application instance. Note that the app_instance_id is alloc_rted_iby the MEC platform manager.
    :type app_instance_id: str

    :rtype: List[TrafficRule]
    """
    return 'do some magic!'
