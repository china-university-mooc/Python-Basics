f = open('data.csv')
datals = []
for line in f:
    line = line.replace('\n','')
    data = [i.strip(' ') for i in line.split(',')]
    datals.append(data)
f.close()

for data in datals:
    print(','.join(data))