def f_sym(s):
    if len(s) == 1 and s in '%-+=/*' \
            or len(s) == 2 and s == '//':
        return True
    else:
        return False


def calc(f_line):
    txt = ''
    try:
        if f_line.count(' ') == 2:
            first_numb, symb, sec_numb = f_line.split()
        else:
            txt = f'ValueError: Срока {f_line} должна содержать два пробела.'
            raise ValueError
        if len(symb) != 1:
            txt = f'SyntaxError: в сроке {f_line} знак операции должен содержать один символ.'
            raise SyntaxError
        if not int(first_numb) and (not f_sym(symb) or not int(sec_numb)):
            txt = f'ValueError: в строке {f_line} содержаться недопустимые символы.'
            raise ValueError
        result = eval(f_line)
        lst_sum[0] += result
        txt = f'ZeroDivisionError: в строке {f_line} деление на ноль!'
    except (SyntaxError, ValueError, ZeroDivisionError) as error:
        print(txt, str(error).title())
    else:
        print(f'{f_line} = {result}')


lst_sum = [0]
with open('calc.txt', 'r', encoding='utf-8') as calc_file:
    for i_line in calc_file:
        if i_line.endswith('\n'):
            i_line = i_line[:len(i_line) - 1]
        calc(i_line)
    print('Сумма результатов всех чисел: ', lst_sum[0])
