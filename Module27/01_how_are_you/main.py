from typing import Callable


def how_are_you(func: Callable) -> Callable:
    """ Надоедливый декоратор"""
    def wrapper(*args, **kwargs):
        input('\nКак дела? ')
        print('А у меня не очень! Ладно, держи свою функцию.')
        res = func(*args, **kwargs)
        return res
    return wrapper


@how_are_you
def print_name(name: str, age: int) -> None:
    """ Декорируемая функция"""
    print("Меня зовут {} и мне {} лет. У меня все хорошо и спасибо за функцию.".format(name, age))


@how_are_you
def test() -> None:
    """ Декорируемая функция"""
    print('<Тут что-то происходит...>')


@how_are_you
def ret_args() -> None:
    """ Декорируемая функция"""
    print(how_are_you)


test()
print_name(name='Иван', age=35)
ret_args()
