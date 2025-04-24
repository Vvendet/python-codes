from tkinter import *
import time, random

#Variáveis globais
gridSize = 10 #lado de cada celula
screenSize = 1000
numCells = int(screenSize/gridSize)

win = Canvas(Tk(),width = screenSize, height = screenSize)

#matriz cellular automata
CA = [[0 for x in range(numCells)] for y in range(numCells)]


#desenhar o plano
def InitCanvas():
    win.delete('all')

    for i in range(numCells):
        win.create_line(0,gridSize * i, screenSize, gridSize * i)
        win.create_line(gridSize * i, 0, gridSize * i, screenSize)
    win.pack()
#atualizar plano
def RefreshGrid():
    global CA

    InitCanvas()

    #pintar as celulas
    for i in range(numCells):
        for j in range(numCells):
            if CA[i][j] == 1:
                x1 = gridSize * i
                y1 = gridSize * j
                win.create_rectangle(x1,y1,x1+gridSize,y1+gridSize,fill='black')
    win.update()

def GameOfLife():
    global CA

    CAnext = [[0 for x in range(numCells)] for y in range(numCells)]

    for i in range(numCells):
        for j in range(numCells):
            lives = 0
#contar quantos vivos
            if CA[(i+0)%numCells][(j+1)%numCells] == 1:
                lives += 1
            if CA[(i+0)%numCells][(j-1)%numCells] == 1:
                lives += 1
            if CA[(i+1)%numCells][(j+0)%numCells] == 1:
                lives += 1
            if CA[(i-1)%numCells][(j+0)%numCells] == 1:
                lives += 1
            if CA[(i+1)%numCells][(j+1)%numCells] == 1:
                lives += 1
            if CA[(i+1)%numCells][(j-1)%numCells] == 1:
                lives += 1
            if CA[(i-1)%numCells][(j+1)%numCells] == 1:
                lives += 1
            if CA[(i-1)%numCells][(j-1)%numCells] == 1:
                lives += 1

            if CA[i][j] == 1:
                if lives == 1:
                    CAnext[i][j] = 0
                elif lives > 3:
                    CAnext[i][j] = 0
                else:
                    CAnext[i][j] = 1
            else:
                if lives == 3:
                    CAnext[i][j] = 1
    CA = CAnext
    RefreshGrid()
            

                
if __name__ == '__main__':

    #Randomly seed the board
    for i in range(numCells):
        for j in range(numCells):
            CA[i][j]=random.randint(0,1)

    RefreshGrid()

    generations = 1000

    for i in range(generations):
        time.sleep(0.1)
        GameOfLife()
