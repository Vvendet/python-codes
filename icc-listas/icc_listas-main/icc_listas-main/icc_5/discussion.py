"""
anda e Urso estão discutindo para 
saber qual letra é a mais recorrente em textos clássicos, "p" ou "u".

Sabendo que você é um experiente programador, 
Panda e Urso vêm pedir seu auxílio para dar um fim a esta disputa."""

n = int(input())
p = 0
u = 0
for i in range(n):
    line = input().lower()
    counter = [list(line).count('p'),list(line).count('u')]
    p += counter[0]
    u += counter[1]

print(p,u)