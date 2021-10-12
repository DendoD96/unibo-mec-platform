# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401 # pylint: disable=unused-import

from typing import List, Dict  # noqa: F401 # pylint: disable=unused-import

from swagger_server.models.base_model_ import Model
from swagger_server import util


class LocationInfoVelocity(Model):
	"""NOTE: This class is auto generated by the swagger code generator program.

	Do not edit the class manually.
	"""

	def __init__(self, bearing: int = None, horizontal_speed: int = None, uncertainty: int = None,
	             velocity_type: int = None, vertical_speed: int = None, vertical_uncertainty: int = None):  # noqa: E501
		"""LocationInfoVelocity - a model defined in Swagger

		:param bearing: The bearing of this LocationInfoVelocity.  # noqa: E501
		:type bearing: int
		:param horizontal_speed: The horizontal_speed of this LocationInfoVelocity.  # noqa: E501
		:type horizontal_speed: int
		:param uncertainty: The uncertainty of this LocationInfoVelocity.  # noqa: E501
		:type uncertainty: int
		:param velocity_type: The velocity_type of this LocationInfoVelocity.  # noqa: E501
		:type velocity_type: int
		:param vertical_speed: The vertical_speed of this LocationInfoVelocity.  # noqa: E501
		:type vertical_speed: int
		:param vertical_uncertainty: The vertical_uncertainty of this LocationInfoVelocity.  # noqa: E501
		:type vertical_uncertainty: int
		"""
		self.swagger_types = {
			'bearing': int,
			'horizontal_speed': int,
			'uncertainty': int,
			'velocity_type': int,
			'vertical_speed': int,
			'vertical_uncertainty': int
		}

		self.attribute_map = {
			'bearing': 'bearing',
			'horizontal_speed': 'horizontalSpeed',
			'uncertainty': 'uncertainty',
			'velocity_type': 'velocityType',
			'vertical_speed': 'verticalSpeed',
			'vertical_uncertainty': 'verticalUncertainty'
		}
		self._bearing = bearing
		self._horizontal_speed = horizontal_speed
		self._uncertainty = uncertainty
		self._velocity_type = velocity_type
		self._vertical_speed = vertical_speed
		self._vertical_uncertainty = vertical_uncertainty

	@classmethod
	def from_dict(cls, dikt) -> 'LocationInfoVelocity':
		"""Returns the dict as a model

		:param dikt: A dict.
		:type: dict
		:return: The LocationInfo_velocity of this LocationInfoVelocity.  # noqa: E501
		:rtype: LocationInfoVelocity
		"""
		return util.deserialize_model(dikt, cls)

	@property
	def bearing(self) -> int:
		"""Gets the bearing of this LocationInfoVelocity.

		Bearing, expressed in the range 0° to 360°, as defined in [14].  # noqa: E501

		:return: The bearing of this LocationInfoVelocity.
		:rtype: int
		"""
		return self._bearing

	@bearing.setter
	def bearing(self, bearing: int):
		"""Sets the bearing of this LocationInfoVelocity.

		Bearing, expressed in the range 0° to 360°, as defined in [14].  # noqa: E501

		:param bearing: The bearing of this LocationInfoVelocity.
		:type bearing: int
		"""
		if bearing is None:
			raise ValueError("Invalid value for `bearing`, must not be `None`")  # noqa: E501

		self._bearing = bearing

	@property
	def horizontal_speed(self) -> int:
		"""Gets the horizontal_speed of this LocationInfoVelocity.

		Horizontal speed, expressed in km/h and defined in [14].  # noqa: E501

		:return: The horizontal_speed of this LocationInfoVelocity.
		:rtype: int
		"""
		return self._horizontal_speed

	@horizontal_speed.setter
	def horizontal_speed(self, horizontal_speed: int):
		"""Sets the horizontal_speed of this LocationInfoVelocity.

		Horizontal speed, expressed in km/h and defined in [14].  # noqa: E501

		:param horizontal_speed: The horizontal_speed of this LocationInfoVelocity.
		:type horizontal_speed: int
		"""
		if horizontal_speed is None:
			raise ValueError("Invalid value for `horizontal_speed`, must not be `None`")  # noqa: E501

		self._horizontal_speed = horizontal_speed

	@property
	def uncertainty(self) -> int:
		"""Gets the uncertainty of this LocationInfoVelocity.

		Horizontal uncertainty, as defined in [14]. Present only if \"velocityType\" equals 3 or 4  # noqa: E501

		:return: The uncertainty of this LocationInfoVelocity.
		:rtype: int
		"""
		return self._uncertainty

	@uncertainty.setter
	def uncertainty(self, uncertainty: int):
		"""Sets the uncertainty of this LocationInfoVelocity.

		Horizontal uncertainty, as defined in [14]. Present only if \"velocityType\" equals 3 or 4  # noqa: E501

		:param uncertainty: The uncertainty of this LocationInfoVelocity.
		:type uncertainty: int
		"""

		self._uncertainty = uncertainty

	@property
	def velocity_type(self) -> int:
		"""Gets the velocity_type of this LocationInfoVelocity.

		Velocity information, as detailed in [14], associated with the reported location coordinate: <p>1 = HORIZONTAL <p>2 = HORIZONTAL_VERTICAL <p>3 = HORIZONTAL_UNCERT <p>4 = HORIZONTAL_VERTICAL_UNCERT  # noqa: E501

		:return: The velocity_type of this LocationInfoVelocity.
		:rtype: int
		"""
		return self._velocity_type

	@velocity_type.setter
	def velocity_type(self, velocity_type: int):
		"""Sets the velocity_type of this LocationInfoVelocity.

		Velocity information, as detailed in [14], associated with the reported location coordinate: <p>1 = HORIZONTAL <p>2 = HORIZONTAL_VERTICAL <p>3 = HORIZONTAL_UNCERT <p>4 = HORIZONTAL_VERTICAL_UNCERT  # noqa: E501

		:param velocity_type: The velocity_type of this LocationInfoVelocity.
		:type velocity_type: int
		"""
		if velocity_type is None:
			raise ValueError("Invalid value for `velocity_type`, must not be `None`")  # noqa: E501

		self._velocity_type = velocity_type

	@property
	def vertical_speed(self) -> int:
		"""Gets the vertical_speed of this LocationInfoVelocity.

		Vertical speed, expressed in km/h and defined in [14]. Present only if \"velocityType\" equals 2 or 4  # noqa: E501

		:return: The vertical_speed of this LocationInfoVelocity.
		:rtype: int
		"""
		return self._vertical_speed

	@vertical_speed.setter
	def vertical_speed(self, vertical_speed: int):
		"""Sets the vertical_speed of this LocationInfoVelocity.

		Vertical speed, expressed in km/h and defined in [14]. Present only if \"velocityType\" equals 2 or 4  # noqa: E501

		:param vertical_speed: The vertical_speed of this LocationInfoVelocity.
		:type vertical_speed: int
		"""

		self._vertical_speed = vertical_speed

	@property
	def vertical_uncertainty(self) -> int:
		"""Gets the vertical_uncertainty of this LocationInfoVelocity.

		Vertical uncertainty, as defined in [14]. Present only if \"velocityType\" equals 4  # noqa: E501

		:return: The vertical_uncertainty of this LocationInfoVelocity.
		:rtype: int
		"""
		return self._vertical_uncertainty

	@vertical_uncertainty.setter
	def vertical_uncertainty(self, vertical_uncertainty: int):
		"""Sets the vertical_uncertainty of this LocationInfoVelocity.

		Vertical uncertainty, as defined in [14]. Present only if \"velocityType\" equals 4  # noqa: E501

		:param vertical_uncertainty: The vertical_uncertainty of this LocationInfoVelocity.
		:type vertical_uncertainty: int
		"""

		self._vertical_uncertainty = vertical_uncertainty
