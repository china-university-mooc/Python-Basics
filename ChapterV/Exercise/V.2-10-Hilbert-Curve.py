import turtle as tt

def hilbert(len, level, style):
    if level > 0:
        joinLen = len / pow(2, level)
        nextLen = len / 2
        nextLevel = level - 1
        sign = 1 if style == 'l' else -1
        oppositeStyle = 'r' if style == 'l' else 'l'
        
        tt.left(sign * 90)
        hilbert(nextLen, nextLevel, oppositeStyle)
        tt.fd(joinLen)

        tt.right(sign * 90)
        hilbert(nextLen, nextLevel, style)
        tt.fd(joinLen)
        hilbert(nextLen, nextLevel, style)
        tt.right(sign * 90)

        tt.fd(joinLen)
        hilbert(nextLen, nextLevel, oppositeStyle)
        tt.left(sign * 90)

def main():
    tt.setup(800, 800)
    tt.speed('fastest')
    tt.pencolor('blue')
    tt.penup()
    tt.goto(-200, -200)
    tt.pendown()

    hilbert(512, 8, 'l')
    tt.hideturtle()
    tt.done()

main()