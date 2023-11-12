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
