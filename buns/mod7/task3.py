import time


def validate_args(func):
    def wrapped_func(*args, **kwargs):
        if len(args) != 1:
            return "NotEnoughArguments" if len(args) < 1 else "TooManyArguments"
        elif not isinstance(args[0], int):
            return "WrongTypes"
        elif args[0] < 0:
            return "NegativeArgument"
        else:
            return func(*args, **kwargs)
    return wrapped_func


def memoize(func):
    dictionary = {}

    def wrapped_func(*args, **kwargs):
        key = (args, frozenset(kwargs.items()))
        if key not in dictionary:
            result = func(*args, **kwargs)
            dictionary[key] = result
        return dictionary[key]
    wrapped_func.__name__ = func.__name__
    wrapped_func.__doc__ = func.__doc__
    return wrapped_func


def timer(func):
    def wrapped_func(*args, **kwargs):
        if not hasattr(wrapped_func, 'start'):
            wrapped_func.start = time.time()
        result = func(*args, **kwargs)
        if not hasattr(wrapped_func, 'end'):
            wrapped_func.end = time.time()
            print(f"функция выполнялась {wrapped_func.end - wrapped_func.start} секунд(ы)")
        return result
    return wrapped_func

# можно было обойтись без hasattr,но написать доп.функцию,однако это очень сильно замедляет работу
# @timer
# @memoize
# @validate_args
# def do_fibonacci(n):
#     result = fibonacci(n)
#     return result


@timer
@memoize
@validate_args
def fibonacci(n):
    """Функция считает числа Фибоначчи"""
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
