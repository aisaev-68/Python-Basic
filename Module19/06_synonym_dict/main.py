def input_synonym(numb):
    count = 0
    print('Введите слова через дефис.')
    while count < numb:
        txt_syn = input(f'{count + 1} пара: ').title()
        word, syn = txt_syn.split(' - ')
        if word in dict_syn.keys():
            dict_syn[word].append(syn)
        else:
            dict_syn[word] = [syn]
        count += 1
    print(dict_syn)


def search_syn():
    logic = False
    while True:
        word = input('\nВведите слово: ').title()
        for key, value in dict_syn.items():
            if word == key:
                logic = True
                word = value
            elif word in value:
                logic = True
                word = key
        if logic:
            print(f'Синоним: {word}')
            break
        else:
            print('Такого слова в словаре нет.')


dict_syn = dict()
numb_syn = int(input('Введите количество пар слов: '))
input_synonym(numb_syn)
search_syn()
