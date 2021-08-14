def f_song(lst):
    total_time = 0.0
    n_count = 0
    numb_songs = int(input('Сколько песен выбрать? '))
    if numb_songs > 0:
        while n_count < numb_songs:
            logic = True
            print('Название', n_count + 1, 'песни: ', end='')
            song = input()
            for i in range(len(lst)):
                if lst[i].count(song) > 0:
                    total_time += float(lst[i][1])
                    logic = False
            if logic:
                print('\nВ списке отсутствует песня,', song, '. Выберите другую песню.\n')
                n_count -= 1
            n_count += 1
    else:
        print('\nПесны не выбраны! Повторите ввод!\n')
        f_song(lst)
    if total_time > 0:
        print('\nОбщее время звучания песен:', round(total_time, 2), 'минут.')


violator_songs = [['World in My Eyes', 4.86], ['Sweetest Perfection', 4.43],
                  ['Personal Jesus', 4.56], ['Halo', 4.9], ['Waiting for the Night', 6.07],
                  ['Enjoy the Silence', 4.20], ['Policy of Truth', 4.76], ['Blue Dress', 4.29],
                  ['Clean', 5.83]]
f_song(violator_songs)
