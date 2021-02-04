import math


def picard_peano_equations_method(x, y, fx, fy, precision):
    prev_x, prev_y = x + 10, y + 10  # Make sure x - prev != 0
    while abs(x - prev_x) > precision or abs(y - prev_y) > precision:
        prev_x, prev_y = x, y
        x, y = fx(x, y), fy(x, y)
    return x, y

def newton_equations_method(x, y, f1, f2, f1x, f2x, f1y, f2y, precision):
    prev_x, prev_y = x + 10, y + 10  # Make sure x - prev != 0
    while abs(x - prev_x) > precision or abs(y - prev_y) > precision:
        prev_x, prev_y = x, y
        jacobian = f1x(x, y) * f2y(x, y) - f2x(x, y) * f1y(x, y)
        x, y = x - (f1(x, y) * f2y(x, y) - f2(x, y) * f1y(x, y)) / jacobian, y - (f2(x, y) * f1x(x, y) - f1(x, y) * f2x(x, y)) / jacobian
    return x, y

def newton_equation_method(x, f, fx, precision):
    prev_x = x + 10  # Make sure x - prev != 0
    while abs(x - prev_x) > precision:
        prev_x = x
        x = x - f(x) / fx(x)
    return x

def fx(x, y):
    return ((x*y+5*x-1)/2)**0.5
def fy(x, y):
    return (3*math.log(x)+x)**0.5


def f1(x, y):
    return 2*x**2-x*y-5*x+1

def f2(x, y):
    return x+3*math.log(x)-y**2

def f1x(x, y):
    return 4*x-y-5

def f1y(x, y):
    return -x

def f2x(x, y):
    return 1+3/x

def f2y(x, y):
    return -2*y

def fu(x):
    return x * math.exp(-x * 4 * 60) - (0.17325/60) * math.exp(-(0.17325/60) * 4 * 60)

def fux(x):
    return math.exp(-x * 240) - 240 * x * math.exp(-x * 240)

# Tests
def main():
    precision = 0.00000000000000001
    #print(picard_peano_equations_method(4, 4, fx, fy, precision))
    #print(newton_equations_method(4, 4, f1, f2, f1x, f2x, f1y, f2y, precision))
    print(newton_equation_method(0.005, fu, fux, precision))
    return 0

main()