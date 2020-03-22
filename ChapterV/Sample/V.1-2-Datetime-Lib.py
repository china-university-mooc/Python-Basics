from datetime import datetime

# 创建
print("===创建")
print(datetime.now())
print(datetime.utcnow())
print(datetime(2020, 3, 22, 9, 15, 30, 9))

# 属性
print("===属性")
now = datetime.now()
print(now.min)
print(now.max)
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)
print(now.microsecond)

# 方法
print("===方法")
now = datetime.now()
print(now.isoformat())
print(now.isoweekday())
print(now.strftime('%Y-%m-%d %H-%M-%S.%f'))
