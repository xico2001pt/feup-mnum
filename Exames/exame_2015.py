import math

# Exercicio 1
def dt(t,T):
    return -0.25*(T-37)
def euler(xi, yi, f, h, n):
    x, y = xi, yi
    for i in range(n + 1):
        print(i, x, y)
        y += f(x, y) * h
        x += h
euler(5, 3, dt, 0.4, 2)

# Exercicio 2 (resolvido no Maxima)
# a)
# matrix([1, 1/2, 1/3],
# 		[0,	1,	1],
# 		[0,	0,	1])
# matrix([-1],
# 		[18],
# 		[-30])
# b)
# matrix([-15],
# 		[48],
# 		[-30])
# c)
# matrix([1, 1/2, 1/3],
# 		[0,	1,	1],
# 		[0,	0,	1])
# matrix([-0.1],
# 		[-0.6],
# 		[-3])
# d) X3

# Exercicio 4 (resolvido no Maxima)
# 1.a) X1 e X2
# b) Nenhum
# c) X1 e X2
# 2.
def fu(x):
    return 2*math.log(2*x)
def picard_peano(x, f, n):
    for i in range(n+1):
        print(i, x)
        x = f(x)
picard_peano(1.1,fu,1)
# 3.
print(1.5769147207285406-1.1)

# Exercicio 5
def l(x):
    return math.sqrt(1 + (2.5*math.exp(2.5*x))**2)
def trapezios(xi, xf, f, h):
    res = f(xi) + f(xf)
    n = (xf - xi) / h
    for i in range(1, int(n)):
        res += 2 * f(xi + i*h)
    return res * h / 2
def simpsons(xi, xf, f, h):
    res = f(xi) + f(xf)
    h = h / 2
    n = (xf - xi) / h
    for i in range(1, int(n)):
        if i % 2 == 1:
            res += 4 * f(xi + i * h)
        else:
            res += 2 * f(xi + i * h)
    return res * h / 3
print(trapezios(0,1,l,0.125))
print(simpsons(0,1,l,0.125))
print(trapezios(0,1,l,0.125/2))
print(simpsons(0,1,l,0.125/2))
print(trapezios(0,1,l,0.125/4))
print(simpsons(0,1,l,0.125/4))

# Exercicio 7
def func(x):
    return x**3 - 10 * math.sin(x) + 2.8
def bissecao(a, b, f, n):
    for i in range(n+1):
        print(i, a, b)
        m = (a + b) / 2
        if f(a) * f(m) < 0:
            b = m
        else:
            a = m
bissecao(1.5,4.2,func,2)