from datetime import datetime, timezone

from swagger_server.controllers.internal.applications_information_manager import get_current_time
from swagger_server.models.MEC011_application_support.timing_caps import TimingCaps
from swagger_server.models.MEC011_application_support.timing_caps_time_stamp import TimingCapsTimeStamp


def timing_caps_get():  # noqa: E501
	"""timing_caps_get

	This method retrieves the information of the platform's timing capabilities which corresponds to the timing capabilities query # noqa: E501


	:rtype: TimingCaps
	"""
	date = datetime.now(timezone.utc)
	return TimingCaps(time_stamp=TimingCapsTimeStamp(seconds=int(date.timestamp()), nano_seconds=0))


def timing_current_time_get():  # noqa: E501
	"""timing_current_time_get

	This method retrieves the information of the platform&#x27;s current time which corresponds to the get platform time procedure # noqa: E501


	:rtype: CurrentTime
	"""
	return get_current_time()
