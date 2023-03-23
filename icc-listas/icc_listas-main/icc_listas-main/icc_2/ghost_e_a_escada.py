"""No caminho para encontrar Jon Snow em Dragonstone, o lobo Ghost enfrenta um problema: uma grande escada. Os degraus da escada são numeradas de 1 até infinito. Sendo um lobo esperto, Ghost decidiu calcular dois valores, o número de degraus percorridos com números pares e ímpares.

Você precisa checar se o número de passos em degraus pares e ímpares encontrados pelo Ghost estão corretos. Considere que ele não pula nenhum degrau e que ele sobe pelo menos o degrau de número 1."""

A, B = input().split()

A, B = [int(A), int(B)]

degrau = 0
degraus = A + B
i,p = 0,0

while degraus > 0:
    if degraus%2 == 0:
        p += 1
    elif degraus%2 != 0:
        i += 1
    degraus -= 1

if A == 0 and B == 0:
    print("0 0 errados")
elif  A == p and B == i:
    print(f'{A} {B} ok')
else:
    print(f'{A} {B} errados')