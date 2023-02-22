from math import gcd


def make_rat(x, y):
    g = gcd(x, y)
    return [x // g, y // g]


def numer(x):
    return x[0]


def denom(x):
    return x[1]


def rat_equal(x, y):
    return numer(x) * denom(y) == numer(y) * denom(x)


def add_rat(x, y):
    xn, xd = x
    yn, yd = y
    return make_rat(xn * yd + yn * xd, xd * yd)


def mul_rat(x, y):
    return make_rat(numer(x) * numer(y), denom(x) * denom(y))


def print_rat(x):
    print(numer(x), '/', denom(x))



a = make_rat(6, 11)
b = make_rat(5, 3)