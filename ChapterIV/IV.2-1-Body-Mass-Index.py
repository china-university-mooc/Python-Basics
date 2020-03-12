height, weight = eval(input())
bmi = weight/(height**2)

if bmi < 18.5:
    a = '偏瘦'
elif bmi < 25:
    a = '正常'
elif bmi < 30:
    a = '偏胖'
else:
    a = '肥胖'

if bmi < 18.5:
    b = '偏瘦'
elif bmi < 24:
    b = '正常'
elif bmi < 28:
    b = '偏胖'
else:
    b = '肥胖'

print('BMI数值为:{:.2f}'.format(bmi))
print("BMI指标为:国际'{}',国内'{}'".format(a, b))