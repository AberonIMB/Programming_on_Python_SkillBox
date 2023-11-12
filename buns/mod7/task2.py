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


@memoize
def fibonacci(n):
    """Функция считает числа Фибоначчи"""
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(10))
print(fibonacci.__name__)
print(fibonacci.__doc__)
