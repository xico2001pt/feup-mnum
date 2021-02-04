import math

# Exercicio 1
# 1. 3 zeros
# 2. [3, 5]
# 3
def bis(a,b,f,n):
    for i in range(n+1):
        m = (a + b) / 2
        print(a, b, m, f(a), f(b), f(m))
        if f(a) * f(m) < 0:
            b = m
        else:
            a = m
bis(-1,0,lambda x: math.exp(0.7*x) - x**2 - 0.5, 2)
# 4
print(-math.log10(abs(-0.5+0.25)))  # Logo, a resposta é 0
# 5
print(abs(-0.5+0.25))

# Exercicio 2
def f1(x,y):
    return x**2-y-1.2
def f2(x,y):
    return -x+y**2-0.5
def f1x(x,y):
    return 2*x
def f1y(x,y):
    return -1
def f2x(x,y):
    return -1
def f2y(x,y):
    return 2*y
def newton(x,y,f1,f2,f1x,f2x,f1y,f2y,n):
    for i in range(n+1):
        print(x, y)
        jacobian = f1x(x,y)*f2y(x,y)-f2x(x,y)*f1y(x,y)
        nx = x - (f1(x,y)*f2y(x,y)-f2(x,y)*f1y(x,y))/jacobian
        ny = y - (f2(x,y)*f1x(x,y)-f1(x,y)*f2x(x,y))/jacobian
        x, y = nx, ny
newton(1.1,1.1,f1,f2,f1x,f2x,f1y,f2y,2)

# Exercicio 3
# 1. Metodo da tangente
# 2. Sim, mas |g'(x)| < 1

# Exercicio 4 (resolvido no Maxima)
# [x1,x2,x3,x4]:[308.31575,-2268.24132,4466.38001,-2573.4]$;
# e1: 0.5*x1+0.33333*x2+0.25*x3+0.2*x4 - 0;
# e2: 0.33333*x1+0.25*x2+0.2*x3+0.16667*x4 - 0.1;
# e3: 0.25*x1+0.2*x2+0.16667*x3+0.14286*x4 - 0.2;
# e4: 0.2*x1+0.16667*x2+0.14286*x3+0.125*x4 - 0;

# Exercicio 5 (resolvido no Maxima)
# [4.5, 5.1]
