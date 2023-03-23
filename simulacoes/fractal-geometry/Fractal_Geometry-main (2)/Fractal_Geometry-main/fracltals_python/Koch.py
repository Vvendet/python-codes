import turtle

koch = 'FRFRF'
iterations = input("Enter the number of generations: ") #type in a string
iterations = int(iterations) #now it's an integer
startLength=200 #Length of the generation 0 line

#pick the pen up and move cursor to a good starting point
turtle.up()
turtle.setpos(-startLength*3/2,startLength*3/2/2)
turtle.speed(0)

#make the L-System we want to process
for i in range(iterations):
    koch = koch.replace("F","FLFRFLF")

turtle.down() #pen down
turtle.color('red','black') #draw line in red, fill black
turtle.begin_fill() #set the fill setting

for move in koch: #another way to loop through all the characters in a string
    if move == "F":
        turtle.forward(startLength / (3 ** (iterations - 1)))
    elif move == "L":
        turtle.left(60)
    elif move == "R":
        turtle.right(120)

turtle.end_fill() #fill any enclosed areas
