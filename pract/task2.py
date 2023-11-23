import re
import doctest


def check_colors_correctness(color):
    """
    Examples:

    >>> check_colors_correctness('rgb(10,7,65)')
    True
    >>> check_colors_correctness('rgb(10%,20%,0%)')
    True
    >>> check_colors_correctness('#21f48D')
    True
    >>> check_colors_correctness('#888')
    True
    >>> check_colors_correctness('hsl(200,100%,50%)')
    True
    >>> check_colors_correctness('hsl(0,0%,0%)')
    True
    >>> check_colors_correctness('hsl(20,10,0.5)')
    False
    >>> check_colors_correctness('hsl(34%, 20%,50%)')
    False
    >>> check_colors_correctness('#2345')
    False
    >>> check_colors_correctness('ffffff')
    False
    >>> check_colors_correctness('rgb(257,50,10)')
    False
    """
    sub_pattern1 = r'(25[0-5]|2[0-4]\d|1\d{2}|[1-9]\d|\d)'
    sub_pattern3 = r'(360|3[0-5]\d|2\d{2}|1\d{2}|[1-9]\d|\d)'
    sub_pattern3_percent = r'(100|[1-9]\d|\d)%'

    pattern1 = r'rgb\({0},{0},{0}\)'.format(sub_pattern1)
    pattern1_percent = r'rgb\({0}%,{0}%,{0}%\)'.format(sub_pattern1)
    pattern2 = r'#([0-9A-Fa-f]{3}){1,2}\b'
    pattern3 = r'hsl\({0},{1},{1}\)'.format(sub_pattern3, sub_pattern3_percent)


    if re.match(pattern1, color) or re.match(pattern1_percent, color) or re.match(pattern2, color) or re.match(pattern3, color):
        return True
    return False


doctest.testmod()