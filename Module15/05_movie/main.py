films = ['Крепкий орешек', 'Назад в будущее', 'Таксист', 'Леон', 'Богемская рапсодия',
         'Город грехов', 'Мементо', 'Отступники', 'Деревня']
new_list = []

while True:
    name_film = input('Введите название фильма: ')
    for n_film in films:
        if name_film == n_film:
            new_list.append(n_film)
        else:
            print('Ошибка!')
            break

print('Список любимых фильмов: ', new_list)