from collections.abc import Callable
from functools import wraps


def singleton(cls) -> Callable:
    """Декоратор singleton, который превращает класс в одноэлементный"""

    @wraps(cls)
    def wrapper(*args, **kwargs) -> Callable:
        if not wrapper.instance:
            wrapper.instance = cls(*args, **kwargs)
        return wrapper.instance

    wrapper.instance = None
    return wrapper


@singleton
class Example:
    pass


my_obj = Example()
my_another_obj = Example()

print('Результат:')
print(id(my_obj))
print(id(my_another_obj))
if id(my_obj) == id(my_another_obj):
    print('True')
