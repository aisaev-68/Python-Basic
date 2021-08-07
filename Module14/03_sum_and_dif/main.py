def sum_dig(a):
    dig_sum = 0
    while a > 0:
        dig_sum += a % 10
        a //= 10
    return dig_sum


def amount_dig(b):
    dig_amount = 0
    while b > 0:
        b //= 10
        dig_amount += 1
    return dig_amount


numb = int(input('Введите целое положительное число: '))
if numb > 0:
    print('\nСумма цифр:', sum_dig(numb), '\nКол-во цифр в числе:', amount_dig(numb),
          '\nРазность суммы и кол-ва цифр:', sum_dig(numb) - amount_dig(numb))
else:
    print('\nОшибка ввода!')
