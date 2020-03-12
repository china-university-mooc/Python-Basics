def dayUp(dayFactor):
    power = 1.0
    for i in range(366):
        if (i % 7 in [6, 0]):
            power *= (1 - 0.01)
        else:
            power *= (1 + dayFactor)
    return power
    
pa = pow((1 + 0.01), 365)
pb = 0.01
while(dayUp(pb) < pa):
    pb += 0.001
    
print("工作日的努力参数是: {:.3f}".format(pb))