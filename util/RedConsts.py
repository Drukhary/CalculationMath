from sympy import *

x = Symbol('x')
sin = sin
tan = tan
STEP = 0.001
INF = 1/STEP

def condition(value):
    if value is nan or value is zoo or abs(value) >= INF:
        return True
    else:
        return False