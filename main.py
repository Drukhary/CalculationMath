import math
from util.Function import RedFunction
from util.Integration import Method
from util.RedConsts import x

LEFT_BORDER = 1
RIGHT_BORDER = 2
EPSILON = 0.01
STEP = 0.1


def RedRound(value, epsilon):
    return round(value, -int(math.floor(math.log(epsilon, 10))))


def process():
    red_function = RedFunction(x ** 4 / 10 + x ** 2 / 5 - 7, 'x^4/10 + x^2/5 - 7')
    # red_function = RedFunction(5/x, '5/x')
    integra = [Method.RECTANGLE, Method.SIMPSON, Method.TRAPEZE]
    for method in integra:
        n = int(math.floor(method.fault(EPSILON, red_function, LEFT_BORDER, RIGHT_BORDER)))
        if n % 2 != 0:
            n += 1
        print(n)
        S, table = method.NumericMethod(red_function, LEFT_BORDER, RIGHT_BORDER, EPSILON, n)
        print('S = {0} ({1})'.format(RedRound(S, EPSILON), S))
        print(table)
    # x = np.arange(LEFT_BORDER, RIGHT_BORDER + EPSILON, STEP)
    # y = [float(red_function.value(i)) for i in x]
    # print(y)
    # DrawGraphic(LEFT_BORDER, RIGHT_BORDER,
    #             min(y), max(y),
    #             x, y, red_function.getDisplay())


if __name__ == '__main__':
    process()
