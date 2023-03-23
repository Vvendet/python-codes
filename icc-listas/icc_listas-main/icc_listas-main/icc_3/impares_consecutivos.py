"""
Leia um valor inteiro N que especifica a quantidade de casos de teste que vem a seguir. 
Cada caso de teste consiste de dois inteiros, X e Y. Você deve apresentar a soma de Y ímpares 
consecutivos a partir de X, inclusive o próprio X se ele for ímpar. Por exemplo: para a entrada 4 5, 
a saída deve ser 45, que é equivalente a: 5 + 7 + 9 + 11 + 13, para a entrada 7 4, a saída deve ser 40, 
que é equivalente a: 7 + 9 + 11 + 13. No final, imprima também a 
maior e a menor soma entre todos os casos de teste, e a média destas duas últimas somas (a maior e a menor).
"""
n = int(input())
somas = []
for i in range(0,n):
    x,y = a, n = input().split()
    x, y = [int(x), int(y)]
    a = []
    soma = 0
    while len(a) < y:
        if x%2 != 0:
            a.append(x)
        x += 1
    for i in a:
        soma += i
    print(soma)
    somas.append(soma)


maior = -99999
menor = 99999
for i in somas:
    if i > maior:
        maior = i
for j in somas:
    if j < menor:
        menor = j
print(maior)
print(menor)
print(f'{(maior+menor)/2:.2f}')