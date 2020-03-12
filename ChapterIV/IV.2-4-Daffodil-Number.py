def isDaffoil(num):
    sum = 0
    n = num
    while num > 0:
        digit = num % 10
        sum += pow(digit, 3)
        num //= 10
    return sum == n

daffoils = []
for i in range(100, 1000):
    if isDaffoil(i):
        daffoils.append(str(i))


print(','.join(daffoils))