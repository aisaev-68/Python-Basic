students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}


def f(st_dict):
    lst_int = []
    sum_letter = 0
    for k, v in st_dict.items():
        sum_letter += len(v['surname'])
        if st_dict[k]['interests'] not in lst_int:
            lst_int.extend(st_dict[k]['interests'])
    return lst_int, sum_letter


print('ID студента — возраст')
for key, value in students.items():
    print(f'{key}:', value['age'])
my_lst, len_fam = f(students)
print(f'\nИнтересы студенов: {my_lst}, \nобщая длина всех фамилий: {len_fam}')
