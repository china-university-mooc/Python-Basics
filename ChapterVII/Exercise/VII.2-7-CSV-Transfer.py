f = open('data.csv')
datals = []
for line in f:
    line = line.replace('\n','')
    data = line.split(',')
    datals.append(data)
f.close()

for data in datals:
    print(','.join(data[::-1]))