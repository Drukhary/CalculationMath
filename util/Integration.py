import math

import numpy as np
from sympy import zoo
from util.RedConsts import INF

import enum


def calculate_function(x, function):
    y = []
    for i in x:
        value = function(i)
        if abs(value) >= INF or value is zoo:
            raise ValueError(i)
        else:
            y.append(value)
    return y


def create_table(x, y, title, dx='|  x  |', dy='|  y  |'):
    return title + dx \
           + '|'.join(["{0:8.4f}".format(i) for i in x]) + '|\n' + \
           dy \
           + '|'.join(["{0:8.4f}".format(float(i)) for i in y]) + '|' + '\n'


def simpson_method(red_function, x, h):
    y = calculate_function(x, red_function.value)
    result = - y[0] + y[-1]
    for i in range(len(y) - 1):
        result += 4 * y[i] if i % 2 == 1 else 2 * y[i]
    return result * (h / 3), create_table(x, y,
                                          '|     |' + '|'.join(["{0:8}".format(i + 1) for i in range(len(x))]) + '|\n')


def rectangle_method(red_function, x, h):
    table = ''
    y = calculate_function(x, red_function.value)
    table += create_table(x, y, '|     |' + '|'.join(["{0:8}".format(i + 1) for i in range(len(x))]) + '|\n')
    x = [(x[i] + x[i + 1]) / 2 for i in range(len(x) - 1)]
    y = calculate_function(x, red_function.value)
    result = sum(y) * h
    table += create_table(x, y,
                          '|     |        |' + '|'.join(["{0:8}".format(i + 1) for i in range(len(x))]) + '|\n',
                          '|x_t-1|        |', '|y_t-1|        |')
    return result, table


def trapeze_method(red_function, x, h):
    y = calculate_function(x, red_function.value)
    result = - (y[0] + y[-1]) / 2 + sum(y)
    result *= h
    return result, create_table(x, y, '|     |' + '|'.join(["{0:8}".format(i + 1) for i in range(len(x))]) + '|\n')


def simpson_fault(r, red_function, a, b):
    return (max([abs(red_function.derivative(i, 4)) for i in np.arange(a, b, r)]) * ((b - a) ** 5) / 180 / r) \
           ** (1 / 4)


def trapeze_fault(r, red_function, a, b):
    return (max([abs(red_function.derivative(i, 2)) for i in np.arange(a, b, r)]) * ((b - a) ** 3) / 12 / r) \
           ** (1 / 2)


def rectangle_fault(r, red_function, a, b):
    return (max([abs(red_function.derivative(i, 2)) for i in np.arange(a, b, r)]) * (b - a) ** 3) / 24 / r \
           ** (1 / 2)


class Method(enum.Enum):
    SIMPSON = (simpson_method, simpson_fault, "Simpson method")
    RECTANGLE = (rectangle_method, rectangle_fault, "Rectangle method")
    TRAPEZE = (trapeze_method, trapeze_fault, "Trapeze method")

    def __init__(self, type, fault, title):
        self.type = type
        self.fault = fault
        self.title = title

    def NumericMethod(self, red_function, a, b, epsilon=0.01, n=4):
        h = (b - a) / n
        x = np.arange(a, b + epsilon, h)
        if len(x) == 0:
            return 0, ''
        result = 0
        table = ''
        try:
            result, table = self.type(red_function, x, h)
        except ValueError as exc:
            result_1, table_1 = self.NumericMethod(red_function,
                                                   a, exc.args[0] - epsilon, epsilon, n)
            result_2, table_2 = self.NumericMethod(red_function,
                                                   exc.args[0] + epsilon, b, epsilon, n)
            result = result_1 + result_2
            table = table_1 + table_2
        finally:
            return result, table

    def approximate_calculation(self, red_function, a, b, eps=0.01, n=4):
        tables = []
        I_0, table = self.NumericMethod(red_function, a, b, eps, n)
        table = '\nfor n = {}\nI = {}\n'.format(n, I_0) + table
        tables.append(table)
        n *= 2
        I_1, table = self.NumericMethod(red_function, a, b, eps, n)
        table = 'for n = {}\n' \
                'I = {} ({})\n' \
                '|I_1 - I_0| = {} ({})\n' \
                    .format(n, I_1, RedRound(I_1, eps), RedRound(abs(I_1 - I_0), eps), abs(I_1 - I_0)) + table
        tables.append(table)
        while abs(I_1 - I_0) > eps:
            n *= 2
            I_0, (I_1, table) = I_1, self.NumericMethod(red_function, a, b, eps, n)
            table = 'for n = {}\n' \
                    'I = {} ({})\n' \
                    '|I_1 - I_0| = {} ({})\n'\
                        .format(n, I_1,RedRound(I_1,eps),RedRound(abs(I_1 - I_0),eps), abs(I_1 - I_0)) + table
            tables.append(table)
        return I_1, '\n'.join(tables),n

def RedRound(value, epsilon):
    return round(value, -int(math.floor(math.log(epsilon, 10))))
