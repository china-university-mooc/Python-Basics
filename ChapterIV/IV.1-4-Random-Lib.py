import random

# seed(),random()
random.seed(10)
print(random.random())
print(random.random())
random.seed(10)
print(random.random())

# randint(),randrange(),getrandbits(),uniform()
print(random.randint(5, 10))
print(random.randint(5, 10))

print(random.randrange(1, 10, 3))
print(random.randrange(1, 10, 3))

print(random.getrandbits(16))
print(random.getrandbits(16))

print(random.uniform(2, 3))
print(random.uniform(2, 3))

# choice(),shuffle()
list = [1, 2, 3, 4, 5, 6, 7]
print(random.choice(list))
print(random.choice(list))
random.shuffle(list)
print(list)