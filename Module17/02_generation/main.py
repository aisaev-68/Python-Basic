list_length = int(input('Введите длину списка: '))
if list_length > 0:
    print(list(1 if i % 2 == 0 else i % 5 for i in range(list_length)))
else:
    print(list(1 if i % 2 == 0 else i % 5 for i in range(list_length, - 1)))
