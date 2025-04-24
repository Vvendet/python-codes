N,M = input().split()
N,M = int(N),int(M)
menor = 9999999
menor_pop = []
todos = []
for a in range(N*M):
    coord = input()
    todos.append(coord)
    if int(coord.split()[2]) <= menor:
        menor = int(coord.split()[2])
    else:
        pass
   
for i in todos:
    if int(i.split()[2]) == menor:
        menor_pop.append(i)
    else:
        pass
menor_pop.sort()
print(menor_pop[0].split()[0] + " " + menor_pop[0].split()[1])