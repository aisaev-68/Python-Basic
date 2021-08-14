lst = []
n_count = 0
numb = int(input('Количество чисел: '))
while n_count < numb:
    n_count += 1
    print('Число', n_count, end=': ')
    n = int(input())
    lst.append(n)
print('Последовательность: ', lst)
txt = ''
n = 0
k = len(lst)
if int(lst[k - 1]) == int(lst[k - 2]):
    for i in range(len(lst) - 2, - 1, - 1):
        txt += str(lst[i])
        n += 1
else:
    for i in range(len(lst) - 2, - 1, - 1):
        txt += str(lst[i])
        n += 1


print('Нужно приписать чисел: ', n)
print('Сами числа: ', txt)
