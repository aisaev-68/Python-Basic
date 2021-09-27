from collections.abc import Iterable


class SquareNumber:
    def __init__(self, numb: int):
        self.numb = numb
        self.counter = 0

    def __iter__(self) -> Iterable:
        return self

    def __next__(self) -> int:
        if self.counter < self.numb:
            self.counter += 1
            return self.counter ** 2
        else:
            raise StopIteration


def gen_iter(numb: int):
    count = 0
    while numb > count:
        count += 1
        yield count ** 2


number = int(input('Введите число: '))
try:
    print('Класс-итератор:')
    my_iter = SquareNumber(numb=number)
    for item in my_iter:
        print(item, end=' ')

    print('\n\nФункция-генератор:')
    my_gen = gen_iter(numb=number)
    for elem in my_gen:
        print(elem, end=' ')

    print('\n\nГенераторное выражение:')
    my_gen_iter = (item ** 2 for item in range(1, number + 1))
    for item in my_gen_iter:
        print(item, end=' ')
except (ValueError, TypeError) as error:
    print('\nОшибка ввода!')
