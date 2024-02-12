import sympy
import random
import pytest
from read import to_expr, to_line_object
from classes import Point, Line

POINTS = {
    'A': Point('A', 5, 5),
    'O': Point('O', 0, 0),
    'B': Point('B', 5, 0)
}


def test_pi():
    assert to_expr('π', POINTS) == sympy.pi
    assert to_expr('2*π', POINTS) == 2 * sympy.pi


def test_angle():
    assert to_expr('tan∠AOB', POINTS) == 1


def test_sqrt():
    assert to_expr('sqrt(4)', {}) == 2
    assert to_expr('sqrt(16)', {}) == 4

    # Auto Generated Cases
    for _ in range(100):
        x = random.randrange(int(0), int(1e5))

        assert to_expr(f'sqrt({x**2})', {}) == x


def test_to_line_object():
    assert to_line_object('BO', POINTS).p1 == POINTS['B']
    assert to_line_object('BO', POINTS).p2 == POINTS['O']
    assert to_line_object('BO', POINTS).k == 0

    with pytest.raises(ZeroDivisionError):
        to_line_object('AB', POINTS)
