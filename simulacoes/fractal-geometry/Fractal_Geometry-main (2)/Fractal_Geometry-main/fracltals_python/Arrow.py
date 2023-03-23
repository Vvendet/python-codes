import turtle as t

def setTurtle(myTuple):
    t.up()
    t.setx(myTuple[0])
    t.sety(myTuple[1])
    t.setheading(myTuple[2])
    t.down()

def make_fractal(length,langle,rangle,iterations,axiom,target,replace,target2,replace2):
    state = axiom
    turtleState=[]
    
    #make the L-System we want to process
    for i in range(iterations):
        nextState=''
        for character in state:
            if character == target:
                nextState += replace
            elif character == target2:
                nextState += replace2
            else:
                nextState += character
        state = nextState

    for move in state: 
        if move == '[':
            turtleState.append((t.xcor(),t.ycor(),t.heading()))
        elif move == ']':
            setTurtle(turtleState.pop())
        elif move == "F":
            t.forward(length)
        elif move == "-":
            t.left(langle)
        elif move == "+":
            t.right(rangle)
        elif move == 'L':
            t.right(rangle)
            t.forward(length)
            t.left(langle)
            t.forward(length)
            t.left(langle)
            t.forward(length)
            t.right(rangle)
        elif move == 'R':
            t.left(langle)
            t.forward(length)
            t.right(rangle)
            t.forward(length)
            t.right(rangle)
            t.forward(length)
            t.left(langle)

if __name__ == '__main__':
    iterations = int(input("Enter the number of generations: "))
    myLen = int(input("Enter the forward movement length: "))
    
    t.speed(0)
    w = myLen * (2 ** (iterations + 1))

    t.setup(width=w,height=w,startx=0,starty=0)
    setTurtle((-t.window_width()/2,-t.window_height()/2,0))
    t.setup(width=w*1.2,height=w*1.2,startx=0,starty=0)

    #Sierpinski Arrowhead
    make_fractal(myLen,60,60,iterations,'R','L','+R-L-R+','R','-L+R+L-')

   
