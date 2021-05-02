import numpy as np
import RedConsts as rc


class Integration:
    @staticmethod
    def __CreateTable__(x, y, dx='|  x  |', dy='|  y  |'):
        return dx \
               + '|'.join(["{0:8.4f}".format(i) for i in x]) + '|\n' + \
               dy \
               + '|'.join(["{0:8.4f}".format(float(i)) for i in y]) + '|' + '\n'

    @staticmethod
    def RectangleMethod(redfunction, a, b, epsilon=0.01, n=10):
        h = (b - a) / n
        x = np.arange(a, b + epsilon, h)
        y = []
        result = 0
        table = ''
        try:
            for i in x:
                value = redfunction.value(i)
                if abs(value) >= rc.INF or value is rc.zoo:
                    raise ValueError(i)
                else:
                    y.append(value)
            table += Integration.__CreateTable__(x, y)
            x = [(x[i] + x[i + 1]) / 2 for i in range(len(x)-1)]
            y = []
            for i in x:
                value = redfunction.value(i)
                if abs(value) >= rc.INF or value is rc.zoo:
                    raise ValueError(i)
                else:
                    y.append(value)
            result += sum(y)
            result *= h
            table += Integration.__CreateTable__(x, y,'|x_t-1|'+' '*8+'|','|y_t-1|'+' '*8+'|')
        except ValueError as exc:
            result_1, table_1 = Integration.RectangleMethod(redfunction, a, exc.args[0] - epsilon, epsilon, n)
            result_2, table_2 = Integration.RectangleMethod(redfunction, exc.args[0] + epsilon, b, epsilon, n)
            result = result_1 + result_2
            table = table_1 + table_2
        finally:
            return result, table

    @staticmethod
    def SimpsonMethod(redfunction, a, b, epsilon=0.01, n=4):
        if n % 2 == 1:
            n = n - 1
        h = (b - a) / n
        x = np.arange(a, b + epsilon, h)
        y = []
        result = 0
        table = ''
        try:
            for i in x:
                value = redfunction.value(i)
                if abs(value) >= rc.INF or value is rc.zoo:
                    raise ValueError(i)
                else:
                    y.append(value)
            result = - y[0] + y[-1]
            for i in range(0, n - 1):
                result += 4 * y[i] if i % 2 == 1 else 2 * y[i]
            result = result * (h / 3)
            table = Integration.__CreateTable__(x, y)
        except ValueError as exc:
            result_1, table_1 = Integration.SimpsonMethod(redfunction, a, exc.args[0] - epsilon, epsilon, n)
            result_2, table_2 = Integration.SimpsonMethod(redfunction, exc.args[0] + epsilon, b, epsilon, n)
            result = result_1 + result_2
            table = table_1 + table_2
        finally:
            return result, table

    @staticmethod
    def TrapezeMethod(redfunction, a, b, epsilon=0.01, n=10):
        h = (b - a) / n
        x = np.arange(a, b + epsilon, h)
        y = []
        result = 0
        table = ''
        try:
            for i in x:
                value = redfunction.value(i)
                if abs(value) >= rc.INF or value is rc.zoo:
                    raise ValueError(i)
                else:
                    y.append(value)
            result -= (y[0] + y[-1]) / 2
            result += sum(y)
            result *= h
            table = Integration.__CreateTable__(x, y)
        except ValueError as exc:
            result_1, table_1 = Integration.TrapezeMethod(redfunction, a, exc.args[0] - epsilon, epsilon, n)
            result_2, table_2 = Integration.TrapezeMethod(redfunction, exc.args[0] + epsilon, b, epsilon, n)
            result = result_1 + result_2
            table = table_1 + table_2
        finally:
            return result, table

    @staticmethod
    def SimpsonFault(R, redfunction, a, b):
        n = (abs(redfunction.derivative(max([a, b]), 4)) * ((b - a) ** 5) / 180 / R) \
            ** (1 / 4)
        return n

    @staticmethod
    def TrapezeFault(R, redfunction, a, b):
        n = (abs(redfunction.derivative(max([a, b]), 2)) * ((b - a) ** 3) / 12 / R) \
            ** (1 / 2)
        return n

    @staticmethod
    def RectangleFault(R, redfunction, a, b):
        n = (abs(redfunction.derivative(max([a, b]), 2)) * ((b - a) ** 3) / 24 / R) \
            ** (1 / 2)
        return n
