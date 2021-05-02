from sympy import *
from RedConsts import x, INF


class RedFunction:
    def __init__(self, expr,display):
        self.expr, self.display = expr,display

    expr = x
    display = "x"

    def value(self, argument):
        return self.expr.subs({x: argument}).n()

    def derivative(self, argument, power=1):
        return diff(self.expr, x, power).subs({x: argument}).n()

    def getDisplay(self):
        return self.display


def function_0():
    return x ** 3 - 7 * x ** 2 + 7 * x + 7 \
        , "x^3 - 7x^2 + 7x + 7"


def function_1():
    return 5 / x \
        , "5/x"


def function_2():
    return tan(x) \
        , "5/x"