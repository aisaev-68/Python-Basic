numb = int(input('Введите количество целых чисел в списке: '))
numb_list = [int(input('Число: ')) for _ in range(numb)]
print('Исходный список: ', numb_list)
for i_item in numb_list:
    if int(i_item) == 0:
        numb_list.append(i_item)
        numb_list.remove(i_item)
print('Список после добавления 0 в конец: ', numb_list)
for _ in numb_list:
    for i_elem in numb_list:
        if int(i_elem) == 0:
            numb_list.remove(i_elem)
            break
print('Список после удаления 0: ', numb_list)
