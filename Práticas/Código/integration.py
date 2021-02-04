import math

def regra_trapezios(n, func, a, b):
    h = (b - a) / n
    result = func(a) + func(b)
    for i in range(1, n):
        result += 2 * func(a + i * h)
    return result * h / 2

def regra_trapezios_lista(h, lista):
    result = lista[0] + lista[-1]
    for i in range(1, len(lista) - 1):
        result += 2 * lista[i]
    return result * h / 2

def regra_simpson(n, func, a, b):
    h = (b - a) / n / 2
    result = func(a) + func(b)
    for i in range(1, 2 * n):
        if i % 2 == 0:
            result += 2 * func(a + i * h)
        else:
            result += 4 * func(a + i * h)
    return result * h / 3

def regra_simpson_lista(h, lista):
    result = lista[0] + lista[-1]
    for i in range(1, len(lista) - 1):
        if i % 2 == 0:
            result += 2 * lista[i]
        else:
            result += 4 * lista[i]
    return result * h / 3

def integral_duplo_trapezios(n ,func, ax, bx, ay, by):
    hx, hy = (bx - ax) / n, (by - ay) / n
    # Vertices
    result = func(ax, ay) + func(ax, by) + func(bx, ay) + func(bx, by)
    # Pontos medios
    for y in range(1, n):
        result += 2 * (func(ax, ay + y * hy) + func(bx, ay + y * hy))
    for x in range(1, n):
        result += 2 * (func(ax + x * hx, ay) + func(ax + x * hx, by))
    # Centros
    for x in range(1, n):
        for y in range(1, n):
            result += 4 * func(ax + x * hx, ay + y * hy)
    return hx * hy * result / 4

def integral_duplo_simpson(n ,func, ax, bx, ay, by):
    hx, hy = (bx - ax) / n, (by - ay) / n
    # Vertices
    result = func(ax, ay) + func(ax, by) + func(bx, ay) + func(bx, by)
    # Pontos medios
    for y in range(1, n):
        result += 4 * (func(ax, ay + y * hy) + func(bx, ay + y * hy))
    for x in range(1, n):
        result += 4 * (func(ax + x * hx, ay) + func(ax + x * hx, by))
    # Centros
    for x in range(1, n):
        for y in range(1, n):
            result += 16 * func(ax + x * hx, ay + y * hy)
    return hx * hy * result / 9

# Tests
def f(x):
    return 1 - math.exp(-2 * x)

def g(x, y):
    return x ** 2 - 2 * y ** 2 + x * y ** 3

def main():
    #lista = [35,5,-10,2,5,3,20]
    #print(regra_trapezios_lista(2,lista))
    #print(regra_simpson_lista(2, lista))
    print(integral_duplo_trapezios(2, g, 0, 2, -1, 1))
    print(integral_duplo_simpson(2, g, 0, 2, -1, 1))
    return 0

main()