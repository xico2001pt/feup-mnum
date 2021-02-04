# Exercicio 1
# a) 2
# b) Sim, Sim, Não, Sim
# c) Sim, Sim, Não
# d)
def g(x):
    return (4*x**3-x+1) ** (1/4)
def peano(x,g,n):
    for i in range(n+1):
        print(i,x)
        x = g(x)
peano(4,g,2)

# Exercicio 2 (resolvido no Maxima)
# b)
# matrix([0.9726302407454251],
# 		[-3.064432247413487],
# 		[0.3266196833104984],
# 		[1.820376198802823])
# c)
# matrix([0.122491439589405],
# 		[0.5670005471209465],
# 		[-0.01530142537550729],
# 		[0.1343867838941213])
