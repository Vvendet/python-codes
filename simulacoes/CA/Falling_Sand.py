import tkinter
from tkinter import *
import time, random


gridSize = 10 #tamanho de cada quadrado, cada célula
screenSize = 400#tamanho da tela
numCells = int(screenSize/gridSize)

win = Canvas(Tk(),width = screenSize, height = screenSize) #definir tela

#Matriz que guarda as células (inicialmente todas as entradas nulas)
CA = [[0 for x in range(numCells)] for y in range(numCells)]
Stable = [[0 for x in range(numCells)] for y in range(numCells)]



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

    #desenha o retangulo amarelo, se existe um grão de areia
    for i in range(numCells):
        for j in range(numCells):
            if CA[i][j] == 1:
                x1 = gridSize * i
                y1 = gridSize * j
                win.create_rectangle(x1,y1,x1+gridSize,y1+gridSize,fill='yellow') 
            elif CA[i][j]==0:
                x1 = gridSize * i
                y1 = gridSize * j
                win.create_rectangle(x1,y1,x1+gridSize,y1+gridSize,fill='black') 
    win.update()

def FallingSand(): #aplicar as regras em cada celula
    global CA

    CAnext = [[0 for x in range(numCells)] for y in range(numCells)] #definir matriz da proxima iteracao

    for i in range(numCells): 
        for j in range(numCells):

            if CA[i][j]==1 and Stable[i][j]==1:#verificar se o grão está em uma casa estável
                if CA[i+1][j+1]==0 and Stable[i+1][j]==0 :
                    CAnext[i+1][j+1] =1
                    #Stable[i+1][j]=1
                elif CA[i-1][j+1]==0 and Stable[i-1][j]==0 :
                    CAnext[i-1][j+1] =1
                    #Stable[i-1][j]=1
                else:
                    CAnext[i][j]=1
                    #Stable[i][j-1]=1

            elif CA[i][j] == 1 and j<numCells-1:

                CAnext[i][j+1] = 1
                CAnext[i][j] = 0

            elif CA[i][j]==1 and j ==numCells-1:
                CAnext[i][j]=1
                Stable[i][j-1]=1


    for i in range(numCells): 
        for j in range(numCells):
            if CAnext[i][j]==1 and Stable[i][j]==1:
                Stable[i][j-1]=1
            elif Stable[i][j]==1 and Stable[i][j-1]==0:
                Stable[i][j]=0


    CA = CAnext
    
    RefreshGrid()


                





def click_handler(event): #desenhar os grãos na tela

    CA[event.x//gridSize][event.y//gridSize] =1

def is_stable(event): #desenhar os grãos na tela
    if Stable[event.x//gridSize][event.y//gridSize]==1:
        print("Stable")
    elif Stable[event.x//gridSize][event.y//gridSize]==0:
        print("Not Stable")

                
if __name__ == '__main__':

    RefreshGrid()

    generations = 50
    win.bind("<B1-Motion>", click_handler)
    win.bind("<Button>", is_stable)
    while True:
        FallingSand()