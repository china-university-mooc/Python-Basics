n = eval(input())
for i in range(1, n + 1, 2):
    s = '*' * i
    print(s.center(n))