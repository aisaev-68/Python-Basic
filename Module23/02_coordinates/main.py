import random


def f(x, y):
    x += random.randint(0, 10)
    y += random.randint(0, 5)
    return x / y


def f2(x, y):
    x -= random.randint(0, 10)
    y -= random.randint(0, 5)
    return y / x


with open('result.txt', 'w') as file_2:
    with open('coordinates.txt', 'r') as file:
        for line in file:
            nums_list = line.split()
            try:
                res1 = f(int(nums_list[0]), int(nums_list[1]))
                try:
                    res2 = f2(int(nums_list[0]), int(nums_list[1]))
                    try:
                        number = random.randint(0, 100)
                        my_list = sorted([res1, res2, number])
                        file_2.write(str(' '.join(my_list)))
                    except Exception:
                        print("Что-то пошло не так : ")
                except:
                    print("Что-то пошло не так с второй функцией")
            except Exception:
                print("Что-то пошло не так с первой функцией")
