import os


def info_folders(in_path):
    dir_info = [0, 0, 0]
    for i_elem in os.listdir(in_path):
        if os.path.isfile(os.path.abspath(os.path.join(in_path, i_elem))):
            file_path = os.path.abspath(os.path.join(in_path, i_elem))
            dir_info[0] += os.path.getsize(file_path)
            dir_info[1] += 1
        else:
            res = info_folders(os.path.abspath(os.path.join(in_path, i_elem)))
            dir_info[0] += res[0]
            dir_info[1] += res[1]
            dir_info[2] += 1
    return dir_info


def find_folder(cur_path, fold):
    if os.path.exists(cur_path):
        for i_elem in os.listdir(cur_path):
            new_path = os.path.join(cur_path, i_elem)
            if fold == i_elem:
                return new_path
            if os.path.isdir(new_path):
                res = find_folder(new_path, fold)
                if res:
                    break
        else:
            res = None
        return res


# name_path = 'python_basic\Module14'
name_path = input('Введите путь к каталогу: ')
if not os.path.basename(name_path) == '':
    path = find_folder('..', os.path.basename(name_path))
    result = info_folders(path)
    print(f'Размер каталога (в Кб): {result[0] / 1024}\nКоличество файлов: {result[1]}'
          f'\nКоличество подкаталогов:{result[2]}')
else:
    print('Введите каталог для поиска.')
