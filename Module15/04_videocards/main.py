def f_max_model(lst):
    prev_model = 0
    max_model = 0
    for n_mod in lst:
        if int(j) > prev_model:
            max_model = int(n_mod)
            prev_model = max_model
        else:
            prev_model = int(n_mod)
    return max_model


n_cards = int(input('Кол-во видеокарт: '))
old_list = []
new_list = []
for _ in range(n_cards):
    model = int(input('Видеокарта: '))
    old_list.append(model)
for j in old_list:
    if j != f_max_model(old_list):
        new_list.append(j)

print('\nСтарый список видеокарт: ', old_list)
print('Новый список видеокарт: ', new_list)


