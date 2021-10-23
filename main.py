from shapes import *

shape_list = {1: 'Square', 2: 'Cube', 3: 'Rectangle', 4: 'Parallelepiped', 5: 'Trapezoid', 6: 'Rhombus', 7: 'Circle',
              8: 'Sphere', 9: 'Cylinder', 10: 'Triangle', 11: 'Cone', 12: 'Pyramid'}

while True:
    print('Выберите фигуру: ')
    for key, value in shape_list.items():
        print(key, value)
    number = int(input())
    print(
    '''Для Квадрата, Куба, Прямоугольника, Треугольника и Параллепипеда  введите последовательно стороны через ввод 
Для Трапеции 2 стороны и высоту
Для Ромба сторону и высоту
Для Сферы и Круга введите радиус
Для Цилиндра введите радиус и высоту
Для Конуса введите радиус и образующую
Для Пирамиды введите сторону и боковую грань''')
    if number == 1: 
        myshape = Square(int(input()))
        print('Периметр = ', myshape.perimeter())
        print('Площадь = ', myshape.area())
    elif number == 2:
        myshape = Cube(int(input()))
        print('Площадь = ', myshape.area())
    elif number == 3:
        myshape = Rectangle(int(input()), int(input()))
        print('Периметр = ', myshape.perimeter())
        print('Площадь = ', myshape.area())
    elif number == 4:
        myshape = Parallelepiped(int(input()), int(input()), int(input()))
        print('Периметр = ', myshape.perimeter())
        print('Площадь = ', myshape.area())
    elif number == 5:
        myshape = Trapezoid(int(input()), int(input()), int(input()))
        print('Площадь = ', myshape.area())
    elif number == 6:
        myshape = Rhombus(int(input()), int(input()))
        print('Периметр = ', myshape.perimeter())
        print('Площадь = ', myshape.area())
    elif number == 7:
        myshape = Circle(int(input()))
        print('Площадь = ', myshape.area())
    elif number == 8:
        myshape = Sphere(int(input()))
        print('Площадь = ', myshape.area())
    elif number == 9:
        myshape = Cylinder(int(input()), int(input()))
        print('Площадь = ', myshape.area())
    elif number == 10:
        myshape = Triangle(int(input()), int(input()), int(input()))
        print('Медиана = ', myshape.median())
        print('Площадь = ', myshape.area())
    elif number == 11:
        myshape = Cone(int(input()), int(input()))
        print('Площадь = ', myshape.area())
    elif number == 12:
        myshape = Pyramid(int(input()), int(input()))
        print('Площадь = ', myshape.area())

