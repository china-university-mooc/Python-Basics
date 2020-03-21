class Column:
    def __init__(self, name, discNum):
        self.name = name
        self.discs = [discNum - i for i in range(discNum)]

    def move(self, to):
        disc = self.discs.pop(-1)
        to.discs.append(disc)
        print("{} -{}-> {}".format(self.name, disc, to.name))

def hanoi(n, src, to, mid):
    if (n == 1):
        src.move(to)
        print(columns[0].discs, columns[1].discs, columns[2].discs)
        return 1
    else:
        c1 = hanoi(n - 1, src, mid, to)
        c2 = hanoi(1, src, to, mid)
        c3 = hanoi(n - 1, mid, to, src)
        return c1 + c2 + c3

src = Column('A', 2)
mid = Column('B', 0)
to = Column('C', 0)
columns = [src, mid, to]

step = hanoi(2, src, to, mid)
print("Total step: {}".format(step))
