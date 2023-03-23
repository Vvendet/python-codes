def maior(x):
    if x > 0:
        return True
    else:
        return False
def menor(x):
    if x<0:
        return True
    else:
        return False
def plusMinus(arr):
    # Write your code here
    maiores = []
    for i in filter(maior,arr):
        maiores.append(i)
    menores = []
    for j in filter(menor,arr):
        menores.append(j)
    zeros = arr.count(0)
    print(f'{len(maiores)/len(arr):.10f}')
    print(f'{len(menores)/len(arr):.10f}')
    print(f'{zeros/len(arr):.10f}')

arr = [-4, 3, -9 ,0, 4, 1]
plusMinus(arr)