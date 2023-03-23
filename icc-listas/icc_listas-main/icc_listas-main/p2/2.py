a = True
b = []
while a:
    s = input()
    if s == "Fim":
        a = False
    else:
        s = s.split()
        for i in s:
            b.append(i)

d = {e:b.count(e) for e in b}
maximo = max(d.values())
def get_key(val):
    for key, value in d.items():
         if val == value:
             return key
f = []
while maximo in d.values():
    f.append(get_key(maximo))
    del d[get_key(maximo)]
nomes = []
numeros = []
for i in f:
    try:
        numeros.append(int(i))
    except:
        nomes.append(i)

nomes.sort()
numeros.sort()
for i in range(len(numeros)):
    numeros[i] = str(numeros[i])

if len(nomes) > 0 and len(numeros) > 0:


    print(' '.join(nomes),' '.join(numeros))
elif len(nomes) > 0 and len(numeros) == 0:

    print(' '.join(nomes),' '.join(numeros))
else:
    
    print(' '.join(numeros))