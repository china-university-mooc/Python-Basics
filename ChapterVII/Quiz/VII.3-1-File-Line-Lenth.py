f =  open('latex.log')
sum = 0
count = 0
for line in f:
    line = line.replace('\n', '')
    if len(line) > 0:
        sum += len(line)
        count += 1
f.close()
print(round(sum/count))
