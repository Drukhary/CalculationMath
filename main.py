import math
import sympy as sp
from util.Function import RedFunction
from util.Integration import Method
from util.RedConsts import x
from util.Interface import process


LEFT_BORDER = 1
RIGHT_BORDER = 2
EPSILON = 0.001
STEP = 0.1


# def process():
#     red_function = RedFunction(x ** 4 / 10 + x ** 2 / 5 - 7, 'x^4/10 + x^2/5 - 7')
#     # red_function = RedFunction(x**2, 'x^2')
#     integra = [Method.RECTANGLE
#         , Method.SIMPSON, Method.TRAPEZE
#                ]
#     for method in integra:
#         n = int(math.ceil(abs(method.fault(EPSILON, red_function, LEFT_BORDER, RIGHT_BORDER))))
#         if n % 2 != 0:
#             n += 1
#         I, table = method.NumericMethod(red_function, LEFT_BORDER, RIGHT_BORDER, EPSILON, 4)
#         truth_I = red_function.integrate(LEFT_BORDER, RIGHT_BORDER)
#         print('{}\nn = {}\nS = {} ({})\n|R| = |I-Iтр| = {:8.4f} ({})\n{}'.format(
#             method.title, 4,
#             RedRound(I, EPSILON),
#             I,
#             abs(truth_I - I),
#             abs(truth_I - I),
#             table
#         ))
#     method = Method.RECTANGLE
#     n_begin = 4
#     I, table, n_end = method.approximate_calculation(red_function, LEFT_BORDER, RIGHT_BORDER, EPSILON, n_begin)
#     truth_I = red_function.integrate(LEFT_BORDER, RIGHT_BORDER)
#     print('{}\nbegin n = {}\nend n = {}\nresult S = {} ({})\nepsilon = \n|R| = |I-Iтр| = {:8.4f} ({})\n{}'.format(
#         method.title,
#         n_begin, n_end,
#         RedRound(I, EPSILON),EPSILON,
#         I,
#         abs(truth_I - I),
#         abs(truth_I - I),
#         table
#     ))
#     # x = np.arange(LEFT_BORDER, RIGHT_BORDER + EPSILON, STEP)
#     # y = [float(red_function.value(i)) for i in x]
#     # print(y)
#     # DrawGraphic(LEFT_BORDER, RIGHT_BORDER,
#     #             min(y), max(y),
#     #             x, y, red_function.getDisplay())


if __name__ == '__main__':
    process()
