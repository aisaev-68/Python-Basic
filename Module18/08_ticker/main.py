def lists_compare(lst1, lst2):
    shift = 0
    while shift <= len(lst1):
        new_list = lst2[shift:] + lst2[:shift]
        if new_list == lst1:
            print(f'\nПервая строка получается из второй со сдвигом {shift}.')
            break
        elif shift == len(lst1):
            print('\nПервую строку нельзя получить из второй с помощью циклического сдвига.')
            break
        shift += 1


def input_lists():
    count = 0
    n_list2 = ''
    n_list1 = input("Введите 1 - й список в одну строчку: ")
    while count != len(n_list1):
        n_list2 = input("Введите 2 - й список в одну строчку: ")
        count = len(n_list2)
        if count < len(n_list1):
            print(f'\nКоличество элементов во второй таблице должно быть равно {len(n_list1)}. \nПовторите ввод.')
    lists_compare(n_list1, n_list2)


input_lists()
