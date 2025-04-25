import pygame
from pygame.locals import *
from sys import exit
import math
import numpy

pygame.init()

screensize = 500
gridSize = 10 #tamanho de cada quadrado, cada célula
numCells = int(screensize/gridSize) #numero de celulas



tela = pygame.display.set_mode((screensize, screensize))
pygame.display.set_caption('Sand Falling')
fonte = pygame.font.SysFont('arial',15,bold=True,italic = False)

#Matriz que guarda as células (inicialmente todas as entradas nulas)
CA = [[0 for x in range(numCells)] for y in range(numCells)]


#Matriz para guardar celulas que sao estaveis
#Celulas estaveis sao celulas onde a areia não pode mais cair
Stable = [[0 for x in range(numCells)] for y in range(numCells)] 

#limpa a tela e inicia
def InitCanvas():
    #draw grid
    for i in range(numCells): #desenhar as linhas para a tabela
        pygame.draw.line(tela, (255,255,255), (0,gridSize * i), (screensize, gridSize * i), 1)
        pygame.draw.line(tela, (255,255,255), (gridSize * i,0), (gridSize * i, screensize), 1)

def RefreshGrid(): #função para atualizar a tela
    global CA

    InitCanvas()

    #desenha o retangulo amarelo, se existe um grão de areia
    for i in range(numCells):
        for j in range(numCells):
            if CA[i][j] == 1:
                x1 = gridSize * i
                y1 = gridSize * j
                pygame.draw.rect(tela, (255,255,255), (x1,y1,gridSize,gridSize))
                #a areia é amarela 

def FallingSand(): #aplicar as regras em cada celula
    global CA

    CAnext = [[0 for x in range(numCells)] for y in range(numCells)] #definir matriz da proxima iteracao

    for i in range(numCells): #percorrer as colunas
        for j in range(numCells): #percorrer as linhas

            #verificar se o grão chegou a uma casa estável
            if CA[i][j]==1 and Stable[i][j]==1:
                #verificar se é possível "escorregar" para os lados
                if CA[i+1][j+1]==0 and Stable[i+1][j]==0 :
                    CAnext[i+1][j+1] =1
                    #Stable[i+1][j]=1
                elif CA[i-1][j+1]==0 and Stable[i-1][j]==0 :
                    CAnext[i-1][j+1] =1
                    #Stable[i-1][j]=1

                #se nao for possível, então o grão permanece na casa estável
                else:
                    CAnext[i][j]=1
                    #Stable[i][j-1]=1

            #bloco onde o grão está a cair        
            elif CA[i][j] == 1 and j<numCells-1:

                CAnext[i][j+1] = 1
                CAnext[i][j] = 0

            #verificar se o grão chegou até o limite (chão)
            elif CA[i][j]==1 and j ==numCells-1:
                CAnext[i][j]=1
                Stable[i][j-1]=1

    #definir as casas estáveis
    for i in range(numCells): 
        for j in range(numCells):
            if CAnext[i][j]==1 and Stable[i][j]==1:
                Stable[i][j-1]=1
            elif Stable[i][j]==1 and Stable[i][j-1]==0:
                Stable[i][j]=0


    CA = CAnext
    
    RefreshGrid()


while True:
    rect = pygame.draw.rect(tela, (0,0,0), (0,0,screensize,screensize))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if rect.collidepoint(event.pos):
                dragging = True
                # Get the mouse position
                if dragging:
                    mouse_x, mouse_y = event.pos
                    CA[mouse_x//gridSize][mouse_y//gridSize]=1

        elif event.type == pygame.MOUSEBUTTONUP:
            dragging = False

    pygame.draw.rect(tela, (0,0,0), (0,0,screensize,screensize))
    
    FallingSand()
    
    pygame.display.update()