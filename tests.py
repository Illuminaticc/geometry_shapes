import unittest
from math import pi, sqrt
from shapes import *


class SquareTester(unittest.TestCase):
    def test_perimeter(self):
        a = 2
        s = Square(a)
        perimeter = 4 * a
        self.assertEqual(s.perimeter(), perimeter)

    def test_area(self):
        a = 2
        s = Square(a)
        area = a ** 2
        self.assertEqual(s.area(), area)


class CubeTester(unittest.TestCase):
    def test_area(self):
        a = 2
        c = Cube(a)
        area = 6 * a ** 2
        self.assertEqual(c.area(), area)


class RectangleTester(unittest.TestCase):
    def test_perimeter(self):
        a = 2
        b = 4
        r = Rectangle(a, b)
        perimeter = 2 * (a + b)
        self.assertEqual(r.perimeter(), perimeter)

    def test_area(self):
        a = 2
        b = 4
        r = Rectangle(a, b)
        area = a * b
        self.assertEqual(r.area(), area)


class ParallelepipedTester(unittest.TestCase):
    def test_perimeter(self):
        a = 2
        b = 2
        c = 2
        p = Parallelepiped(a, b, c)
        perimeter = (a + b + 2) * c
        self.assertEqual(p.perimeter(), perimeter)
    
    def test_area(self):
        a = 2
        b = 2
        c = 2
        p = Parallelepiped(a, b, c)
        area = 2 * (a * b + b * c + a * c)
        self.assertEqual(p.area(), area)


class TrapezoidTester(unittest.TestCase):
    def test_area(self):
        a = 2
        b = 4
        h = 3
        t = Trapezoid(a, b, h)
        area = (a + b) / 2 * h
        self.assertEqual(t.area(), area)


class RhombusTester(unittest.TestCase):
    def test_perimeter(self):
        a = 6
        h = 4
        r = Rhombus(a, h)
        perimeter = 4 * a
        self.assertEqual(r.perimeter(), perimeter)
    
    def test_area(self):
        a = 4
        h = 4
        c = Rhombus(a, h)
        area = a * h
        self.assertEqual(c.area(), area)


class CircleTester(unittest.TestCase):
    def test_area(self):
        r = 5
        c = Circle(r)
        area = pi * r ** 2
        self.assertEqual(c.area(), area)


class SphereTester(unittest.TestCase):
    def test_area(self):
        r = 3
        s = Sphere(r)
        area = 4 * pi * r ** 2
        self.assertEqual(s.area(), area)


class CylinderTester(unittest.TestCase):
    def test_area(self):
        r = 3
        h = 6
        c = Cylinder(r, h)
        area = 2 * pi * r * (r + h)
        self.assertEqual(c.area(), area)


class TriangleTester(unittest.TestCase):
    def test_median(self):
        a = 3
        b = 4
        c = 5
        t = Triangle(a, b, c)
        median = 0.5 * sqrt(2 * a ** 2 + 2 * b ** 2 - c**2)
        self.assertEqual(t.median(), median)
    
    def test_area(self):
        a = 2
        b = 3
        c = 4
        t = Triangle(a, b, c)
        p = (a + b + c) / 2
        area = sqrt(p * (p - a) * (p - b) * (p - c))
        self.assertEqual(t.area(), area)


class ConeTester(unittest.TestCase):
    def test_area(self):
        r = 5
        g = 3
        c = Cone(r, g)
        area = pi * r * (g + r)
        self.assertEqual(c.area(), area)


class PyramidTester(unittest.TestCase):
    def test_area(self):
        a = 3
        s = 4
        p = Pyramid(a, s)
        area = a ** 2 + 2 * a * sqrt((s ** 2) - (a ** 2 / 4))
        self.assertEqual(p.area(), area)


def main():
    unittest.main(verbosity=2)


if __name__ == '__main__':
    main()
