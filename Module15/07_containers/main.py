def input_validation(mass, max_mass):
    if mass > max_mass:
        print('\nВесь не может превышать 200 кг. Повторите ввод.')
        logic = True
    else:
        logic = False
    return logic


def input_mass(numb, max_mass):
    lst_container = []
    numb_count = 0
    prev_weight = max_mass
    while numb_count < numb:
        numb_count += 1
        weight = int(input('Введите вес контейнера: '))
        if input_validation(weight, max_mass):
            numb_count -= 1
        elif weight <= prev_weight:
            lst_container.append(weight)
            prev_weight = weight
        else:
            print('\nВес необходимо вводить в невозрастающей последовательности. Повторите ввод.')
            numb_count -= 1
    print('\nСписок контейнеров с массами: ', lst_container)
    return lst_container


def unique_item(u_lst):
    lst_unique = []
    prev_item = ""
    for i in u_lst:
        n_count = 0
        for j in u_lst:
            if i == j and prev_item != j:
                n_count += 1
                prev_item = i
        if n_count == 1:
            lst_unique.append(i)
    return lst_unique


def change_list(lst, max_mass):
    m = 0
    ind = 0
    new_lst = unique_item(lst)
    new_mass = int(input('Введите вес нового контейнера: '))
    if input_validation(new_mass, max_mass):
        change_list(lst, max_mass)
    else:
        for i in new_lst:
            if lst.count(lst[len(lst) - 1]) == len(lst):
                lst.append(new_mass)
            elif int(i) < new_mass:
                m = lst.count(i)
                if m == 1:
                    ind = lst.index(i) - 1
                else:
                    ind = lst.index(i) - 2
                lst.insert(ind + m, new_mass)
                break
            elif int(i) == new_mass:
                m = lst.count(i)
                if m == 1:
                    ind = lst.index(i)
                else:
                    ind = lst.index(i)
                lst.insert(ind + m, new_mass)
                break
    print('\nНомер, куда встанет новый контейнер:', m + ind + 1)
    print('Обновленный список контейнеров с массами: ', lst)


max_weight = 200
n_container = int(input('Кол-во контейнеров: '))
new_list = input_mass(n_container, max_weight)
change_list(new_list, max_weight)

