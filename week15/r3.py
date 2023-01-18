from __future__ import annotations  # type hint support
from typing import Iterator

from numbers import Real
import math
import pickle

class R3:
	def __init__(self, x: Real = 0.0, y: Real = 0.0, z: Real = 0.0):
		self.x = x
		self.y = y
		self.z = z

	def __repr__(self) -> str:
		return f"R3({self.x}, {self.y}, {self.z})"

	def __str__(self) -> str:
		return f"<{self.x}, {self.y}, {self.z}>"

	def __abs__(self) -> R3:
		return R3(abs(self.x), abs(self.y), abs(self.z))

	def __len__(self) -> Real:
		return math.sqrt(self.x**2 + self.y**2 + self.z**2)

	def __bool__(self) -> bool:
		return len(self) == 0

	def __bytes__(self) -> bytes:
		return pickle.dumps(self)

	def __getitem__(self, index: int | str) -> Real:
		if isinstance(index, int):
			return [self.x, self.y, self.z][index]
		elif isinstance(index, str):
			return {"x": self.x, "y": self.y, "z": self.z}[index]
		else:
			raise TypeError(f"Index must be int or str, not {type(index)}")

	def __setitem__(self, index: int | str, value: Real) -> None:
		if isinstance(index, int):
			match index:
				case 0:
					self.x = value
				case 1:
					self.y = value
				case 2:
					self.z = value
				case _:
					raise IndexError(f"Index {index} out of range")
		elif isinstance(index, str):
			match index:
				case "x":
					self.x = value
				case "y":
					self.y = value
				case "z":
					self.z = value
				case _:
					raise KeyError(f"Key {index} not found")

	def __iter__(self) -> Iterator[Real]:
		yield self.x
		yield self.y
		yield self.z
		# TODO: how does '__next__' work?

	def __add__(self, other: R3) -> R3:
		return R3(self.x + other.x, self.y + other.y, self.z + other.z)

	def __iadd__(self, other: R3) -> R3:
		self.x += other.x
		self.y += other.y
		self.z += other.z
		return self

	def __sub__(self, other: R3) -> R3:
		return R3(self.x - other.x, self.y - other.y, self.z - other.z)

	def __isub__(self, other: R3) -> R3:
		self.x -= other.x
		self.y -= other.y
		self.z -= other.z
		return self

	def __mul__(self, other: Real | R3) -> Real | R3:
		if isinstance(other, R3):  # dot product
			return self.x * other.x + self.y * other.y + self.z * other.z
		elif isinstance(other, Real):  # scalar multiplication
			return R3(self.x * other, self.y * other, self.z * other)

	def __rmul__(self, other: Real | R3) -> Real | R3:
		return self.__mul__(other)

	def __matmul__(self, other: R3):  # cross product
		return R3(
			self.y * other.z - self.z * other.y,
			self.z * other.x - self.x * other.z,
			self.x * other.y - self.y * other.x,
		)

	def __neg__(self) -> R3:
		return R3(-self.x, -self.y, -self.z)

	def __pos__(self) -> R3:
		return R3(self.x, self.y, self.z)

	def __eq__(self, other: object) -> bool:
		if isinstance(other, R3):
			return self.x == other.x and self.y == other.y and self.z == other.z
		raise TypeError(f"Cannot compare R3 to {type(other)}")

	def normalized(self) -> R3:
		return self * (1 / len(self))

	def addMultiple(self, *args: R3) -> R3:
		for arg in args:
			self += arg
		return self