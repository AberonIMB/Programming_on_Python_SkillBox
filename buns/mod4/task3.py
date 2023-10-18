def f(a, b):
    if min(a, b) == 0:
        return max(a, b)
    else:
        return f(min(a, b), max(a, b) % min(a, b))