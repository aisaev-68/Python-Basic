import math


class Circle:

    def __init__(self, x=0, y=0, radius=1):
        self.x = x
        self.y = y
        self.radius = radius
        print(f'Создан окружность с цетром в точке {(self.x, self.y)} и радисом {self.radius}')

    def square(self, circle):
        return math.pi * circle.radius ** 2

    def size_square(self, circle, s):
        return math.sqrt(s) * math.pi * circle.radius ** 2

    def size_perimeter(self, circle, s):
        return 2 * math.pi * circle.radius * s

    def perimeter(self, circle):
        return 2 * math.pi * circle.radius

    def crossing(self, circle1):
        if abs(self.radius - circle1.radius) < math.sqrt((circle1.x - self.x) ** 2 + (circle1.y - self.y) ** 2) \
                < self.radius + circle1.radius:
            print('Окружности пересекаются')
        else:
            print('Окружности не пересекаются')

    def print_info(self, circle):
        print(f'Площадь окружности равна {self.square(circle)}, периметр равна {self.perimeter(circle)}')


print('Демонстрация методов класса Circle')
cirl_info1 = input('Введите через пробел координаты (X, Y), радиус R '
                   '\nи коэфициент K увелечиния первой окружности: ').split()
try:
    cir = Circle(int(cirl_info1[0].strip()), int(cirl_info1[1].strip()), int(cirl_info1[2].strip()))
    cir.print_info(cir)
    print(
        f'Периметр {cir.size_perimeter(cir, int(cirl_info1[3]))} и площадь {cir.size_square(cir, int(cirl_info1[3]))} '
        f'окружности после ее увеличения в {int(cirl_info1[3])} раз')
    print('\nТеперь определим пересекаются окружности или нет.')
    cirl_info2 = input('Введите через координаты (X, Y) и радиус R второй окружности: ').split()
    cir1 = Circle(int(cirl_info2[0].strip()), int(cirl_info2[1].strip()), int(cirl_info2[2].strip()))
    cir.crossing(cir1)
except IndexError:
    print('Ошибка: введите полные запрашиваемые данные через пробел.')
