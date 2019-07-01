import unittest

from pyscience.geometry import *


class TestGeometry(unittest.TestCase):

    def test_square(self):
        square = Square(l=9)

        self.assertEqual(square.area, 81)
        self.assertEqual(square.perimeter, 36)

    def test_triangle(self):
        triangle = Triangle(b=10, h=8)

        self.assertEqual(triangle.area, 40)

    def test_rectangle(self):
        rectangle = Rectangle(b=10, h=5)

        self.assertEqual(rectangle.area, 50)
        self.assertEqual(rectangle.perimeter, 30)

    # TODO: Parallelogram tests
    # def test_parallelogram(self):

    # TODO: Diamond tests
    # def test_diamond(self):

    def test_polygon(self):
        polygon = Polygon(L=5, a=5, nL=6)

        self.assertEqual(polygon.perimeter, 30)
        self.assertEqual(polygon.area, 75)
