from collections.abc import Callable


def decorator_with_args_for_any_decorator(dec: Callable) -> Callable:
    """Декоратор с аргументами"""

    def decorator(*args, **kwargs):
        def wrapper(func):
            return dec(func, *args, **kwargs)

        return wrapper

    return decorator


@decorator_with_args_for_any_decorator
def decorated_decorator(func: Callable, *args, **kwargs) -> Callable:
    def wrapper(function_arg1, function_arg2):
        print('Переданные арги и кварги в декоратор: {}, {}'.format(args, kwargs))
        return func(function_arg1, function_arg2)

    return wrapper


@decorated_decorator(100, 'рублей', 200, 'друзей')
def decorated_function(text: str, num: int) -> None:
    print("Привет", text, num)


print('Результат:')
decorated_function("Юзер", 101)
