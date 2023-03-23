"""
Usando recursividade, faça um programa que dado um inteiro n positivo 
lido do teclado, retorne todos os números pares maiores ou iguais a 
dois, que são menores ou iguais a n.
"""
m = int(input())

def funct(n):
    if n == 2:
        return 2
    elif n < 2:
        return ''
    else:
        if n %2 == 0:
            return '{a} {b}'.format(a=n, b=funct(n-2))
        else:
            return '{a} {b}'.format(a=n-1, b=funct(n-3))
for i in funct(m).split():
    print(i)