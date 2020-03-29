
def getNum():
    inStr = input()
    return eval('[{}]'.format(inStr))

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
    ls.sort()
    size = len(ls)
    if size % 2 == 0:
        med = (ls[size//2 -1] + ls[size//2]) / 2
    else:
        med = ls[size//2]
    return med

def main():  
    nums = getNum()
    print("平均值:{:.2f},标准差:{:.2f},中位数:{}".format(average(nums), variance(nums), median(nums)))

main()