import math

# Exercicio 1
def func(t,y):
    return y / (t - 1)

def euler(t,y,f,h,n):
    for i in range(n+1):
        print(i, t, y)
        y = y + f(t,y)*h
        t = t + h

def rk4(t,y,f,h,n):
    for i in range(n+1):
        dy1 = h*f(t,y)
        dy2 = h*f(t+h/2,y+dy1/2)
        dy3 = h*f(t+h/2,y+dy2/2)
        dy4 = h*f(t+h,y+dy3)
        print(i,t,y,dy1, dy2, dy3, dy4)
        y = y + dy1/6+dy2/3+dy3/3+dy4/6
        t = t + h

euler(2,2,func,0.25,2)
rk4(2,2,func,0.25,2)

# Exercicio 3
def w(x,y):
    return -1.7*x*y + 12*y + 7*x**2 - 8*x
def dwx(x,y):
    return -1.7*y +14*x - 8
def dwy(x,y):
    return 12 - 1.7*x
def min_grad(x,y,f,fx,fy,l,n):
    for i in range(n+1):
        print(i, x, y, f(x,y))
        new_y = y - l * fy(x,y)
        new_x = x - l * fx(x,y)
        if f(new_x,new_y) < f(x, y):
            l = 2 * l
            x, y = new_x, new_y
        else:
            l = l / 2
min_grad(2.4,4.3,w,dwx,dwy,0.1,1)

# Exercicio 4
# math.sqrt((x+1)*(x-1)) - x, idk...

# Exercicio 5
def f1(x,y):
    return x**2 - y - 2
def f1x(x,y):
    return 2*x
def f1y(x,y):
    return -1
def f2(x,y):
    return y**2 - x - 2
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
newton(1.5,0.8,f1,f2,f1x,f1y,f2x,f2y,2)

# Exercicio 6 (resolvido no Maxima)
# [4.6, 5.0]
