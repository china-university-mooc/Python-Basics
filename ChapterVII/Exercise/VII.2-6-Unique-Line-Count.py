f =  open('latex.log')
lines = f.readlines()
f.close()

counts = {}
for line in lines:
    counts[line] = counts.get(line, 0) + 1

total = 0
for value in counts.values():
    if value == 1:
        total += 1
print('共{}独特行'.format(total))
