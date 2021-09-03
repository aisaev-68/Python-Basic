import zipfile

dict_bargraph = dict()
with zipfile.ZipFile('voina-i-mir.zip') as zip_file:
    zip_file.extractall('.')
    name_txt = zip_file.filename
txt_voina_i_mir = zip_file.namelist()[0]

with open(txt_voina_i_mir, encoding='utf-8') as file:
    while True:
        i_line = file.readline()
        if i_line:
            for sym in i_line:
                if sym.isalpha():
                    if dict_bargraph.get(sym):
                        dict_bargraph[sym] += 1
                    else:
                        dict_bargraph[sym] = 1
        else:
            break

with open('out.txt', 'w', encoding='utf-8') as new_file:
    print('Статистика по буквам в возрастающем порядке:')
    for key1, value1 in sorted(dict_bargraph.items()):
        print(key1, ' : ', value1)
        new_file.write(f'{key1} : {value1}\n')
print('Данные сохранены в файл out.txt.')
