def diagonalDifference(arr):
    direita = 0
    for i in range(0,len(arr)):
        direita += arr[i][i]
    
    esquerda = 0
    for j in range(len(arr)):
        esquerda += arr[j][-(1+j)]
        print(arr[j])
    
    r = direita - esquerda
    if r < 0:
        return -r
    else:
        return r

n = int(input())
arr = []

for i in range(n):
    t = []
    b = input().split()
    for j in range(len(b)):
        b[j] = int(b[j])
    arr.append(b)


    
print(arr)
print(diagonalDifference(arr))