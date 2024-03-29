from __future__ import annotations
import math

class Vector:

	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y

	# Define what to show when print'ing this class
	def __repr__(self):
		return 'Vector(%r, %r)' % (self.x, self.y)

	# Define the absolute as the magnitude of a vector
	def __abs__(self):
		return math.hypot(self.x, self.y)

	# Addition of Vector types
	def __add__(self, other):
		x = self.x + other.x
		y = self.y + other.y
		return Vector(x, y)
	
	# Subtraction of Vector types
	def __sub__(self, other):
		x = self.x - other.x
		y = self.y - other.y
		return Vector(x, y)

	# Multiplication: Vector on the left of the operation
	def __mul__(self, scalar):
		return Vector(self.x * scalar, self.y * scalar)

	# Multiplication: allow Vector to be on the right of the operation
	def __rmul__(self, scalar: int):
		return Vector(self.x * scalar, self.y * scalar)

	# vector dot product
	def dot(self, other: Vector) -> int:
		"""

		:param other: Vector object to multiply with
		:type other: Vector
		:rtype: int
		"""
		return self.x * other.x + self.y * other.y
