import math

# Exercicio 1
def fu1(x,y):
    return math.sin(x+y) - math.exp(x-y)
def fu1x(x,y):
    return math.cos(x+y) - math.exp(x-y)
def fu1y(x,y):
    return math.cos(x+y) + math.exp(x-y)
def fu2(x,y):
    return math.cos(x+y) - x*x*y*y
def fu2x(x,y):
    return -math.sin(y+x) - 2*x*y*y
def fu2y(x,y):
    return -math.sin(x+y) - 2*x*x*y
def newton(x,y,f1,f2,f1x,f1y,f2x,f2y,n):
    for i in range(n+1):
        print(x, y)
        jacobian = f1x(x,y)*f2y(x,y) - f2x(x,y)*f1y(x,y)
        new_x = x - (f1(x,y)*f2y(x,y) - f2(x,y)*f1y(x,y)) / jacobian
        new_y = y - (f2(x,y)*f1x(x,y) - f1(x,y)*f2x(x,y)) / jacobian
        x, y = new_x, new_y
newton(0.5,0.25,fu1,fu2,fu1x,fu1y,fu2x,fu2y,2)

# Exercicio 2
# a) I, pois a matriz tem de ser diagonalmente dominante
# b) III
# c)
# xn+1 = (1.2 - 61yn - 41zn) / 103
# yn+1 = (0 - xn+1 - 3zn) / 5.5
# zn+1 = (-13 - 2xn+1 - 10yn+1) / 13

# Exercicio 3
def double_integral():
    res = 1.1 + 9.8 + 1.2 + 7.8
    res += 4 * (2.1 + 1.4 + 2.2 + 1.5)
    res += 16 * 4
    return res / 9
print(double_integral())

# Exercicio 4
def dy(x,y,z):
    return z
def dz(x,y,z):
    return -7*z-4*y
def euler(xi, xf, y, z, dy, dz, h):
    n = (xf - xi) / h + 1
    x = xi
    for i in range(int(n)+1):
        print(x, y, z)
        new_z = z + h * dz(x,y,z)
        new_y = y + h * dy(x, y, z)
        new_x = x + h
        x, y, z = new_x, new_y, new_z
euler(0.4,1,2,1,dy,dz,0.2)

# Exercicio 5
# a) 0.2583e1 + 0.2115e-3 + 0.4523e4 = 0.2583e1 + 0.00002115e1 + 0.4523e4
# = 0.2583e1 + 0.4523e4 = 0.0002583e4 + 0.4523e4 = 0.4525583e4 = 0.4526e4
# b) 0.4168e0
# c) 0.009
