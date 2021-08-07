import math


def f_circle(x, y, r):
    if math.sqrt(x ** 2 + y ** 2) <= r:
        print('\nМонетка где-то рядом')
    else:
        print('\nМонетки в области нет')


radius = float(input('Введите радиус окружности: '))
coord_x = float(input('Введите координату икс: '))
coord_y = float(input('Введите координату игрек: '))
f_circle(coord_x, coord_y, radius)
