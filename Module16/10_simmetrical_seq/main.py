def f_split(text):
    word = ''
    for item in text:
        word += item + ' '
    return word


def f_palindrome(txt):
    txt_reverse = txt[::-1]
    if txt == txt_reverse:
        return True
    else:
        return False


lst = lst_dig = ''
numb = int(input('Количество чисел: '))
for i in range(1, numb + 1):
    print('Число', i, end=': ')
    n_dig = int(input())
    lst += str(n_dig)

for i in range(0, numb):
    if f_palindrome(lst[i:numb]):
        lst_dig = lst[:-(numb - i)]
        lst_dig = lst_dig[::-1]
        break


print('Последовательность: ', f_split(lst))
print('Нужно приписать чисел: ', len(lst_dig))
print('Сами числа: ', f_split(lst_dig))
