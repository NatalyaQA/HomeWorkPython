def sum_it(x, y):
    return x + y


def prod(x, y):
    return x * y


def diff(x, y):
    return x - y


def devision(x, y):
    try:
        return round(x/y, 2)
    except ZeroDivisionError:
        print("На ноль делить нельзя")


def squaring(x):
    return x**2


def cubing(x):
    return x**3