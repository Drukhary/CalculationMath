import numpy

from util.Function import RedFunction
from util.RedConsts import x, condition
from util.Integration import Method, RedRound
from util.graphic import draw_graphic

Functions = [
    RedFunction(x ** 4 / 10 + x ** 2 / 5 - 7, 'x^4/10 + x^2/5 - 7'),
    RedFunction(3 * x ** 3 - 4 * x ** 2 + 7 * x - 17, '3x^3 - 4x^2 + 7x - 17'),
    RedFunction(1 / x, '1 / x'),
    RedFunction((2 ** 2 - x ** 2) / (x ** 2 - 2 ** 2), '(4 - x^2) / (x^2 - 4)'),
    RedFunction(x ** 2 - 2 * x + 1, 'x^2 - 2x - 1')
]

def process():
    step = 0.001
    left = 1
    right = 2
    epsilon = 0.01
    red_function = Functions[1]
    red_method = Method.SIMPSON

    while True:
        print('Enter a command')
        user_str = input()
        if user_str == 'exit' or '':
            break
        elif user_str == 'set left' or user_str == 'sl':  # set left border
            print('Enter the left border')
            user_str = input()
            if user_str == 'exit' or user_str == '':
                break
            while True:
                try:
                    left = float(user_str)
                    break
                except:
                    print('Enter the correct digit')
                    user_str = input()
        elif user_str == 'set right' or user_str == 'sr':  # set right border
            print('Enter the right border')
            user_str = input()
            if user_str == 'exit' or user_str == '':
                break
            while True:
                try:
                    right = float(user_str)
                    break
                except:
                    print('Enter the correct digit')
                    user_str = input()
        elif user_str == 'set eps' or user_str == 'set epsilon' or user_str == 'se':  # set epsilon
            print('Enter the epsilon')
            user_str = input()
            if user_str == 'exit' or user_str == '':
                break
            while True:
                try:
                    epsilon = float(user_str)
                    break
                except:
                    print('Enter the correct digit')
                    user_str = input()
        elif user_str == 'set function' or user_str == 'sf':  # choose function
            for i in range(len(Functions)):
                print('Enter {} for {}'.format(i + 1, Functions[i].getDisplay()))
            while True:
                user_str = input()
                if user_str == 'exit' or '':
                    break
                try:
                    number = int(user_str)
                    red_function = Functions[number - 1]
                    break
                except:
                    print('Enter a number of functions again')
        elif user_str == 'set method' or user_str == 'sm':  # choose function
            while True:
                print('Choose the method:\n'
                      'Enter "rect" for {}\n'
                      'Enter "trap" for {}\n'
                      'Enter "simp" or "simpson" for {}\n'
                      .format(Method.RECTANGLE.title, Method.TRAPEZE.title, Method.SIMPSON.title))
                user_str = input()
                if user_str == 'rect':
                    while True:
                        print('Enter rectangle method mode:\n"left","right" or "center"')
                        user_str = input()
                        if user_str == 'left':
                            red_method = Method.RECTANGLE_LEFT
                            break
                        elif user_str == 'right':
                            red_method = Method.RECTANGLE_RIGHT
                            break
                        elif user_str == 'center':
                            red_method = Method.RECTANGLE_CENTER
                            break
                        else:
                            print('Invalid input')
                    break
                elif user_str == 'trap':
                    red_method = Method.TRAPEZE
                    break
                elif user_str == 'simp' or user_str == 'simpson':
                    red_method = Method.SIMPSON
                    break
                elif user_str == 'exit' or user_str == '':
                    break
        elif user_str == 'now' or user_str == 'n':
            print('The function: {}\n'
                  'The method: {} ({})\n'
                  'left border(a) = {}\n'
                  'right border(b) = {}\n'
                  'epsilon = {}\n'
                  .format(red_function.getDisplay(), red_method.title,red_method.desc, left, right, epsilon))
        elif user_str == 'ncalc' or user_str == 'calc':
            if user_str == 'ncalc':
                while True:
                    print("Enter n")
                    try:
                        n = int(input())
                        if n < 2:
                            raise Exception
                        break
                    except:
                        print("Invalid input")
                I, table = red_method.num_method(red_function, left, right, epsilon, n)
                truth_I = red_function.integrate(left, right)
                print('{} ({})\n'
                      'n = {}\n'
                      'I = {} ({})\n'
                      '|R| = |I-Iтр| = {} ({})\n'
                      '\n{}'.format(
                    red_method.title, red_method.desc,
                    n,
                    RedRound(I, epsilon),
                    I,
                    RedRound(abs(truth_I - I), epsilon / 100),
                    abs(truth_I - I),
                    table
                ))
            else:
                n, I, table = red_method.n_num_method(red_function, left, right, epsilon)
                truth_I = red_function.integrate(left, right)
                print('{} ({})\n'
                      'n = {}\n'
                      'I = {} ({})\n'
                      '|R| = |I-Iтр| = {} ({})\n'
                      '\n{}'.format(
                    red_method.title, red_method.desc,
                    n,
                    RedRound(I, epsilon),
                    I,
                    RedRound(abs(truth_I - I), epsilon/100),
                    abs(truth_I - I),
                    table
                ))
            # print('n = {}'.format(red_method.fault(epsilon, red_function, left, right)))
            # try:
            #     n = n = int(math.ceil(red_method.fault(epsilon, red_function, left, right)))
            #     if n == 0: n = 2
            # except:
            #     print("Impossible")
            #     continue
        elif user_str == 'appr' or user_str == 'approximate calculation':
            n_begin = 4
            I, table, n_end = red_method.approximate_calculation(red_function, left, right, epsilon, n_begin)
            truth_I = red_function.integrate(left, right)
            print(
                '{} ({})\n'
                'begin n = {}\n'
                'end n = {}\n'
                'result I = {} ({})\n'
                'epsilon = {}\n'
                '|R| = |I-Iтр| = {}  ({})\n'
                '{}'.format(
                    red_method.title, red_method.desc,
                    n_begin, n_end,
                    RedRound(I, epsilon),
                    I,
                    epsilon,
                    RedRound(abs(truth_I - I), epsilon/100),
                    abs(truth_I - I),
                    table
                ))

        elif user_str == 'draw':
            args = numpy.arange(left, right + step, step)
            args = [RedRound(i, step * 0.01) for i in args]
            x, x_sub, y, y_sub = [], [], [], []
            for i in range(len(args)):
                value = red_function.value(args[i])
                if condition(value):
                    x.append(x_sub)
                    y.append(y_sub)
                    x_sub, y_sub = [], []
                else:
                    y_sub.append(value)
                    x_sub.append(args[i])
            x.append(x_sub)
            y.append(y_sub)
            draw_graphic(left, right, -25, 25, x, y, 'f(x) = ' + red_function.getDisplay())
        elif user_str == 'help' or user_str == 'h':
            print(
                'Enter "help" to show every commands\n'
                'Enter "set left" to set left border\n'
                'Enter "set left" to set right border\n'
                'Enter "set eps" to set epsilon\n'
                'Enter "set function" to choose function\n'
                'Enter "set method" to choose method\n'
                'Enter "calc" to begin calculation\n'
                'Enter "ncalc" to begin calculation with assigned n\n'
                'Enter "now" to begin calculation\n'
                'Enter "exit" to exit (Suddenly, isn\'t it?)\n'
            )
