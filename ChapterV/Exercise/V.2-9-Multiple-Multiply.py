def cmul(*nums):
    p = 1
    for i in nums:
        p *= i
    return p

print(eval("cmul({})".format(input())))