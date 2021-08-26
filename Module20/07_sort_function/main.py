def sort_tuple(tup):
    new_list = list(tup)
    logic = True
    while logic:
        logic = False
        for i in range(len(new_list) - 1):
            if str(new_list[i]).isdigit():
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


my_tuple = tuple(i for i in input('Введите через пробел элементы кортежа: ').split())
print('Исходный кортеж: ', my_tuple)
print('Результат выполнения программы: ', sort_tuple(my_tuple))
