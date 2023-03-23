"""Em épocas de pouco dinheiro, os comerciantes estão procurando aumentar suas vendas oferecendo desconto. Faça um programa que possa entrar com o valor de um produto e imprima o novo valor tendo em vista que o desconto foi de 6%."""

val = float(input())
print("{p:.2f}".format(p=val-(val*6/100)))