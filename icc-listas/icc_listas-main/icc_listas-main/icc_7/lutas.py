F = int(input())

Lutadores = {}
Lutas = {}
for i in range(F):
    string = input().split()
    Lutadores[string[0]] = 0

n = 0
while True:
    imp = input().split()
    if imp[0] == 'FINISHHIM':
        while True:
            if Lutas[imp[1]][2] not in Lutadores:
                n += 1
                imp[1] = Lutas[imp[1]][2]
            else:
                n += 1
                print(n)
                break
        break
    else:
        Lutas[imp[0]] = imp[1:]
