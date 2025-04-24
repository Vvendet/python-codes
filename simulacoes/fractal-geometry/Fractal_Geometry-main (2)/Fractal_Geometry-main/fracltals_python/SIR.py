from tkinter import *
import time, random

#Variáveis globais
gridSize = 10 #tamanho de cada quadrado, cada célula
screenSize = 1000#tamanho da tela
numCells = int(screenSize/gridSize)

win = Canvas(Tk(),width = screenSize, height = screenSize) #definir tela

#Matriz que guarda as células (inicialmente todas as entradas nulas)
CA = [[0 for x in range(numCells)] for y in range(numCells)]

#matriz para contar tempo de recuperacao
R = [[0 for x in range(numCells)] for y in range(numCells)]

rec = 8 #iteracoes para recuperação
propagacao = 2
probabilidade = 5


# 8 2 5
# 7 3 10
# 4 2 1.000000000000002

#limpa a tela e inicia
def InitCanvas():
    win.delete('all')

    #draw grid
    for i in range(numCells): #desenhar as linhas para a tabela
        win.create_line(0,gridSize * i, screenSize, gridSize * i)
        win.create_line(gridSize * i, 0, gridSize * i, screenSize)
    win.pack()

def RefreshGrid(): #função para atualizar a tela
    global CA

    InitCanvas()

    #desenha o retangulo vermelho, se a celula é infectada
    for i in range(numCells):
        for j in range(numCells):
            if CA[i][j] == 1:
                x1 = gridSize * i
                y1 = gridSize * j
                win.create_rectangle(x1,y1,x1+gridSize,y1+gridSize,fill='red') 
    win.update()

def SIR(): #aplicar as regras em cada celula
    global CA, R, rec

    CAnext = [[0 for x in range(numCells)] for y in range(numCells)] #definir matriz da proxima iteracao

    for i in range(numCells): 
        for j in range(numCells):
            infected = 0
            #contar quantidade de individuos propagacao
            if CA[(i+0)%numCells][(j+1)%numCells] == 1:
                infected += 1
            if CA[(i+0)%numCells][(j-1)%numCells] == 1:
                infected += 1
            if CA[(i+1)%numCells][(j+0)%numCells] == 1:
                infected += 1
            if CA[(i-1)%numCells][(j+0)%numCells] == 1:
                infected += 1
            if CA[(i+1)%numCells][(j+1)%numCells] == 1:
                infected += 1
            if CA[(i+1)%numCells][(j-1)%numCells] == 1:
                infected += 1
            if CA[(i-1)%numCells][(j+1)%numCells] == 1:
                infected += 1
            if CA[(i-1)%numCells][(j-1)%numCells] == 1:
                infected += 1

            if CA[i][j]==1: #verificar se a celular é infectada
                R[i][j] +=1

            if infected >= propagacao and CA[i][j] ==0 and R[i][j]<rec: #preencher matriz da proxima iteracao
                CAnext[i][j] = 1

            elif CA[i][j] ==1 and R[i][j]>=rec:
                CAnext[i][j]=0
            else:
                CAnext[i][j] = CA[i][j]


            
    CA = CAnext
    RefreshGrid()
            
def Count():
    global CA
    I = 0
    S = 0
    R = 0
    for i in range(numCells): 
        for j in range(numCells):
            if CA[i][j] == 1:
                I += 1
            elif CA[i][j] == 0:
                S +=0

    return I, S

                
if __name__ == '__main__':

    #gerar as celulas aleatoriamente
    for i in range(numCells):
        for j in range(numCells):
            if random.randint(1,100) < probabilidade:
                CA[i][j] = 1
            else:
                CA[i][j] = 0

    RefreshGrid()

    generations = 50
    filename = 'output.dat'
    with open(filename, 'w') as file:
        for i in range(generations):
            time.sleep(0.5)
            SIR()
            file.write(f"{i}    ")
            file.write(f"{Count()[0]}\n")


###
#Observações feitas:
#Para este modelo castrófico, não é possível uma pessoa não ser contaminada antes da extinção da doença
#Para que isto aconteça, todas sua vizinhança contaminada deve se curar antes de transmitir a doença,
#que é o mesmo que dizer se curar antes de estar doente.

#Para geração inicial da pop, se mais de 30% das pessoas estiverem contaminadas, então rapidamente todos estarão. 
#Consequentemente, todos irão ser imunes à doença iterações a frente (a depender de N*).
