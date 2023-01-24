"""
Description: 3D mathmatical vector class and brief testing
Names: Millan and Jerry 
Date: 1/24/23
"""

from __future__ import annotations  # type hint support
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
            return NotImplemented

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
        else:
            return NotImplemented

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
        else:
            return NotImplemented

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
            return self * (1.0 / abs(self))  # types are actually fine here

    def addMultiple(self, *args: Vector3) -> None:
        """Add multiple vectors to self."""
        for vec in args:
            self += vec


def main():
    """Test the Vector3 class."""

    vec3 = Vector3(1, 2, 3)

    # test __str__
    assert str(vec3) == "<1, 2, 3>"

    # test __repr__
    assert repr(vec3) == "Vector3(1, 2, 3)"

    # test __getitem__
    assert vec3[0] == 1
    assert vec3[1] == 2
    assert vec3[2] == 3

    assert vec3["x"] == 1
    assert vec3["y"] == 2
    assert vec3["z"] == 3

    # test __setitem__
    vec3[0] = 4
    vec3[1] = 5
    vec3[2] = 6

    assert vec3[0] == 4
    assert vec3[1] == 5
    assert vec3[2] == 6

    vec3["x"] = 7
    vec3["y"] = 8
    vec3["z"] = 9

    assert vec3["x"] == 7
    assert vec3["y"] == 8
    assert vec3["z"] == 9

    # test __mul__(float)
    assert vec3 * 2.0 == Vector3(14, 16, 18)
    assert 2.0 * vec3 == Vector3(14, 16, 18)

    otherVec3 = Vector3(1, 2, 3)

    # test __mul__(Vector3)
    assert vec3 * otherVec3 == 50
    assert otherVec3 * vec3 == 50

    # test __matmul__
    assert vec3 @ otherVec3 == Vector3(6, -12, 6)
    assert otherVec3 @ vec3 == Vector3(-6, 12, -6)


if __name__ == "__main__":
    main()
