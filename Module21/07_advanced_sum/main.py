from typing import Iterable


def sum(*args):
    result = 0
    for arg in args:
        if isinstance(arg, Iterable):
            for elem in arg:
                if isinstance(elem, Iterable):
                    result += sum(elem)
                else:
                    result += elem
        else:
            for item in [arg]:
                result += item
    return result


print('Примеры вызовов функции:')
print('sum([[1, 2, [3]], [1], 3])')
print('Ответ:', sum([[1, 2, [3]], [1], 3]))
print('\nsum(1, 2, 3, 4, 5)')
print('Ответ:',sum(1, 2, 3, 4, 5))