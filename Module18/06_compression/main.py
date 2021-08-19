def f_coding(str_txt):
    cod = ''
    elem_count = 0
    item_count = 0
    while elem_count < len(str_txt):
        count = 0
        while str_txt.startswith(str_txt[item_count], elem_count, elem_count + 1):
            elem_count += 1
            count += 1
        cod += str_txt[item_count] + str(count)
        item_count += count
    return cod


print('\nЗакодированная строка: ', f_coding(input('Введите строку: ')))
