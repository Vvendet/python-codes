from tkinter import *
import random

w = 1000 # width of the canvas
win = Canvas(Tk(),height=w,width=w)
win.pack()

def f(a,x):    
    return a * x * (1-x)

minA = 2
maxA = 4.0
a = minA
maxIts = 400

while a <= maxA:
    x = random.random()
    minY,maxY = 0.0, f(a,0.5)
    plotX=(a-minA)*w/(maxA-minA)
    for numit in range(maxIts):
        if numit > maxIts/10:
            win.create_line(plotX,w-w*x,plotX+1,w-w*x+1)
        x = f(a,x)
    a += (maxA-minA)/w
    


