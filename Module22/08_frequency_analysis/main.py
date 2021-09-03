dict_bargraph = dict()
with open('text.txt', encoding='utf-8') as file:
    print('\nСодержимое файла text.txt: ')
    while True:
        i_line = file.readline()
        print(f'{i_line}')
        if i_line:
            for sym in i_line.lower():
                if sym.isalpha():
                    if dict_bargraph.get(sym):
                        dict_bargraph[sym] += 1
                    else:
                        dict_bargraph[sym] = 1
        else:
            break

count_sym = sum(dict_bargraph.values())
with open('analysis.txt', 'w', encoding='utf-8') as new_file:
    print('Содержимое файла analysis.txt: ')
    for key1, value1 in sorted(dict_bargraph.items(), key=lambda x: (-x[1], x[0])):
        freq = str(round(value1 / count_sym, 3))
        print(key1, freq)
        new_file.write(f'{key1} {freq}\n')
