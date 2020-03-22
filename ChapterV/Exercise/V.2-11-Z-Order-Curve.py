import turtle as tt
from math import *

def calDegreeAndLen(x, y):
    rad = atan(y / x)
    deg = degrees(rad)
    len = x / cos(rad)
    return deg, len

def zOrder(len, level):
    if level > 0:
        nextLen = len / 2
        nextLevel = level - 1
        joinLen = len / pow(2, level)
        d1, l1 = calDegreeAndLen(joinLen, joinLen * (pow(2, level - 1) - 1))
        d2, l2 = calDegreeAndLen(joinLen * (pow(2, level) - 1), joinLen)

        zOrder(nextLen, nextLevel)
        tt.left(d1)
        tt.fd(l1)
        tt.right(d1)
        zOrder(nextLen, nextLevel)

        tt.right(180 - d2)
        tt.fd(l2)
        tt.left(180 - d2)

        zOrder(nextLen, nextLevel)
        tt.left(d1)
        tt.fd(l1)
        tt.right(d1)
        zOrder(nextLen, nextLevel)

def main():
    tt.setup(480, 480)
    tt.speed('fastest')
    tt.pencolor('blue')
    tt.penup()
    tt.goto(-200, 200)
    tt.pendown()

    zOrder(400, 6)
    tt.hideturtle()
    tt.done()

main()