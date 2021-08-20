lst = [i.lower() for i in input('Введите строку: ').split()]
count = 0
for item in lst:
    lst1 = [j for j in item]
    if lst1[0].isalpha():
        lst1[0] = item[0].upper()
        lst[count] = ''.join(lst1)
    count += 1
print('\nРезультат: ', ' '.join([''.join(i) for i in lst]))
