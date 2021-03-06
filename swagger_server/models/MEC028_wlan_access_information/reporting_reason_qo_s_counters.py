# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class ReportingReasonQoSCounters(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, qos_ack_failure: bool=None, qos_discarded: bool=None, qos_failed: bool=None, qos_frame_duplicate: bool=None, qos_multiple_retry: bool=None, qos_retry: bool=None, qos_rts_failure: bool=None):  # noqa: E501
        """ReportingReasonQoSCounters - a model defined in Swagger

        :param qos_ack_failure: The qos_ack_failure of this ReportingReasonQoSCounters.  # noqa: E501
        :type qos_ack_failure: bool
        :param qos_discarded: The qos_discarded of this ReportingReasonQoSCounters.  # noqa: E501
        :type qos_discarded: bool
        :param qos_failed: The qos_failed of this ReportingReasonQoSCounters.  # noqa: E501
        :type qos_failed: bool
        :param qos_frame_duplicate: The qos_frame_duplicate of this ReportingReasonQoSCounters.  # noqa: E501
        :type qos_frame_duplicate: bool
        :param qos_multiple_retry: The qos_multiple_retry of this ReportingReasonQoSCounters.  # noqa: E501
        :type qos_multiple_retry: bool
        :param qos_retry: The qos_retry of this ReportingReasonQoSCounters.  # noqa: E501
        :type qos_retry: bool
        :param qos_rts_failure: The qos_rts_failure of this ReportingReasonQoSCounters.  # noqa: E501
        :type qos_rts_failure: bool
        """
        self.swagger_types = {
            'qos_ack_failure': bool,
            'qos_discarded': bool,
            'qos_failed': bool,
            'qos_frame_duplicate': bool,
            'qos_multiple_retry': bool,
            'qos_retry': bool,
            'qos_rts_failure': bool
        }

        self.attribute_map = {
            'qos_ack_failure': 'qosAckFailure',
            'qos_discarded': 'qosDiscarded',
            'qos_failed': 'qosFailed',
            'qos_frame_duplicate': 'qosFrameDuplicate',
            'qos_multiple_retry': 'qosMultipleRetry',
            'qos_retry': 'qosRetry',
            'qos_rts_failure': 'qosRtsFailure'
        }
        self._qos_ack_failure = qos_ack_failure
        self._qos_discarded = qos_discarded
        self._qos_failed = qos_failed
        self._qos_frame_duplicate = qos_frame_duplicate
        self._qos_multiple_retry = qos_multiple_retry
        self._qos_retry = qos_retry
        self._qos_rts_failure = qos_rts_failure

    @classmethod
    def from_dict(cls, dikt) -> 'ReportingReasonQoSCounters':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ReportingReasonQoSCounters of this ReportingReasonQoSCounters.  # noqa: E501
        :rtype: ReportingReasonQoSCounters
        """
        return util.deserialize_model(dikt, cls)

    @property
    def qos_ack_failure(self) -> bool:
        """Gets the qos_ack_failure of this ReportingReasonQoSCounters.

        dot11QoSAckFailure  # noqa: E501

        :return: The qos_ack_failure of this ReportingReasonQoSCounters.
        :rtype: bool
        """
        return self._qos_ack_failure

    @qos_ack_failure.setter
    def qos_ack_failure(self, qos_ack_failure: bool):
        """Sets the qos_ack_failure of this ReportingReasonQoSCounters.

        dot11QoSAckFailure  # noqa: E501

        :param qos_ack_failure: The qos_ack_failure of this ReportingReasonQoSCounters.
        :type qos_ack_failure: bool
        """
        if qos_ack_failure is None:
            raise ValueError("Invalid value for `qos_ack_failure`, must not be `None`")  # noqa: E501

        self._qos_ack_failure = qos_ack_failure

    @property
    def qos_discarded(self) -> bool:
        """Gets the qos_discarded of this ReportingReasonQoSCounters.

        dot11QoSDiscarded  # noqa: E501

        :return: The qos_discarded of this ReportingReasonQoSCounters.
        :rtype: bool
        """
        return self._qos_discarded

    @qos_discarded.setter
    def qos_discarded(self, qos_discarded: bool):
        """Sets the qos_discarded of this ReportingReasonQoSCounters.

        dot11QoSDiscarded  # noqa: E501

        :param qos_discarded: The qos_discarded of this ReportingReasonQoSCounters.
        :type qos_discarded: bool
        """
        if qos_discarded is None:
            raise ValueError("Invalid value for `qos_discarded`, must not be `None`")  # noqa: E501

        self._qos_discarded = qos_discarded

    @property
    def qos_failed(self) -> bool:
        """Gets the qos_failed of this ReportingReasonQoSCounters.

        dot11QoSFailed   # noqa: E501

        :return: The qos_failed of this ReportingReasonQoSCounters.
        :rtype: bool
        """
        return self._qos_failed

    @qos_failed.setter
    def qos_failed(self, qos_failed: bool):
        """Sets the qos_failed of this ReportingReasonQoSCounters.

        dot11QoSFailed   # noqa: E501

        :param qos_failed: The qos_failed of this ReportingReasonQoSCounters.
        :type qos_failed: bool
        """
        if qos_failed is None:
            raise ValueError("Invalid value for `qos_failed`, must not be `None`")  # noqa: E501

        self._qos_failed = qos_failed

    @property
    def qos_frame_duplicate(self) -> bool:
        """Gets the qos_frame_duplicate of this ReportingReasonQoSCounters.

        dot11QoSFrameDuplicate  # noqa: E501

        :return: The qos_frame_duplicate of this ReportingReasonQoSCounters.
        :rtype: bool
        """
        return self._qos_frame_duplicate

    @qos_frame_duplicate.setter
    def qos_frame_duplicate(self, qos_frame_duplicate: bool):
        """Sets the qos_frame_duplicate of this ReportingReasonQoSCounters.

        dot11QoSFrameDuplicate  # noqa: E501

        :param qos_frame_duplicate: The qos_frame_duplicate of this ReportingReasonQoSCounters.
        :type qos_frame_duplicate: bool
        """
        if qos_frame_duplicate is None:
            raise ValueError("Invalid value for `qos_frame_duplicate`, must not be `None`")  # noqa: E501

        self._qos_frame_duplicate = qos_frame_duplicate

    @property
    def qos_multiple_retry(self) -> bool:
        """Gets the qos_multiple_retry of this ReportingReasonQoSCounters.

        dot11QoSMultipleRetry  # noqa: E501

        :return: The qos_multiple_retry of this ReportingReasonQoSCounters.
        :rtype: bool
        """
        return self._qos_multiple_retry

    @qos_multiple_retry.setter
    def qos_multiple_retry(self, qos_multiple_retry: bool):
        """Sets the qos_multiple_retry of this ReportingReasonQoSCounters.

        dot11QoSMultipleRetry  # noqa: E501

        :param qos_multiple_retry: The qos_multiple_retry of this ReportingReasonQoSCounters.
        :type qos_multiple_retry: bool
        """
        if qos_multiple_retry is None:
            raise ValueError("Invalid value for `qos_multiple_retry`, must not be `None`")  # noqa: E501

        self._qos_multiple_retry = qos_multiple_retry

    @property
    def qos_retry(self) -> bool:
        """Gets the qos_retry of this ReportingReasonQoSCounters.

        dot11QoSRetry  # noqa: E501

        :return: The qos_retry of this ReportingReasonQoSCounters.
        :rtype: bool
        """
        return self._qos_retry

    @qos_retry.setter
    def qos_retry(self, qos_retry: bool):
        """Sets the qos_retry of this ReportingReasonQoSCounters.

        dot11QoSRetry  # noqa: E501

        :param qos_retry: The qos_retry of this ReportingReasonQoSCounters.
        :type qos_retry: bool
        """
        if qos_retry is None:
            raise ValueError("Invalid value for `qos_retry`, must not be `None`")  # noqa: E501

        self._qos_retry = qos_retry

    @property
    def qos_rts_failure(self) -> bool:
        """Gets the qos_rts_failure of this ReportingReasonQoSCounters.

        dot11QoSRTSFailure  # noqa: E501

        :return: The qos_rts_failure of this ReportingReasonQoSCounters.
        :rtype: bool
        """
        return self._qos_rts_failure

    @qos_rts_failure.setter
    def qos_rts_failure(self, qos_rts_failure: bool):
        """Sets the qos_rts_failure of this ReportingReasonQoSCounters.

        dot11QoSRTSFailure  # noqa: E501

        :param qos_rts_failure: The qos_rts_failure of this ReportingReasonQoSCounters.
        :type qos_rts_failure: bool
        """
        if qos_rts_failure is None:
            raise ValueError("Invalid value for `qos_rts_failure`, must not be `None`")  # noqa: E501

        self._qos_rts_failure = qos_rts_failure
