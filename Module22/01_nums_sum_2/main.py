summ = 0
with open('answer.txt', 'r+', encoding='utf-8') as answ_file:
    with open('number.txt', 'r', encoding='utf-8') as n_file:
        print('Содержимое файла numbers.txt')
        for i_numb in n_file:
            print(f'{i_numb}', end='')
            if ' '.join(i_numb.split()).isdigit():
                summ += int(' '.join(i_numb.split()))
        answ_file.write(str(summ))
    answ_file.seek(0)
    print('\n\nСодержимое файла answer.txt')
    for i_answ in answ_file:
        print(f'{i_answ}\n')
