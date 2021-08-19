lst = [i for i in input('Введите строку, содержащую пробелы: ').split()]
n = max_smb = 0
elem = ''
s = '"'
for item in lst:
    k = len(item)
    if k > n:
        k, n = n, k
        max_smb = k
        elem = item
    else:
        max_smb = n
print(f'Самое длинное слово - {s}{elem}{s} с длиной {max_smb} символов.')
