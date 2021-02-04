import math

# Exercicio 1 (resolvido no Maxima)
# matrix([0.003202439524275008],
# 		[-0.008847027174975562],
# 		[0.004216161388074291])

# Exercicio 2
def gauss_seidel(x,n):
    for i in range(n+1):
        print(x)
        x[0] = (25-0.5*x[1]-3*x[2]-0.25*x[3])/6
        x[1] = (10-1.2*x[0]-0.25*x[2]-0.2*x[3])/3
        x[2] = (7+x[0]-0.25*x[1]-2*x[3])/4
        x[3] = (-12-2*x[0]-4*x[1]-x[2])/8
gauss_seidel([2.12687,2.39858,3.99517,-3.73040],1)

# Exercicio 3
x_val = [x/4 for x in range(9)]
y_val = [1.04,0.37,0.38,1.49,1.08,0.13,0.64,0.84,0.12]
x2_val = [x/2 for x in range(5)]
y2_val = [1.04,0.38,1.08,0.64,0.12]
def simpson(x,f,h):
    res = f[0] + f[-1]
    for i in range(1, len(x)-1):
        if i % 2 == 0:
            res += 2 * f[i]
        else:
            res += 4 * f[i]
    return h * res / 3
print(simpson(x_val,y_val,0.25), (simpson(x_val,y_val,0.25) - simpson(x2_val,y2_val,0.5))/15)

# Exercicio 4
fu = [[1.1,2.1,7.3],[1.4,3.1,1.5],[7.7,2.2,1.2]]
print(1 * 1 / 4 * (fu[0][0]+fu[2][0]+fu[0][2]+fu[2][2]+2*(fu[1][0]+fu[0][1]+fu[1][2]+fu[2][1])+4*(fu[1][1])))

# Exercicio 5
def dz(t,y,z):
    return 2+t**2+t*z
def dy(t,y,z):
    return z
def euler(dy,dz,t,y,z,h,n):
    for i in range(n+1):
        print(i, t, y)
        delta_y = dy(t,y,z)*h
        delta_z = dz(t,y,z)*h
        y += delta_y
        z += delta_z
        t += h
euler(dy,dz,1,1,0,0.25,2)