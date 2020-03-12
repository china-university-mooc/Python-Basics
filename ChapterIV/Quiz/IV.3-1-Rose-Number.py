
def isRose(num):
    n = len(str(num))
    sum = 0
    i = num
    while i > 0:
        digit = i % 10
        sum += pow(digit, n)
        i //= 10
    return sum == num

for i in range(1000, 10000):
    if (isRose(i)):
        print(i)