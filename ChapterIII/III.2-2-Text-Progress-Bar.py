import time as t

scale = 50
print("执行开始".center(scale//2, "-"))
start = t.perf_counter()
for i in range(scale + 1):
    a = '*' * i
    b = '.' * (scale - i)
    x = i / scale * 100
    duration = t.perf_counter() - start
    print("\r{:3.0f}%[{}->{}]{:.2f}s".format(x, a,b, duration), end="")
    t.sleep(0.01)
print("\n" + "执行结束".center(scale//2, "-"))