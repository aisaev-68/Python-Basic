import random

summa = 0
file_name = input('Введите имя выходного файла: ')
with open(file_name + '.txt', 'w+', encoding='utf-8') as out_file:
    while summa <= 777:
        try:
            numb = int(input('Введите число: '))
        except ValueError:
            print('Ошибка ввода: введите целое число.')
            raise
        summa += numb
        try:
            if random.randint(1, 13) == 6:
                raise Exception
            out_file.write(str(numb) + '\n')
        except Exception:
            print('Случайное исключение.')
            raise
