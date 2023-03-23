"""
    Um pequeno jogo de adivinhação funciona da seguinte forma: você deﬁne um número n e chama um amigo, 
    que deverá adivinhar o número escolhido. Faça um programa que peça um inteiro e então ﬁque pedindo que 
    um usuário tente adivinhá-lo até que acerte. 
    Em cada tentativa o programa deve dizer se o chute foi maior ou menor que o número certo.
"""

n = int(input())
b = True
while b:
    a = int(input())
    if a == n:
        print("Parabéns! Você acertou.")
        b = False
    elif a < n:
        print("O número correto é maior.")
    elif a > n:
        print("O número correto é menor.")