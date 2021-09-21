import random


class Student:

    def __init__(self, surname_and_name, id_group):
        self.surname_and_name = surname_and_name
        self.id_group = id_group
        self.stud_perf = [0, 0, 0, 0, 0]

    def performance(self, stud):
        stud.stud_perf = [random.randint(1, 5) for _ in range(5)]

    def out_perf(self, stud):
        stud.performance(stud)
        return f'{self.id_group} {self.surname_and_name} {sum(self.stud_perf) / 5}'


def print_info(inf):
    if perf_dict.get(inf[3].strip()):
        perf_dict[inf[3].strip()].update({(inf[1].strip() + ' ' + inf[2].strip()): inf[0].strip()})
    else:
        perf_dict[inf[3].strip()] = {(inf[1].strip() + ' ' + inf[2].strip()): inf[0].strip()}


list_students = ['Иванов Сергей', 'Ельцин Борис', 'Гарбачев Михаил',
                 'Медведев Дмитрий', 'Путин Владимир', 'Лавров Сергей',
                 'Шойгу Сергей', 'Кириенко Сергей', 'Матвиенко Валенитина', 'Володин Незнаюкто']

perf_dict = {}
for ind, i_tem in enumerate(list_students):
    name = Student(i_tem, ind + 1)
    info = name.out_perf(name).split()
    print_info(info)

print('ID      Фамилия и имя    Средний балл')
for key, value in sorted(perf_dict.items()):
    for k, v in value.items():
        print('{0:3}  {1:>20} {2:>5}'.format(v, k, key))
