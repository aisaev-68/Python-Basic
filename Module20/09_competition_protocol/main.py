def f_sort(item):
    return item[1][0] * 1000 - item[1][1]


def input_game_results(numb):
    print('Введите результат - имя участника (через пробел)')
    for count in range(numb):
        record = input('{count + 1} запись:').title()
        ball, name = record.split()
        ball = int(ball)
        if name in dict_scores:
            if ball > dict_scores[name][0]:
                dict_scores[name][0] = ball
                dict_scores[name][1] = count + 1
        else:
            dict_scores[name] = [ball, count + 1]


dict_scores = {}
numb_row = int(input('Сколько записей вносится в протокол? '))
input_game_results(numb_row)
scores = list(dict_scores.items())
scores.sort(key=f_sort, reverse=True)
print('\nИтоги соревнований: ')
for index in 0, 1, 2:
    print(f'{index + 1} место. {scores[index][0]} ({scores[index][1][0]})')
