"""
Usando funções recursivas, faça um programa que 
dado um inteiro n lido do teclado, retorne e imprima 
na tela a soma de todos os números pares de 0 até n−2, incluindo n−2,
 se for o caso. Caso n seja menor que 0, imprima na tela "-1".
"""
a = int(input())
def pares(n):
    if n == 0:
        return 0
    elif n < -2:
        return -1
    elif n == -2:
        return 0
    else:
        if n %2 == 0:
            return n + pares(n-2)
        else:
            return n-1 + pares(n-3)

print(pares(a-2))