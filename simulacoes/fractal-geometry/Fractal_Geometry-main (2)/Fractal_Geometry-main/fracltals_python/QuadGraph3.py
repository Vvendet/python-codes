import tkinter as tk
from tkinter import *

w = 1000 #canvas width/height

root = tk.Tk()

win = tk.Canvas(root,width = w, height = w, background='white')
win.pack(side = tk.RIGHT)

frm = tk.Frame(root)
frm.pack(side = tk.LEFT)

def f(a,x):
    return a*x*(1-x)


def _draw():
    win.delete('all')
    a = float(param.get())
    for x in range(w):
        win.create_line(x,w-w*f(a,x/w),x+1,w-w*f(a,x/w)+1,fill='green')
        win.create_line(x,w-x,x+1,w-x+1,fill='red')
    
def _Iterate():
    _draw()

    startingX = float(X0input.get())
    numits = int(NumItInput.get())
    a = float(param.get())

    prior, current = startingX, f(a,startingX)

    x1,y1,x2,y2 = startingX*w,w,startingX*w,w*(1-current)
    win.create_line(x1,y1,x2,y2)
    win.create_line(x2,y2,w-y2,y2)
    x1,y1 = w-y2, y2

    for i in range(numits-1):
        prior, current = current, f(a,current)

        x2,y2 = prior * w, w * (1-current)
        win.create_line(x1,y1,x2,y2)
        win.create_line(x2,y2,w-y2,y2)
        x1,y1 = w-y2, y2

Label(frm,text='f(x)=ax(1-x)',font=('Arial',20)).grid(row=0)

#a parameter
Label(frm,text='a=',font=('Arial',20)).grid(row=1)
param = StringVar()
e1 = Entry(frm, textvariable=param, font=('Arial',20)).grid(row=1,column=1)
param.set('1')

#Initial X value
Label(frm,text='X0=',font=('Arial',20)).grid(row=2)
X0input = StringVar()
e2 = Entry(frm, textvariable=X0input, font=('Arial',20)).grid(row=2,column=1)
X0input.set('0.234')

#Number of iterations input
Label(frm,text='Numits=',font=('Arial',20)).grid(row=3)
NumItInput = StringVar()
e3 = Entry(frm, textvariable=NumItInput, font=('Arial',20)).grid(row=3,column=1)
NumItInput.set('10')

btn = tk.Button(frm,text='Draw',command=_draw,font=('Arial',20)).grid(row=4)
btn2 = tk.Button(frm,text='Iterate',command=_Iterate,font=('Arial',20)).grid(row=5)


if __name__ == '__main__':
    _draw()
    root.mainloop()
    
