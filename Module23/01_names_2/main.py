count = 0
lst = [0]
with open('log1.txt', 'w', encoding='utf-8') as log_file:
    with open('people.txt', 'r', encoding='utf-8') as people_file:
        k = len(people_file.readlines())
        people_file.seek(0)
        while count < k:
            i_line = people_file.readline().strip()
            if i_line.endswith('\n'):
                lst[0] += len(i_line) - 1
            else:
                lst[0] += len(i_line)
            try:
                if i_line.isalpha():
                    if len(i_line) - 1 < 3:
                        txt = f'Ошибка: в строке {count + 1} меньше трех символов!'
                        raise Exception
                else:
                    txt = f'Ошибка: в строке {count + 1} содержаться не только буквы!'
                    raise ValueError
            except (ValueError, Exception) as error:
                log_file.write(txt + '\n')
                print(txt)
            count += 1
print('Количество символов во всех строках файла равно', lst[0])
