def f_guests(logic, lst, txt_com, count_guests):
    n_count = len(lst)
    print('Сейчас на вечеринке', n_count, 'человек:', lst)
    if logic:
        print('\nКоманды:', txt_com)
        logic = False
    question = input('Гость пришёл или ушёл? ')
    if txt_com[0] == question:
        print('\nВечеринка закончилась, все легли спать.')
    elif txt_com[1] == question:
        name = input('Имя гостя: ')
        if n_count < count_guests:
            print('Привет,', name, '!\n')
            lst.append(name)
#            n_count += 1
            f_guests(logic, lst, txt_com, count_guests)
        else:
            print('Прости,', name, ', но мест нет.\n')
            f_guests(logic, lst, txt_com, count_guests)
    elif txt_com[2] == question:
        name = input('Имя гостя: ')
        print('Пока,', name, '!\n')
        lst.remove(name)
        f_guests(logic, lst, txt_com, count_guests)
    else:
        print('\nТакого ответа не существует. Повторите ввод.\n')
        f_guests(logic, lst, txt_com, count_guests)


guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']
txt_commands = ['Пора спать', 'пришел', 'ушел']
n_guests = len(guests)
f_guests(True, guests, txt_commands, 6)
