def input_synonym(numb):
    count = 0
    print('Введите слова через дефис.')
    while count < numb:
        txt_syn = input(f'{count + 1} пара: ').lower()
        txt_syn = txt_syn.split(' - ')
        if txt_syn[0].title() in dict_syn.keys():
            print(f'Слово {txt_syn[0].title()} содержится в словаре.\n')
        else:
            dict_syn[txt_syn[0].title()] = txt_syn[1].title()
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
            elif word == value:
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
