def input_cont(numb, con_dict):
    count_citi = 0
    print('\nВедите информацию через пробел: страна, город1, город2...')
    while count_citi < numb:
        info = input(f'{count_citi + 1} страна: ').split()
        input_info(info, con_dict)
        count_citi += 1
    return con_dict


def input_info(info, info_dict):
    if info_dict.get(info[0]):
        for i_info in info[1:]:
            if i_info not in info_dict.get(info[0]):
                info_dict[info[0].title()].append(i_info.title())
            else:
                print(f'Город {i_info} сущуствует в базе.\n')
    else:
        info_dict[info[0].title()] = []
        for i_info in info[1:]:
            info_dict[info[0].title()].append(i_info.title())


def search_info(numb, info_dict):
    count = 0
    print(f'\nВведите {numb} города для получения информации.')
    while count < numb:
        n_count = 0
        citi = input(f'{count + 1} город: ').title()
        for key in info_dict:
            if citi in info_dict[key]:
                n_count = 1
                print(f'Город {citi} расположен в стране {key}.\n')
                break
        if n_count == 0:
            print(f'По городу {citi} данных нет.\n')
            break
        count += 1


contRi = dict()
numb_contRi = int(input('Кол-во стран: '))
if numb_contRi > 0:
    input_cont(numb_contRi, contRi)
    search_info(3, contRi)
else:
    print('Не задано количество стран.')
