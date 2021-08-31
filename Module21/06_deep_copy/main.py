import copy


def add_dict(name):
    new_site = {f'Сайт для {name}': copy.deepcopy(site)}
    val = change_dict(new_site, name)
    lst.append(val)


def change_dict(struct, name):
    if 'h2' in struct:
        struct['h2'] = f'У нас самая низкая цена на {name}'
        return struct
    if isinstance(struct, dict):
        for key, value in struct.items():
            if key == 'title':
                struct[key] = f'Куплю/продам {name} недорого'
            else:
                change_dict(value, name)
    return struct


def print_struct(obj, i=0):
    i += 1
    if isinstance(obj, dict):
        for key, value in obj.items():
            if i == 1:
                print(f"{key}:")
            elif i == 2:
                print("site = {\n\t", f"'{key}':", "{")
            elif i == 3:
                print(f"\t\t'{key}':", '{')
            else:
                print(f"\t\t\t'{key}':", end='')
            print_struct(value, i)
    else:
        print(' ', f"'{obj}'")


site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на dddd',
            'div': 'Купить',
            'p': 'продать'
        }
    }
}


lst = []
count = 0
numb = int(input('Сколько сайтов: '))
while count < numb:
    name_site = input('Введите название продукта для нового сайта: ')
    add_dict(name_site)
    for item in lst:
        print_struct(item)
    print("\t\t}\n\t}\n}")
    count += 1
