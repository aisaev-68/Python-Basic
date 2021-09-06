import os


def write_correct_data(cor_line):
    with open('registrations_good.log', 'a', encoding='utf-8') as correct_log:
        correct_log.write(cor_line + '\n')


def write_error_data(cor_line):
    with open('registrations_bad.log', 'a', encoding='utf-8') as error_log:
        error_log.write(cor_line + '\n')


def data_validation(f_line):
    txt = ''
    try:
        if f_line.count(' ') == 2:
            name, email, age = f_line.split()
        else:
            txt = 'ValueError: в строке должны быть два пробела.'
            raise ValueError
        if len(f_line.split()) < 3 or (not age.isdigit() and int(age) < 10 or int(age) > 99):
            txt = 'ValueError: в строке должны быть три поля или дата рождения должна ' \
                  'быть равным числу от 10 до 99.'
            raise ValueError
        if not name.isalpha():
            txt = 'NameError: в имени должны буквы.'
            raise NameError
        if '@' and '.' not in email:
            txt = "SyntaxError: адрес почты должен содержать '@' и точку."
            raise SyntaxError
        write_correct_data(f_line)
    except (SyntaxError, ValueError, NameError) as error:
        write_error_data(f_line)
        print(txt, str(error).title())


f1 = open(os.path.join(os.getcwd(), 'registrations_good.log'), 'w', encoding='utf-8')
f2 = open(os.path.join(os.getcwd(), 'registrations_bad.log'), 'w', encoding='utf-8')
f1.close()
f2.close()

with open('registrations.txt', 'r', encoding='utf-8') as reg_file:
    for i_line in reg_file:
        if i_line.endswith('\n'):
            i_line = i_line[:len(i_line) - 1]
        data_validation(i_line)
