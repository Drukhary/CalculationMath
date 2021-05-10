import math

import numpy
import numpy as np
from sympy import zoo
from util.RedConsts import condition, x, STEP, INF

import enum


def calculate_function(x, function):
    y = []
    for i in x:
        value = function(i)
        if condition(value):
            raise ValueError(i)
        else:
            y.append(value)
    return y


def create_table(x, y, title, dx='|  x  |', dy='|  y  |'):
    return title + dx \
           + '|'.join(["{0:8.4f}".format(i) for i in x]) + '|\n' + \
           dy \
           + '|'.join(["{0:8.4f}".format(float(i)) for i in y]) + '|' + '\n'


def simpson_method(red_function, x, h, y=None):
    if (y is None):
        y = calculate_function(x, red_function.value)
    result = - y[0] + y[-1]
    for i in range(len(y) - 1):
        result += 4 * y[i] if i % 2 == 1 else 2 * y[i]
    return result * (h / 3), create_table(x, y,
                                          '|     |' + '|'.join(["{0:8}".format(i + 1) for i in range(len(x))]) + '|\n')


def left(x):
    return x[0:-1]


def right(x):
    return x[1:]


def center(x):
    return [(x[i] + x[i + 1]) / 2 for i in range(len(x) - 1)]


class Mode(enum.Enum):
    LEFT = left
    RIGHT = right
    CENTER = center

    def __init__(self, mode):
        self.type = mode


def rectangle_method_factory(mode):
    def rectangle_method(red_function, x, h, y=None):
        if (y is None):
            y = calculate_function(x, red_function.value)
        table = create_table(x, y, '|     |' + '|'.join(["{0:8}".format(i + 1) for i in range(len(x))]) + '|\n')
        x = mode(x)
        y = calculate_function(x, red_function.value)
        result = sum(y) * h
        table += create_table(x, y,
                              '|     |        |' + '|'.join(["{0:8}".format(i + 1) for i in range(len(x))]) + '|\n',
                              '|x_t-1|        |', '|y_t-1|        |')
        return result, table

    return rectangle_method


def trapeze_method(red_function, x, h, y=None):
    if (y is None):
        y = calculate_function(x, red_function.value)
    result = - (y[0] + y[-1]) / 2
    result += sum(y)
    result *= h
    return result, create_table(x, y, '|     |' + '|'.join(["{0:8}".format(i + 1) for i in range(len(x))]) + '|\n')


def fault(derivative_power, power, denominator):
    EPSILON = 0.01

    def fault(r, red_function, a, b):
        the_derivative = red_function.diff(derivative_power)
        try:
            n = (max([abs(the_derivative.subs({x: i}).n()) for i in np.arange(a, b + EPSILON, EPSILON)])
                 * ((b - a) ** power) / denominator / r) ** (1 / derivative_power)
        except:
            n = None
        return n

    return fault


class Method(enum.Enum):
    SIMPSON = (simpson_method, fault(derivative_power=4, power=5, denominator=180), "Simpson method", 4)
    RECTANGLE = (
        rectangle_method_factory(Mode.CENTER), fault(derivative_power=2, power=3, denominator=24), "Rectangle method",
        2)
    RECTANGLE_LEFT = (
        rectangle_method_factory(Mode.LEFT), fault(derivative_power=1, power=2, denominator=2), "Rectangle method", 1)
    RECTANGLE_RIGHT = (
        rectangle_method_factory(Mode.RIGHT), fault(derivative_power=1, power=2, denominator=2), "Rectangle method", 1)
    RECTANGLE_CENTER = (
        rectangle_method_factory(Mode.CENTER), fault(derivative_power=2, power=3, denominator=24), "Rectangle method",
        2)
    TRAPEZE = (trapeze_method, fault(derivative_power=2, power=3, denominator=12), "Trapeze method", 2)

    def __init__(self, type, fault, title, order_of_accuracy, desc=''):
        self.type = type
        self.fault = fault
        self.title = title
        self.order_of_accuracy = order_of_accuracy
        self.desc = desc

    def numeric_method(self, red_function, a, b, epsilon=0.01, n=4):
        h = (b - a) / n
        x = np.arange(a, b + h, h)
        if len(x) == 0:
            return 0, ''
        result = 0
        table = ''
        try:
            result, table = self.type(red_function, x, h)
        except ValueError as exc:
            result_1, table_1 = self.numeric_method(red_function,
                                                    a, exc.args[0] - epsilon, epsilon, n)
            result_2, table_2 = self.numeric_method(red_function,
                                                    exc.args[0] + epsilon, b, epsilon, n)
            result = result_1 + result_2
            table = table_1 + table_2
        finally:
            return result, table

    def approximate_calculation(self, red_function, a, b, eps=0.01, n=4):
        tables = []
        I_0, table = self.numeric_method(red_function, a, b, eps, n)
        table = '\nfor n = {}\nI = {}\n'.format(n, I_0) + table
        tables.append(table)
        n *= 2
        I_1, table = self.numeric_method(red_function, a, b, eps, n)
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
                    '|I_1 - I_0| = {} ({})\n' \
                        .format(n, I_1, RedRound(I_1, eps), RedRound(abs(I_1 - I_0), eps), abs(I_1 - I_0)) + table
            tables.append(table)
        return I_1, '\n'.join(tables), n

    def n_num_method(self, red_function, a, b, epsilon=0.01):
        result = 0
        table = ''
        n = []
        x, y = self.find_intervals(red_function, a, b, epsilon)
        for i in x:
            temp = self.fault(epsilon, red_function, i[0], i[-1])
            if temp<2:temp=2
            n.append(temp)
        for i in range(len(n)):
            if n[i] is not None:
                _x_ = np.arange(x[i][0], x[i][-1]+(x[i][-1] - x[i][0]) / n[i], (x[i][-1] - x[i][0]) / n[i])
                sub_res, sub_table = self.type(red_function, _x_, (_x_[-1] - _x_[0]) / n[i])
                result += sub_res
                table += sub_table
        return n, result, table

    def find_intervals(self, the_function, a, b, STEP):
        args = numpy.arange(a, b + STEP, STEP)
        args = [RedRound(i, STEP * 0.01) for i in args]
        x, x_sub, y, y_sub = [], [], [], []
        for i in range(len(args)):
            value = the_function.value(args[i])
            if condition(value):
                if (len(x_sub) > 0):
                    x.append(x_sub)
                    y.append(y_sub)
                    x_sub, y_sub = [], []
            else:
                y_sub.append(value)
                x_sub.append(args[i])
        x.append(x_sub)
        y.append(y_sub)
        return x, y

    def num_method(self, red_function, a, b, epsilon=0.01, n=4):
        h = (b - a) / n
        result = 0
        table = ''
        x, y = self.find_intervals(red_function, a, b, h)
        for i in range(len(x)):
            sub_res, sub_table = self.type(red_function, x[i], h, y[i])
            result += sub_res
            table += sub_table
        return result, table


def RedRound(value, epsilon):
    return round(value, -int(math.floor(math.log(epsilon, 10))))
