def mystic_years(start, stop):
    m = 0
    logic = True
    for i in range(start, stop + 1, 1):
        for k in range(0, 10, 1):
            n = 0
            for j in str(i):
                if k == int(j):
                    n += 1
            if n == 3:
                m += 1
                if m == 1:
                    print('\nГоды от', start, 'до', stop, 'с тремя одинаковыми цифрами:')
                    logic = False
                print(i)
    if logic:
        print('\nВ диапазоне от', start, 'до', stop, 'годы с тремя одинаковыми цифрами отсутствуют.')


def menu_input():
    a = int(input('Введите первое четырехзначное число: '))
    b = int(input('Введите второе четырехзначное число: '))
    if a < 999 or b <= 999:
        print('\nВведенные числа не являются четырехзначными!\nПовторите ввод!\n')
        menu_input()
    else:
        if a > b:
            start = b
            stop = a
        else:
            start = a
            stop = b
        mystic_years(start, stop)


menu_input()
