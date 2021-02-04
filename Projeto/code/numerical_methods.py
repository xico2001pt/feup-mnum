# Bisection Method
def bisection_method(a, b, function, precision):
    # a and b is the range of the interval
    while abs(b - a) > precision:
        m = (a + b) / 2
        if function(a) * function(m) < 0:
            b = m
        else:
            a = m
    return (a + b) / 2


# String Method
def chordZero(x1, x2, func):
    num = (x1 * func(x2) - x2 * func(x1))
    den = func(x2) - func(x1)
    return num / den

def string_method(a, b, func, precision):
    guess = 0
    prev = guess + 10  # Make sure loop occurs
    while (abs(guess- prev) > precision):
        prev = guess
        if func(a) * func(chordZero(a,b, func)) < 0:
            b = chordZero(a,b, func)
            guess = b    
        else:
            a = chordZero(a, b, func)
            guess = a
            
    return chordZero(a,b, func)

# Newton Method
def newton_method(guess, function, derivative, precision):
    prev_guess = guess + 10  # Make sure loop occurs
    while abs(guess - prev_guess) > precision:
        prev_guess = guess
        guess = guess - function(guess) / derivative(guess)
    return guess


# Picard-Peano Method
def picard_peano_method(guess, function, precision):
    prev_guess = guess + 10  # Make sure loop occurs
    while abs(guess - prev_guess) > precision:
        prev_guess = guess
        guess = function(guess)
    return guess


# Euler Method
def euler_method(xn, xf, yn, zn, fy, fz, delta_x):
    res = [[xn],[yn],[zn]]
    n = (xf - xn) / delta_x
    for i in range(int(n)):
        yn = yn +  delta_x * fy(xn,yn,zn)
        zn = zn + delta_x * fz(xn,yn,zn)
        xn += delta_x
        
        res[0].append(xn)
        res[1].append(yn)
        res[2].append(zn)       
        
    return res

# Runge-Kuta Second Order Method
def rk2_method(xi, xf, yi, zi, fy, fz, h):
    x, y, z = xi, yi, zi
    n = (xf - xi) / h
    result = [[xi], [yi], [zi]]
    for i in range(int(n)):
        M1 = fy(x + h / 2, y + fy(x,y,z) * (h / 2), z + fz(x,y,z) * (h / 2))
        M2 = fz(x + h / 2, y + fy(x,y,z) * (h / 2), z + fz(x,y,z) * (h / 2))

        y += M1 * h
        z += M2 * h
        x += h
        result[0].append(x)
        result[1].append(y)
        result[2].append(z)
    return result


# Runge-Kuta Fourth Order Method
def rk4_method(xi, xf, yi, zi, fy, fz, h):
    x, y, z = xi, yi, zi
    n = (xf - xi) / h  # number of steps
    result = [[xi], [yi], [zi]]  # [[x0,...,xn],[y0,...,yn],[z0,...,zn]]
    for _ in range(int(n)):
        dy1, dz1 = h * fy(x, y, z), h * fz(x, y, z)
        dy2, dz2 = h * fy(x + h / 2, y + dy1 / 2, z + dz1 / 2), h * fz(x + h / 2, y + dy1 / 2, z + dz1 / 2)
        dy3, dz3 = h * fy(x + h / 2, y + dy2 / 2, z + dz2 / 2), h * fz(x + h / 2, y + dy2 / 2, z + dz2 / 2)
        dy4, dz4 = h * fy(x + h, y + dy3, z + dy3), h * fz(x + h, y + dy3, z + dy3)

        z = z + dz1 / 6 + dz2 / 3 + dz3 / 3 + dz4 / 6
        y = y + dy1 / 6 + dy2 / 3 + dy3 / 3 + dy4 / 6
        x = x + h
        result[0].append(x)
        result[1].append(y)
        result[2].append(z)
    return result
