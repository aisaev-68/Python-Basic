data = {
    "address": "0x544444444444",
    "ETH": {
        "balance": 444,
        "totalIn": 444,
        "totalOut": 4
    },
    "count_txs": 2,
    "tokens": [
        {
            "fst_token_info": {
                "address": "0x44444",
                "name": "fdf",
                "decimals": 0,
                "symbol": "dsfdsf",
                "total_supply": "3228562189",
                "owner": "0x44444",
                "last_updated": 1519022607901,
                "issuances_count": 0,
                "holders_count": 137528,
                "price": False
            },
            "balance": 5000,
            "totalIn": 0,
            "total_out": 0
        },
        {
            "sec_token_info": {
                "address": "0x44444",
                "name": "ggg",
                "decimals": "2",
                "symbol": "fff",
                "total_supply": "250000000000",
                "owner": "0x44444",
                "last_updated": 1520452201,
                "issuances_count": 0,
                "holders_count": 20707,
                "price": False
            },
            "balance": 500,
            "totalIn": 0,
            "total_out": 0
        }
    ]
}
item_dict = dict()
print('Исходные данные:\n')
for key, value in data.items():
    if key == 'tokens':
        lst = value
        print(f'Ключ: {key}')
        for item in lst:
            item_dict = item
            for key1, value1 in item_dict.items():
                if key1 == 'fst_token_info' or key1 == 'sec_token_info':
                    print(f'           Ключ: {key1}')
                    for k, v in value1.items():
                        print(f'                              Ключ: {k}, значение: {v}')
                else:
                    print(f'           Ключ: {key1}, значение: {value1}')
    else:
        if key == 'ETH':
            print(f'Ключ: {key}')
            for i, j in value.items():
                print(f'           Ключ: {i}, значение: {j}')
        else:
            print(f'Ключ: {key}, значение: {value}')


#2. В “ETH” добавить ключ “total_diff” со значением 100.
data['ETH']['total_diff'] = 100


# 3. Внутри “fst_token_info” значение ключа “name” поменять с “fdf” на “doge”.
for item in data['tokens']:
    for key in item:
        if key == 'fst_token_info':
            new_dict = item[key]
            new_dict['name'] = 'doge'


#4. Удалить “total_out” из tokens и присвоить его значение в “total_out” внутри “ETH”.
for key, value in data.items():
    if key == 'tokens':
        lst = value
        for item in lst:
            item_dict = item
            item_dict.pop('total_out')
for key, value in data['ETH'].items():
    data['ETH']['totalOut'] = 0


# 5. Внутри "sec_token_info" изменить название ключа “price” на “total_price”.
for key, value in data.items():
    if key == 'tokens':
        lst = value
        for item in lst:
            item_dict = item
            for k, v in item_dict.items():
                if k == 'sec_token_info':
                    v['total_price'] = v.pop('price')


print('\nДанные после изменений:\n')
for key, value in data.items():
    if key == 'tokens':
        lst = value
        print(f'Ключ: {key}')
        for item in lst:
            item_dict = item
            for key1, value1 in item_dict.items():
                if key1 == 'fst_token_info' or key1 == 'sec_token_info':
                    print(f'           Ключ: {key1}')
                    for k, v in value1.items():
                        print(f'                              Ключ: {k}, значение: {v}')
                else:
                    print(f'           Ключ: {key1}, значение: {value1}')
    else:
        if key == 'ETH':
            print(f'Ключ: {key}')
            for i, j in value.items():
                print(f'           Ключ: {i}, значение: {j}')
        else:
            print(f'Ключ: {key}, значение: {value}')
