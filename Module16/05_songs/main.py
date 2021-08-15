def f_total_time(my_list, lst):
    total_time = 0.0
    for item in my_list:
        k = 0
        for _ in lst:
            if item == lst[k][0]:
                total_time += float(lst[k][1])
            k += 1
    return total_time


def f_search(var, song_lst):
    logic = False
    for i in range(len(song_lst)):
        if var == song_lst[i][0]:
            logic = True
    return logic


def f_song(lst):
    my_lst = []
    n_count = 0
    numb_songs = int(input('Сколько песен выбрать? '))
    if numb_songs > 0:
        while n_count < numb_songs:
            print('Название', n_count + 1, 'песни: ', end='')
            name_song = input()
            if f_search(name_song, lst):
                if my_lst.count(name_song) == 0:
                    my_lst.append(name_song)
                else:
                    print('\nВведенная песня содержится в Вашем списке. Повторите ввод.')
                    n_count -= 1
            else:
                print('\nВ списке отсутствует песня,', name_song, '. Выберите другую песню.\n')
                n_count -= 1
            n_count += 1
    else:
        print('\nПесны не выбраны! Повторите ввод!\n')
        f_song(lst)
    print('\nОбщее время звучания песен:', round(f_total_time(my_lst, lst), 2), 'минут.')


violator_songs = [['World in My Eyes', 4.86], ['Sweetest Perfection', 4.43],
                  ['Personal Jesus', 4.56], ['Halo', 4.9], ['Waiting for the Night', 6.07],
                  ['Enjoy the Silence', 4.20], ['Policy of Truth', 4.76], ['Blue Dress', 4.29],
                  ['Clean', 5.83]]
f_song(violator_songs)
