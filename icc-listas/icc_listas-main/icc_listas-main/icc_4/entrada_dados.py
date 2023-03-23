"""
Usando uma função, faça um programa que leia 10 números 
inteiros e imprima na tela o maior deles. No caso de 
valores iguais, imprima qualquer um dos maiores. Caso 
o maior número seja múltiplo do primeiro número n lido,
 imprima n na tela.

"""
l = []
def entrada():
    a = int( input())
    l.append(a)
for i in range(0,10):
    entrada()
print(max(l))
if max(l)%l[0] == 0:
    print(l[0])