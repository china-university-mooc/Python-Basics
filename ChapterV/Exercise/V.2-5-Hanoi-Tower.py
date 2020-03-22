
def hanoi(n, src, to, mid):
    global step
    if (n == 1):
        step += 1
        print("[STEP{:>4}] {}->{}".format(step, src, to))
    else:
        hanoi(n - 1, src, mid, to)
        hanoi(1, src, to, mid)
        hanoi(n - 1, mid, to, src)

step = 0
n = eval(input())
hanoi(n, 'A', 'C', 'B')

