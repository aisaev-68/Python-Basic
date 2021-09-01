def search_elem(struct, k, m=1000, i=0):
    if k in struct:
        return struct[k]
    for value in struct.values():
        if m > i and isinstance(value, dict):
            result = search_elem(value, k, m, i + 1)
            if result:
                break
    else:
        result = None
    return result


def out_info(res):
    if res:
        print(res)
    else:
        print('Такого ключа в структуре нет.')
site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}


key = input('Введите искомый ключ: ')
search_depth = int(input('Введите глубину поиска (по умалчанию - ноль): '))
if search_depth == 0:
    out_info(search_elem(site, key, 2))
elif search_depth > 0:
    out_info(search_elem(site, key, search_depth))
else:
    print('Ошибка ввода!')
