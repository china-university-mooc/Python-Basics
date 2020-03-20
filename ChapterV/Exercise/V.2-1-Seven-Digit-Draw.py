import turtle as tt
import time
from datetime import datetime

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

def writeWord(word):
    tt.write(word, False, font=('Arial', 20, 'normal'))

def drawDate(date):
    tt.pencolor('red')
    for i in date:
        if i == '+':
            writeWord('年')
            fdFly(40)
            tt.pencolor('green')
        elif i == '-':
            writeWord('月')
            fdFly(40)
            tt.pencolor('blue')
        elif i == '=':
            writeWord('日')
        else:
            drawDigit(eval(i), 5)
            fdFly(20)

def drawTime(time):
    tt.pencolor('red')
    for i in time:
        if i == '+':
            writeWord('时')
            fdFly(40)
            tt.pencolor('green')
        elif i == '-':
            writeWord('分')
            fdFly(40)
            tt.pencolor('blue')
        elif i == '=':
            writeWord('秒')
        else:
            drawDigit(eval(i), 5)
            fdFly(20)

tt.setup(800, 500, 200, 200)
fdFly(-340)
tt.speed('fastest')
t = datetime.now()
gotoFly(-330, 80)
drawDate(t.strftime('%Y+%m-%d='))
gotoFly(-260, -80)
drawTime(t.strftime('%H+%M-%S='))

tt.hideturtle()
tt.done()
