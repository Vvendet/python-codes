n = int(input())
indices = []
problems = []
solucoes = []
dif = []

for i in range(n):
    indices.append(i)
    a = input().split()
    problems.append(a[0])
    solucoes.append(a[1])
    dif.append(a[2])
    
print(indices)

