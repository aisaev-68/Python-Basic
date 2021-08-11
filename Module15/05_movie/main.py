films = ['Крепкий орешек', 'Назад в будущее', 'Таксист', 'Леон', 'Богемская рапсодия',
         'Город грехов', 'Мементо', 'Отступники', 'Деревня']
new_list = []

while True:
    name_film = input('Введите название фильма: ')
    if films.count(name_film) > 0:
        if new_list.count(name_film) == 0:
            new_list.append(name_film)
        else:
            print('\nФильм присутствует в списке. Введите название другого фильма.')
    else:
        print('\nОшибка!')
        break

print('\nСписок любимых фильмов: ', new_list)
