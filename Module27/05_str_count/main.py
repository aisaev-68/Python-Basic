from collections.abc import Callable


def counter(func: Callable) -> Callable:
    """ Декоратор, считающий и выводящий количество вызовов декорируемой функции"""
    def wrapper() -> int:
        wrapper.count += 1
        func()
        return wrapper.count

    wrapper.count = 0
    return wrapper


@counter
def test() -> None:
    """ Декорируемая функция"""
    pass


print('Вызываем функцию')
for i in range(15):
    test()

print('\n{} вызовов функции {}'.format(test.count, test.__name__))
