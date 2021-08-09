films = ['Крепкий орешек', 'Назад в будущее', 'Таксист', 'Леон', 'Богемская рапсодия',
         'Город грехов', 'Мементо', 'Отступники', 'Деревня']
new_list = []

while True:
    name_film = input('Введите название фильма: ')
    if films.count(name_film) > 0:
        new_list.append(name_film)
    else:
        print('Ошибка!')
        break

print('Список любимых фильмов: ', new_list)
