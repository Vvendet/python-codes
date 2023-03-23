"""
# Faça um algoritmo para ler um valor inteiro T, um valor A e um valor N. 
# Leia T vezes valores inteiros A e N e imprima cada um dos N números consecutivos a partir de A, incluindo o A. 
# Imprima também a soma dos N números a partir de A (inclusive), para cada um dos valores A e N lidos.
"""

t = int(input())
for i in range(0,t):
    a, n = input().split()
    a, n = [int(a), int(n)] 
    b = [a]
    while len(b) < n:
        print(b[-1],end=' ')
        b.append(b[-1]+1)
    print(b[-1])
    soma = 0
    for d in b:
        soma += d
    print(soma)