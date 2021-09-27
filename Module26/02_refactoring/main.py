from collections.abc import Iterable


def gen_numb(number: int) -> Iterable:
    numb_1 = numb_2 = 0
    try:
        for i_item in list_1:
            for i_elem in list_2:
                if i_item * i_elem == number:
                    numb_1, numb_2 = i_item, i_elem
                    raise StopIteration
    except StopIteration:
        yield f'Found!!!\n{numb_1} * {numb_2} = {numb_1 * numb_2}'


list_1 = [2, 5, 7, 10]
list_2 = [3, 8, 4, 9]
to_find = 56

my_gen = gen_numb(number=to_find)
print('Результат поиска(с помощью функции - генератора):')
for item in my_gen:
    print(item)

print('\nРезультат поиска(с помощью генератора выражений):')
[print(f'Found!!!\n{elem} * {item} = {elem * item}') for elem in list_1 for item in list_2 if elem * item == to_find]
