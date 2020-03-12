import math

# 数学常数
print('-'*50)

print(math.pi)
print(math.e)
print(math.inf)
print(math.nan)

# 基本运算
print('-'*50)

print(math.fabs(-1.234))
print(math.fmod(3.4, 2))
print(math.fsum([1.0, 2.0])) # 精确求和
print(math.ceil(2.1))
print(math.floor(2.9))
print(math.factorial(3))
print(math.gcd(3, 7))
print(math.isnan(3))
print(math.isfinite(math.inf))

# 幂对函数
print('-'*50)

print(math.pow(2, 3))
print(math.exp(3))
print(math.sqrt(9))
print(math.log(27))
print(math.log(3, 27))
print(math.log2(8))
print(math.log10(100))

# 三角函数
print('-'*50)
print(math.degrees(math.pi))
print(math.radians(180))
print(math.hypot(3, 4)) # 坐标到原点的距离
print(math.sin(math.pi/2))
print(math.asin(0))