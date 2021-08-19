def check_file(txt):
    smb = '@№$%^&*()'
    file_extension1 = '.txt'
    file_extension2 = '.docx'
    if txt.endswith(file_extension1) or txt.endswith(file_extension2):
        if not txt[0] in smb:
            print('\nФайл назван верно.')
        else:
            print('\nОшибка: название начинается на один из специальных символов')
    else:
        print(f'\nОшибка: неверное расширение файла. Ожидалось {file_extension1} или {file_extension2}')


name_file = input('Название файла: ')
check_file(name_file)
