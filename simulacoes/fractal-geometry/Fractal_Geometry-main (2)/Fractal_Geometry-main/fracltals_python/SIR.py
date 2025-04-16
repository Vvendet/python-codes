from tkinter import *
import time, random

#Variáveis globais
gridSize = 10 #tamanho de cada quadrado, cada célula
screenSize = 1000#tamanho da tela
numCells = int(50)

win = Canvas(Tk(),width = screenSize, height = screenSize) #definir tela

#Matriz que guarda as células (inicialmente todas as entradas nulas)
CA = [[0 for x in range(numCells)] for y in range(numCells)]
#matriz para contar tempo de recuperacao
R = [[0 for x in range(numCells)] for y in range(numCells)]
rec = 2 #iteracoes para recuperação



#limpa a tela e inicia
def InitCanvas():
    win.delete('all')

    #draw grid
    for i in range(numCells):
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
    global CA

    CAnext = [[0 for x in range(numCells)] for y in range(numCells)] #definir matriz da proxima iteracao

    for i in range(numCells): 
        for j in range(numCells):
            infected = 0
            #contar quantidade de individuos infectados
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

            if CA[i][j]==1:
                R[i][j] +=1

            if infected >= 1 and CA[i][j] ==0 and R[i][j]<rec: #preencher matriz da proxima iteracao
                CAnext[i][j] = 1

            elif CA[i][j] ==1 and R[i][j]>=rec:
                CAnext[i][j]=0
            else:
                CAnext[i][j] = CA[i][j]


            
    CA = CAnext
    RefreshGrid()
            

                
if __name__ == '__main__':

    #gerar as celulas aleatoriamente
    for i in range(numCells):
        for j in range(numCells):
            if random.randint(1,100) < 33:
                CA[i][j] = 1
            else:
                CA[i][j] = 0

    RefreshGrid()

    generations = 1000

    for i in range(generations):
        time.sleep(0.5)
        SIR()
