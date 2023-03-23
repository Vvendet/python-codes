def comparacao(x,y):
    if x>y:
        return 1
    elif x == y:
        return 0
    else:
        return -1

x = int(input())
y = int(input())

if comparacao(x,y) > 0:
    print("x e maior que y")
elif comparacao(x,y) < 0:
    print("x e menor que y")
else:
    print("x e igual a y")