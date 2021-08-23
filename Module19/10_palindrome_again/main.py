def f_palindrome(txt_str):
    for sym in txt_str:
        if sym in pol.keys():
            pol[sym] += 1
        else:
            pol[sym] = 1
    print(pol)
    letter = ''
    for item in pol:
        if letter and pol[item] % 2 == 1:
            return False
        elif pol[item] % 2 == 1:
            letter = item
    return True


pol = dict()
txt = input('Введите строку: ').lower()
if txt.isalpha():
    if f_palindrome(txt):
        print('\nМожно сделать палиндромом')
    else:
        print('\nНельзя сделать палиндромом')
else:
    print('Ошибка ввода.')
