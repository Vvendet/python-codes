"""
Leia 3 valores de ponto flutuante A, B e C e ordene-os de modo que A representa o maior dos 3 lados. A seguir, determine o tipo de triângulo que estes três lados formam, com base nos seguintes casos, sempre escrevendo uma mensagem adequada:"""

a = float(input())
b = float(input())
c = float(input())
A,B,C = 0,0,0
lista = [a,b,c]
for i in lista:
    if i > A:
        A = i
lista.remove(A)
for i in lista:
    if i > B:
       B = i
lista.remove(B)
C = lista[0]

if A >= B+C:
    print("NAO FORMA TRIANGULO")
elif A**2 == (B**2 + C**2):
    print("TRIANGULO RETANGULO")
elif A == B and A == C:
    print("TRIANGULO EQUILATERO")
elif A==B or B == C or A == C:
    print("TRIANGULO ISOSCELES")
else:
    print("TRIANGULO ACUTANGULO OU OBTUSANGULO")
