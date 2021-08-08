word = list(input('Введите слово: '))
if word == word[len(word)::-1]:
    print('Слово является палиндромом')
else:
    print('Слово не является палиндромом')
