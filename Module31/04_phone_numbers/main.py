import re

if __name__ == '__main__':
    print('Результат:')
    for ind, item in enumerate(['9999999999', '999999-999', '99999x9999']):
        print(f'{ind + 1} номер: все в порядке' if re.match(r'\d{10}',
                                                            item) is not None else f'{ind + 1} номер: не подходит')
