n_lst = int(input('Количество элементов массива: '))
if n_lst >= 0:
    print('Список для заказчика: ', list([1+i, 5+i, 9+i] for i in range(n_lst)))
else:
    print('Ошибка ввода!')
