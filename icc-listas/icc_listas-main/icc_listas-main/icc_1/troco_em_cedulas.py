"""Leia um valor inteiro. A seguir, calcule o menor número de notas possı́veis (cédulas) no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1.
A seguir mostre o valor lido e a relação de notas necessárias."""

val = int(input())
c = 0
d5 = 0
d2 = 0
d1 = 0
u5 = 0
u2 = 0
u = 0
print(val)
while val != 0:
    if val >= 100:
        val -= 100
        c +=1
    elif val >=50 and val < 100:
        val -= 50
        d5 += 1
    elif val >= 20 and val < 50:
        val -= 20
        d2 += 1
    elif val >=10 and val < 20:
        val -= 10
        d1 += 1
    elif val >= 5 and val < 10:
        val -= 5
        u5 += 1
    elif val >= 2 and val < 5:
        val -= 2
        u2 += 1
    elif val >= 1 and val < 2:
        val -= 1
        u +=1
    
print(c,'nota(s) de R$ 100,00')
print(d5,'nota(s) de R$ 50,00')
print(d2,'nota(s) de R$ 20,00')
print(d1,'nota(s) de R$ 10,00')
print(u5,'nota(s) de R$ 5,00')
print(u2,'nota(s) de R$ 2,00')
print(u,'nota(s) de R$ 1,00')   