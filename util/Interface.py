import math

from util.Function import RedFunction
from util.RedConsts import x
from util.Integration import Method, RedRound

Functions = [
    RedFunction(x ** 4 / 10 + x ** 2 / 5 - 7, 'x^4/10 + x^2/5 - 7'),
    RedFunction(x ** 2, 'x^2'),
    RedFunction(x ** 4 / 10 + x ** 2 / 5 - 7, 'x^4/10 + x^2/5 - 7')
]


def process():
    left = 1.
    right = 2.
    epsilon = 0.01
    red_function = Functions[0]
    red_method = Method.SIMPSON
    while True:
        print('Enter a command')
        user_str = input()
        if user_str == 'exit' or '':
            break
        elif user_str == 'set left':  # set left border
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
        elif user_str == 'set right':  # set right border
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
        elif user_str == 'set eps' or user_str == 'set epsilon':  # set epsilon
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
        elif user_str == 'choose function':  # choose function
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
        elif user_str == 'choose method':  # choose function
            while True:
                print('Choose the method:\n'
                      'Enter "rect" for {}\n'
                      'Enter "trap" for {}\n'
                      'Enter "simp" or "simpson" for {}\n'
                      .format(Method.RECTANGLE.title, Method.TRAPEZE.title, Method.SIMPSON.title))
                user_str = input()
                if user_str == 'rect':
                    red_method = Method.RECTANGLE
                    break
                elif user_str == 'trap':
                    red_method = Method.TRAPEZE
                    break
                elif user_str == 'simp' or user_str == 'simpson':
                    red_method = Method.SIMPSON
                    break
                elif user_str == 'exit' or user_str == '':
                    break
        elif user_str == 'now':
            print('The function: {}\n'
                  'The method: {}\n'
                  'left border(a) = {}\n'
                  'right border(b) = {}\n'
                  'epsilon = {}\n'
                  .format(red_function.getDisplay(),red_method.title, left, right, epsilon))
        elif user_str == 'calc' or user_str == 'calculation':
            n = int(math.ceil(abs(red_method.fault(epsilon, red_function, left, right))))
            if n % 2 != 0:
                n += 1
            I, table = red_method.NumericMethod(red_function, left, right, epsilon, n)
            truth_I = red_function.integrate(left, right)
            print('{}\n'
                  'n = {}\n'
                  'I = {} ({})\n'
                  '|R| = |I-Iтр| = {} ({})\n'
                  '\n{}'.format(
                red_method.title,
                n,
                RedRound(I, epsilon),
                I,
                RedRound(abs(truth_I - I), epsilon),
                abs(truth_I - I),
                table
            ))
        elif user_str == 'appr' or user_str == 'approximate calculation':
            n_begin = 4
            I, table, n_end = red_method.approximate_calculation(red_function, left, right, epsilon, n_begin)
            truth_I = red_function.integrate(left, right)
            print(
                '{}\n'
                'begin n = {}\n'
                'end n = {}\n'
                'result I = {} ({})\n'
                'epsilon = {}\n'
                '|R| = |I-Iтр| = {:8.4f} ({})\n'
                '{}'.format(
                    red_method.title,
                    n_begin, n_end,
                    RedRound(I, epsilon),
                    I,
                    epsilon,
                    RedRound(abs(truth_I - I), epsilon),
                    abs(truth_I - I),
                    table
                ))
        elif user_str == 'help' or user_str == 'h':
            print('Enter "help" to show every commands\n'
                  'Enter "set left" to set left border\n'
                  'Enter "right left" to set right border\n'
                  'Enter "set eps" to set epsilon\n'
                  'Enter "choose function" to choose function\n'
                  'Enter "choose method" to choose method\n'
                  'Enter "calc" to begin calculation\n'
                  'Enter "now" to begin calculation\n'
                  'Enter "exit" to exit (Suddenly, isn\'t it?)\n'
                  )
