n = 966

sum = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        i = -i
    sum += i

print(sum)