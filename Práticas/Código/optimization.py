import math

def aurea_rule(function, x1, x2, precision):
    B = (math.sqrt(5)-1)/2
    A = B**(2)
    while (abs(x1-x2) > precision):
        x3 = x1+A*(x2-x1)
        x4 = x1+B*(x2-x1)
        if (function(x3) < function(x4)):
            x2=x4
        else:
            x1=x3
    return x1, function(x1)

def gradient_method(function, diff_x, diff_y, initial_x, initial_y, h, precision):
    x, y = initial_x, initial_y
    before_x, before_y = 1e10, 1e10
    back = False
    while (back or abs(before_x - x) > precision or abs(before_y - y) > precision):
        back = False
        before_x = x
        before_y = y
        x = before_x - h * diff_x(before_x, before_y)
        y = before_y - h * diff_y(before_x, before_y)
        if (function(x, y) < function(before_x, before_y)):
            h *= 2
        else:
            h /= 2
            x = before_x
            y = before_y
            back = True
    return (x, y, function(x, y))

def quadric_method(Hd, initial_x, initial_y, precision): # Eficaz quando está muito perto do mínimo
    x, y = initial_x, initial_y
    before_x, before_y = 1e10, 1e10
    while (abs(before_x - x) > precision or abs(before_y - y) > precision):
        print(x, y)
        before_x = x
        before_y = y
        x = before_x - Hd[0](before_x, before_y)
        y = before_y - Hd[1](before_x, before_y)
    return x, y


# Main
def f1(x,y):
    return 4*x-2*y
def f2(x,y):
    return 2*y-2*x-6
def f3(x,y):
    return y**2-2*x*y-6*y+2*x**2+12

def f4(x,y):
    return -(2*y-2*x+2)
def f5(x,y):
    return -(2*x-4*y)
def f6(x,y):
    return -(2*x*y+2*x-x**2-2*y**2)

Hd = [lambda x, y: (2*x+(math.cos(x/2)/2)) / (2-((math.sin(x/2)/4))),
    lambda x, y: math.sin(y)/math.cos(y)
]

def main():
    #print(aurea_rule(lambda x: (2*x+1)**2-5*math.cos(10*x), -1, 0, 0.001))
    #print(aurea_rule(lambda x: -((2 * x + 1) ** 2 - 5 * math.cos(10 * x)), -1, 0, 0.001))
    #print(gradient_method(f3, f1, f2, 1, 1, 1, 0.001))
    #print(gradient_method(f6, f4, f5, -1, 1, 1, 0.001))
    #print(quadric_method(Hd, -3, -1, 0.001))
    return 0

main()