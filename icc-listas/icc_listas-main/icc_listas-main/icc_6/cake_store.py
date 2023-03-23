n,ia = input().split()
n,ia = [int(n),int(ia)]
fatias = []
for i in range(n):
    fatias.append(i)
while n > 0:
    pessoa = input().split()
    idf = int(pessoa[1])
    if fatias[idf] == ia:
        print(pessoa[0])
        break
    else:
        fatias.pop(idf)
    n -= 1