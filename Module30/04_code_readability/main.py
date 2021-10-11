from typing import List


if __name__ == '__main__':
    print('Необходимо вывести на экран список простых чисел от 0 до 1000. \nРеализуйте это двумя способами: ')
    print('1. «однострочным» кодом, без объявления дополнительных функций;')
    print('1 способ: ', list(map(int, filter(lambda x: all(map(lambda y: x % y != 0, range(2, x))), range(2, 1001)))))
    print('2 способ: ', [i for i in range(2, 1001) if 0 not in [i % j for j in range(2, i)]])

    print('2. обычным, «своим» кодом, который покажется вам наиболее красивым')
    print([i for i in range(2, 1001) if 0 not in [i % j for j in range(2, i)]])

    print('Мне удобен 2 способ')