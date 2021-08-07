import math


def revers_numb(n_var):
    dig_conv = ''
    while n_var > 0:
        dig_conv += str(n_var % 10)
        n_var //= 10
    return dig_conv


def f_fraction(a):
    return int(round(a - math.floor(a), 2) * 100)


def whole_part(b):
    return int(math.floor(b))


first_minus = sec_minus = ''
n = float(input('Введите первое число: '))
k = float(input('Введите второе число: '))
n = round(n, 2)
k = round(k, 2)
if n < 0:
    n = - n
    first_minus = '-'
elif k < 0:
    k = - k
    sec_minus = '-'
first_numb = first_minus + revers_numb(whole_part(n)) + '.' + revers_numb(f_fraction(n))
sec_numb = sec_minus + revers_numb(whole_part(k)) + '.' + revers_numb(f_fraction(k))
print('\nПервое число наоборот: ', first_numb)
print('Второе число наоборот: ', sec_numb)
print('Сумма:', round(float(first_numb) + float(sec_numb), 2))
