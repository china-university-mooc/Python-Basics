inStr = input()

numToCount = {}
for ch in inStr:
    num = eval(ch)
    numToCount[num] = numToCount.get(num, 0) + 1

sum = 0
for key in numToCount:
    sum += key
print(sum)