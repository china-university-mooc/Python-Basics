import random

def genpwd(length):
    start = pow(10, length - 1)
    end = pow(10, length) - 1
    num = random.randint(start, end)
    return str(num)

length = eval(input())
random.seed(17)
for i in range(3):
    print(genpwd(length))
