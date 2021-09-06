import random

summa = 0
file_name = input('Введите имя выходного файла: ')
with open(file_name + '.txt', 'w+', encoding='utf-8') as out_file:
    while summa <= 777:
        try:
            numb = int(input('Введите число: '))
            if numb < 0:
                txt = 'Ошибка ввода: введите целое положительное число.'
                raise ValueError
            summa += numb
            if random.randint(1, 13) == 5:
                txt = 'Случайное исключение.'
                raise Exception
            out_file.write(str(numb) + '\n')
        except (Exception, TypeError, ValueError) as error:
            print(txt, str(error).title())
