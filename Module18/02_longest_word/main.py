txt = input('Введите строку, содержащую пробелы: ')
if ' ' in txt:
    lst = [i for i in txt.split()]
    n = max_smb = 0
    elem = ''
    s = '"'
    for item in lst:
        k = len(item)
        if k > n:
            max_smb = k
            k, n = n, k
            elem = item
        else:
            n = max_smb
    print(f'Самое длинное слово - {s}{elem}{s} с длиной {max_smb} символов.')
else:
    print('Сказано же с пробелом! Повторите ввод.')
