"""Criar um programa que leia o valor de um depósito e o valor da taxa de juros mensal. Calcular e imprimir o valor do rendimento e o valor total depois do rendimento para o primeiro mês."""

d = float(input())
i = float(input())
r = d*i/100
res = d + r
print("{a:.2f}".format(a=r))
print("{b:.2f}".format(b=res))