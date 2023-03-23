convidados = []
c = int(input())
for i in range(c):
    convidados.append(input())
if "André" in convidados:
    print("Cuidado!")
else:
    print("Seguro!")