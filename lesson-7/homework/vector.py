from __future__ import annotations
import math
class Vector:
    def __init__(self, *args):
        self.values = args
    
    def __len__(self):
        return len(self.values)
    
    def __add__(self, other: Vector):
        if len(self) != len(other):
            raise Exception("Vectors in two different dimensions can not be added!")
        else :
            s = Vector(*(i + j for i, j in zip(self.values, other.values)))
            return s
    
    def __sub__(self, other: Vector):
        if len(self) != len(other):
            raise Exception("Vectors in two different dimensions can not be added!")
        else :
            return Vector(*(i - j for i, j in zip(self.values, other.values)))

    def __mul__(self, other: Vector | int | float):
        if isinstance(other, Vector): 
            if len(self) != len(other):
                raise ValueError("Vectors in different dimensions cannot be multiplied!")
            return sum(i * j for i, j in zip(self.values, other.values))

        elif isinstance(other, (int, float)):  
            return Vector(*(i * other for i in self.values))

        else:
            raise TypeError("Multiplication is only supported for Vectors or scalars.")

    def magnitude(self):
        return math.sqrt(sum(i ** 2 for i in self.values))

    def normalize(self):
        return Vector(*((round(i / self.magnitude(), 3) for i in self.values)))

    def __str__(self):
        return f'Vector{self.values}'

v1 = Vector(1, 2, 3, 5, 35, -354, 565)
v2 = Vector(4, 5, 6, 45, -334, -34, -343)
print(v1)

v3 = v1 + v2
print(v3)

v4 = v2 - v1
print(v4)

dot_product = v1 * v2
print(dot_product)

v5 = v1 * 3
print(v5)

print(v1.magnitude())

v_unit = v1.normalize()
print(v_unit)