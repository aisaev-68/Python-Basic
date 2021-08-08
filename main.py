import math


def f_game(lst, p_count, p_minus):
    start_count = 0
    del_count = 1
    while p_count != 1:
        print('\nТекущий круг людей:', lst, '\nНачало счёта с номера', lst[start_count])
        print('Выбывает человек под номером', lst[del_count])
        if p_minus % len(lst) == 0:
            del_count = len(lst) - 1
            start_count = 0
        else:
            del_count = p_minus % len(lst) - 1
            start_count = del_count + 1
        lst.remove(lst[del_count])
        p_count -= 1

    print('\nОстался человек под номером', lst[0])


def menu_input():
    people_count = int(input('Кол-во человек: '))
    if people_count > 0:
        first_list = list(range(1, people_count + 1))
        people_minus = int(input('Какое число в считалке? '))
        if people_minus > 0:
            f_game(first_list, people_count, people_minus)
            print('Значит, выбывает каждый', people_minus, 'человек')
        else:
            print('\nОшибка ввода. Повторите ввод!\n')
            menu_input()
    else:
        print('\nОшибка ввода. Повторите ввод!\n')
        menu_input()


menu_input()
