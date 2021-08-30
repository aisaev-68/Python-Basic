def my_zip(*args):
    return list(tuple([elem[i] for elem in args]) for i in range(len(min(args, key=len))))


letter = input('Введите через пробел элементы первого итерируемого объекта:')
my_letter= [a for a in letter.split()]
tup = input('Введите через пробел элементы второго итерируемого объекта: ')
my_tup = [a for a in tup.split()]

print('Результат:')
print(my_zip(my_letter, my_tup))
for item in my_zip(my_letter, my_tup):
    print(item)
