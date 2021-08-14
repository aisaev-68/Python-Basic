def input_debt():
    count_deb = 0
    lst = list()
    fr = int(input('Кол-во друзей: '))
    n_deb = int(input('Долговых расписок: '))
    if fr >= 2:
        lst = create_empty_list(fr)
        while n_deb != count_deb:
            count_deb += 1
            print('\n', count_deb, 'расписка')
            to_whom = int(input('Кому: '))
            from_whom = int(input('От кого: '))
            how_much = int(input('Сколько: '))
            if to_whom != from_whom and 0 < to_whom <= fr and 0 < from_whom <= fr:
                for i_item in range(len(lst)):
                    if int(lst[i_item][0]) == to_whom and int(lst[i_item][1]) == from_whom:
                        lst[i_item][2] = int(lst[i_item][2]) - how_much
                for i_item in range(len(lst)):
                    if int(lst[i_item][0]) == from_whom and lst[i_item][1] == to_whom:
                        lst[i_item][2] = int(lst[i_item][2]) + how_much
                        break
            elif to_whom > fr or from_whom > fr:
                print('\nОшибка ввода! Друзей всего -', fr, '. Повторите ввод.\n')
                count_deb -= 1
            elif to_whom == from_whom:
                print('\nОшибка ввода! Сам себе никто кредиты не выдает. Повторите ввод.\n')
                count_deb -= 1
            else:
                print('\nОшибка ввода!\n')
                count_deb -= 1
    else:
        print('\nОшибка ввода! Введите двух или более друзей.\n')
    f_sum_credit(lst, fr)


def create_empty_list(fr_n):
    count = 0
    lst1 = list([j, 0, 0] for j in range(1, fr_n + 1) for _ in range(fr_n - 1))
    for i in range(1, fr_n + 1):
        for j in range(1, fr_n + 1):
            if i != j:
                for k in range(count, len(lst1)):
                    if lst1[k][0] == i:
                        lst1[k][1] = j
                        count += 1
                        break
    return lst1


def f_sum_credit(lst_s, fr):
    for i_fr in range(1, fr + 1):
        sum_deb = 0
        for i_elem in range(len(lst_s)):
            if lst_s[i_elem][0] == i_fr:
                sum_deb += int(lst_s[i_elem][2])
        print('\nБаланс друзей:')
        print(i_fr, ':', sum_deb)


input_debt()
