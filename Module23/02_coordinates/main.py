import random


def f(x, y):
    x += random.randint(0, 10)
    y += random.randint(0, 5)
    try:
        return y / x
    except ZeroDivisionError as error1:
        print('Что-то пошло не так с первой функцией:', str(error1).title())


def f2(x, y):
    x -= random.randint(0, 10)
    y -= random.randint(0, 5)
    try:
        return y / x
    except ZeroDivisionError as error2:
        print("Что-то пошло не так с второй функцией: ", str(error2).title())


with open('result.txt', 'w') as file_2, open('coordinates.txt', 'r') as file:
    for line in file:
        nums_list = line.split()
        try:
            res1 = f(int(nums_list[0].strip()), int(nums_list[1].strip()))
            res2 = f2(int(nums_list[0].strip()), int(nums_list[1].strip()))
            number = random.randint(0, 100)
            my_list = sorted([res1, res2, number])
            file_2.write(f'{str(my_list[0])}  {str(my_list[1])}  {str(my_list[2])}\n')
        except (TypeError, NameError) as error:
            print('Что-то пошло не так :', str(error).title())
