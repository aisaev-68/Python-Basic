def write_correct_data(txt):
    with open('registrations_good.log', 'a', encoding='utf-8') as correct_log:
        correct_log.write(txt + '\n')


def write_error_data(txt):
    with open('registrations_bad.log', 'a', encoding='utf-8') as error_log:
        error_log.write(txt + '\n')


def data_validation(f_line):
    result = 0
    name, email, age = f_line.split()
    try:
        if len(f_line.split()) < 3 or (not age.isdigit() and int(age) < 10 or int(age) > 99):
            raise ValueError
        try:
            if not name.isalpha():
                raise NameError
            try:
                if '@' and '.' not in email:
                    raise SyntaxError
            except SyntaxError:
                result += 1
                print("SyntaxError: адрес почты должен содержать '@' и точку.")
        except NameError:
            result += 1
            print('NameError: в имени должны буквы.')
    except ValueError:
        result += 1
        print('ValueError: в строке должны быть три поля или дата рождения должна быть равным числу от 10 до 99.')
    if result == 0:
        write_correct_data(f_line)
    else:
        write_error_data(f_line)


with open('registrations.txt', 'r', encoding='utf-8') as reg_file:
    for i_line in reg_file:
        if i_line.endswith('\n'):
            i_line = i_line[:len(i_line) - 1]
        data_validation(i_line)
