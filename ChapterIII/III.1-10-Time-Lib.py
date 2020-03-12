import time

# 时间获取：time(),ctime(),gmtime()
print('-'*50)

print(time.time())
print(time.ctime())
print(time.gmtime())

# 格式化：strftime(),strptime()
print('-'*50)

print(time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime()))
print(time.strptime('2020-03-12 12:12:12', '%Y-%m-%d %H:%M:%S'))

# 记时：sleep(),perf_counter()
print('-'*50)
start = time.perf_counter()
time.sleep(0.010) # s
print(time.perf_counter() - start)