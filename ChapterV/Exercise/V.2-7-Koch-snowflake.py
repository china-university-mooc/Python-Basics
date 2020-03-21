import turtle as tt

def fdFly(len):
    tt.penup()
    tt.fd(len)
    tt.pendown()

def gotoFly(x, y):
    tt.penup()
    tt.goto(x, y)
    tt.pendown()

def koch(len, level):
    if level == 1:
        tt.fd(len)
    else:
        koch(len/3, level - 1)
        tt.left(60)
        koch(len/3, level - 1)
        tt.right(120)
        koch(len/3, level - 1)
        tt.left(60)
        koch(len/3, level - 1)

def kochSnowflake(len, level):
    koch(len, level)
    tt.right(120)
    koch(len, level)
    tt.right(120)
    koch(len, level)

tt.setup(800, 600)
tt.speed('fastest')
gotoFly(-200, 130)
tt.begin_fill()
tt.fillcolor('red')
kochSnowflake(300, 4)
tt.end_fill()
tt.hideturtle()
tt.done()