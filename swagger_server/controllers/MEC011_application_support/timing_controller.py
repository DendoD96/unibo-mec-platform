from swagger_server.models.internal.applications_services_data import get_current_time


def timing_caps_get():  # noqa: E501
	"""timing_caps_get

	This method retrieves the information of the platform's timing capabilities which corresponds to the timing capabilities query # noqa: E501


	:rtype: TimingCaps
	"""
	return 'do some magic!'


def timing_current_time_get():  # noqa: E501
	"""timing_current_time_get

	This method retrieves the information of the platform&#x27;s current time which corresponds to the get platform time procedure # noqa: E501


	:rtype: CurrentTime
	"""
	return get_current_time()
