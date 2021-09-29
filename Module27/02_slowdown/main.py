from collections.abc import Callable
import datetime
import time


def execution_time(func: Callable) -> Callable:
    """Декоратор, который перед выполнением декорируемой функции ждёт несколько секунд"""
    def wrapper(sec) -> None:
        print('Сейчас время {}'.format(datetime.datetime.now()))
        time.sleep(sec)
        func()
        print('[*] Время задержки выполнения: {} секунд.'.format(round(sec, 2)))

    return wrapper


@execution_time
def check_webpage() -> None:
    """ Декорируемая функция"""
    print('Время после выполнения функции - {}'.format(datetime.datetime.now()))


check_webpage(sec=4)
