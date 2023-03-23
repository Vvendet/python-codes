n = int(input())
space = []
for i in range(n):
    space.append(input().split())

def descer(x,y):
    global space
    space[x+1][y] = 'o'
    space[x][y] = '.'
    verificar()


def verificar():
    global space
    for i in range(0,n-1):
        for j in range(0,n):
            if space[i][j] == 'o':
                if space[i+1][j] == '.':
                    descer(i,j)
                    
                else:
                    pass
    return 
verificar()
for i in range(n):
    for j in space[i]:
        print(j,end=' ')
    print('')
