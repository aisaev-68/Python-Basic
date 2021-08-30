def fibb(n):
    if n > 0:
        if n == 1:
            return 1
        summa = fibb(n - 1) + fibb(n - 2)
    else:
        if n == 0:
            return 0
        elif n == -1:
            return 1
        summa = fibb(n + 2) - fibb(n + 1)
    return summa


numb = int(input('Введите позицию числа в ряде Фибоначчи: '))
print(f'Число: {fibb(numb)}')
