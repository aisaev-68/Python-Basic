from collections.abc import Callable
import datetime
import random


def logging(func: Callable) -> Callable:
    """Декоратор,отвечающий за логирование функций"""

    print('{} - название функции, \nдокументация функции: \n{}'.format(func.__name__, func.__doc__))

    def wrapper(numb: int, counter: int = 0) -> None:
        if counter == numb:
            return
        try:
            while counter < numb:
                counter += 1
                func()
        except Exception as error:
            with open('function_errors.log', 'a', encoding='utf-8') as log_file:
                log_file.writelines('{}  {}  {}\n'.format(datetime.datetime.now(), func.__name__, error))
            wrapper(numb, counter)

    return wrapper


@logging
def test() -> float:
    """Деление двух случайных чисел от 0 до 10"""
    x = random.randint(0, 10)
    y = random.randint(0, 4)
    return x / y


test(150)
