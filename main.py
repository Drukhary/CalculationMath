from function import RedFunction, function_0,function_1
from Integration import Integration as Intgr
from graphic import DrawGraphic
import numpy as np
import sympy as sp
import RedConsts as rc
LEFT_BORDER = 0
RIGHT_BORDER = 5
EPSILON = 0.01
STEP = 0.1

def process():
    x=rc.x
    # redfunction = RedFunction(x**4/10+x**2/5-7,'x^4/10 + x^2/5 - 7')
    redfunction = RedFunction(5/x, '5/x')
    print(Intgr.RectangleFault(EPSILON,redfunction,LEFT_BORDER,RIGHT_BORDER))
    S,table=Intgr.RectangleMethod(redfunction, LEFT_BORDER, RIGHT_BORDER, EPSILON, 8)
    print(S)
    print(table)
    # x = np.arange(LEFT_BORDER, RIGHT_BORDER + EPSILON, STEP)
    # y = [redfunction.value(i) for i in x]
    # DrawGraphic(LEFT_BORDER, RIGHT_BORDER,
    #             -25, 25,
    #             x, y, redfunction.getDisplay())


if __name__ == '__main__':
    process()
