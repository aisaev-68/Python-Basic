import random


def guess_number(numb):
    s = set([i for i in range(1, numb + 1)])
    rand_numb = random.randint(1, numb)
    while True:
        str_numbs = input('Нужное число есть среди вот этих чисел: ')
        if ''.join(str_numbs.split()).isdigit():
            numbers = set([int(i) for i in str_numbs.split()])
            if numbers <= s:
                if rand_numb in numbers:
                    if len(numbers) == 1:
                        print(f'Ответ Артёма: Вы угадали число {rand_numb}.')
                        break
                    else:
                        print('Ответ Артёма: Да.\n')
                        s = numbers
                else:
                    print('Ответ Артёма: Нет.\n')
                    numbers = s.difference(numbers)
                    s = numbers
            else:
                print(f'\nВведите числа меньшие или равные {numb}.')
        else:
            if str_numbs == 'Помогите!':
                print(f'Артём мог загадать следующие числа: {sorted(s)}')
                break
            else:
                print('\nОшибка ввода. Повторите ввод.\n')


max_numb = int(input('Введите максимальное число: '))
if max_numb > 0:
    guess_number(max_numb)
else:
    print('Введите число большее нуля.')
