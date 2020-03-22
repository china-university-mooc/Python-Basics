str = input()
chanese = ['零','一','二','三','四','五','六','七','八','九']

result = ''
for i in str:
    digit = eval(i)
    result += chanese[digit]
print(result)