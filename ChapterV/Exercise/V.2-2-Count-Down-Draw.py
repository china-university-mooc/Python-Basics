import turtle as tt
import time

def drawLine(draw):
    fdFly(5)
    if not draw:
        tt.penup()
    tt.fd(40)
    if not draw:
        tt.pendown()
    fdFly(5)

def fdFly(len):
    tt.penup()
    tt.fd(len)
    tt.pendown()

def gotoFly(x, y):
    tt.penup()
    tt.goto(x, y)
    tt.pendown()

def drawDigit(digit, penSize):
    oldSize = tt.pensize()
    tt.pensize(penSize)

    drawLine(True) if digit in [2,3,4,5,6,8,9] else drawLine(False)
    tt.right(90)
    drawLine(True) if digit in [0,1,3,4,5,6,7,8,9] else drawLine(False)
    tt.right(90)
    drawLine(True) if digit in [0,2,3,5,6,8,9] else drawLine(False)
    tt.right(90)
    drawLine(True) if digit in [0,2,6,8] else drawLine(False)
    drawLine(True) if digit in [0,4,5,6,8,9] else drawLine(False)
    tt.right(90)
    drawLine(True) if digit in [0,2,3,5,6,7,8,9] else drawLine(False)
    tt.right(90)
    drawLine(True) if digit in [0,1,2,3,4,7,8,9] else drawLine(False)
    tt.left(90)
    tt.pensize(oldSize)

def countdown():
    for i in range(9, -1, -1):
        drawDigit(i, 5)
        fdFly(-50)
        time.sleep(1)
        tt.clear()

tt.setup(200, 200)
tt.speed('fastest')
tt.pencolor('blue')
gotoFly(-25, 0)
tt.hideturtle()
countdown()
tt.done()
