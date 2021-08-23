def create_dict(numb):
    count = 0
    while count < numb - 1:
        txt = input(f'{count + 1} пара: ').title()
        if f_check_sym(txt):
            des, par = txt.split()
            pedigree[des] = par
            pedigree_height[des] = 0
            pedigree_height[par] = 0
        else:
            print('\nСтрока должна содержать один пробел.\n')
        count += 1


def f_check_sym(txt_str):
    count_sym = 0
    for i_sym in txt_str:
        if ' ' in i_sym:
            count_sym += 1
    if count_sym == 1:
        return True
    else:
        return False


def print_pedigree():
    print("\n“Высота” каждого члена семьи:")
    for key in pedigree:
        new_key = key
        while new_key in pedigree:
            new_key = pedigree[new_key]
            pedigree_height[key] += 1
    for item in sorted(pedigree_height):
        print(item, pedigree_height[item])


pedigree = dict()
pedigree_height = dict()
people_numbs = int(input('Введите количество человек: '))
if people_numbs > 0:
    create_dict(people_numbs)
    print_pedigree()
else:
    print('Ошибка ввода.')
