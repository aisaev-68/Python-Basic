def add_contact():
    name = input('\nВведите имя: ').title()
    surname = input('Введите фамилию: ').title()
    phone = input('Введите номер телефона: ')
    sur_name = surname + ' ' + name
    if phonebook.get(sur_name):
        print(f'\n{sur_name} есть в справочнике!\n')
    else:
        phonebook[sur_name] = [phone]
        print('\nТекущий словарь контактов: ', phonebook, '\n')


def search_contact():
    count = 0
    surname = input('\nВведите фамилию: ').title()
    print()
    for key, value in phonebook.items():
        sur_name, name = key.split()
        if sur_name == surname:
            for ph in value:
                print(key, ph)
                count = 1
    print()
    if count == 0:
        print(f'{surname} отсутствует в справочнике.\n')


def main_menu():
    while True:
        print('Действия:\n1 - Добавить контакт\n2 - Поиск человека по фамилии')
        question = int(input('Введите действие: '))
        if question == 1:
            add_contact()
        elif question == 2:
            search_contact()
        else:
            print('\nОшибка ввода. Поворите ввод.\n')


phonebook = dict()
main_menu()
