"""Efetuar o cálculo da quantidade de litros de combustível (gasolina) gastos em uma viagem, sabendo-se que o carro faz 14.2 km com um litro (na estrada). Deverão ser lidos o tempo gasto na viagem e a velocidade média. Utilizar as seguintes fórmulas:

distancia = tempo x velocidade

litros = distancia / 14.2"""

t = float(input())
v = float(input())
d = t * v
print("{a} {b:.2f}".format(a= d,b=d/14.2))