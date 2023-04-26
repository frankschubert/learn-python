import Vector


def test_create_instance_with_defaults():
    v1 = Vector.Vector()
    assert v1.x == 0
    assert v1.y == 0


def test_create_instance_with_values():
    v1 = Vector.Vector(1, 2)
    assert v1.x == 1
    assert v1.y == 2


def test_repr():
    assert repr(Vector.Vector(1, 2)) == "Vector(1, 2)"


def test_abs():
    v1 = Vector.Vector(3, 4)
    assert abs(v1) == 5


def test_addition():
    v1 = Vector.Vector(1, 2)
    v2 = Vector.Vector(1, 2)
    v3 = v1 + v2
    assert v3.x == 2
    assert v3.y == 4


def test_subtraction():
    v1 = Vector.Vector(2, 4)
    v2 = Vector.Vector(1, 2)
    v3 = v1 - v2
    assert v3.x == 1
    assert v3.y == 2


def test_multiplication():
    v1 = Vector.Vector(1, 2)
    v2 = v1 * 2
    assert v2.x == 2
    assert v2.y == 4


def test_dot_multiplication():
    v1 = Vector.Vector(-6, 8)
    v2 = Vector.Vector(5, 12)
    assert v1.dot(v2) == 66
