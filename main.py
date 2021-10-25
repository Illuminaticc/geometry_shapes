from shapes import *

shape_list = ['Square', 'Cube', 'Rectangle', 'Parallelepiped', 'Trapezoid', 'Rhombus', 'Circle',
              'Sphere', 'Cylinder', 'Triangle', 'Cone', 'Pyramid']
string_perimeter = 'Периметр = '
string_area = 'Площадь = '


def main():
    while True:
        try:
            print('Выберите фигуру: ')
            for i, shape in enumerate(shape_list, start=1):
                print(i, shape)
            number = int(input())
            print('''Для Квадрата, Куба, Прямоугольника, Треугольника и Параллепипеда  введите последовательно стороны 
            через ввод, 
            Для Трапеции 2 стороны и высоту,
            Для Ромба сторону и высоту,
            Для Сферы и Круга введите радиус,
            Для Цилиндра введите радиус и высоту,
            Для Конуса введите радиус и образующую,
            Для Пирамиды введите сторону и боковую грань.''')
            if number == 1:
                my_shape = Square(float(input()))
                print(f'{string_perimeter}', my_shape.perimeter())
                print(f'{string_area}', my_shape.area())
            elif number == 2:
                my_shape = Cube(int(input()))
                print(f'{string_area}', my_shape.area())
            elif number == 3:
                my_shape = Rectangle(int(input()), int(input()))
                print(f'{string_perimeter}', my_shape.perimeter())
                print(f'{string_area}', my_shape.area())
            elif number == 4:
                my_shape = Parallelepiped(int(input()), int(input()), int(input()))
                print(f'{string_perimeter}', my_shape.perimeter())
                print(f'{string_area}', my_shape.area())
            elif number == 5:
                my_shape = Trapezoid(float(input()), float(input()), float(input()))
                print(f'{string_area}', my_shape.area())
            elif number == 6:
                my_shape = Rhombus(float(input()), float(input()))
                print(f'{string_perimeter}', my_shape.perimeter())
                print(f'{string_area}', my_shape.area())
            elif number == 7:
                my_shape = Circle(float(input()))
                print(f'{string_area}', my_shape.area())
            elif number == 8:
                my_shape = Sphere(float(input()))
                print(f'{string_area}', my_shape.area())
            elif number == 9:
                my_shape = Cylinder(float(input()), float(input()))
                print(f'{string_area}', my_shape.area())
            elif number == 10:
                my_shape = Triangle(float(input()), float(input()), float(input()))
                print('Медиана = ', my_shape.median())
                print(f'{string_area}', my_shape.area())
            elif number == 11:
                my_shape = Cone(float(input()), float(input()))
                print(f'{string_area}', my_shape.area())
            elif number == 12:
                my_shape = Pyramid(float(input()), float(input()))
                print(f'{string_area}', my_shape.area())
        except (ValueError, ArithmeticError):
            print('Ввести необходимо числа через Enter!')


if __name__ == '__main__':
    main()
