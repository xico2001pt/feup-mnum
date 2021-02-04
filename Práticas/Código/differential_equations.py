import math

def diff_eq_euler(diff, xi, xf, yi, h):
    n = (xf - xi) / h
    x, y = xi, yi
    for _ in range(0, int(n) + 1):
        new_x = x + h
        new_y = y + diff(x, y) * h
        x, y = new_x, new_y
        print("y({}) = {}".format(x, y))
    return

def diff_eq_rk2(diff, xi, xf, yi, h):
    # NÃO TESTADO
    n = (xf - xi) / h
    x, y = xi, yi
    print("y({}) = {}".format(x, y))
    for _ in range(0, int(n)):
        new_x = x + h
        new_y = y + h * diff(x + h / 2, y + h * diff(x, y) / 2)
        x, y = new_x, new_y
        print("y({}) = {}".format(x, y))
    return

def diff_eq_rk4(diff, xi, xf, yi, h):
    n = (xf - xi) / h
    x, y = xi, yi
    for _ in range(0, int(n) + 1):
        d1 = h * diff(x, y)
        d2 = h * diff(x + h / 2, y + d1 / 2)
        d3 = h * diff(x + h / 2, y + d2 / 2)
        d4 = h * diff(x + h, y + d3)

        new_x = x + h
        new_y = y + (d1 / 6 + d2 / 3 + d3 / 3 + d4 / 6)
        x, y = new_x, new_y
        print("y({}) = {}".format(x, y))
    return

def diff_eq_euler_sup(diffy, diffz, xi, xf, yi, zi, h):
    n = (xf - xi) / h
    x, y, z = xi, yi, zi
    for _ in range(0, int(n) + 1):
        new_x = x + h
        new_y = y + diffy(x, y, z) * h
        new_z = z + diffz(x, y, z) * h
        x, y, z = new_x, new_y, new_z
        print("y({}): y={} ; z={}".format(x, y, z))
    return

def diff_eq_rk2_sup(diffy, diffz, xi, xf, yi, zi, h):
    # A FUNÇÃO NÃO FUNCIONA CORRETAMENTE
    n = (xf - xi) / h
    x, y, z = xi, yi, zi
    print("y({}): y={} ; z={}".format(x, y, z))
    for _ in range(0, int(n)):
        new_x = x + h
        new_y = y + h * diffy(x + h / 2, y + h * diffy(x, y, z) / 2, z + h * diffz(x, y, z) / 2)
        new_z = z + h * diffz(x + h / 2, y + h * diffy(x, y, z) / 2, z + h * diffz(x, y, z) / 2)
        x, y, z = new_x, new_y, new_z
        print("y({}): y={} ; z={}".format(x, y, z))
    return

def diff_eq_rk4_sup(diffy, diffz, xi, xf, yi, zi, h):
    n = (xf - xi) / h
    x, y, z = xi, yi, zi
    print("y({}): y={} ; z={}".format(x, y, z))
    for _ in range(0, int(n)):
        dy1, dz1 = h * diffy(x, y, z), h * diffz(x, y, z)
        dy2, dz2 = h * diffy(x + h / 2, y + dy1 / 2, z + dz1 / 2), h * diffz(x + h / 2, y + dy1 / 2, z + dz1 / 2)
        dy3, dz3 = h * diffy(x + h / 2, y + dy2 / 2, z + dz2 / 2), h * diffz(x + h / 2, y + dy2 / 2, z + dz2 / 2)
        dy4, dz4 = h * diffy(x + h, y + dy3, z + dz3), h * diffz(x + h, y + dy3, z + dz3)

        new_x = x + h
        new_y = y + (dy1 / 6 + dy2 / 3 + dy3 / 3 + dy4 / 6)
        new_z = z + (dz1 / 6 + dz2 / 3 + dz3 / 3 + dz4 / 6)
        x, y, z = new_x, new_y, new_z
        print("y({}): y={} ; z={}".format(x, y, z))
    return

# Tests

def f(x, y):
    return x ** 2 + y ** 2

def f1(x, y, z):
    return z * y + x

def f2(x, y, z):
    return z * x + y

def f3(x, y, z):
    return - 2 * y + 4 * math.exp(-x)

def f4(x, y, z):
    return -y * z * z / 3

def f5(x, y, z):
    return z

def f6(x, y, z):
    return - (0.6 * z + 8 * y)

def f7(x, y, z):
    return z

def f8(x, y, z):
    return 0.5 * z - y

def main():
    #diff_eq_rk2(f, 0, 1.4, 0, 0.1)
    #diff_eq_euler(f, 0, 1.4, 0, 0.05)
    #diff_eq_euler(f, 0, 1.4, 0, 0.025)
    #print((1.0222713067772329-0.9307268557086219)/(1.0747561648232127-1.0222713067772329))
    #diff_eq_euler_sup(f1, f2, 0, 0.5, 1, 1, 0.05)
    #diff_eq_rk2_sup(f1, f2, 0, 0.5, 1, 1, 0.05)
    #diff_eq_rk4_sup(f3, f4, 0, 0.2, 2, 4, 0.2)
    #diff_eq_rk4_sup(f5, f6, 0, 0.5, 4, 0, 0.1)
    diff_eq_rk2_sup(f7, f8, 0, 4, 2, 0, 0.01)
    return 0

main()