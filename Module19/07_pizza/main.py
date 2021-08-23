def input_order(numb):
    count = 0
    print('Введите заказ через пробел\n(Покупатель, название пиццы, кол-во заказанных пицц).\n')
    while count < numb:
        txt_order = input(f'{count + 1} заказ: ').title()
        if f_check_sym(txt_order):
            txt_order = txt_order.split()
            if not dict_order.get(txt_order[0]):
                dict_order[txt_order[0]] = txt_order[0]
                dict_order[txt_order[0]] = [{txt_order[1]: int(txt_order[2])}]
            else:
                for key, value in dict_order.items():
                    if key == txt_order[0]:
                        for i_dict in value:
                            if i_dict.get(txt_order[1]):
                                summ = i_dict[txt_order[1]] + int(txt_order[2])
                                i_dict.update({txt_order[1]: summ})
                                break
                            else:
                                value.append({txt_order[1]: int(txt_order[2])})
                                break
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
    for key, value in dict_order.items():
        print(f'{key}:')
        for i_item in value:
            for key1, value1 in i_item.items():
                print(f'  {key1}: {value1}')


dict_order = dict()
numbs_orders = int(input('Введите кол-во заказов: '))
if numbs_orders >= 0:
    input_order(numbs_orders)
    print_order()
else:
    print('Ошибка ввода.')
