def txt_reverse(lst1):
    word_list = []
    logic1 = True
    logic2 = False
    for item in lst1:
        words = word2 = word3 = ''
        n = len(item)
        for elem in item[::-1]:
            if logic1 and elem.isalpha() or elem.isdigit():
                words += elem
                n -= 1
            elif logic2 and n >= 0:
                word3 += elem
                n -= 1
                if n == 0:
                    logic1 = True
                    logic2 = False
            else:
                word2 = elem
                n -= 1
                logic1 = False
                logic2 = True
        words = word3 + word2 + words
        word_list.append(words)
    return ' '.join(word_list)


print('\nНовое сообщение:', txt_reverse(input('Сообщение: ').split(' ')))
