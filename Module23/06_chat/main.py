def file_open_write(f_name, mess):
    with open('chat.txt', 'a', encoding='utf-8') as chat_file:
        chat_file.write(f'{f_name}: {mess}\n')


def file_open_read():
    with open('chat.txt', 'r', encoding='utf-8') as chat_file:
        for i_line in chat_file:
            print(i_line, end='')
    print()


name = input('Введите имя: ')
while True:
    print('\n1 - Посмотреть текущий текст чата.')
    print('2 - Отправить сообщение.')

    question = int(input('Выберите действие: '))
    if question == 1:
        file_open_read()
    elif question == 2:
        message = input('\nВведите сообщение: ')
        file_open_write(name, message)
        print('Собщение отправлено.')
