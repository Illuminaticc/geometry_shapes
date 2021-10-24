from math import pi, sqrt


class Shape:
    """
    This is a abstract class representing geometrical shape.
    """
    title = 'Фигура'

    def area(self):
        """
        Calculates shape's area.
        returns: float -> area of the shape
        """
        pass


class Square(Shape):
    title = 'Квадрат'

    def __init__(self, a: int):
        """
        Constructs a Square object
        param a: int -> side of a Square
        """
        super().__init__()
        self.a = a

    def perimeter(self):
        """
        Calculates Square perimeter using formula: 4 * a
        return: float -> perimeter of the Square
        """
        return 4 * self.a
    
    def area(self):
        """
        Calculates Square area using formula: a ** 2
        return: float -> area of the Square
        """
        return self.a ** 2


class Cube(Square):
    title = 'Куб'

    def area(self):
        """
        Calculates Cube area using formula: 6 * a ** 2
        return: float -> area of the Cube
        """
        return 6 * self.a ** 2


class Rectangle(Square):
    title = 'Прямоугольник'

    def __init__(self, a, b: int):
        """
        Constructs a Rectangle object
        param a: int -> first side of a Rectangle
        param b: int -> second side of a Rectangle
        """
        super().__init__(a)
        self.b = b

    def perimeter(self):
        """
        Calculates Rectangle perimeter using formula: 2 * (a + b)
        return: float -> perimeter of the Rectangle
        """
        return 2 * (self.a + self.b)

    def area(self):
        """
        Calculates Rectangle area using formula: a * b
        return: float -> area of the Rectangle
        """
        return self.a * self.b


class Parallelepiped(Rectangle):
    title = 'Параллелепипед'
    
    def __init__(self, a, b, c: int):
        """
        Constructs a Parallelepiped object
        param a: int -> first side of a Parallelepiped
        param b: int -> second side of a Parallelepiped
        param c: int -> third side of a Parallelepiped
        """
        super().__init__(a, b)
        self.c = c

    def perimeter(self):
        """
        Calculates Parallelepiped perimeter using formula: (a + b + 2) * c
        return: float -> perimeter of the Parallelepiped
        """
        return (self.a + self.b + 2) * self.c 

    def area(self):
        """
        Calculates Parallelepiped area using formula: a * b + b * c + a * c
        return: float -> area of the Parallelepiped
        """
        return 2 * (self.a * self.b + self.b * self.c + self.a * self.c)


class Trapezoid(Rectangle):
    title = 'Трапеция'
    
    def __init__(self, a, b, h: int):
        """
        Constructs a Trapezoid object
        param a: int -> first side of a Trapezoid
        param b: int -> second side of a Trapezoid
        param h: int -> height  of a Trapezoid
        """
        super().__init__(a, b)
        self.h = h

    def area(self):
        """
        Calculates Trapezoid area using formula: (a * b) / 2 * h
        return: float -> area of the Trapezoid
        """
        return (self.a + self.b) / 2 * self.h 


class Rhombus(Square):
    title = 'Ромб'
    
    def __init__(self, a, h: int):
        """
        Constructs a Rhombus object
        param a: int -> first side of a Rhombus
        param h: int -> height of a Rhombus

        """
        super().__init__(a)
        self.h = h

    def perimeter(self):
        """
        Calculates Trapezoid perimeter using formula: 4 * a
        return: float -> perimeter of the Trapezoid
        """
        return 4 * self.a
    
    def area(self):
        """
        Calculates Rhombus area using formula: (a * c) / (b * d) / 2 
        return: float -> area of the Rhombus
        """
        return self.a * self.h


class Circle(Shape):
    title = 'Круг'

    def __init__(self, r: int):
        """
        Constructs a Circle object
        param r: int -> radius of a Circle
        """
        super().__init__()
        self.r = r

    def area(self):
        """
        Calculates Circle area using formula: 3.14 * r ** 2
        return: float -> area of the Circle
        """
        return pi * self.r ** 2


class Sphere(Circle):
    title = 'Сфера'

    def area(self):
        """
        Calculates Sphere area using formula: 4 * 3.14 * r ** 2
        return: float -> area of the Circle
        """
        return 4 * pi * self.r ** 2


class Cylinder(Circle):
    title = 'Цилиндр'

    def __init__(self, r, h: int):
        """
        Constructs a Cylinder object
        param r: int -> radius of a Cylinder
        param h: int -> height of a Cylinder
        """    
        super().__init__(r)
        self.h = h

    def area(self):
        """
        Calculates Cylinder area using formula: 2 * 3.14 * r * (r * h)
        return: float -> area of the Cylinder
        """
        return 2 * pi * self.r * (self.r + self.h)


class Triangle(Shape):
    title = 'Треугольник'

    def __init__(self, a: int, b: int, c: int):
        """
        Constructs a Triangle object
        param a: int -> first side of a Triangle
        param b: int -> second side of a Triangle
        param c: int -> third side of a Triangle
        """    
        self.a = a
        self.b = b
        self.c = c

    def median(self):
        return 0.5 * sqrt(2 * self.a ** 2 + 2 * self.b ** 2 - self.c**2)
    
    def area(self):
        """
        Calculates Triangle area using formula: sqrt(p * (p - a) * (p - b) * (p - c))
        return: float -> area of the Triangle
        """
        p = (self.a + self.b + self.c) / 2
        return sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))


class Cone(Circle):
    title = 'Конус'

    def __init__(self, r, g: int):
        """
        Constructs a Cone object
        param r: int -> radius of a Cone
        param g: int -> generatrix of a Cone
        """    
        super().__init__(r)
        self.g = g

    def area(self):
        """
        Calculates Cone area using formula: 0,5 * r * g
        return: float -> area of the Cone
        """
        return pi * self.r * (self.g + self.r)


class Pyramid(Square):
    title = 'Пирамида'

    def __init__(self, a, side: int):
        """
        Constructs a Pyramid object
        param a: int -> side of a Pyramid
        param side: int -> side edge of a Pyramid
        """    
        super().__init__(a)
        self.side = side

    def area(self):
        """
        Calculates Pyramid area using formula: 2 * a * sqrt(side ** 2 - a ** 2 / 4)
        return: float -> area of the Pyramid
        """
        return self.a ** 2 + 2 * self.a * sqrt((self.side ** 2) - (self.a ** 2 / 4))
