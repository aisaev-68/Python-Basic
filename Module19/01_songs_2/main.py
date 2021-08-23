def input_songs(n_songs, viol_songs):
    count = 0
    sym = '"'
    total_time = 0
    new_songs_dict = dict()
    while count < n_songs:
        name_song = input(f'Название {count + 1} песни: ')
        if viol_songs.get(name_song):
            if check_new_dict(name_song, viol_songs, new_songs_dict):
                total_time += float(viol_songs.get(name_song))
                count += 1
            else:
                print(f'\nПесня {sym}{name_song}{sym} присутствует в Вашем списке. Повторите ввод!')
        else:
            print(f'\nПесня {sym}{name_song}{sym} отсутствует в исходном списке. Повторите ввод!')
    print(f'\nОбщее время звучания песен: {round(total_time, 2)} минут.')


def check_new_dict(song, viola_dict, new_dict):
    if new_dict.get(song):
        return False
    else:
        new_dict[song] = viola_dict[song]
        return True


violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}

numb_songs = int(input('Сколько песен выбрать? '))
if numb_songs > 0:
    input_songs(numb_songs, violator_songs)
else:
    print('Песни не выбраны!')
