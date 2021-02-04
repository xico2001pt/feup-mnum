import math

# Exercise 1
c, g = 15, 10
def vel(m, t):
    return g * m / c * (1 - math.exp(-c * t / m)) - 35

def dvel(m, t):
    return g / c * (1 - math.exp(-c * t / m)) - g * t / m * math.exp(-c * t / m)

def bissection(a, b, t, f, prec):
    it = 0
    prev = a - b + 10
    while abs(prev - (a - b)) > prec:
        it += 1
        prev = a - b
        m = (a + b) / 2
        if f(a, t) * f(m, t) < 0:
            b = m
        else:
            a = m
    return m, it

def newton(x, t, f, fx, prec):
    prev = x +10
    it = 0
    while abs(prev - x) > prec:
        it += 1
        prev = x
        x = x - f(x, t) / fx(x, t)
    return x, it


# Exercise 2
x0, y0 = 1.2, 1.2

def eq1(x, y):
    return -x ** 2 + x + 0.75

def eq2(x,y):
    return (x ** 2 - y) / 5 / y

def picard_peano(x, y, fx, fy, steps):
    for _ in range(steps):
        x, y = fx(x,y), fy(x,y)
    return x, y

# Exercise 3
matrix_a = [[10,2,-1],[-3,-6,2],[1,1,5]]
matrix_b = [27,-61.5,-21.5]

def gauss_jacobi(x, a, b, steps):
    for it in range(steps):
        xp = x.copy()
        for i in range(len(x)):
            soma = 0
            for j in range(len(x)):
                if i != j:
                    soma += a[i][j] * xp[j]
            x[i] = (-soma + b[i]) / a[i][i]
        print(it + 1, x)
    return x

def gauss_seidel(x, a, b, steps):
    for it in range(steps):
        xp = x.copy()
        for i in range(len(x)):
            soma1 = 0
            soma2 = 0
            for j in range(len(x)):
                if j < i:
                    soma1 += a[i][j]*x[j]
            for j in range(len(x)):
                if j > i:
                    soma2 += a[i][j]*xp[j]
            x[i] = (-soma1 - soma2 + b[i]) / a[i][i]
        print(it+1, x)
    return x

# Exercise 4
def int_func(x):
    return 2*math.exp(-1.5*x)

x_val = [0, 0.05, 0.1, 0.2, 0.25, 0.3, 0.4, 0.5, 0.55, 0.6]
fx_val = [2, 1.855, 1.721, 1.482, 1.375, 1.275, 1.098, 0.945, 0.876, 0.813]

def trapezio(x, fx):
    soma = (x[1] - x[0]) * fx[0] + (x[-1] - x[-2]) * fx[-1]
    for i in range(1, len(fx) - 1):
        soma += (x[i+1] - x[i]) * 2 * fx[i]
    return soma / 2

def simpson(x, fx):
    soma = (x[1] - x[0]) * fx[0] + (x[-1] - x[-2]) * fx[-1]
    for i in range(1, len(fx) - 1):
        if i % 2 == 0:
            soma += (x[i+1] - x[i]) * 4 * fx[i]
        else:
            soma += (x[i + 1] - x[i]) * 2 * fx[i]
    return soma / 3

def f_trapezio(a,b,f,h):
    soma = f(a) + f(b)
    while a < b - h:
        a += h
        soma += 2 * f(a)
    return h * soma / 2

def f_simpson(a,b,f,h):
    h = h / 2
    n = int((b - a) / h)
    result = f(a) + f(b)
    for i in range(1, n):
        if i % 2 == 0:
            result += 2 * f(a + i * h)
        else:
            result += 4 * f(a + i * h)
    return result * h / 3

# Test
def main():
    # Exercise 1
    print("Exercise 1:")
    print(bissection(10, 100, 9, vel, 0.0001))
    print(newton(1, 9, vel, dvel, 0.0001))

    # Exercise 2
    print("\nExercise 2:")
    print(picard_peano(x0, y0, eq2, eq1, 6))

    # Exercise 3
    print("\nExercise 3:")
    gauss_jacobi([0,0,0],matrix_a, matrix_b, 3)
    gauss_seidel([0,0,0],matrix_a,matrix_b, 3)

    # Exercise 4
    print("\nExercise 4:")
    print(trapezio(x_val,fx_val))
    print(simpson(x_val,fx_val))
    print(f_trapezio(0,0.6,int_func,0.15))
    print(f_simpson(0,0.6,int_func,0.15))
    return 0

main()