
def getNum():
    nums = []
    numStr = input()
    while numStr != '':
        nums.append(eval(numStr))
        numStr = input()
    return nums

def sum(ls):
    s = 0.0
    for num in ls:
        s += num
    return s

def average(ls):
    return sum(ls) / len(ls)

def variance(ls):
    avg = average(ls)
    svar = 0.0
    for num in ls:
        svar += (num - avg)**2
    return pow(svar / (len(ls) - 1), 0.5)

def median(ls):
    sorted(ls)
    size = len(ls)
    if size % 2 == 0:
        med = (ls[size//2 -1] + ls[size//2]) / 2
    else:
        med = ls[size//2]
    return med

def main():  
    nums = getNum()
    print("avg={}, var={:.3}, med={}".format(average(nums), variance(nums), median(nums)))

main()