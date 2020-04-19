import turtle as t

f = open('data.txt')
datals = []
for line in f:
    line = line.replace('\n','')
    datals.append(list(map(eval, line.split(','))))
f.close()
print(datals)

t.setup(800, 600)
t.title('自动轨迹绘制')
t.pensize(5)
for data in datals:
    t.pencolor(data[3], data[4], data[5])
    t.fd(data[0])
    if data[1] == 0:
        t.left(data[2])
    else:
        t.right(data[2])

t.hideturtle()
t.done()