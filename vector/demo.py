from Vector import Vector

v1 = Vector(2, 4)
v2 = Vector(2, 1)

print(v1)
print(v2)


v3 = v1 + v2
print('v1 + v2 = ', v3)

v4 = v1 - v2
print('v1 - v2 = ', v4)

v4 = v1 * 5
print('v1 * 5 = ', v4)

v5 = 5 * v1
print('5 * v1 = ', v5)

v3 = Vector(-6, 8)
v4 = Vector(5, 12)
scalar = v3.dot(v4)
print(scalar)
