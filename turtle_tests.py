# learning about turtle, a Python module
# http://docs.python.org/3.1/library/turtle.html 

import turtle
t = turtle.Pen()

# draw a line for 50 pixels
t.forward(50)

# rotate the turtle 90 degrees, turning left
t.left(90)

# draw a line for 50 pixels in the opposite direction of the pointed end 
t.backward(50)

# clear the drawing canvas
# t.clear()
# t.reset()

def drawlr():
    r = raw_input("Should the turtle go left or right? ")
    d = raw_input("How far should the turtle travel? ")
    d = int(d)

    if (r == "left" or r == "l" or r == "L"):
         t.seth(180) # seth is same as setheading
#        t.left(90)  # rotation will depend on last heading 
    else:
         t.seth(0)
#        t.right(90)
    t.forward(d)
    drawud() # run next function 

def drawud():
    r = raw_input("Should the turtle go up or down? ")
    d = raw_input("How far should the turtle travel? ")
    d = int(d)

    if (r == "up" or r == "u" or r == "U"):
        t.seth(90) # seth is same as setheading 
    else:
        t.seth(270)
    t.forward(d)
    cont() # run next function

def cont():
    a = raw_input("Continue playing? ")
    if (a == "yes" or a == "y" or a == "Y"):
        drawlr() # run the first function again
    else:
        # this is here to keep the window open 
        print "Press Enter or Return to end the program."
        raw_input()

drawlr()
