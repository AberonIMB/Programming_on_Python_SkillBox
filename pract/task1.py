import re
import doctest


def check_password(password):
    """
    Examples:

    >>> check_password('rtG3FG!Tr^e')
    True

    >>> check_password('aA1!*!1Aa')
    True

    >>> check_password('oF^a1D@y5e6')
    True

    >>> check_password('enroi#$rkdeR#$092uWedchf34tguv394h')
    True

    >>> check_password('пароль')
    False

    >>> check_password('password')
    False

    >>> check_password('qwerty')
    False

    >>> check_password('lOngPa$$$W0Rd')
    False
    """

    pattern = r'^(?=.*[A-Z]){2,}(?=.*\d)(?!.*(.)\1\1)(?=(.*[%@#^$&*!?]){2,})[a-zA-Z0-9^$%@#&*!?]{6,}$'
    result = re.match(pattern, password)
    if result and len(set(re.findall(r'[%@#^$&*!?]', password))) > 1: #Написал так, потому что не знаю, как эту проверку запихнуть в pattern
        return True
    return False


print(check_password('SS234!@'))
doctest.testmod()