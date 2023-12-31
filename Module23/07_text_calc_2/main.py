import os


def f_sym(s):
    if len(s) == 1 and s in '%-+=/*' \
            or len(s) == 2 and s == '//':
        return True
    else:
        return False


def f_summa(var):
    buf_list[0] += eval(var)


def calc(f_line, r_file):
    lst = f_line.split()
    try:
        if f_line.count(' ') != 2:
            txt = 'В строке должно быть два символа.'
            raise ValueError
        if int(lst[0].strip()) and f_sym(lst[1].strip()) and int(lst[2].strip()):
            f_summa(f_line)
        else:
            txt = 'В строке недопустимые символы.'
            raise ValueError
    except (ValueError, ZeroDivisionError) as error:
        question = input(f'Обнаружена ошибка ({txt}) в строке: {f_line} '
                         f'\nХотите исправить (исправить - да, любой символ - нет) ? ').lower()
        if question == 'да':
            new_line = input('Введите исправленную строку: ')
            f_summa(new_line)
            for index, elem in enumerate(r_file):
                if elem == f_line + '\n':
                    new_lst[index] = new_line + '\n'


buf_list = [0]
path = os.path.join(os.getcwd(), 'calc.txt')
if not os.path.exists(path):
    f = open(os.path.join(os.getcwd(), 'calc.txt'), 'w', encoding='utf-8')
    f.close()

with open('calc.txt', 'r', encoding='utf-8') as calc_file:
    new_lst = [i_elem for i_elem in calc_file.readlines()]
    for i_line in new_lst:
        if i_line.endswith('\n'):
            i_line = i_line[:len(i_line) - 1].strip()
        calc(i_line, new_lst)
    with open('calc.txt', 'w', encoding='utf-8') as change_file:
        for i_line in new_lst:
            change_file.write(i_line)

    print(f'\nСумма результатов: {buf_list[0]}')
