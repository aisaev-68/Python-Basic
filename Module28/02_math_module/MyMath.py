import math


class MyMath:
    """Класс MyMath, реализущий методы:
    - нахождение длины окружности,
    - площадь окружности,
    - объём куба,
    - площадь поверхности сферы.
    """
    @classmethod
    def circle_len(cls, radius: float) -> float:
        """Метод - Длина окружности"""
        return 2 * math.pi * radius

    @classmethod
    def circle_sq(cls, radius: float) -> float:
        """Метод - Площадь окружности"""
        return math.pi * radius ** 2

    @classmethod
    def surface_area(cls, radius: float) -> float:
        """Метод - Площадь поверхности сферы"""
        return 4 * math.pi * radius ** 2

    @classmethod
    def cube_volume(cls, size: float) -> float:
        """Метод - Объем куба"""
        return size ** 3