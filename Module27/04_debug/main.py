from collections.abc import Callable


def wrap_func(func: Callable) -> Callable:
    """Декоратор, который при каждом вызове декорируемой функции выводит её имя
    (вместе со всеми передаваемыми аргументами), а затем — какое значение она возвращает"""

    def wrapper(name, age=None):
        if age:
            print('\nВызывается {}({}, {})'.format(func.__name__, name, age))
        else:
            print('\nВызывается {}({})'.format(func.__name__, name))
        print("{} вернула значение '{}'".format(func.__name__, func(name, age)))
    return wrapper


@wrap_func
def greeting(name: int, age: int = None) -> str:
    """Декорируемая функция - возвращает строку"""
    if age:
        return "Ого, {name}! Тебе уже {age} лет, ты быстро растёшь!".format(name=name, age=age)
    else:
        return "Привет, {name}!".format(name=name)


greeting("Том")
greeting("Миша", age=100)
greeting(name="Катя", age=16)
