print('Результат работы программы:')
with open('zen.txt', 'r', encoding='utf-8') as dzen_file:
    dzen_list = dzen_file.readlines()
    for i_line in range(len(dzen_list) - 1, -1, -1):
        if i_line == len(dzen_list) - 1:
            print(dzen_list[i_line], end='\n')
        else:
            print(dzen_list[i_line], end='')
