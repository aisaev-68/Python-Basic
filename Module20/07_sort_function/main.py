def sort_tuple(tup):
    new_list = list(tup)
    logic = True
    while logic:
        logic = False
        for i in range(len(new_list) - 1):
            if isinstance(new_list[i], int):
                if new_list[i] > new_list[i + 1]:
                    new_list[i], new_list[i + 1] = new_list[i + 1], new_list[i]
                    logic = True
            else:
                new_list.clear()
                break
    if new_list:
        return tuple(new_list)
    else:
        return tup


print('Сортировка кортежа, состоящего из целых чисел.')
my_tuple = tuple([float(i) if '.' in i else int(i) for i in input('Введите через пробел целые числа: ').split()])
print('Исходный кортеж: ', my_tuple)
print('Результат выполнения программы: ', sort_tuple(my_tuple))
