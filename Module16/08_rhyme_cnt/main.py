def f_game(lst, p_minus, p_count):
    new_list = list(lst)
    start = p_minus - 1
    index = start % len(lst)
    while len(lst) > 1:
        print('\nТекущий круг людей:', lst, '\nНачало счёта с номера', new_list[0])
        new_list.clear()
        print('Выбывает человек под номером', lst[index])
        if index == len(lst) - 1:
            new_list = lst[::index]
        else:
            new_list = lst[index + 1::]
        lst.remove(lst[index])
        index = (index + start) % len(lst)
    if p_count > 1:
        print('\nОстался человек под номером', lst[0])
    else:
        print('\nОстался человек под номером', 0)


def menu_input():
    people_count = int(input('Кол-во человек: '))
    if people_count > 0:
        first_list = list(range(1, people_count + 1))
        people_minus = int(input('Какое число в считалке? '))
        if people_minus > 0:
            print('Значит, выбывает каждый', people_minus, 'человек')
            f_game(first_list, people_minus, people_count)
        else:
            print('\nОшибка ввода. Повторите ввод!\n')
            menu_input()
    else:
        print('\nОшибка ввода. Повторите ввод!\n')
        menu_input()


menu_input()
