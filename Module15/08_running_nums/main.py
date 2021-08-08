def f_lst(s, lst):
    k = 0
    new_list = []
    for i in lst:
        new_list.append(lst[lst.index(i) - s % len(lst)])
        k += 1
    print('Сдвинутый список: ', new_list)


n_shift = int(input('Сдвиг: '))
lst_input = input("\nВведите список в одну строчку: ")  # например, 1 2 3 4 5
n_list = [int(elem) for elem in lst_input.split()]
print('\nИзначальный список: ', n_list)
f_lst(n_shift, n_list)
