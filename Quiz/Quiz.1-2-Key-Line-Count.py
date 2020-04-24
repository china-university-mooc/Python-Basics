f = open('latex.log')

lineCount = {}
for line in f:
    lineCount[line] = lineCount.get(line, 0) + 1
f.close()

print("共{}关键行".format(len(lineCount)))
