# 顺序
print('-'*50)
print("{} {} {}".format('a', 1, 2.0))
print("{2} {1} {0}".format('a', 1, 2.0))

# 对齐
print('-'*50)
print('{:=^20}'.format('python'))
print('{:=>20}'.format('python'))
print('{:=<20}'.format('python'))

# 千位分隔，精度
print('-'*50)
print('{:,}'.format(10000000))
print('{:.2f}'.format(1.55555)) # 四舍五入

# 整数类型
print('-'*50)
print('{:b}'.format(255)) # 二进制
print('{:c}'.format(255)) # 字符
print('{:d}'.format(255)) # 十进制
print('{:o}'.format(255)) # 八进制
print('{:x}'.format(255)) # 十六进制
print('{:X}'.format(255))

# 浮点类型
print('-'*50)
print('{:e}'.format(0.034))
print('{:E}'.format(0.034))
print('{:f}'.format(0.034))
print('{:%}'.format(0.034))