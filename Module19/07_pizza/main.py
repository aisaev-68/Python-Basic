def input_order(numb):
    count = 0
    print('Введите заказ через пробел\n(Покупатель, название пиццы, кол-во заказанных пицц).\n')
    while count < numb:
        txt_order = input(f'{count + 1} заказ: ').title()
        if f_check_sym(txt_order):
            surname, name_pizza, number = txt_order.split()
            if not dict_order.get(surname):
                dict_order[surname] = surname
                dict_order[surname] = {name_pizza: int(number)}
            else:
                if dict_order[surname].get(name_pizza):
                    summ = dict_order[surname][name_pizza] + int(number)
                    dict_order[surname][name_pizza] = int(summ)
                else:
                    dict_order[surname][name_pizza] = name_pizza
                    dict_order[surname][name_pizza] = int(number)
        else:
            print('\nВ строке заказа должно быть два пробела\n')
            count -= 1
        count += 1


def f_check_sym(txt_str):
    count = 0
    for i_sym in txt_str:
        if ' ' in i_sym:
            count += 1
    if count == 2:
        return True
    else:
        return False


def print_order():
    print()
    for key, value in sorted(dict_order.items()):
        print(f'{key}:')
        result = sorted(value, key=lambda x: x[0])
        for key1 in sorted(result):
            print(f'  {key1}: {value[key1]}')


dict_order = dict()
numbs_orders = int(input('Введите кол-во заказов: '))
if numbs_orders >= 0:
    input_order(numbs_orders)
    print_order()
else:
    print('Ошибка ввода.')
