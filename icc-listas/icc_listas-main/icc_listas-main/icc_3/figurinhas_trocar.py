"""
Raphael e Luiza são aficcionados por figurinhas de futebol. Ambos também têm o 
hábito de trocarem as figuras repetidas com seus amigos e certo dia pensaram em 
uma brincadeira diferente.

Chamaram todos os amigos e propuseram o seguinte: com as figurinhas em mãos,
 cada um tentava fazer uma troca com o amigo que estava mais perto seguindo a 
 seguinte regra: cada um contava quantas figurinhas tinha. Em seguida, eles tinham que
  dividir as figurinhas de cada um em pilhas tal que todas as pilhas, entre ambos, 
  tivessem o mesmo tamanho e esse fosse o maior possível. Então, cada um escolhia 
  uma das pilhas de figurinhas do amigo para receber. 

Por exemplo, se Raphael e Luiza fossem trocar as figurinhas e tivessem respectivamente 
8 e 12 figurinhas, ambos dividiriam as suas quantidades em pilhas de 4 figurinhas cada 
pois esse seria o maior tamanho de pilha comum a ambos. Assim, Raphael teria 2 pilhas e 
Luiza teria 3 pilhas, cada pilha contendo 4 figurinhas. Em seguida, ambos escolheriam uma 
pilha do amigo para receber.

Você pode fazer um programa para ajudá-los com essa brincadeira?
"""

a,b  = input().split()
a,b = [int(a),int(b)]
maximo = 0
def divisor(m,n):
    global maximo
    d = m
    while maximo == 0:
        if m%d == 0 and n%d == 0:
            maximo = d
        d -= 1
if a<b:
    divisor(a,b)
else:
    divisor(b,a)
print(maximo)