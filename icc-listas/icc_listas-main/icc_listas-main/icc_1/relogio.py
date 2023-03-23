"""Leia do teclado um valor inteiro x, que é o tempo de duração em segundos de um determinado evento, e informe-o expresso no formato: horash:minutosm:segundoss."""

t = int(input())
m = t//60
h = 0
if m > 60:
    h += m//60
    while m >60:
        m -= 60
t = t%60
print("{h}h:{m}m:{s}s".format(h=h,m=m,s=t))