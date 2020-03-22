import turtle as t

t.pensize(4)
r = 200
for i in range(4):
    t.right(45)
    t.fd(r)
    t.left(90)
    t.circle(r, 45)
    t.left(90)
    t.fd(r)
    t.right(90)
t.done()