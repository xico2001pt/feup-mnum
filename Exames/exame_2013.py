import math

# Exercicio 1
def dy(t,y,z):
    return z
def dz(t,y,z):
    return 0.5 + t**2 + t*z
def euler(t,y,z,dy,dz,h,n):
    for i in range(n+1):
        print(i, t, y)
        delta_z = h * dz(t,y,z)
        delta_y = h * dy(t,y,z)
        t = t + h
        y = y + delta_y
        z = z + delta_z
def rk4(t,y,z,dy,dz,h,n):
    for i in range(n+1):
        print(i, t, y)
        dy1, dz1 = h * dy(t,y,z), h * dz(t,y,z)
        dy2, dz2 = h * dy(t+h/2,y+dy1/2,z+dz1/2), h * dz(t+h/2,y+dy1/2,z+dz1/2)
        dy3, dz3 = h * dy(t+h/2,y+dy2/2,z+dz2/2), h * dz(t+h/2,y+dy2/2,z+dz2/2)
        dy4, dz4 = h * dy(t+h,y+dy3,z+dz3), h * dy(t+h,y+dy3,z+dz3)
        t = t + h
        y = y + dy1/6+dy2/3+dy3/3+dy4/6
        z = z + dz1/6+dz2/3+dz3/3+dz4/6
euler(0,0,1,dy,dz,0.25,2)
rk4(0,0,1,dy,dz,0.25,2)

# Exercicio 2
def z(x,y):
    return 3*x**2 - y*x + 11*y + y**2 - 8*x
def dzx(x,y):
    return 6*x - y - 8
def dzy(x,y):
    return -x + 11 + 2*y
def gradiente(x,y,z,dzx,dzy,l,n):
    for i in range(n+1):
        print(i, x, y, z(x,y), dzx(x,y), dzy(x,y))
        new_x = x - l * dzx(x,y)
        new_y = y - l * dzy(x,y)
        if z(new_x,new_y) < z(x,y):
            x = new_x
            y = new_y
            l *= 2
        else:
            l /= 2
gradiente(2,2,z,dzx,dzy,0.5,1)

# Exercicio 4
def f(x):
    return math.exp(1.5*x)
def simpson(a,b,f,h):
    h *= 2
    n = (b - a) / h
    res = f(a) + f(b)
    for i in range(1, int(n)):
        if i % 2 == 0:
            res += 2 * f(a + i * h)
        else:
            res += 4 * f(a + i * h)
    return h * res / 3
print(simpson(1,1.5,f,0.125))
print(simpson(1,1.5,f,0.125/2))
print(simpson(1,1.5,f,0.125/4))
print("QC =", (3.337387330987544-3.337725115668087)/(3.337365941424579-3.337387330987544))
print("Erro estimado =", (3.337365941424579-3.337387330987544)/15)

# Exercicio 5
def fun(x):
    return x - 3.7 + math.cos(x + 1.2)**3
def funx(x):
    return 1 - 3 * math.cos(x + 1.2) ** 2 * math.sin(x + 1.2)
def newton(x,f,fx,n):
    for i in range(n+1):
        print(i,x)
        x = x - f(x) / fx(x)
newton(3.8,fun,funx,1)