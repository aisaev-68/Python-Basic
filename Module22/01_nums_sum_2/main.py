def print_contents(file):
    with open(file, 'r', encoding='utf-8') as d_file:
        print('\nСодержимое файла', file)
        for i_elem in d_file.readlines():
            print(i_elem, end='')
        print()


summ = 0
name_file = input('Введите имя выходного файла: ')
with open(name_file + '.txt', 'w', encoding='utf-8') as answ_file:
    with open('number.txt', 'r', encoding='utf-8') as n_file:
        for i_numb in n_file.readlines():
            if i_numb.endswith('\n'):
                i_numb = i_numb[:len(i_numb)]
            for dig in i_numb.split():
                if dig.isdigit():
                    summ += int(dig)
                else:
                    print(f'{dig} не является числом.')
        answ_file.write(str(summ))
print_contents(n_file.name)
print_contents(answ_file.name)
