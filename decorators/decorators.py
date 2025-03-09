import time
from typing import Callable, Any, Optional

"""Декоратор,который  считает время на работу функции и выводит данные в терминал"""

def log(filename: Optional[str] = None) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            print(f'Начало работы функции {func.__name__}')
            time_1 = time.time()
            try:
                result = func(*args, **kwargs)
                print(f'конец работы функции {func.__name__}')
                print(f'Время работы функции: {time.time() - time_1}, результат работы: {result}')
                if filename:
                    with open(filename, 'a') as f:
                        f.write(f'{func.__name__} ok\n')
                else:
                    print(f'{func.__name__} ok')
                return result
            except Exception as e:
                error_message = f'{func.__name__} error: {str(e)}. Inputs: {args}, {kwargs}'
                if filename:
                    with open(filename, 'a') as f:
                        f.write(error_message + "\n")
                else:
                    print(error_message)
                raise
        return wrapper
    return decorator


@log(filename="mylog.txt")
def my_function(x:int, y:int)->int:
    return x + y

my_function(1, 2)

