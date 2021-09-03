import os


def numb_sym(sym):
    count = 0
    for elem in sym:
        if elem.isalpha():
            count += 1
    return count


def numb_word(txt):
    count = 0
    for elem in txt.split():
        if elem.isalpha():
            count += 1
    return count


def min_elem(text):
    for sym in letters:
        count = 0
        for elem in text:
            if elem.isalpha() and sym == elem:
                count += 1
        if count > 0:
            sym_dict[sym] = count
    for key, value in sym_dict.items():
        if value == min(sym_dict.values()):
            print(f'Буква, которая встречается в тексте наименьшее количество раз ({value} раза): {key}')


sym_dict = dict()
letters = 'abcdefghijklmnopqrstuvwxyz'
n_sym = 0
n_word = 0
path = os.path.abspath(os.path.join('..', '..', 'Module22', '02_zen_of_python', 'zen.txt'))
print(path)
with open(path, 'r') as dzen_file:
    dzen_list = dzen_file.readlines()
    for i_line in range(len(dzen_list)):
        n_sym += numb_sym(dzen_list[i_line])
        n_word += numb_word(dzen_list[i_line])
    print(f'\nКоличество букв: {n_sym}, количество слов: {n_word}, количество строк: {len(dzen_list)}')
    dzen_file.seek(0)
    min_elem(dzen_file.read().lower())
    dzen_file.close()
