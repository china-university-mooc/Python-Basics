import turtle as tt

def piano(len, level, style):
    if level > 0:
        joinLen = len / pow(3, level)
        nextLen = len / 3
        for i in range(9):
            piano(nextLen, level - 1, style)
            if i == 2 or i == 5:
                tt.right(90 if style == 'l' else -90)
            if i < 8:
                tt.fd(joinLen)
            if i == 2 or i == 5:
                tt.right(90 if style == 'l' else -90)

            style = 'r' if style == 'l' else 'l'

def main():
    tt.setup(450, 450)
    tt.speed('fastest')
    tt.pencolor('blue')
    tt.penup()
    tt.goto(-202, -202)
    tt.pendown()
    tt.left(90)

    piano(405, 4, 'l')
    tt.hideturtle()
    tt.done()

main()