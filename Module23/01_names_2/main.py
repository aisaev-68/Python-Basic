count = 0
lst = [0]
with open('log1.txt', 'w', encoding='utf-8') as log_file:
    with open('people.txt', 'r', encoding='utf-8') as people_file:
        k = len(people_file.readlines())
        people_file.seek(0)
        while count < k:
            try:
                i_line = people_file.readline().strip()
                count += 1
                if i_line.endswith('\n'):
                    lst[0] += len(i_line) - 1
                else:
                    lst[0] += len(i_line)
                if len(i_line) - 1 < 3:
                    raise Exception
            except Exception:
                log_file.write(f'Ошибка: в строке {count} меньше трех символов!\n')
                print(f'Ошибка: в строке {count} меньше трех символов!')

print('Количество букв во всех строках файла равно', lst[0])
