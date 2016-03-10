#!/usr/bin/env python
from math import pi

######################################################
##############    CIRCLE CLASS EXERCISE ##############
######################################################

class Circle(object):

	def __init__(self, radius):
		self._radius = radius
		self._diameter = (radius*2)
		self._area = (pi*radius**2)

	def __str__(self):
		return 'Circle with radius: {}'.format(self._radius)

	#cant get this to work
	def __repr__(self):
		return 'Circle(%s)' % super (Circle, self).__repr__()

	@classmethod
	def from_diameter(cls, diameter):
		return cls(diameter/2)

	@property
	def radius(self):
		return self._radius

	@property
	def diameter(self):
		return self._diameter
	
	@property
	def area(self):
		return self._area

	@radius.setter
	def radius(self, radius):
		self._radius = radius
		self._diameter = (radius*2)

	@diameter.setter
	def diameter(self, diameter):
		self._diameter = diameter
		self._radius = (diameter/2)


