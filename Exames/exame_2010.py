import math

# Exercicio 1 (resolvido no Maxima)
# a) X1 e X2
# b) X1 e X2
# c) Nenhum

# Exercicio 2
def picard_peano(x, g, n):
    for i in range(n+1):
        print(i, x)
        x = g(x)
picard_peano(0.9,lambda x:2*math.log(2*x),1)
print(1.1755733298042381 - 0.9)

# Exercicio 3
# a)
def fun(x, y):
    return math.sin(y) + math.sin(2*x)
def rk4(xi, xf, yi, f, h):
    x, y = xi, yi
    n = (xf - xi) / h
    for i in range(int(n)+1):
        print(i,x,y)
        d1 = h * f(x, y)
        d2 = h * f(x+h/2, y+d1/2)
        d3 = h * f(x+h/2, y+d2/2)
        d4 = h * f(x+h, y+d3)
        y = y + d1/6+d2/3+d3/3+d4/6
        x = x + h
rk4(1,1.5,0,fun,0.5)
rk4(1,1.5,0,fun,0.5/2)
rk4(1,1.5,0,fun,0.5/4)
# b)
print("QC =", (0.3915025536720874-0.39123792364375565)/(0.39151725381482005-0.3915025536720874))
# c)
print(0.5/8)

# Exercicio 4
# a) O elemento da diagonal em cada linha terá de ser maior do que a soma dos restantes. Logo, I.
# b) III
# c)
# xn+1 = (2 - 6y - z) / 10
# yn+1 = (0 - xn+1 -3z) / 11
# zn+1 = (-8 - 2xn+1 - 7yn+1) / 13

# Exercicio 5
def zfun(x,y):
    return 6*x**2 -x*y+ 12*y + y**2 -8*x
def zfunx(x,y):
    return 12*x -y -8
def zfuny(x,y):
    return -x +12 +2*y
def grad(x,y,f,fx,fy,delta,n):
    for i in range(n+1):
        print(i, x, y, f(x,y), fx(x,y), fy(x,y))
        new_x = x - delta * fx(x,y)
        new_y = y - delta * fy(x,y)
        if f(new_x, new_y) < f(x, y):
            x = new_x
            y = new_y
            delta *= 2
        else:
            delta /= 2
grad(0,0,zfun,zfunx,zfuny,0.25,1)

# Exercicio 6 (resolvido no Maxima)
# matrix([0.003202439524275008],
# 		[-0.008847027174975562],
# 		[0.004216161388074291])
