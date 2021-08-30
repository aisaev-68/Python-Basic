def search_elem(struct, k, m=1000, i=1):
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
val = search_elem(site, key, 2)
if val:
    print(val)
else:
    print('Такого ключа в структуре нет.')
