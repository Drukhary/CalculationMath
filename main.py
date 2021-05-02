from function import RedFunction, function_0,function_1
from Integration import Integration as Intgr
from graphic import DrawGraphic
import numpy as np
import sympy as sp
import RedConsts as rc
LEFT_BORDER = -3
RIGHT_BORDER = 5
EPSILON = 0.01
STEP = 0.1

def process():
    x=rc.x
    redfunction = RedFunction(x**4/10+x**2/5-7,'x^4/10 + x^2/5 - 7')
    # redfunction = RedFunction(x**2, '5/x')
    print(Intgr.RectangleFault(EPSILON,redfunction,LEFT_BORDER,RIGHT_BORDER))
    S,table=Intgr.RectangleMethod(redfunction, LEFT_BORDER, RIGHT_BORDER, EPSILON, 50)
    print(S)
    print(table)
    print(Intgr.TrapezeFault(EPSILON,redfunction,LEFT_BORDER,RIGHT_BORDER))
    S,table=Intgr.TrapezeMethod(redfunction, LEFT_BORDER, RIGHT_BORDER, EPSILON, 50)
    print(S)
    print(table)
    print(Intgr.SimpsonFault(EPSILON,redfunction,LEFT_BORDER,RIGHT_BORDER))
    S,table=Intgr.SimpsonMethod(redfunction, LEFT_BORDER, RIGHT_BORDER, EPSILON, 16)
    print(S)
    print(table)
    x = np.arange(LEFT_BORDER, RIGHT_BORDER + EPSILON, STEP)
    y = [float(redfunction.value(i)) for i in x]
    print(y)
    DrawGraphic(LEFT_BORDER, RIGHT_BORDER,
                min(y), max(y),
                x, y, redfunction.getDisplay())


if __name__ == '__main__':
    process()
