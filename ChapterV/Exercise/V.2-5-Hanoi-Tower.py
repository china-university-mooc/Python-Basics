
def hanoi(n, src, to, mid):
    if (n == 1):
        print("{}: {} -> {}".format(1, src, to))
    else:
        hanoi(n - 1, src, mid, to)
        print("{}: {} -> {}".format(n, src, to))
        hanoi(n - 1, mid, to, src)

hanoi(2, 'A', 'C', 'B')

