"""
Usando funções faça um programa que leia um valor n 
indefinidas vezes. O programa deve encerrar quando o 
valor de n for zero. Para cada n lido apresente o quadrado de cada um dos valores pares 
(conforme formato especificado abaixo) de 1 até n, inclusive n, se for o caso.
"""
def pares(n):
    if n ==2:
        return '2'
    elif n < 2:
        return ''
    else:
        if n %2 == 0:
            return '{a} {b}'.format(a=n, b=pares(n-2))
        else:
            return '{a} {b}'.format(a=n-1, b=pares(n-3))
def entrar():
    n = int(input())
    if n == 0:
        return 
    else:
        for i in pares(n).split():
            print(f'{int(i)}^2 = {int(i)**2}')
        return entrar()
entrar()
        
