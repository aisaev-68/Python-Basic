goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}
store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}
goods.update(store)
print('Результат работы программы.')
for key, value in goods.items():
    for key1, value1 in store.items():
        summ1 = summ2 = 0
        if value == key1:
            for item in value1:
                summ1 += item['quantity']
                summ2 += item['price'] * item['quantity']
            print(f'{key} - {summ1} шт, стоимость {summ2} руб')
