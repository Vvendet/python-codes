"""
O mínimo múltiplo comum (mmc) de dois inteiros a e b 
é o menor inteiro positivo que é múltiplo simultaneamente
 de a e b . Se não existir tal inteiro positivo, por exemplo, 
 se a=0 ou b=0, então mmc(a,b) é zero por definição. O mínimo
  múltiplo comum é útil em operações de soma e subtração de 
  frações vulgares, onde é preciso um denominador comum entre 
  as frações operadas. Usando recursividade faça um programa 
  que leia dois números separados por espaço indefinidas vezes
   e calcule o seu mmc. O programa deve encerrar quando a entrada 
   conter um número negativo.
"""

a,b = input().split()
a,b = [int(a), int(b)]
def mmc(x,y):
    global a,b
    if x == 0 or y == 0:
        return 0
    elif x%y == 0 or y%x == 0:
        if x > y:
            return x
        else:
            return y
    else:
        if x> y:
            if (x//a >= 900):
                return a*b
            else:

                return mmc(a+x,y)
        else:
            if (x//b >= 900):
                return a*b
            else:
                return mmc(x,b+y)
    
while True:
    if a < 0 or b < 0:
        break
    print(mmc(a,b))
    a,b = input().split()
    a,b = [int(a), int(b)]
    