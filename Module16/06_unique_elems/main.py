def f_create_list(n, n_count):
    lst = []
    print('Ввод списка', n)
    for i in range(1, n_count + 1):
        print(i, 'число :', end='')
        numb = int(input())
        lst.append(numb)
    print('')
    return lst


def duplicates(f_lst):
    for item in f_lst:
        while f_lst.count(item) > 1:
            f_lst.remove(item)


first_list = f_create_list(1, 3)
sec_list = f_create_list(2, 7)
print('Первый список: ', first_list)
print('Второй список: ', sec_list)
first_list.extend(sec_list)
duplicates(first_list)
print('\nНовый первый список с уникальными элементами:', first_list)
