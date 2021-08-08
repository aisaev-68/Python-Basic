def no_even(n):
    no_even_list = []
    for i in range(1, n + 1, 2):
        no_even_list.append(i)
    return no_even_list

numb = int(input('Введите целое число: '))
if numb >= 1:
    print('Список нечетных чисел в диапазоне от 1 до', numb, ':', no_even(numb))
else:
    print('Ошибка ввода! Число должно быть больше или равно единице.')
