import math

def prime(m):
    if (m < 2):
        return False
    
    limit = math.floor(math.sqrt(m)) + 1
    for i in range(2, limit):
        if m % i == 0:
            return False
    return True

n = eval(input())
n = math.ceil(n)

primes = []
while len(primes) < 5:
    if prime(n):
        primes.append(str(n))
    n += 1
print(','.join(primes))