from abc import ABC, abstractmethod
import math


class Square:
    """Класс Square - квадрат"""

    def __init__(self, size: float) -> None:
        self.__size = size

    def get_square(self) -> float:
        return self.__size

    def set_square(self, val: float) -> None:
        self.__size = val

    size = property(get_square, set_square)

    @property
    def square(self) -> float:
        return self.__size ** 2

    @property
    def perimeter(self) -> float:
        return self.__size * 4

    def __str__(self) -> str:
        return f'Площадь квадрата: {self.square}\nПериметр квадрата: {self.perimeter}\n'


class Triangle:
    """Класс Triangle - треугольник"""

    def __init__(self, base: float, height: float):
        self.__base = base
        self.__height = height

    def get_base(self) -> float:
        return self.__base

    def set_base(self, val: float) -> None:
        self.__base = val

    base = property(get_base, set_base)

    def get_height(self) -> float:
        return self.__height

    def set_height(self, val: float) -> None:
        self.__height = val

    height = property(get_height, set_height)

    @property
    def square_tr(self) -> float:
        return self.__base * self.__height / 2

    @property
    def perimeter(self) -> float:
        return self.__base + 2 * math.sqrt(self.__height ** 2 + self.__base ** 2 / 4)

    def __str__(self) -> str:
        return f'Площадь треугольника: {self.square_tr}' \
               f'\nПериметр треугольника: {self.perimeter}\n'


class Mix:
    def __init__(self, size: float, base: float, height: float) -> None:
        self.size = size
        self.base = base
        self.height = height


class Pyramid(Mix, Square, Triangle):
    """Класс Pyramid - пирамида, унаследованный от класса Square - квадрат
    Square - квадрата и Triangle - треугольника
    """

    def __init__(self, size: float, base: float, height: float) -> None:
        super().__init__(size, base, height)
        self.__pyramid = [super().square] + [super().square_tr] * 4

    def __str__(self) -> str:
        return f'Площадь поверхности пирамиды {self.__pyramid}: {sum(self.__pyramid)}\n'


class Cube(Square):
    """Класс Cube - куб, унаследованный от класса Square - квадрат"""

    def __init__(self, size: float) -> None:
        super().__init__(size)
        self.__cube = [self.square] * 6

    def __str__(self) -> str:
        return f'Площадь поверхности куба {self.__cube}: {sum(self.__cube)}\n'


sq = Square(10)
print(sq)
tr = Triangle(10, 6)
print(tr)
cub = Cube(10)
print(cub)
pyr = Pyramid(10, 10, 6)
print(pyr)
