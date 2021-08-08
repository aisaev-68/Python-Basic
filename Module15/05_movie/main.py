films = ['Крепкий орешек', 'Назад в будущее', 'Таксист', 'Леон', 'Богемская рапсодия',
         'Город грехов', 'Мементо', 'Отступники', 'Деревня']
new_list = []

while True:
    name_film = input('Введите название фильма: ')
    if films.count(name_film):
        new_list.append(name_film)
    else:
        print('\nОшибка!\n')
        break

print('Список любимых фильмов: ', new_list)