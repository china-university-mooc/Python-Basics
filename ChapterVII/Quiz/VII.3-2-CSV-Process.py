f = open('data.csv')
datals = []
for line in f:
    line = line.replace('\n','')
    data = [d.strip() for d in line.split(',')]
    datals.append(data)
f.close()

for data in datals[::-1]:
    print(';'.join(data[::-1]))