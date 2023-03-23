import tkinter as tk
from tkinter import *
def cantor_set(x,y,l):
    if l > 1/10: 
        win.create_line(x,y,x+l,y) 
        y = y + 50 
        cantor_set(x,y,l/3) 
        cantor_set(x+2/3*l,y,l/3) 


w,h = 500,500
win = Canvas(Tk(),width=w,height=h)
win.pack()
cantor_set(10,10,w-20)

win.mainloop()