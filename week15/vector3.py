from __future__ import annotations  # type hint support
from typing import Iterator

# from numbers import float
import math
import pickle


class Vector3:
    """Represents a mathmatical 3D vector"""
    def __init__(self, x: float = 0.0, y: float = 0.0, z: float = 0.0):
        """Initialize self. See help(type(self)) for accurate signature."""
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self) -> str:
        """Python-readable string representation"""
        return f"Vector3({self.x}, {self.y}, {self.z})"

    def __str__(self) -> str:
        """Human-readable string representation"""
        return f"<{self.x}, {self.y}, {self.z}>"

    def __abs__(self) -> float:
        """Returns the magnitude of the vector"""
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def __len__(self) -> int:
        """Returns the number of dimensions of the vector (always 3)"""
        return 3

    def __bool__(self) -> bool:
        """Returns False if zero vector"""
        return abs(self) != 0

    def __bytes__(self) -> bytes:
        """Pickled version of self"""
        return pickle.dumps(self)

    def __getitem__(self, index: int | str) -> float:
        """Supports access using 0, 1, 2, 'x', 'y', or 'z' as index."""
        if isinstance(index, int):
            return [self.x, self.y, self.z][index]
        elif isinstance(index, str):
            return {"x": self.x, "y": self.y, "z": self.z}[index]
        else:
            raise TypeError(f"Index must be int or str, not {type(index)}")

    def __setitem__(self, index: int | str, value: float) -> None:
        """Supports access using 0, 1, 2, 'x', 'y', or 'z' as index."""
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

    def __iter__(self) -> Iterator[float]:
        """Iterate over the components of the vector."""
        yield self.x
        yield self.y
        yield self.z
        # TODO: how does '__next__' work?

    def __add__(self, other: Vector3) -> Vector3:
        """Component-wise addition"""
        return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __iadd__(self, other: Vector3) -> Vector3:
        """Component-wise addition"""
        self.x += other.x
        self.y += other.y
        self.z += other.z
        return self

    def __sub__(self, other: Vector3) -> Vector3:
        """Component-wise subtraction"""
        return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __isub__(self, other: Vector3) -> Vector3:
        """Component-wise subtraction"""
        self.x -= other.x
        self.y -= other.y
        self.z -= other.z
        return self

    def __mul__(self, other: float | Vector3) -> float | Vector3:
        """
        Dot product, or scalar multiplication, depending on inputs.
        If other is a float, component-wise scalar multiplication
        If other is a Vector3, dot product between self and other.
        """
        if isinstance(other, Vector3):  # dot product
            return self.x * other.x + self.y * other.y + self.z * other.z
        elif isinstance(other, float):  # scalar multiplication
            return Vector3(self.x * other, self.y * other, self.z * other)

    def __rmul__(self, other: float | Vector3) -> float | Vector3:
        """Handles case scalar * Vector3 -> Vector3"""
        return self.__mul__(other)

    def __matmul__(self, other: Vector3):  # cross product
        """Returns the cross product of self and other."""
        return Vector3(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x,
        )

    def __neg__(self) -> Vector3:
        """Negate each coordinate"""
        return Vector3(-self.x, -self.y, -self.z)

    def __pos__(self) -> Vector3:
        """Return a copy of self"""
        return Vector3(self.x, self.y, self.z)

    def __eq__(self, other: object) -> bool:
        """Two vectors are equal if all three components are equal."""
        if isinstance(other, Vector3):
            return self.x == other.x and self.y == other.y and self.z == other.z
        raise TypeError(f"Cannot compare Vector3 to {type(other)}")

    def normalized(self) -> Vector3:
        """Unit vector in the same direction as self."""
        length = abs(self)
        if length == 0:
            return +self  # '+' is used here to make a copy
        else:
            return self * (1.0 / abs(self)) # types are actually fine here

    def addMultiple(self, *args: Vector3) -> Vector3:
        """Add multiple vectors to self."""
        for arg in args:
            self += arg
        return self


def main():
    """Test the Vector3 class."""

    ...

if __name__ == "__main__":
    main()