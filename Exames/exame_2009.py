import math

# Exercicio 1
def func(x):
    return (x - 2.6) + math.cos(x + 1.1) ** 3
def funcx(x):
    return 1 - 3 * math.cos(x + 1.1) ** 2 * math.sin(x + 1.1)

def newton(x, f, fx, n):
    for i in range(n+1):
        print(i, x)
        x = x - f(x) / fx(x)

newton(1.8, func, funcx, 1)

# Exercicio 2
# Escolheria a equação a), pois a derivada da b) é mais complexa, fazendo com que seja necessário efetuar mais calculos,
# aumentando assim as hipóteses de ocorrer mais erros devido a arredondamentos.

# Exercicio 3 (resolvido no Maxima)
# a)
# matrix([0.1,	0.5,	3.0,	0.25],
# 		[0.0,	1.0,	6.163793103448276,	0.4827586206896551],
# 		[0.0,	0.0,	1.0,	-0.9541745134965461],
# 		[0.0,	0.0,	0.0,	1.0])
# matrix([0],
# 		[0.1724137931034483],
# 		[-1.410336890562878],
# 		[1.820376198802824])

# b)
# matrix([0.9726302407454251],
# 		[-3.064432247413487],
# 		[0.3266196833104984],
# 		[1.820376198802823])

# c)
# matrix([0.2041523993156747],
# 		[0.9450009118682405],
# 		[-0.02550237562584488],
# 		[0.2239779731568687])

# Exercicio 4
def fun(x):
    return 5 * math.cos(x) - math.sin(x)

def sec_aurea(x1, x2, f, n):
    B = (math.sqrt(5) - 1) / 2
    A = B ** 2
    for i in range(n+1):
        x3, x4 = x1 + A * (x2 - x1), x1 + B * (x2 - x1)
        print(i, "[{}, {}, {}, {}]".format(x1, x2, x3, x4),"[{}, {}, {}, {}]".format(f(x1), f(x2), f(x3), f(x4)))
        if f(x3) < f(x4):
            x2 = x4
        else:
            x1 = x3

sec_aurea(2, 4, fun, 3)
print(3.23606797749979-2.7639320225002106)

# Exercicio 5
def f(t,x):
    return math.sin(x) + math.sin(2*t)
def rk4(ti, tf, xi, df, h):
    n = (tf - ti) / h
    t, x = ti, xi
    for i in range(int(n)+1):
        print(t, x)
        d1 = h*df(t,x)
        d2 = h*df(t+h/2,x+d1/2)
        d3 = h*df(t+h/2,x+d2/2)
        d4 = h*df(t+h,x+d3)
        x = x + d1/6+d2/3+d3/3+d4/6
        t = t + h

for h in [0.5,0.5/2,0.5/4]:
    rk4(1,1.5,1,f,h)
print("QC =",(1.768150065488432-1.7678157507615062)/(1.768184051418221-1.768150065488432))

# Exercicio 6
# a) Regra dos Trapézios
# b) 11.2, 15.6, 5.27
# c)
print("QC =", (5.27-5.18)/(5.235-5.27))
# d) Não, pois é muito diferente de 4
# e)
print("erro =", abs((5.235-5.27)/3))
