def add(a, b):
    a = int(a)
    b = int(b)
    return a+b


def sub(a, b):
    a = int(a)
    b = int(b)
    return a-b


def product(a, b):
    a = int(a)
    b = int(b)
    return a*b


def divide(a, b):
    a = int(a)
    b = int(b)
    if (b != 0):
        return a/b
    else:
        return "Can't divide by ZERO"
