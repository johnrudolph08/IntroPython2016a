import circle_class as cc
import pytest
from math import pi

def test_radius():
	'''
	test that radius can be set on init
	and called via get property
	'''
	radius = 4
	c = cc.Circle(4)
	assert radius == c.radius

def test_diameter():
	'''
	test that diameter is set when radius is provided
	'''
	radius = 4
	c = cc.Circle(4)
	assert radius*2 == c.diameter

def test_set_diameter():
	'''
	test that a new diameter can be set based on set property
	test that radius is reset when diameter is set
	'''
	c = cc.Circle(4)
	new_diameter = 2
	c.diameter = new_diameter
	assert c.diameter == new_diameter
	assert c.radius == 1

def test_area():
	'''
	test that an area attribute is set when Circle is init
	'''
	c = cc.Circle(4)
	area = (c.radius**2*pi)
	assert c.area == area

def test_area_error():
	'''
	Check if setting area raises an Attribute Error
	'''
	c = cc.Circle(4)
	with pytest.raises(AttributeError):
		c.area = 2

def test_alternate_constructor():
	'''
	Check if setting area raises an Attribute Error
	'''
	diameter = 8
	c = cc.Circle.from_diameter(diameter)
	assert c.radius == (diameter/2)
	
def test_str_method():
	'''
	Check if __str__ method works as intended
	'''
	radius = 4
	c = cc.Circle(radius)
	s = 'Circle with radius: {}'.format(radius)
	assert s == str(c)

def test_repr_method():
	'''
	Check if __str__ method works as intended
	'''
	radius = 4
	c = cc.Circle(radius)
	s = 'Circle({})'.format(radius)
	repr(c)
	d = eval(repr(c))
	assert s == d

c = Circle(4)
repr(c)
d = eval(repr(c))
print(d)
