def txt_reverse(lst1):
    word_list = []
    for item in lst1:
        words = ''
        word = ''
        if f_check_sym(item):
            for i_elem in item:
                if i_elem.isalpha() or i_elem.isdigit():
                    word += i_elem
                else:
                    words += word[::-1] + i_elem
                    word = ''
            words += word[::-1]
        else:
            words += item[::-1]
        word_list.append(words)
    return ' '.join(word_list)


def f_check_sym(txt_str):
    count = 0
    sym = ' ~`@#$%^&*()-_=+<>?/,.|:;'
    for i_sym in sym:
        if i_sym in txt_str:
            count += 1
    if count >= 1:
        return True
    else:
        return False


txt = input('Сообщение: ')
if f_check_sym(txt):
    print('\nНовое сообщение:', txt_reverse(txt.split(' ')))
else:
    print('Текст должен содержать слова и знаки препинания')
