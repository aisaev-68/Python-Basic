import os


def save_file(txt):
    dir_name = input('\nКуда хотите сохранить документ? '
                     '\nВведите последовательность папок (через пробел): ')
    if dir_name:
        dir_path = os.path.join(os.sep, os.path.join(os.sep.join(dir_name.split())))
        if os.path.exists(dir_path):
            os.chdir(dir_path)
            while True:
                name_file = input('\nВведите имя файла: ')
                if name_file:
                    name_file = name_file + '.txt'
                    if os.path.exists(os.path.join(dir_path, name_file)):
                        write_request = input('Вы действительно хотите перезаписать файл? (да или нет): ').lower()
                        if write_request == 'да':
                            file = open(name_file, 'w', encoding='utf-8')
                            file.write(txt)
                            print('Файл успешно перезаписан!')
                            break
                        elif write_request == 'нет':
                            print('Файл не перезаписан.')
                            break
                        else:
                            print('Ошибка ввода. Повторите ввод.')
                    else:
                        file = open(name_file, 'w', encoding='utf-8')
                        file.write(txt)
                        file.close()
                        print('Файл успешно сохранён!')
                        break
                else:
                    print('Вы не ввели название файла. Повторите ввод.')
            print('\nСодержимое файла: ')
            file = open(name_file, 'r', encoding='utf-8')
            print(file.readline())
            file.close()
    else:
        print('Вы ввели пустую строку! Повторите ввод.')
        save_file(txt)


input_txt = input('Введите строку: ')
if input_txt:
    save_file(input_txt)
else:
    print('Вы ввели пустую строку! Повторите ввод.')
