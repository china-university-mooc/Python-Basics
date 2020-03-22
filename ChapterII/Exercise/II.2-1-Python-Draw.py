import turtle as t

t.penup()
t.backward(250)
t.pendown()
t.pensize(25)
t.pencolor('purple')
t.right(40)
for i in range(4):
    t.circle(40, 80)
    t.circle(-40, 80)
t.circle(40, 40)
t.fd(40)
t.circle(20, 180)
t.fd(40 * 2 / 3)
t.done()
