"""Leia a hora inicial, minuto inicial, hora final e minuto final de um jogo. A seguir calcule a duração do jogo, considerando que o jogo pode acabar em um dia e terminar em outro, tendo uma duração máxima de 24 horas."""

x = input().split()
h1 = int(x[0])
h2 = int(x[2])

m1 = int(x[1])
m2 = int(x[3])
if m1 < m2:
    minute = m2 - m1
else:
    minute = (60 - m1) + m2
if h1 < h2:
    t = h2 - h1
else:
    t = (24 - h1) + h2


if minute > 0 and minute < 60:
    t -= minute/60
    t = round(t)
elif minute == 60:
    minute = 0
print(f'O jogo durou {int(t)} hora(s) e {minute} minuto(s).')