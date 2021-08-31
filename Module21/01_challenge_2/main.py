def recurs(n):
    if n == 1:
        return '1'
    else:
        return '{0} {1}'.format(recurs(n - 1), str(n))


numb = int(input('Введите число: '))
if numb > 0:
    print('Результат: ', recurs(numb))
else:
    print('Введите положительное число!')
