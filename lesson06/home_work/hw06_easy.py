# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

import math


class Triangle:

    # вычисление длинн отрезков через координаты

    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1, self.y1, self.x2, self.y2, self.x3, self.y3 = x1, y1, x2, y2, x3, y3
        self.a = math.sqrt(abs(((x1 - x2) ** 2 + (y1 - y2) ** 2)))
        self.b = math.sqrt(abs(((x2 - x3) ** 2 + (y2 - y3) ** 2)))
        self.c = math.sqrt(abs(((x3 - x1) ** 2 + (y3 - y1) ** 2)))

    # периметр треугольника

    def _perimeter(self):
        self.perimeter = self.a + self.b + self.c
        return self.perimeter

    # площадь треугольника

    def _area(self):
        p = self.perimeter / 2
        self.area = math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
        return self.area

    # высота треугольника

    def _height(self):
        self.height = 2 * self.area / self.a
        return self.height


t = Triangle(0, 2, 3, 4, 5, -10)

print(f'\nДлина строны a = {t.a}, b = {t.b}, c = {t.c}')
print(f'Периметр треугольника P = {t._perimeter()}')
print(f'Площадь треугольника S = {t._area()}')
print(f'Высота треугольника h = {t._height()}', '\n')


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class Trapezium:
    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4):
        self.x1, self.y1, self.x2, self.y2, self.x3, self.y3, self.x4, self.y4 = x1, y1, x2, y2, x3, y3, x4, y4
        self.c = math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))
        self.d = math.sqrt(((x4 - x3) ** 2) + ((y4 - y3) ** 2))
        self.a = math.sqrt(((x3 - x2) ** 2) + ((y3 - y2) ** 2))
        self.b = math.sqrt(((x4 - x1) ** 2) + ((y4 - y1) ** 2))

    def check_trapezium(self):
        if self.c == self.d:
            print("Трапеция равнобокая")
        else:
            print("Трапеция неравнобокая")

    def _perimeter(self) -> object:
        self.perimeter = self.a + self.b + self.c + self.d
        return self.perimeter

    def _area(self):
        self.area = ((self.a + self.b) / 2) * (math.sqrt((self.c ** 2) - ((((self.b - self.a) ** 2) + (self.c ** 2) -
                                                                           (self.d ** 2)) / (2 * (self.b - self.a)))))
        return self.area


tp = Trapezium(0, 0, 2, 2, 4, 4, 6, 6)

tp.check_trapezium()
print(f'Периметр трапеции равен P = {tp._perimeter()}')
print(f'Длина строны a = {tp.a}, b = {tp.b}, c = {tp.c}, d = {tp.d}')
print(f'Площадь: S = {tp._area()}')
