import random


lst = [random.randint(0, 10) for _ in range(10)]
new_lst = []
lst1 = []
print('Оригинальный список: ', lst)
for i in range(len(lst) // 2):
    lst1.clear()
    for j in range(i * 2, i * 2 + 2):
        lst1.append(lst[j])
    new_lst.append(tuple(lst1))
print('1 способ - Новый список: ', new_lst)

print('2 способ - Новый список: ', [(lst[i * 2], lst[i * 2 + 1]) for i in range(len(lst) // 2)])
