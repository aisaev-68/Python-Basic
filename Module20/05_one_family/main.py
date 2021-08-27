def add_contact(n):
    count = 0
    while count < n:
        name = input('\nВведите имя: ').title()
        surname = input('Введите фамилию: ').title()
        age = input('Введите возраст: ')
        s_name = surname + ' ' + name
        if data.get(s_name):
            print(f'\n{s_name} есть в базе!\n')
        else:
            data[s_name] = [int(age)]
        count += 1


data = dict()
#data = {'Сидоров Никита': 35, 'Сидорова Алина': 34, 'Сидоров Павел': 10, 'Иванов Павел': 65, 'Иванова Алина': 60}
numb = int(input('Сколько записей ввести в базу?: '))
add_contact(numb)
sur_name = input('\nВведите фамилию для поиска: ').title()
if sur_name[len(sur_name) - 1:] == 'а':
    sur_name = sur_name[:len(sur_name) - 1]
for key, value in data.items():
    if key.split()[0] == sur_name or key.split()[0] == sur_name + 'а':
        print(key, value)
