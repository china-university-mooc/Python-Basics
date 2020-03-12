import math

def isPrime(num):
    if num < 2:
        return False
    
    max = round(math.sqrt(num))
    for i in range(2, max + 1):
        if (num % i == 0):
            return False
    return True

sum = 0
for i in range(2, 100):
    if isPrime(i):
        sum += i
print(sum)