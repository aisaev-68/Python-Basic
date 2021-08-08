n_cells = int(input('Кол-во клеток: '))
bad_cells = []
for i in range(n_cells):
    print('Эффективность', i + 1, 'клетки: ', end='')
    efficiency = int(input())
    if i >= efficiency:
        bad_cells.append(efficiency)

print('Неподходящие значения: ', end='')
for j in bad_cells:
    print(j, end=' ')
