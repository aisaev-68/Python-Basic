def my_zip(*args):
    return ([elem[i] for elem in args] for i in range(len(min(args, key=len))))


letter = input('Введите строку: ')
tup = input('Введите через пробел элементы кортежа: ')
my_tup = tuple([a for a in tup.split()])
print(my_tup)
print('Результат:')
print(my_zip(letter, my_tup))
for item in my_zip(letter, my_tup):
    print(item)
