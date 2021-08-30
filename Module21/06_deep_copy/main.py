import copy


def change_elem(struct, val1, val2):
    if isinstance(struct, dict):
        for key, value in struct.items():
            if key == 'title':
                value = val1
            elif key == 'h2':
                value = val2
            else:
                change_elem(value, val1, val2)
            struct.update({key: value})


def print_struct(obj):

    if isinstance(obj, dict):
        for key, value in obj.items():
            print(key)
            print_struct(value)
    else:
        print(obj)


def input_arg(numb):
    count = 0
    while count < numb:
        name_site = input('Введите название продукта для нового сайта: ')
        change_elem(new_site, f'Куплю/продам {name_site} недорого', f'У нас самая низкая цена на {name_site}')
        print(f'Сайт для {name_site}:','\nSite = {', end='')
        print_struct(new_site)
        count += 1



site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на iPhone',
            'div': 'Купить',
            'p': 'продать'
        }
    }
}

new_site = copy.deepcopy(site)

num = int(input('Сколько сайтов: '))
input_arg(num)
