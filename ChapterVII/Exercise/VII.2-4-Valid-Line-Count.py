f =  open('latex.log')
count = 0
for line in f:
    if len(line) > 1:
        count += 1
f.close()
print('共{}行'.format(count))
