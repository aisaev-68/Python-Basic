import os
from collections.abc import Iterable

def gen_files_path() -> Iterable:

    for root, dirs, files in os.walk('/aisaev'):
        for i_file in files:
            count = 0
            if i_file.endswith('.py'):
                with open(i_file, 'r', encoding='utf-8') as new_file:
                    for i_line in new_file.readlines():
                        if len(i_line.strip()) > 0 and not i_line.strip().startswith('#'):
                            count += 1
                    yield f'{i_file}: {count}'

def gen_files_path_1() -> Iterable:
    count = 0
    for root, dirs, files in os.walk('/aisaev'):
        for i_file in files:
            if i_file.endswith('.py'):
                with open(i_file, 'r', encoding='utf-8') as new_file:
                    for i_line in new_file.readlines():
                        if len(i_line.strip()) > 0 and not i_line.strip().startswith('#'):
                            count += 1
    yield count


summ = 0
my_gen = gen_files_path()
print('Первый вариант:\n-------------------\nФайл    Кол-во строк')
print('-------------------')
for item in my_gen:
    file, numb = item.split()
    summ += int(numb)
    print(item)
print('Общее количество строк в файлах составляет: {}'.format(summ))

my_list = list()
my_gen1 = gen_files_path_1()
print('\nВторой вариант:')
for item in my_gen1:
    print('Общее количество строк в файлах составляет: {}'.format(item))

