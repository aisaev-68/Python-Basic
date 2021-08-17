count = 0
numb_sticks = int(input('Кол-во палок: '))
row_sticks = ['I'] * numb_sticks
if numb_sticks > 0:
    brace_numbers = int(input('Кол-во бросков: '))
    while count < brace_numbers:
        print('Бросок', count + 1, '. Сбиты палки с ', end='')
        left_ind = int(input('номера '))
        right_ind = int(input('по номер '))
        if 1 <= left_ind <= right_ind <= numb_sticks:
            for j in range(left_ind - 1, right_ind):
                row_sticks[j] = '.'
        else:
            print('\nОшибка ввода. Повторите ввод.\n')
            count -= 1
        count += 1
print('\nРезультат: ', ''.join(row_sticks))
