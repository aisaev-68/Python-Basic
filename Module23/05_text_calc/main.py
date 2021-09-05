def calc(f_line):
    try:
        first_numb, symb, sec_numb = f_line.split()
        if not int(first_numb) and (symb not in '%-+=/*' or not int(sec_numb)):
            raise ValueError
        try:
            result = eval(f_line)
        except ZeroDivisionError:
            print(f'ZeroDivisionError: ({f_line}) делить на ноль нельзя!')
        else:
            print(f'{f_line} = {result}')
    except ValueError:
        print(f'ValueError: в строке {f_line} содержаться недопустимые символы.')


with open('calc.txt', 'r', encoding='utf-8') as calc_file:
    for i_line in calc_file:
        if i_line.endswith('\n'):
            i_line = i_line[:len(i_line) - 1]
        calc(i_line)
