def f_sort(lst):
    logic = True
    k = 0
    n = len(lst) - 1
    while logic:
        logic = False
        for j in range(n - k):
            if int(lst[j]) > int(lst[j + 1]):
                new_last_item = lst[j]
                lst[j] = lst[j + 1]
                lst[j + 1] = new_last_item
                logic = True
        k += 1
    return lst


lst_input = input("\nВведите список в одну строчку (через пробел): ")  # например, 1 2 3 4 5
n_list = [int(elem) for elem in lst_input.split()]
print('Изначальный список: ', n_list)
print('Отсортированный список:', f_sort(n_list))
