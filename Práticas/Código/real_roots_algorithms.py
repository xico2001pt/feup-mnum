import math

def bisection_method(a, b, function, precision):
    prev_diff = 0  # Stores the current and previous difference
    while abs(abs(b - a) - prev_diff) > precision:
        prev_diff = abs(b - a)  # Store previous difference
        m = (a + b) / 2
        if function(a) * function(m) < 0:
            b = m
        else:
            a = m
    return b

def string_method(a, b, function, precision):
    prev_diff = 0
    while abs(abs(b - a) - prev_diff) > precision:
        prev_diff = abs(b - a)
        m = (function(b) * a - function(a) * b) / (function(b) - function(a))
        if function(a) * function(m) < 0:
            b = m
        else:
            a = m
    return b

def newton_method(x, function, derivative, precision):
    prev = x + 10  # Make sure x - prev != 0
    while abs(x - prev) > precision:
        prev = x
        diff = derivative(x)
        if diff == 0:
            print("f'(x) can't be 0")
        x = x - function(x) / diff
    return x

def picard_peano_method(x, function, precision):
    prev = x + 10  # Make sure x - prev != 0
    while abs(x - prev) > precision:
        prev = x
        x = function(x)
    return x


# Tests
def main():
    precision = 10**-5
    #print(bisection_method(0.01, 1, lambda x: x - 2 * math.log(x) - 5, precision))
    #print(string_method(0.01, 1, lambda x: x - 2 * math.log(x) - 5, precision))
    #print(newton_method(0.01, lambda x: x - 2 * math.log(x) - 5, lambda x: 1 - 2 / x, precision))
    print(newton_method(4.54, lambda x: -1+5.5*x-4*x**2+0.5*x**3, lambda x: 1.5*x**2-8*x+5.5, precision))
    #print(picard_peano_method(4, lambda x: (x+1.2)**0.5, precision))

main()