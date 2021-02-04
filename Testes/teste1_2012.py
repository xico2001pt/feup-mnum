import math

# Exercicio 1 (resolvido no Maxima)
# [-1.4, 2.6]

# Exercicio 2
# Bisseção, Bisseção, Picard-Peano, Bisseção

# Exercicio 3 (resolvido no maxima)
# 1.
# matrix([-6.831564556819286],
# 		[-39.87710174340759],
# 		[32.17876622552956])
# 2.
# matrix([-1.852346543939833],
# 		[-9.662932201566356],
# 		[8.42715900209993])
# 3. x2

# Exercicio 4
# Bisseção, Corda

# Exercicio 5
def newton(x,f,fx,n):
    for i in range(n+1):
        print(x)
        x = x - f(x)/fx(x)
newton(0,lambda x:x**3+2*x**2+10*x-17,lambda x:3*x**2+4*x+10,2)
