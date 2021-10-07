import connexion

from swagger_server.models.MEC011_application_support.dns_rule import DnsRule  # noqa: E501


def applications_dns_rule_get(app_instance_id, dns_rule_id):  # noqa: E501
    """applications_dns_rule_get

    This method retrieves information about a DNS rule associated with a MEC application instance. # noqa: E501

    :param app_instance_id: Represents a MEC application instance. Note that the app_instance_id is allocated by the MEC platform manager.
    :type app_instance_id: str
    :param dns_rule_id: Represents a DNS rule.
    :type dns_rule_id: str

    :rtype: DnsRule
    """
    return 'do some magic!'


def applications_dns_rule_put(body, app_instance_id, dns_rule_id):  # noqa: E501
    """applications_dns_rule_put

    This method activates, de-activates or updates a traffic rule. # noqa: E501

    :param body: The updated state is included in the entity body of the request.
    :type body: dict | bytes
    :param app_instance_id: Represents a MEC application instance. Note that the app_instance_id is allocated by the MEC platform manager.
    :type app_instance_id: str
    :param dns_rule_id: Represents a DNS rule.
    :type dns_rule_id: str

    :rtype: DnsRule
    """
    if connexion.request.is_json:
        body = DnsRule.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def applications_dns_rules_get(app_instance_id):  # noqa: E501
    """applications_dns_rules_get

    This method retrieves information about all the DNS rules associated with a MEC application instance. # noqa: E501

    :param app_instance_id: Represents a MEC application instance. Note that the app_instance_id is allocated by the MEC platform manager.
    :type app_instance_id: str

    :rtype: List[DnsRule]
    """
    return 'do some magic!'
