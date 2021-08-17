vowels = 'аоэеиыуёюя'
lst = input('Введите текст: ')
print('Список гласных букв:', list(i for i in lst for j in vowels if i == j),
      '\nДлина списка:', len(list(i for i in lst for j in vowels if i == j)))
