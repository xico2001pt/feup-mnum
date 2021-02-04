import math

# Exercicio 1
# a) 1
# b) ]-1,0[
# c)
def biss(a,b,f,n):
    for i in range(n+1):
        print(i, a, b)
        m = (a + b) / 2
        if f(a) * f(m) < 0:
            b = m
        else:
            a = m
biss(-1,0,lambda x: math.sin(x)+x**5-0.2*x+1,6)
print(-0.828125 - (-0.84375))
print((-0.828125 - (-0.84375))/-0.828125)

# Exercicio 2
def f1(x,y):
    return x**2-y-1.2
def f2(x,y):
    return -x+y**2-1
def f1x(x,y):
    return 2*x
def f1y(x,y):
    return -1
def f2x(x,y):
    return -1
def f2y(x,y):
    return 2*y
def newton(x,y,f1,f2,f1x,f1y,f2x,f2y,n):
    for i in range(n+1):
        print(i, x, y)
        jacobian = f1x(x,y)*f2y(x,y)-f2x(x,y)*f1y(x,y)
        new_x = x - (f1(x,y)*f2y(x,y)-f2(x,y)*f1y(x,y)) / jacobian
        new_y = y - (f2(x,y)*f1x(x,y)-f1(x,y)*f2x(x,y)) / jacobian
        x, y = new_x, new_y
newton(1,1,f1,f2,f1x,f1y,f2x,f2y,2)

# Exercicio 3
def f(x):
    return math.sqrt(1+(1.5*math.exp(1.5*x))**2)
def trapezio(a,b,f,h):
    n = (b - a) / h
    res = f(a) + f(b)
    for i in range(1, int(n)):
        res += 2 * f(a + i * h)
    return res * h / 2
def simspon(a,b,f,h):
    h /= 2
    n = (b - a) / h
    res = f(a) + f(b)
    for i in range(1, int(n)):
        if i % 2 == 0:
            res += 2 * f(a + i * h)
        else:
            res += 4 * f(a + i * h)
    return res * h / 3
print("Trapezio:")
print(trapezio(0,2,f,0.25))
print(trapezio(0,2,f,0.25/2))
print(trapezio(0,2,f,0.25/4))
print("QC =", (19.345728845359307-19.51436410143159)/(19.30347867133232-19.345728845359307))
print("Erro =", (19.30347867133232-19.345728845359307)/3)
print("\nSimpson:")
print(simspon(0,2,f,0.25))
print(simspon(0,2,f,0.25/2))
print(simspon(0,2,f,0.25/4))
print("QC =", (19.28939527998999-19.289517093335213)/(19.289387641597916-19.28939527998999))
print("Erro =", (19.289387641597916-19.28939527998999)/15)

# Exercicio 4
def eq(t, T):
    return -0.25 * (T - 59)
def euler(t, T, f, h, n):
    for i in range(n+1):
        print(i, t, T)
        T += h * f(t,T)
        t += h
euler(2,2,eq,0.5,2)

# Exercicio 5
def fun(x):
    return -5*math.cos(x)+math.sin(x)+10
def aurea(x1, x2, f, n):
    fu = lambda x: -f(x)
    B = (math.sqrt(5) - 1) / 2
    A = B ** 2
    x3 = x1 + A * (x2 - x1)
    x4 = x1 + B * (x2 - x1)
    for i in range(n+1):
        print(x1, x2, x3, x4, f(x1), (x2), f(x3), f(x4))
        if fu(x3) < fu(x4):
            x2 = x4
            x4 = x3
            x3 = x1 + A * (x2 - x1)
        else:
            x1 = x3
            x3 = x4
            x4 = x1 + B * (x2 - x1)
aurea(2,4,fun,2)

# Exercico 6
def z(x,y):
    return 6*x**2-x*y+12*y+y**2-8*x
def dx(x,y):
    return 12*x-y-8
def dy(x,y):
    return -x+12+2*y
def gradiente(x,y,z,dx,dy,h,n):
    for i in range(n+1):
        print(x, y, z(x,y), dx(x,y), dy(x,y))
        new_x = x - h * dx(x,y)
        new_y = y - h * dy(x,y)
        if z(new_x,new_y) < z(x,y):
            x, y = new_x, new_y
            h *= 2
        else:
            h /= 2
gradiente(1,2,z,dx,dy,0.5,1)