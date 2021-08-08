def f_word(txt):
    n_unique = 0
    for first_s in txt:
        n_count = 0
        for sec_s in txt:
            if first_s == sec_s:
                n_count += 1
        if n_count == 1:
            n_unique += 1
    return n_unique


word = input('Введите слово: ')
print('Кол-во уникальных букв: ', f_word(word))
