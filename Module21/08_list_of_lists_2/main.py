from typing import Iterable


def list_of_list(lst):
    [list_of_list(item) if isinstance(item, Iterable) else new_list.append(item) for item in lst]
    return new_list


nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]
new_list = []
print('Ответ:', list_of_list(nice_list))
