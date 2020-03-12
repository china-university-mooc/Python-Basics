import random
import math

stars = eval(input())
hit = 0
random.seed(123)
for i in range(stars):
    x = random.random()
    y = random.random()
    d = math.sqrt(pow(x, 2) + pow(y, 2))
    if (d <= 1):
        hit += 1

pi = 4 * hit / stars
print("{:.6f}".format(pi))
