volleyball_players = ['Артемий', 'Борис', 'Влад', 'Гоша', 'Дима', 'Евгений', 'Женя', 'Захар']
print('Список игроков с четными индексами :', end='')
for i in range(0, 8, 2):
    print(volleyball_players[i], end=', ')
