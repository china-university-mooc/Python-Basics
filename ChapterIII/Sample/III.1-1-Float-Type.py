# 浮点运算存在不确定尾数
print('-'*20)
print(0.1 + 0.2) # 有尾数
print(0.1 + 0.3)
print(0.1 + 0.4)
print(0.1 + 0.5)
print(0.1 + 0.6)
print(0.1 + 0.7) # 有尾数
print(0.1 + 0.8)
print(0.1 + 0.9)

# 浮点数间的比较
print('-'*20)
print(0.1 + 0.2 == 0.3)
print(round(0.1 + 0.2, 1) == 0.3)

# 科学计数法表示
print('-'*20)
a = 4.3e-3
b = 4.3E3
print(a)
print(b)