def move(n, x, y):
    if n == 1:
        print(f"Переложить диск 1 со стержня {x} на {y}")
    else:
        move(n - 1, x, 6 - x - y)
        print(f"Переложить диск {n} со стержня {x} на {y}")
        move(n - 1, 6 - x - y, y)


numb = int(input('Введите количество дисков: '))
if numb > 0:
    move(numb,1,2)
else:
    print('Ошибка ввода.')

