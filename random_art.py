import random
from math import *


# Your job is to create better version of create_expression and
# run_expression to create random art.
# Your expression should have a __str__() function defined for it.


def create_expression():
    """This function takes no arguments and returns an expression that
    generates a number between -1.0 and 1.0, given x and y coordinates."""
    # expr1 = lambda x, y: (x + y)/2
    # expr2 = lambda x, y: (x - y)/2
    # expr3 = lambda x, y: x * y

    res = []
    for n in range(random.randint(1, 5)):
        res.append(random.choice(['sin', 'cos', 'tan']) +
                   random.choice(['(x) ', '(y) ', '(x + y) ', '(x * y) ']))
        if n%2 == 1:
            res.append('x')

    part1 = '*'.join(res)
    part2 = '(random.gauss(0.68, 0.2))*sin('+part1+')'

    return lambda x, y: eval(part2)



    # return random.choice([expr1, expr2, expr3])

def run_expression(expr, x, y):
    """This function takes an expression created by create_expression and
    an x and y value. It runs the expression, passing the x and y values
    to it and returns a value between -1.0 and 1.0."""
    return expr(x, y)
