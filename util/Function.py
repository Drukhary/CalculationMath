from sympy import *
from util.RedConsts import x


class RedFunction:
    def __init__(self, expr,display):
        self.expr, self.display = expr,display

    expr = x
    display = "x"

    def value(self, argument):
        return self.expr.subs({x: argument}).n()

    def derivative(self, argument, power=1):
        return diff(self.expr, x, power).subs({x: argument}).n()

    def diff(self,power):
        return diff(self.expr, x, power)
    def integrate(self,left,right):
        return integrate(self.expr,(x,left,right)).n()
    def singularities(self):
        return singularities(self.expr,x)

    def getDisplay(self):
        return self.display