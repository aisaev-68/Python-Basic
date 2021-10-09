from collections.abc import Callable
from functools import wraps


def check_permission(user: str) -> Callable:
    """Декоратор, который проверяет, есть ли у пользователя доступ к вызываемой функции"""

    def permission_decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                if user in user_permissions:
                    return func(*args, **kwargs)
                else:
                    raise PermissionError

            except PermissionError as error:
                print(
                    f"{error.__class__.__name__}: У пользователя '{user}' "
                    f"недостаточно прав, чтобы выполнить функцию {func.__name__}")

        return wrapper

    return permission_decorator


user_permissions = ['admin']


@check_permission('admin')
def delete_site() -> None:
    print('Удаляем сайт')


@check_permission('user_1')
def add_comment() -> None:
    print('Добавляем комментарий')


delete_site()
add_comment()
