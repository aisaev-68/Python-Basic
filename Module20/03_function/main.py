def out_tuple(my_tup, item):
    lst = []
    lst1 = []
    for i_elem in range(len(my_tup)):
        if my_tup[i_elem] == item:
            lst1.append(i_elem)
    if len(lst1) == 1:
        for i_item in range(lst1[0], len(my_tup)):
            lst.append(my_tup[i_item])
    elif len(lst1) == 2:
        for i_item in range(lst1[0], lst1[1] + 1):
            lst.append(my_tup[i_item])
    new_tuple = tuple(lst)
    return new_tuple


my_tuple = tuple(i for i in input('Введите через пробел элементы кортежа: ').split())
rand_elem = input('Введите случайный элемент: ')
print(out_tuple(my_tuple, rand_elem))
