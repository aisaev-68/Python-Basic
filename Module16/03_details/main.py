def f_shop(lst, detail):
    count = 0
    i_count = 0
    sum_detail = 0
    for _ in lst:
        if lst[i_count][0] == detail:
            count += 1
            sum_detail += lst[i_count][1]
        i_count += 1
    print('Кол-во деталей -', count, '\nОбщая стоимость -', sum_detail)


shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]


name = input('Название детали: ')
f_shop(shop, name)
