def f_diff(n):
    k = 0
    for i in range(2, n + 1, 1):
        if n % i == 0:
            k = i
            break
    return k


numb = int(input('Введите число: '))
if numb > 1:
    print('\nНаименьший делитель, отличный от единицы:', f_diff(numb))
else:
    print('\nОшибка! Вы ввели число меньшую или равную единице.')
