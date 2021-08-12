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


def change_list(lst, max_mass):
    lst_count = 0
    new_mass = int(input('Введите вес нового контейнера: '))
    if input_validation(new_mass, max_mass):
        change_list(lst, max_mass)
    else:
        while lst_count < len(lst) and lst[lst_count] >= new_mass:
            lst_count += 1
        lst.insert(lst_count, new_mass)
        print('\nНомер, куда встанет новый контейнер:', lst_count + 1)
        print('Обновленный список контейнеров с массами: ', lst)


max_weight = 200
n_container = int(input('Кол-во контейнеров: '))
new_list = input_mass(n_container, max_weight)
change_list(new_list, max_weight)
