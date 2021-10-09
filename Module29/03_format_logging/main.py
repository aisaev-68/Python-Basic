import time
from functools import wraps
from collections.abc import Callable


def logged_ex(time_format: str, name_class: str = '') -> Callable:
    """Декаратор методов классов"""
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def decor_func(*args, **kwargs) -> Callable:
            start_time = time.time()
            print("- Запускается '{}'. Дата и время запуска: {} ".format(
                name_class + func.__name__, time.strftime(time_format)))
            result = func(*args, **kwargs)
            print("- Завершение '{}', время работы = {:0.3f} c ".format(
                name_class + func.__name__, time.time() - start_time))
            return result

        decor_func._log_decor = True

        return decor_func

    return decorator


def log_methods(time_format: str) -> Callable:
    """Декаратор классов"""
    def decorator(cls) -> Callable:
        for i_method in dir(cls):
            if i_method.startswith('__') is False:
                cur_method = getattr(cls, i_method)
                decorated_a = logged_ex(time_format, cls.__name__ + ".")
                decorated_a = decorated_a(cur_method)
                setattr(cls, i_method, decorated_a)

        return cls

    return decorator


@log_methods("%b %d %Y - %H:%M:%S")
class A:
    def test_sum_1(self) -> int:
        print('Тут метод test_sum_1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


@log_methods("%b %d %Y - %H:%M:%S")
class B(A):
    def test_sum_1(self) -> None:
        super().test_sum_1()
        print("Тут метод наследника test_sum_1")

    def test_sum_2(self) -> int:
        print("Тут метод test_sum_2")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


my_obj = B()
my_obj.test_sum_1()
my_obj.test_sum_2()
